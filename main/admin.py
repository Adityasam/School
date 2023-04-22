from django.contrib import admin
from .models import *
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

class FeeAdmin(admin.ModelAdmin):
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

class MenuAdmin(admin.ModelAdmin):
    list_display = ['PageCode', 'Title', 'SortOrder']
    list_editable = ['SortOrder']

admin.site.register(Menu, MenuAdmin)

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['Title', "ClassId", 'SectionId', 'Completed']
    list_editable = ['Completed']

admin.site.register(Syllabus, SyllabusAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['StudentCode', "AttendanceDate"]

admin.site.register(Attendance, AttendanceAdmin)