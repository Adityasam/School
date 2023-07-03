from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['FacultyCode','FirstName', 'MiddleName', 'LastName']

admin.site.register(Faculty, FacultyAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['StudentCode','FirstName', 'MiddleName', 'LastName']

admin.site.register(Student, StudentAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['UserId', 'EmployeeCode']

admin.site.register(MyUser, MyUserAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ['StatusCode', 'Title']

admin.site.register(StatusMaster, StatusAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Class, ClassAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Section, SectionAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Subject, SubjectAdmin)

class FacultySubjectAdmin(admin.ModelAdmin):
    list_display = ['FacultyCode']

admin.site.register(FacultySubject, FacultySubjectAdmin)

class FeeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['DocumentCode', 'StudentCode', 'CreatedDate']

admin.site.register(Fee, FeeAdmin)

class ModeAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(PaymentMode, ModeAdmin)

class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(FeeType, FeeTypeAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['ExpenseCode']

admin.site.register(Expense, ExpenseAdmin)

class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(ExpenseType, ExpenseTypeAdmin)

class RoutineAdmin(admin.ModelAdmin):
    list_display = ['ClassId', 'SectionId']

admin.site.register(Routine, RoutineAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Exam, ExamAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display = ['SubjectId', 'ClassId']

admin.site.register(ExamPaper, PaperAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['StudentCode', 'ExamId']

admin.site.register(ReportCard, ReportCardAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Active']

admin.site.register(SchoolSession, SessionAdmin)

class SubClassAdmin(admin.ModelAdmin):
    list_display = ['SubjectId', 'ClassId', "SessionId"]

admin.site.register(SubjectClass, SubClassAdmin)

class MenuAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['PageCode', 'Title', 'SortOrder', 'ForAdmin', 'PageUrl', 'Description']
    list_editable = ['SortOrder','ForAdmin', 'Description']

admin.site.register(Menu, MenuAdmin)

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['Title', "ClassId", 'SectionId', 'Completed']
    list_editable = ['Completed']

admin.site.register(Syllabus, SyllabusAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['StudentCode', "AttendanceDate"]

admin.site.register(Attendance, AttendanceAdmin)

class FacultyAttendanceAdmin(admin.ModelAdmin):
    list_display = ['FacultyCode', "AttendanceDate"]

admin.site.register(FacultyAttendance, FacultyAttendanceAdmin)

class FeeItemAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['FeeId', "TotalAmount"]

admin.site.register(FeeItem, FeeItemAdmin)

class AppSettingAdmin(admin.ModelAdmin):
    list_display = ['HasSection', "LateFee"]

admin.site.register(AppSetting, AppSettingAdmin)

class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ['FacultyCode', "MonthYear"]

admin.site.register(SalaryRecord, SalaryRecordAdmin)

class UserPrivilegeAdmin(admin.ModelAdmin):
    list_display = ['UserId', "PrivilegeCode"]

admin.site.register(UserPrivilege, UserPrivilegeAdmin)

class FacultyRemarkAdmin(admin.ModelAdmin):
    list_display = ['Sender', "Receiver"]

admin.site.register(FacultyRemark, FacultyRemarkAdmin)

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['GivenBy', "ClassId"]

admin.site.register(HomeWork, HomeWorkAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ['StaffCode']

admin.site.register(Staff, StaffAdmin)

class DesignationAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Designation, DesignationAdmin)

class MessageIdAdmin(admin.ModelAdmin):
    list_display = ['UserId']

admin.site.register(MessageId, MessageIdAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ['Title', "RoleCode"]

admin.site.register(Role, RoleAdmin)

class RolePrivilegeAdmin(admin.ModelAdmin):
    list_display = ['RoleCode', "PrivilegeCode"]

admin.site.register(RolePrivilege, RolePrivilegeAdmin)

class BusAdmin(admin.ModelAdmin):
    list_display = ['Name', "BusNo"]

admin.site.register(Bus, BusAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Notice, NoticeAdmin)

class NoticeUserAdmin(admin.ModelAdmin):
    list_display = ['UserCode', "NoticeId"]

admin.site.register(NoticeUser, NoticeUserAdmin)

class CalendarAdmin(admin.ModelAdmin):
    list_display = ["Title", 'EventDate']

admin.site.register(Calendar, CalendarAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_display = ["Title", 'StartTime', "EndTime"]

admin.site.register(Batch, BatchAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ["MemberCode", 'FullName']

admin.site.register(LibraryMember, MemberAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["CompanyCode", 'CompanyName']

admin.site.register(Company, CompanyAdmin)