创建项目

```bash
dotnet new webapp --output aspnetcoreapp --no-https
```

运行

```bash
cd aspnetcoreapp
dotnet run
```

修改 `Pages/Index.cshtml`

```html
@page
@model IndexModel
@{
    ViewData["Title"] = "Home page";
}

<div class="text-center">
    <h1 class="display-4">Welcome</h1>
    <p>Hello, world! The time on the server is @DateTime.Now</p>
</div>
```



