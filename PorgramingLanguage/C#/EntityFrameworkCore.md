```cs
using System.ComponentModel.DataAnnotations;

namespace ArERP.Models.Entity;

public class DepartmentEntity
{
    [Key]
    public int DepartmentId { get; set; }
    public string DepartmentName { get; set; } 
    public DateTime CreationDate { get; set; }
    public bool Deleted { get; set; }
}
```

```cs
using ArERP.Models.Entity;
using Microsoft.EntityFrameworkCore;

namespace ArERP.Repository
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

        public DbSet<Department> Departments { get; set; }
        public DbSet<Employee> Employees { get; set; }
        public DbSet<EmployeeApplication> EmployeeApplications { get; set; }
    }
}
```

```bash
dotnet ef migrations add CreateDepartmentTable
dotnet ef database update
```

