# 数据库表类分析

| 表名          | 用途         |
| ------------- | ------------ |
| JC_Process    | 主流程定义表 |
| JC_ICMO       | 工单生产管理 |
| JC_DataSource | 数据源配置   |
| JC_Dispose    |              |





员工入职记录

| 字段      | 数据类型      |
| --------- | ------------- |
| FID       | INT           |
| FEmpNo    | VARCHAR(20)   |
| FName     | NVARCHAT(50)  |
| FIdNumber | VARCHAR(18)   |
| FAddress  | NVARCHAR(100) |
| FJoinDate | DATETIME      |
| FDept     | NVARCHAR      |
| FPhone    | VARCHAR(50)   |
| FStatus   | TINYINT       |



```sql
CREATE TABLE JC_Emp_Join (
    FID INT IDENTITY(1,1) PRIMARY KEY,
    FNumber VARCHAR(20) NOT NULL,
    FEmpNo VARCHAR(20) NOT NULL,
    FName NVARCHAR(50) NOT NULL,
    FIdNumber VARCHAR(18) NOT NULL,
    FAddress NVARCHAR(100),
    FJoinDate DATETIME NOT NULL,
    FDept NVARCHAR(50),
    FPhone VARCHAR(20),
    FStatus TINYINT DEFAULT 0,
    -- 约束
    CONSTRAINT UK_EmpNo UNIQUE (FEmpNo),     
    CONSTRAINT UK_IdNumber UNIQUE (FIdNumber),
    -- 索引
    INDEX IDX_Dept (FDept),
    INDEX IDX_Status (FStatus)                
);
```

功能有新增、修改、删除、审核、反审、打印、查询

```sql
CREATE PROCEDURE sp_JC_Emp_Join_Insert
    @FNumber VARCHAR(20),
    @FEmpNo VARCHAR(20),
    @FName NVARCHAR(50),
    @FIdNumber VARCHAR(18),
    @FAddress NVARCHAR(100) = NULL,
    @FJoinDate DATETIME,
    @FDept NVARCHAR(50) = NULL,
    @FPhone VARCHAR(20) = NULL,
    @FStatus TINYINT = 0,
    @NewID INT OUTPUT,
    @ResultCode INT OUTPUT,
    @ResultMsg NVARCHAR(100) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- 检查员工工号是否已存在
        IF EXISTS (SELECT 1 FROM JC_Emp_Join WHERE FEmpNo = @FEmpNo)
        BEGIN
            SET @ResultCode = -1;
            SET @ResultMsg = '员工工号已存在';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 检查身份证号是否已存在
        IF EXISTS (SELECT 1 FROM JC_Emp_Join WHERE FIdNumber = @FIdNumber)
        BEGIN
            SET @ResultCode = -2;
            SET @ResultMsg = '身份证号已存在';
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- 插入新记录
        INSERT INTO JC_Emp_Join (
            FNumber,
            FEmpNo,
            FName,
            FIdNumber,
            FAddress,
            FJoinDate,
            FDept,
            FPhone,
            FStatus
        )
        VALUES (
            @FNumber,
            @FEmpNo,
            @FName,
            @FIdNumber,
            @FAddress,
            @FJoinDate,
            @FDept,
            @FPhone,
            @FStatus
        );
        
        -- 获取新插入记录的ID
        SET @NewID = SCOPE_IDENTITY();
        
        -- 设置成功返回码
        SET @ResultCode = 0;
        SET @ResultMsg = '入职记录添加成功';
        
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

