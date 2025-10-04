## 基础资料维护

**离职原因添加**

```sql
CREATE PROCEDURE P_JC_Termination_Save
    @FNumber NVARCHAR(100),
    @FName NVARCHAR(100),
    @FDeleted INT,
    @FUser NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    IF @FNumber = ''
    BEGIN
        SELECT 0 AS FIsOk, '代码不能为空' AS FStrValue;
        RETURN;
    END

    IF @FName = ''
    BEGIN
        SELECT 0 AS FIsOk, '名称不能为空' AS FStrValue;
        RETURN;
    END

    IF EXISTS (SELECT 1 FROM JC_Termination WHERE FNumber = @FNumber)
    BEGIN
        SELECT 0 AS FIsOk, '代码已存在' AS FStrValue;
        RETURN;
    END

    IF EXISTS (SELECT 1 FROM JC_Termination WHERE FName = @FName)
    BEGIN
        SELECT 0 AS FIsOk, '名称已存在' AS FStrValue;
        RETURN;
    END

    -- 事务处理
    BEGIN TRY
        BEGIN TRANSACTION;
        
        INSERT INTO JC_Termination (FNumber, FName, FDeleted)
        VALUES (@FNumber, @FName, ISNULL(@FDeleted, 0));
        
        DECLARE @FEvent NVARCHAR(200);
        SET @FEvent = '代码:' + @FNumber + ';名称:' + @FName;
        EXEC dbo.[P_SysWorkLog_Save] @FUser, '操作工', '新增', @FEvent, '成功';
        
        COMMIT TRANSACTION;
        
        SELECT 1 AS FIsOk, '保存成功' AS FStrValue;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        SELECT 0 AS FIsOk, ERROR_MESSAGE() AS FStrValue;
        RETURN;
    END CATCH;
END;
go


```



## 员工入职记录



员工入职记录

| 字段      | 数据类型      | 解释                       |
| --------- | ------------- | -------------------------- |
| FID       | INT           | 数据ID                     |
| FNumber   | VARCHAR(20)   | 工号                       |
| FName     | NVARCHAT(50)  | 姓名                       |
| FIdNumber | VARCHAR(18)   | 身份证                     |
| FAddress  | NVARCHAR(100) | 地址                       |
| FJoinDate | DATETIME      | 入职日期                   |
| FDept     | NVARCHAR      | 所属部门                   |
| FPhone    | VARCHAR(50)   | 电话                       |
| FStatus   | TINYINT       | 状态（审核中、入职、离职） |



```sql
CREATE TABLE JC_Emp_Join (
    FID INT IDENTITY(1,1) PRIMARY KEY,
    FNumber VARCHAR(20) NOT NULL,
    FName NVARCHAR(50) NOT NULL,
    FIdNumber VARCHAR(18) NOT NULL,
    FAddress NVARCHAR(100),
    FJoinDate DATETIME NOT NULL,
    FDept NVARCHAR(50),
    FPhone VARCHAR(20),
    FStatus TINYINT DEFAULT 0,
    -- Constraints
    CONSTRAINT UK_Number UNIQUE (FNumber),     
    CONSTRAINT UK_IdNumber UNIQUE (FIdNumber),
    -- Indexes
    INDEX IDX_Number (FNumber)                
);
```

功能有新增、修改、删除、审核、反审、打印、查询

```sql
CREATE PROCEDURE P_JC_Emp_Join_Save
    @FNumber VARCHAR(20),
    @FName NVARCHAR(50),
    @FIdNumber VARCHAR(18),
    @FAddress NVARCHAR(100),
    @FJoinDate DATETIME,
    @FDept NVARCHAR(50),
    @FPhone VARCHAR(20)
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRANSACTION
        INSERT INTO JC_Emp_Join (
            FNumber, FName, FIdNumber, FAddress, FJoinDate, FDept, FPhone
        )
        VALUES (
            @FNumber, @FName, @FIdNumber, @FAddress, @FJoinDate, @FDept, @FPhone
        )
        COMMIT TRANSACTION
        SELECT 1 AS FIsOk, '保存成功' AS FStrValue;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION
  
        IF ERROR_NUMBER() IN (2601, 2627)
        BEGIN
            SELECT 0 AS FIsOk, '工号或身份证重复' AS FStrValue;
        END
        ELSE
        BEGIN
            DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
            DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
            DECLARE @ErrorState INT = ERROR_STATE();
            RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
        END
    END CATCH
END
```

```sql
CREATE PROCEDURE sp_JC_Emp_Join_Approve
    @FID INT,                           -- 记录ID
    @FApprover NVARCHAR(50),            -- 审核人
    @ResultCode INT OUTPUT,
    @ResultMsg NVARCHAR(200) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- 检查记录是否存在
        IF NOT EXISTS (SELECT 1 FROM JC_Emp_Join WHERE FID = @FID)
        BEGIN
            SET @ResultCode = -1;
            SET @ResultMsg = '记录不存在';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 检查是否已审核
        DECLARE @CurrentStatus TINYINT;
        SELECT @CurrentStatus = FApprovalStatus FROM JC_Emp_Join WHERE FID = @FID;
        
        IF @CurrentStatus = 1
        BEGIN
            SET @ResultCode = -2;
            SET @ResultMsg = '该记录已审核，无需重复审核';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 更新审核状态
        UPDATE JC_Emp_Join
        SET 
            FApprovalStatus = 1,
            FApprover = @FApprover,
            FApproveDate = GETDATE(),
            FRejectReason = NULL
        WHERE FID = @FID;
        
        -- 设置成功返回码
        SET @ResultCode = 0;
        SET @ResultMsg = '审核成功';
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        SET @ResultCode = -99;
        SET @ResultMsg = ERROR_MESSAGE();
    END CATCH
END;
```

