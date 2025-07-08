创建
```sql
CREATE TABLE JC_Termination (
	FID INT PRIMARY KEY IDENTITY(1,1),
	FNumber NVARCHAR(100) NOT NULL,
	FName NVARCHAR(100) NOT NULL,
	FDeleted INT DEFAULT 0,
	FCreateDate DATE DEFAULT GETDATE()
);
```



查询

```sql
SELECT * FROM sys.procedures WHERE name LIKE '%Termination%';

SP_HELPTEXT P_JC_Reason_Search;

```



删除

```sql
DROP PROCEDURE P_JC_Termination_Save;

DROP TABLE JC_Termination;

```

存储过程

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
```

```sql
CREATE PROCEDURE P_JC_Termination_Modify
	@FID INT,
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

	IF EXISTS(SELECT 1 FROM JC_Termination WHERE (FNumber=@FNumber OR FName=@FName) AND FID<>@FID)
	BEGIN
		SELECT 0 AS FIsOk,'离职原因代码或名称已存在！' AS FStrValue
		RETURN
	END

	DECLARE @FYNumber NVARCHAR(100)
	DECLARE @FYName NVARCHAR(100)

	SELECT @FYNumber=FNumber, @FYName=FName
	FROM JC_Termination
	WHERE FID=@FID

	UPDATE JC_Termination SET FNumber=@FNumber, FName=@FName,
	FDeleted=@FDeleted WHERE FID=@FID

	DECLARE @FEvent NVARCHAR(100)
	SET @FEvent='原代码:'+@FYNumber+';原名称:'+@FYName+';现代码:'+@FNumber+';现名称:'+@FName
	EXEC dbo.[P_SysWorkLog_Save]  @FUser,'离职原因','修改',@FEvent,'成功' 
	SELECT 1 AS FIsOk, '修改成功!' AS FStrValue
END;
```

