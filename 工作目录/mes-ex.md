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



查询通过工号、姓名、部门、进厂日期、状态进行查询。

```sql
ALTER PROCEDURE P_Emp_Join_Search
    @EmpNo VARCHAR(20) = NULL,
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
        AND (@Name IS NULL OR FName LIKE '%' + @Name + '%')
        AND (@Dept IS NULL OR FDept = @Dept)
        AND (@JoinDateFrom IS NULL OR FJoinDate >= @JoinDateFrom)
        AND (@JoinDateTo IS NULL OR FJoinDate <= @JoinDateTo)
        AND (@Status IS NULL OR FStatus = @Status);
    
    SELECT 
        FID,
        FEmpNo,
        FName,
        FIdNumber,
        FAddress,
        FJoinDate,
        FDept,
        FPhone,
        FStatus
    FROM 
        JC_Emp_Join
    WHERE 
        (@EmpNo IS NULL OR FEmpNo LIKE '%' + @EmpNo + '%')
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

