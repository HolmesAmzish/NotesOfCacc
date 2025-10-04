```cs
namespace ArERP.Models.Entity
{
    public class EmployeeEntity
    {
        public int EmployeeId { get; set; }
        public string EmployeeName { get; set; }
        public string Gender { get; set; }
        public DateTime? BirthDate { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
        public DateTime? HireDate { get; set; }
        public string Department { get; set; }
        public string Position { get; set; }
        public decimal? Salary { get; set; }
        public bool IsActive { get; set; }

        public EmployeeEntity () { }
    }
}
```