```sql
CREATE PROCEDURE sp_JC_Emp_Join_Reject
    @FID INT,                           -- 记录ID
    @FApprover NVARCHAR(50),            -- 审核人
    @FRejectReason NVARCHAR(200),       -- 驳回原因
    @ResultCode INT OUTPUT,
    @ResultMsg NVARCHAR(200) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- 检查记录是否存在
        IF NOT EXISTS (SELECT 1 FROM JC_Emp_Join WHERE FID = @FID)
        BEGIN
            SET @ResultCode = -1;
            SET @ResultMsg = '记录不存在';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 检查是否已审核
        DECLARE @CurrentStatus TINYINT;
        SELECT @CurrentStatus = FApprovalStatus FROM JC_Emp_Join WHERE FID = @FID;
        
        IF @CurrentStatus = 1
        BEGIN
            SET @ResultCode = -2;
            SET @ResultMsg = '该记录已审核，请先反审再驳回';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 更新审核状态为驳回
        UPDATE JC_Emp_Join
        SET 
            FApprovalStatus = 2,
            FApprover = @FApprover,
            FApproveDate = GETDATE(),
            FRejectReason = @FRejectReason
        WHERE FID = @FID;
        
        -- 设置成功返回码
        SET @ResultCode = 0;
        SET @ResultMsg = '驳回成功';
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
            
        SET @ResultCode = -99;
        SET @ResultMsg = ERROR_MESSAGE();
    END CATCH
END;
```



```sql
DECLARE @NewID INT, @ResultCode INT, @ResultMsg NVARCHAR(100);

EXEC P_JC_Emp_Join_Insert
    @FNumber = 'HR20250001',
    @FEmpNo = 'EMP20250001',
    @FName = '张三',
    @FIdNumber = '110101199001011234',
    @FAddress = '北京市朝阳区',
    @FJoinDate = '2025-07-10',
    @FDept = '研发部',
    @FPhone = '13800138000',
    @FStatus = 0,
    @NewID = @NewID OUTPUT,
    @ResultCode = @ResultCode OUTPUT,
    @ResultMsg = @ResultMsg OUTPUT;

SELECT @NewID AS NewID, @ResultCode AS ResultCode, @ResultMsg AS ResultMsg;
```



查询通过工号、姓名、部门、进厂日期、状态进行查询。

```sql
CREATE PROCEDURE P_Emp_Join_Search
    @EmpNo VARCHAR(20) = NULL,
    @Number VARCHAR(20) = NULL,
    @Name NVARCHAR(50) = NULL,
    @Dept NVARCHAR(50) = NULL,
    @JoinDateFrom DATETIME = NULL,
    @JoinDateTo DATETIME = NULL,
    @Status TINYINT = NULL,
    @PageNumber INT = 1,
    @PageSize INT = 20,
    @TotalCount INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    -- 计算总记录数
    SELECT @TotalCount = COUNT(*)
    FROM JC_Emp_Join
    WHERE 
        (@EmpNo IS NULL OR FEmpNo LIKE '%' + @EmpNo + '%')
		AND (@Number IS NULL OR FNumber LIKE '%' + @Number + '%')
        AND (@Name IS NULL OR FName LIKE '%' + @Name + '%')
        AND (@Dept IS NULL OR FDept = @Dept)
        AND (@JoinDateFrom IS NULL OR FJoinDate >= @JoinDateFrom)
        AND (@JoinDateTo IS NULL OR FJoinDate <= @JoinDateTo)
        AND (@Status IS NULL OR FStatus = @Status);
    
    SELECT FID, FEmpNo, FNumber, FName, FIdNumber, FAddress, FJoinDate, FDept, FPhone, FStatus
    FROM JC_Emp_Join
    WHERE 
        (@EmpNo IS NULL OR FEmpNo LIKE '%' + @EmpNo + '%')
		AND (@Number IS NULL OR FNumber LIKE '%' + @Number + '%')
        AND (@Name IS NULL OR FName LIKE '%' + @Name + '%')
        AND (@Dept IS NULL OR FDept = @Dept)
        AND (@JoinDateFrom IS NULL OR FJoinDate >= @JoinDateFrom)
        AND (@JoinDateTo IS NULL OR FJoinDate <= @JoinDateTo)
        AND (@Status IS NULL OR FStatus = @Status)
    ORDER BY 
        FJoinDate DESC
    OFFSET (@PageNumber - 1) * @PageSize ROWS
    FETCH NEXT @PageSize ROWS ONLY;
END
```

