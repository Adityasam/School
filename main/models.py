from django.db import models

# Create your models here.

class SchoolSession(models.Model):
    Title = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)

class Faculty(models.Model):
    FacultyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    FirstName = models.CharField(max_length=50, default=None, null=True, blank=True)
    MiddleName = models.CharField(max_length=100, default=None, null=True, blank=True)
    LastName = models.CharField(max_length=100, default=None, null=True, blank=True)
    FullName = models.CharField(max_length=200, default=None, null=True, blank=True)
    EmailId = models.CharField(max_length=100, default=None, null=True, blank=True)
    Mobile = models.CharField(max_length=20, default=None, null=True, blank=True)
    Whatsapp = models.CharField(max_length=20, default=None, null=True, blank=True)
    Gender = models.CharField(max_length=5, default=None, null=True, blank=True)
    DateOfBirth = models.DateField(default=None, null=True, blank=True)
    JoiningDate = models.DateField(default=None, null=True, blank=True)
    Salary = models.FloatField(default=None, null=True, blank=True)
    Photo = models.CharField(max_length=100, default=None, null=True, blank=True)
    Status = models.CharField(max_length=1, default=None, null=True, blank=True)
    AadharNo = models.CharField(max_length=20, default=None, null=True, blank=True)
    Education = models.CharField(max_length=100, default=None, null=True, blank=True)
    Experience = models.PositiveIntegerField(default=None, null=True, blank=True)
    NameInBank = models.CharField(max_length=100,default=None, null=True, blank=True)
    BankAccountNo = models.CharField(max_length=50,default=None, null=True, blank=True)
    IFSC = models.CharField(max_length=50,default=None, null=True, blank=True)
    BankCode = models.CharField(max_length=10,default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Student(models.Model):
    StudentCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    RollNumber = models.PositiveIntegerField(default=None, null=True, blank=True)
    FirstName = models.CharField(max_length=50, default=None, null=True, blank=True)
    MiddleName = models.CharField(max_length=100, default=None, null=True, blank=True)
    LastName = models.CharField(max_length=100, default=None, null=True, blank=True)
    FullName = models.CharField(max_length=200, default=None, null=True, blank=True)
    EmailId = models.CharField(max_length=100, default=None, null=True, blank=True)
    Mobile = models.CharField(max_length=20, default=None, null=True, blank=True)
    Whatsapp = models.CharField(max_length=20, default=None, null=True, blank=True)
    Gender = models.CharField(max_length=5, default=None, null=True, blank=True)
    DateOfBirth = models.DateField(default=None, null=True, blank=True)
    FatherName = models.CharField(max_length=100, default=None, null=True, blank=True)
    MotherName = models.CharField(max_length=100, default=None, null=True, blank=True)
    Photo = models.CharField(max_length=100, default=None, null=True, blank=True)
    Class = models.CharField(max_length=10, default=None, null=True, blank=True)
    Section = models.CharField(max_length=10, default=None, null=True, blank=True)
    FatherPhoto = models.CharField(max_length=100, default=None, null=True, blank=True)
    MotherPhoto = models.CharField(max_length=100, default=None, null=True, blank=True)
    Status = models.CharField(max_length=1, default=None, null=True, blank=True)
    AadharNo = models.CharField(max_length=20, default=None, null=True, blank=True)
    BusService = models.BooleanField(default=False)
    BusId = models.PositiveIntegerField(default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Staff(models.Model):
    StaffCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    FirstName = models.CharField(max_length=50, default=None, null=True, blank=True)
    MiddleName = models.CharField(max_length=100, default=None, null=True, blank=True)
    LastName = models.CharField(max_length=100, default=None, null=True, blank=True)
    FullName = models.CharField(max_length=200, default=None, null=True, blank=True)
    EmailId = models.CharField(max_length=100, default=None, null=True, blank=True)
    Mobile = models.CharField(max_length=20, default=None, null=True, blank=True)
    Whatsapp = models.CharField(max_length=20, default=None, null=True, blank=True)
    Gender = models.CharField(max_length=5, default=None, null=True, blank=True)
    Designation = models.CharField(max_length=5, default=None, null=True, blank=True)
    DateOfBirth = models.DateField(default=None, null=True, blank=True)
    JoiningDate = models.DateField(default=None, null=True, blank=True)
    Salary = models.FloatField(default=None, null=True, blank=True)
    Photo = models.CharField(max_length=100, default=None, null=True, blank=True)
    Status = models.CharField(max_length=1, default=None, null=True, blank=True)
    AadharNo = models.CharField(max_length=20, default=None, null=True, blank=True)
    Education = models.CharField(max_length=100, default=None, null=True, blank=True)
    NameInBank = models.CharField(max_length=100,default=None, null=True, blank=True)
    BankAccountNo = models.CharField(max_length=50,default=None, null=True, blank=True)
    IFSC = models.CharField(max_length=50,default=None, null=True, blank=True)
    BankCode = models.CharField(max_length=10,default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Designation(models.Model):
    Title = models.CharField(max_length=100, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True)
    Deleted = models.BooleanField(default=False)

class DocumentMaster(models.Model):
    MasterCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    Description = models.CharField(max_length=200, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Bank(models.Model):
    Title = models.CharField(max_length=100, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Class(models.Model):
    ClassCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    Title = models.CharField(max_length=100, default=None, null=True, blank=True)
    HasSections = models.BooleanField(default=True, null=True, blank=True)
    ClassTeacher = models.CharField(max_length=20, default=None, null=True, blank=True)
    ClassFee = models.FloatField(default=None, null=True, blank=True)
    SortOrder = models.PositiveIntegerField(default=0)
    RoomNo = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Section(models.Model):
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    ClassId = models.CharField(max_length=50, default=None, null=True, blank=True)
    RoomNo = models.CharField(max_length=30, default=None, null=True, blank=True)
    ClassTeacher = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Subject(models.Model):
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class FacultySubject(models.Model):
    FacultyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=5, default=None, null=True, blank=True)

class StatusMaster(models.Model):
    Type = models.CharField(max_length=20, default=None, null=True, blank=True)
    StatusCode = models.CharField(max_length=10, default=None, null=True, blank=True)
    Title = models.CharField(max_length=30, default=None, null=True, blank=True)
    Color = models.CharField(max_length=20, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class MyUser(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    UserId = models.CharField(max_length=50, default=None, null=True, blank=True)
    Password = models.CharField(max_length=50, default=None, null=True, blank=True)
    EmployeeCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    IsSuperAdmin = models.BooleanField(default=False)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UserType = models.CharField(max_length=50, default=None, null=True, blank=True)
    Blocked = models.BooleanField(default=False, null=True, blank=True)
    Deleted = models.BooleanField(default=False, null=True, blank=True)

class Fee(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    StudentCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    DocumentCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    DocumentDate = models.DateField(default=None, null=True, blank=True)
    Amount = models.FloatField(default=None, null=True, blank=True)
    Discount = models.FloatField(default=None, null=True, blank=True)
    Fine = models.FloatField(default=None, null=True, blank=True)
    TotalAmount = models.FloatField(default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    MonthYear = models.CharField(max_length=10, default=None, null=True, blank=True)
    Type = models.CharField(max_length=10,default=None, null=True, blank=True)
    Mode = models.CharField(max_length=10,default=None, null=True, blank=True)
    ReferenceNo = models.CharField(max_length=50,default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20,default=None, null=True, blank=True)
    Remarks = models.CharField(max_length=500,default=None, null=True, blank=True)
    Type = models.CharField(max_length=2, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class FeeItem(models.Model):
    FeeId = models.PositiveIntegerField(default=None, null=True, blank=True)
    Amount = models.FloatField(default=None, null=True, blank=True)
    Discount = models.FloatField(default=None, null=True, blank=True)
    Fine = models.FloatField(default=None, null=True, blank=True)
    TotalAmount = models.FloatField(default=None, null=True, blank=True)
    MonthYear = models.CharField(max_length=10, default=None, null=True, blank=True)
    Type = models.CharField(max_length=10,default=None, null=True, blank=True)

class Expense(models.Model):
    ExpenseCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    DocumentDate = models.DateField(default=None, null=True, blank=True)
    Amount = models.FloatField(default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    DocumentNo = models.CharField(max_length=50, default=None, null=True, blank=True)
    InvoiceCopy = models.CharField(max_length=50, default=None, null=True, blank=True)
    Type = models.CharField(max_length=10, default=None, null=True, blank=True)
    Mode = models.CharField(max_length=10, default=None, null=True, blank=True)
    ReferenceNo = models.CharField(max_length=50,default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20,default=None, null=True, blank=True)
    Remarks = models.CharField(max_length=500,default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class ExpenseType(models.Model):
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class PaymentMode(models.Model):
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class FeeType(models.Model):
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Amount = models.FloatField(default=0)
    Deleted = models.BooleanField(default=False)

class Menu(models.Model):
    PageCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Description = models.CharField(max_length=200, default=None, null=True, blank=True)
    PageUrl = models.CharField(max_length=50, default=None, null=True, blank=True)
    Icon = models.CharField(max_length=50, default=None, null=True, blank=True)
    SortOrder= models.PositiveIntegerField(default=0, null=True, blank=True)
    ForAdmin = models.BooleanField(default=True)
    Desktop = models.BooleanField(default=True)
    Mobile = models.BooleanField(default=False)
    Visible = models.BooleanField(default=True)

class Routine(models.Model):
    ClassId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SectionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=10, default=None, null=True, blank=True)
    FacultyId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    Day = models.CharField(max_length=10, default=None, null=True, blank=True)
    StartTime = models.TimeField(default=None, null=True, blank=True)
    EndTime = models.TimeField(default=None, null=True, blank=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Deleted = models.BooleanField(default=False)   

class Exam(models.Model):
    Title = models.CharField(max_length=100, default=None, null=True, blank=True)
    StartDate = models.DateField(default=None, null=True, blank=True)
    EndDate = models.DateField(default=None, null=True, blank=True)
    Remarks = models.CharField(max_length=500, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class ExamPaper(models.Model):
    SubjectId = models.CharField(max_length=10, default=None, null=True, blank=True)
    ExamId = models.CharField(max_length=10, default=None, null=True, blank=True)
    ClassId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SectionId = models.CharField(max_length=20, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    TotalMarks = models.PositiveIntegerField(default=None, null=True, blank=True)
    PaperDate = models.DateField(default=None, null=True, blank=True)
    Content = models.TextField(default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class ReportCard(models.Model):
    StudentCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    ClassId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SectionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    ExamId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=10, default=None, null=True, blank=True)
    PaperId = models.CharField(max_length=10, default=None, null=True, blank=True)
    Marks = models.FloatField(default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class SubjectClass(models.Model):
    ClassId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=10, default=None, null=True, blank=True)
    FacultyId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class Syllabus(models.Model):
    ClassId = models.CharField(max_length=10, default=None, null=True, blank=True)
    ParentId = models.PositiveIntegerField(default=0)
    SectionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=10, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    ChapterNo = models.PositiveIntegerField(default=0)
    Title = models.CharField(max_length=200, default=None, null=True, blank=True)
    Completed = models.BooleanField(default=False)
    CompletedOn = models.DateField(default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class Attendance(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    StudentCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    AttendanceDate = models.DateTimeField(default=None, null=True, blank=True)
    Latitude = models.FloatField(default=None, null=True, blank=True)
    Longitude = models.FloatField(default=None, null=True, blank=True)
    Status = models.CharField(max_length=2, default=None, null=True, blank=True)
    Type = models.CharField(max_length=2, default=None, null=True, blank=True)
    MarkedBy = models.CharField(max_length=50, default=None, null=True, blank=True)

class FacultyAttendance(models.Model):
    FacultyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    AttendanceDate = models.DateTimeField(default=None, null=True, blank=True)
    Status = models.CharField(max_length=2, default=None, null=True, blank=True)
    Latitude = models.FloatField(default=0.0)
    Longitude = models.FloatField(default=0.0)
    MarkedBy = models.CharField(max_length=50, default=None, null=True, blank=True)

class AppSetting(models.Model):
    HasSection = models.BooleanField(default=False)
    FeeDate = models.PositiveIntegerField(default=1)
    LateFee = models.PositiveIntegerField(default=0)
    GeneralFee = models.FloatField(default=0)
    FacultyAttendanceDirect = models.BooleanField(default=True)
    FaceId = models.BooleanField(default=True)
    Discussion = models.BooleanField(default=True)

class SalaryRecord(models.Model):
    FacultyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    MonthYear = models.CharField(max_length=10, default=None, null=True, blank=True)
    SessionId = models.CharField(max_length=10, default=None, null=True, blank=True)
    Salary = models.PositiveIntegerField(default=0)
    Days = models.PositiveIntegerField(default=0)
    Payable= models.FloatField(default=0.0)
    Deduction = models.FloatField(default=0.0)
    Incentive = models.FloatField(default=0.0)
    NetSalary = models.FloatField(default=0.0)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=50, default=None, null=True, blank=True)

class UserPrivilege(models.Model):
    PrivilegeCode = models.CharField(max_length=10, default=None, null=True, blank=True)
    UserId = models.CharField(max_length=20, default=None, null=True, blank=True)

class FacultyRemark(models.Model):
    Sender = models.CharField(max_length=20, default=None, null=True, blank=True)
    Receiver = models.CharField(max_length=20, default=None, null=True, blank=True)
    Message = models.TextField(default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Read = models.BooleanField(default=False)
    ReadOn = models.DateTimeField(default=None, null=True, blank = True)

class HomeWork(models.Model):
    SessionId = models.CharField(max_length=5, default=None, null=True, blank=True)
    ClassId = models.CharField(max_length=5, default=None, null=True, blank=True)
    SectionId = models.CharField(max_length=5, default=None, null=True, blank=True)
    SubjectId = models.CharField(max_length=5, default=None, null=True, blank=True)
    GivenDate = models.DateField(default=None, null=True, blank=True)
    SubmitDate = models.DateField(default=None, null=True, blank=True)
    GivenBy = models.CharField(max_length=20 ,default=None, null=True, blank=True)
    Work = models.TextField(default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class MessageId(models.Model):
    UserId = models.CharField(max_length=50, default=None, null=True, blank=True)
    Token = models.TextField(default=None, null=True, blank=True)

class Role(models.Model):
    RoleCode = models.CharField(max_length=5, default=None, null=True, blank=True)
    Title = models.CharField(max_length=50, default=None, null=True, blank=True)
    Active = models.BooleanField(default=True)
    Deleted = models.BooleanField(default=False)

class RolePrivilege(models.Model):
    RoleCode = models.CharField(max_length=5, default=None, null=True, blank=True)
    PrivilegeCode = models.CharField(max_length=20, default=None, null=True, blank=True)

class Notice(models.Model):
    Title = models.CharField(max_length=500, default=None, null=True, blank=True)
    Description = models.TextField(default=None, null=True, blank=True)
    Status = models.CharField(max_length=5, default=None, null=True, blank=True)
    SendTo = models.CharField(max_length=50, default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=20, default=None, null=True, blank=True)
    SendDate = models.DateTimeField(default=None, null=True, blank=True)

class NoticeUser(models.Model):
    NoticeId = models.PositiveIntegerField(default=None, null=True, blank=True)
    UserCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    Status = models.CharField(max_length=10, default=None, null=True, blank=True)

class Bus(models.Model):
    Name = models.CharField(max_length=100, default=None, null=True, blank=True)
    BusNo = models.CharField(max_length=20, default=None, null=True, blank=True)
    DriverName = models.CharField(max_length=100, default=None, null=True, blank=True)
    Route = models.CharField(max_length=100, default=None, null=True, blank=True)
    BusFee = models.FloatField(default=None, null=True, blank=True)
    Deleted = models.BooleanField(default=False)

class Calendar(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    EventDate = models.DateField(default=None, null=True, blank=True)
    Title = models.CharField(max_length=200, default=None, null=True, blank=True)
    Type = models.CharField(max_length=10, default=None, null=True, blank=True)
    Repeat = models.CharField(max_length=10, default=None, null=True, blank=True)

class Batch(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    Title = models.CharField(max_length=100, default=None, null=True, blank=True)
    StartTime = models.TimeField(default=None, null=True, blank=True)
    EndTime = models.TimeField(default=None, null=True, blank=True)
    Fee = models.FloatField(default=0)
    Active = models.BooleanField(default=True)
    Deleted = models.BooleanField(default=False)

class LibraryMember(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    MemberCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    FullName = models.CharField(max_length=200, default=None, null=True, blank=True)
    Picture = models.CharField(max_length=100, default=None, null=True, blank=True)
    AadharNo = models.CharField(max_length=100, default=None, null=True, blank=True)
    AadharPicture = models.CharField(max_length=100, default=None, null=True, blank=True)
    Mobile = models.CharField(max_length=20, default=None, null=True, blank=True)
    Whatsapp = models.CharField(max_length=20, default=None, null=True, blank=True)
    Email = models.CharField(max_length=100, default=None, null=True, blank=True)
    Gender = models.CharField(max_length=10, default=None, null=True, blank=True)
    Status = models.CharField(max_length=2, default=None, null=True, blank=True)
    BatchId = models.PositiveIntegerField(default=None, null=True, blank=True)
    MonthlyFee = models.FloatField(default=0, null=True, blank=True)
    JoiningDate = models.DateField(default=None, null=True, blank=True)
    LeavingDate = models.DateField(default=None, null=True, blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Active = models.BooleanField(default=True)
    Deleted = models.BooleanField(default=False)

class Company(models.Model):
    CompanyCode = models.CharField(max_length=20, default=None, null=True, blank=True)
    CompanyName = models.CharField(max_length=200, default=None, null=True, blank=True)
    MemberPrefix = models.CharField(max_length=10, default=None, null=True, blank=True)
    Latitude = models.FloatField(default=None, null=True, blank=True)
    Longitude = models.FloatField(default=None, null=True, blank=True)
    Radius = models.FloatField(default=None, null=True, blank=True)
    Active = models.BooleanField(default=True)
    Deleted = models.BooleanField(default=False)