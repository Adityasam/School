from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .helper import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings as django_settings
import os
from django.db import connection

# Create your views here.

project_folder_path = django_settings.BASE_DIR

def attendance(request):
    request.session["PAGECODE"] = "PG_00011"
    classes = Class.objects.filter(Deleted = False).order_by("Title")
    sections = Section.objects.filter(Deleted = False)
    sessions = SchoolSession.objects.filter(Deleted = False)

    context = {
        'classes': classes,
        'sections' : sections,
        'sessions' : sessions
    }
    return render(request, "attendance.html", context)

def dashboard(request):
    request.session["PAGECODE"] = "PG_00009"
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def faculty_list(request):
    request.session["PAGECODE"] = "PG_00001"
    subject = Subject.objects.filter(Deleted = False)
    context = {
        'subjects': subject
    }
    return render(request, "faculty.html", context)

def report_card(request):
    request.session["PAGECODE"] = "PG_00007"
    classes = Class.objects.filter(Deleted = False).order_by("Title")
    sections = Section.objects.filter(Deleted = False)
    exams = None
    with connection.cursor() as cursor:
        cursor.execute("""select e.*, s.Title as SessionTitle from main_Exam e
        left join main_SchoolSession s on s.id = e.SessionId
        where e.Deleted = 0""")
        exams = parse_curser(cursor)

    context = {
        'classes': classes,
        'sections' : sections,
        'exams' : exams
    }
    return render(request, "report_card.html", context)

def paper_list(request):
    request.session["PAGECODE"] = "PG_00006"
    exams = None
    papers = None
    with connection.cursor() as cursor:
        cursor.execute("""select e.*, s.Title as SessionTitle from main_Exam e
        left join main_SchoolSession s on s.id = e.Sessionid
        where e.Deleted = 0 and e.enddate > CURRENT_DATE""")
        exams = parse_curser(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""select e.*, x.Title as examtitle, s.Title as subject from main_ExamPaper e
        left join main_Exam x on x.id = e.ExamId
        left join main_Subject s on s.id = e.SubjectId
        where e.Deleted = 0""")
        papers = parse_curser(cursor)

    cls = Class.objects.filter(Deleted = False).order_by("Title")
    sections = Section.objects.filter(Deleted=False)
    subjects = Subject.objects.filter(Deleted = False)
    context = {
        'exams': exams,
        'classes' : cls,
        'subjects': subjects,
        'sections' : sections,
        'papers' : papers
    }

    return render(request, "paper_list.html", context)


def exam_list(request):
    request.session["PAGECODE"] = "PG_00004"
    sessions = SchoolSession.objects.filter(Deleted = False)
    context = {
        'sessions':sessions
    }
    return render(request, "exam_list.html", context)

def class_routine(request):
    request.session["PAGECODE"] = "PG_00003"
    subject = Subject.objects.filter(Deleted = False)
    faculty = Faculty.objects.filter(Deleted = False)
    cls = Class.objects.filter(Deleted = False).order_by("Title")
    section = Section.objects.filter(Deleted = False)
    sessions = SchoolSession.objects.filter(Deleted = False)
    context = {
        'classes': cls,
        'sections' : section,
        'subject' : subject,
        'faculty' : faculty,
        'sessions' : sessions
    }

    return render(request, "class_routine.html", context)

def expense(request):
    request.session["PAGECODE"] = "PG_00010"
    type = ExpenseType.objects.filter(Deleted = False)
    mode = PaymentMode.objects.filter(Deleted = False)
    sessions = SchoolSession.objects.filter(Deleted = False)
    context = {
        'type': type,
        'modes' : mode,
        'sessions' : sessions
    }
    return render(request, "expense.html", context)

def student_list(request):
    request.session["PAGECODE"] = "PG_00002"
    classes = Class.objects.filter(Deleted = False).order_by("Title")
    sections = Section.objects.filter(Deleted = False)
    context = {
        'classes': classes,
        'sections' : sections
    }
    return render(request, "student.html", context)

def settings(request):
    request.session["PAGECODE"] = "PG_00008"
    faculty = Faculty.objects.filter(Deleted = False)
    faculty = parse_data(faculty)
    cls = Class.objects.filter(Deleted=False).order_by("Title")
    subject = Subject.objects.filter(Deleted = False)
    sess = SchoolSession.objects.filter(Deleted = False)
    context = {
        'faculty': faculty,
        'classes': cls,
        'subjects': subject,
        'sessions' : sess
    }
    return render(request, "settings.html", context)

def fee_collection(request):
    request.session["PAGECODE"] = "PG_00005"
    student = Student.objects.filter(Deleted = False)
    mode = PaymentMode.objects.filter(Deleted = False)
    feetype = FeeType.objects.filter(Deleted = False)
    sessions = SchoolSession.objects.filter(Deleted = False)
    context = {
        'students': student,
        'modes': mode,
        'feetype': feetype,
        'sessions' : sessions
    }
    return render(request, "fee_collection.html", context)

@csrf_exempt
def save_class(request):
    cls = None
    if "classid" in request.POST:
        cls = Class.objects.filter(id = request.POST.get("classid"))
        cls = cls[0]
    else:
        cls = Class()
    cls.ClassTeacher = request.POST.get("faculty")
    cls.Title = request.POST.get("title")
    cls.HasSections = request.POST.get("hassection")
    cls.ClassFee = request.POST.get("fee")
    cls.save()

    return JsonResponse({"classid":str(cls.id)})

@csrf_exempt
def save_subject(request):
    cls = None
    if "subjectid" in request.POST:
        cls = Subject.objects.filter(id = request.POST.get("subjectid"))
        cls = cls[0]
    else:
        cls = Subject()

    cls.Title = request.POST.get("title")
    cls.save()

    return JsonResponse({"subjectid":str(cls.id)})

@csrf_exempt
def save_exam(request):
    exam = None
    if "examid" in request.POST:
        exam = Exam.objects.filter(id = request.POST.get("examid"))
        exam = exam[0]
    else:
        exam = Exam()

    exam.Title = request.POST.get("title")
    exam.SessionId= request.POST.get("sessionid")
    exam.StartDate = request.POST.get("startdate")
    exam.EndDate = request.POST.get("enddate")
    exam.Remarks = request.POST.get("remarks")
    exam.CreatedBy = "admin"
    exam.save()

    return JsonResponse({"examid":str(exam.id)})

@csrf_exempt
def save_paper(request):
    paper = None
    if "paperid" in request.POST:
        paper = ExamPaper.objects.filter(id = request.POST.get("paperid"))
        paper = paper[0]
    else:
        paper = ExamPaper()

    print(request.POST.get("section"))
    paper.SubjectId = request.POST.get("subject")
    paper.ClassId = request.POST.get("class")
    paper.TotalMarks = request.POST.get("totalmarks")
    paper.SectionId = request.POST.get("section")
    if "paperdate" in request.POST:
        paper.PaperDate = request.POST.get("paperdate")
    else:
        paper.PaperDate = None
    paper.CreatedBy = "admin"
    paper.ExamId = request.POST.get("exam")
    paper.Content = request.POST.get("content")
    paper.CreatedBy = "admin"
    paper.save()

    return JsonResponse({"paperid":str(paper.id)})

@csrf_exempt
def get_exam_list(request):
    sessionid = request.POST.get("sessionid")
    alldata = None
    with connection.cursor() as cursor:
        cursor.execute("""select *, (case when e.enddate < CURRENT_DATE then '1' else '0' end) as Finished
        from main_Exam e
        where e.Deleted = 0 and e.SessionId = %s""", [sessionid])
        alldata = parse_curser(cursor)
    return JsonResponse(alldata, safe=False)

@csrf_exempt
def save_routine(request):
    rout = None
    if "routineid" in request.POST:
        rout = Routine.objects.filter(id = request.POST.get("routineid"))
        rout = rout[0]
    else:
        rout = Routine()

    rout.SessionId = request.POST.get("sessionid")
    rout.ClassId = request.POST.get("class")
    rout.SectionId = request.POST.get("section")
    rout.SubjectId = request.POST.get("subject")
    rout.FacultyId = request.POST.get("faculty")
    rout.Day = request.POST.get("day")
    rout.StartTime = request.POST.get("starttime")
    rout.EndTime = request.POST.get("endtime")
    rout.CreatedBy = "admin"
    rout.save()

    return JsonResponse({"status":"success"})

@csrf_exempt
def save_section(request):
    cls = None
    if "sectionid" in request.POST:
        cls = Section.objects.filter(id = request.POST.get("sectionid"))
        cls = cls[0]
    else:
        cls = Section()

    cls.ClassTeacher = request.POST.get("faculty")
    cls.Title = request.POST.get("title")
    cls.ClassId = request.POST.get("classid")
    cls.RoomNo = request.POST.get("roomno")
    cls.save()

    return JsonResponse({"sectionid":str(cls.id)})

@csrf_exempt
def get_class_subject(request):
    cls = request.POST.get("classid")
    sectionid = request.POST.get("sectionid")
    sessionid = request.POST.get("sessionid")
    examid = request.POST.get("examid")

    student = None
    subjects = None

    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCT r.id as paperid, s.Title
        from main_ExamPaper r
        inner join main_Exam ex on ex.id = r.ExamId
        inner join main_Subject s on s.id = r.SubjectId
        where r.ClassId=%s and (r.SectionId='' or r.SectionId is null or r.SectionId like %s) and ex.SessionId=%s''', [cls, '%'+sectionid+'%', sessionid])

        subjects = parse_curser(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""select s.FullName, s.StudentCode
        from main_Student s
        where s.Deleted = 0 and s.Class=%s and s.Section = %s""", [cls, sectionid])
        student = parse_curser(cursor)

    return JsonResponse({"students":student, "subs": subjects})

@csrf_exempt
def get_student_marks(request):
    studentcode = request.POST.get("studentcode")
    papers = request.POST.get("papers").split("^")
    alldata = {}
    print(papers[:-1])
    for p in papers[:-1]:
        res = ReportCard.objects.filter(PaperId = p, StudentCode = studentcode)
        if len(res) > 0:
            alldata[p] = res[0].Marks
    return JsonResponse(alldata, safe=False)

@csrf_exempt
def get_student_by_class(request):
    classid = request.POST.get("classid")
    sectionid = request.POST.get("sectionid")
    sessionid = request.POST.get("sessionid")

    alldata = None
    with connection.cursor() as cursor:
        cursor.execute('''select s.StudentCode, s.FullName, s.id,
        (select GROUP_CONCAT(a.AttendanceDate|| '#' || a.Status, '^') from main_Attendance a 
        where a.StudentCode = s.StudentCode and a.SessionId = %s) as attendancedata 
        from main_Student s
        where Class=%s and Section=%s''', [sessionid ,classid, sectionid])

        alldata = parse_curser(cursor)

    return JsonResponse(alldata, safe=False)

@csrf_exempt
def save_attendance(request):
    mon = request.POST.get("month").split("-")
    data = request.POST.get("datastring")
    sessionid = request.POST.get("sessionid")

    spl = data.split("!")

    for s in spl[:-1]:
        sp = s.split("#")
        code = sp[0]
        att = sp[1].split("^")

        #Deleting old data
        old = Attendance.objects.filter(SessionId = sessionid, AttendanceDate__year = mon[0], AttendanceDate__month = mon[1], StudentCode = code)
        old.delete()

        ##saving the data
        ind = 0
        for a in att[:-1]:
            ind+=1
            if a != "O":
                attendance = Attendance()
                attendance.StudentCode = code
                attendance.Status = a
                attendance.SessionId = sessionid
                attendance.SessionId = sessionid
                attendance.AttendanceDate = mon[0]+"-"+mon[1]+"-"+'{:02d}'.format(ind)
                attendance.MarkedBy = "admin"
                attendance.save()

    return JsonResponse({"status": "success"})

@csrf_exempt
def get_class_fee(request):
    cls = Class.objects.get(id = request.POST.get("classid"))
    classfee = 0
    if cls is not None:
        classfee = cls.ClassFee
    return JsonResponse(classfee, safe=False)

@csrf_exempt
def get_class_routine(request):
    cls = request.POST.get("class")
    sec = request.POST.get("section")
    day = request.POST.get("day")
    sessionid = request.POST.get("sessionid")

    rout = None
    with connection.cursor() as cursor:
        cursor.execute("""select r.*, c.Title as SubjectTitle, f.FirstName as firstname, f.MiddleName as middlename, f.LastName as lastname
        from main_Routine r
        left join main_Subject c on c.id = r.SubjectId
        left join main_Faculty f on f.FacultyCode = r.FacultyId
        where r.Classid = %s and (r.sectionid = '' or r.sectionid = %s) and r.day = %s and r.SessionId=%s
        order by r.starttime""", [cls, sec, day, sessionid])

        rout = parse_curser(cursor)
    return JsonResponse({"data":rout})

@csrf_exempt
def get_all_class(request):
    alldata = None
    with connection.cursor() as cursor:
        cursor.execute("""select c.*,
        (select COUNT(s.id) from main_SubjectClass s where c.id = s.ClassId and s.SessionId = """ + current_session() + """) as totalsubjects
        from main_Class c
        where c.Deleted = 0
        order by c.Title""")

        alldata = parse_curser(cursor)
    return JsonResponse({"data":alldata})

@csrf_exempt
def get_all_section(request):
    cls = Section.objects.filter(Deleted = False)
    alldata = parse_data(cls)
    return JsonResponse({"data":alldata})

@csrf_exempt
def get_all_subject(request):
    cls = Subject.objects.filter(Deleted = False)
    alldata = parse_data(cls)
    return JsonResponse({"data":alldata})

@csrf_exempt
def save_fee(request):
    fee = Fee()
    if "feeid" in request.POST:
        fee = Fee.objects.filter(id = request.POST.get("feeid"))
        if len(fee) > 0:
            fee = fee[0]
        else:
            fee = Fee()

    fee.StudentCode = request.POST.get("student")
    fee.Type = request.POST.get("feetype")
    fee.MonthYear = request.POST.get("monthyear")
    fee.DocumentDate = request.POST.get("collectdate")
    fee.Amount = request.POST.get("amount")
    fee.Discount = request.POST.get("discount")
    fee.Fine = request.POST.get("fine")
    fee.Mode = request.POST.get("mode")
    fee.TotalAmount = request.POST.get("total")
    fee.Remarks = request.POST.get("remarks")
    fee.ReferenceNo = request.POST.get("refno")
    fee.CreatedBy = "admin"
    fee.SessionId = request.POST.get("modalsession")
    fee.save()
    newid = fee.id
    fee.DocumentCode = "REC-"+'{:05d}'.format(newid)
    fee.save()

    return JsonResponse({"status": "success"})

@csrf_exempt
def save_class_subject(request):
    classid = request.POST.get("classid")
    sessionid = request.POST.get("sessionid")
    datastring = request.POST.get("datastring").split("#")

    old = SubjectClass.objects.filter(ClassId = classid, SessionId = sessionid)
    old.delete()
    for data in datastring:
        subclass = SubjectClass()
        subclass.ClassId = classid
        subclass.SessionId = sessionid

        subfac = data.split("^")
        subclass.SubjectId = subfac[0]
        subclass.FacultyId = subfac[1]
        subclass.save()

    return JsonResponse({"status":"success"})

@csrf_exempt
def save_expense(request):
    exp = Expense()
    if "expenseid" in request.POST:
        exp = Expense.objects.filter(ExpenseCode = request.POST.get("expenseid"))
        if len(exp) > 0:
            exp = exp[0]
        else:
            exp = Expense()

    exp.SessionId = request.POST.get("sessionid")
    exp.DocumentDate = request.POST.get("expensedate")
    exp.Amount = request.POST.get("amount")
    exp.DocumentNo = request.POST.get("docno")
    exp.SessionId = request.POST.get("modalsession")
    exp.CreatedBy = "admin"
    exp.Type = request.POST.get("expensetype")
    exp.InvoiceCopy = request.POST.get("invoice")
    exp.Remarks = request.POST.get("remarks")
    exp.Mode = request.POST.get("mode")
    exp.ReferenceNo = request.POST.get("refno")
    exp.save()
    newid = exp.id
    newcode = "EXP-"+'{:05d}'.format(newid)
    exp.ExpenseCode = newcode
    exp.save()

    return JsonResponse({"code": newcode})


@csrf_exempt
def save_faculty(request):
    faculty = Faculty()

    if "facultycode" in request.POST:
        faculty = Faculty.objects.filter(FacultyCode = request.POST.get("facultycode"))
        if len(faculty) > 0:
            faculty = faculty[0]
            newcode = faculty.FacultyCode
        else:
            faculty = Faculty()

    firstname = request.POST.get("firstname")
    middlename = request.POST.get("middlename")
    lastname = request.POST.get("lastname")

    if firstname is None:
        firstname = ""
    if middlename is None:
        middlename = ""
    if lastname is None:
        lastname = ""

    faculty.FirstName = firstname
    faculty.MiddleName = middlename
    faculty.LastName = lastname
    faculty.FullName = firstname + " " + middlename + " "+lastname
    faculty.AadharNo = request.POST.get("aadhar")
    faculty.JoiningDate = request.POST.get("joiningdate")
    faculty.Active = True
    faculty.Photo = request.POST.get("photo")
    faculty.BankAccountNo = request.POST.get("bankaccount")
    faculty.BankCode = request.POST.get("bankcode")
    faculty.CreatedBy = "admin"
    faculty.DateOfBirth = request.POST.get("dob")
    faculty.Education = request.POST.get("education")
    faculty.EmailId = request.POST.get("email")
    faculty.Gender =request.POST.get("gender")
    faculty.IFSC = request.POST.get("ifsc")
    faculty.Mobile = request.POST.get("mobile")
    faculty.Whatsapp = request.POST.get("whatsapp")
    faculty.Salary = request.POST.get("salary")
    faculty.Experience = request.POST.get("experience")
    faculty.NameInBank = request.POST.get("nameinbank")
    faculty.Status = 'A'
    faculty.save()
    newid = faculty.id
    newcode = "FAC-"+'{:05d}'.format(newid)
    faculty.FacultyCode = newcode
    faculty.save()

    FacultySubject.objects.filter(FacultyCode = newcode).delete()
    subjects = request.POST.get("subjects").split("^")
    for s in subjects:
        if s != "":
            su = FacultySubject()
            su.FacultyCode = newcode
            su.SubjectId = s
            su.save()

    return JsonResponse({"code":newcode})

@csrf_exempt
def save_student(request):
    student = Student()

    if "studentcode" in request.POST:
        student = Student.objects.filter(StudentCode = request.POST.get("studentcode"))
        if len(student) > 0:
            student = student[0]
            newcode = student.StudentCode
        else:
            student = Student()
            student.StudentCode = newcode

    firstname = request.POST.get("firstname")
    middlename = request.POST.get("middlename")
    lastname = request.POST.get("lastname")

    if firstname is None:
        firstname = ""
    if middlename is None:
        middlename = ""
    if lastname is None:
        lastname = ""

    student.RollNumber = request.POST.get("rollnumber")
    student.FirstName = firstname
    student.MiddleName = middlename
    student.LastName = lastname
    student.FullName = firstname + " " + middlename + " "+lastname
    student.AadharNo = request.POST.get("aadhar")
    student.Active = True
    student.Photo = request.POST.get("photo")
    student.CreatedBy = "admin"
    student.DateOfBirth = request.POST.get("dob")
    student.Section = request.POST.get("section")
    student.EmailId = request.POST.get("email")
    student.Gender =request.POST.get("gender")
    student.FatherName = request.POST.get("fathername")
    student.MotherName = request.POST.get("mothername")
    student.Mobile = request.POST.get("mobile")
    student.Whatsapp = request.POST.get("whatsapp")
    student.Class = request.POST.get("class")
    student.Status = 'A'
    student.save()
    newid = student.id
    newcode = "STD-"+'{:05d}'.format(newid)
    student.StudentCode = newcode
    student.save()
    return JsonResponse({"code":newcode})

@csrf_exempt
def get_faculty_list(request):
    status = request.POST.get("status")
    search = request.POST.get("search")
    alldata = None
    with connection.cursor() as cursor:
        cursor.execute("""select f.*,
        (select GROUP_CONCAT(s.Title, ', ') from main_FacultySubject fs
        left join main_Subject s on s.id = fs.SubjectId
        where fs.FacultyCode = f.FacultyCode) as SubjectName
        from main_Faculty f
        where f.FullName like %s and f.status = %s and f.Deleted=0""", ['%'+search+'%', status])

        alldata = parse_curser(cursor)
    return JsonResponse(alldata, safe=False)

@csrf_exempt
def get_student_list(request):
    status = request.POST.get("status")
    search = request.POST.get("search")
    cls = request.POST.get("class")
    alldata = []
    with connection.cursor() as cursor:
        cursor.execute("""select s.*, c.Title as classtitle, ' - ' ||t.Title as SectionTitle from main_Student s
        left join main_Class c on c.id = s.Class
        left join main_Section t on t.id = s.Section
        where s.Deleted = 0 and s.Status = %s and s.FullName like %s and (%s = '' or %s = s.Class)
        order by s.Class desc, s.RollNumber""",
        [status,"%"+search+"%" ,cls, cls])

        alldata = parse_curser(cursor)
    return JsonResponse(alldata, safe=False)

@csrf_exempt
def save_report_card(request):
    classid = request.POST.get("classid")
    sectionid = request.POST.get("sectionid")
    examid = request.POST.get("examid")
    datastring = request.POST.get("datastring")

    datasplit = datastring.split("#")
    for data in datasplit[:-1]:
        sp1 = data.split("*")
        scode = sp1[0]
        markstring = sp1[1]
        marksplit = sp1[1].split(">")

        old = ReportCard.objects.filter(ExamId = examid, StudentCode = scode)
        old.delete()

        for m in marksplit:
            if m != "":
                report = ReportCard()
                report.StudentCode = scode
                report.ExamId = examid
                report.ClassId = classid
                report.SectionId = sectionid
                report.PaperId = m.split("/")[0]
                report.Marks = m.split("/")[1]
                report.save()

    return JsonResponse({"status":"success"})

@csrf_exempt
def get_fee_list(request):
    search = request.POST.get("search")
    sessionid = request.POST.get("sessionid")
    alldata = []
    with connection.cursor() as cursor:
        cursor.execute("""select f.*, s.FullName as StudentName,
          m.Title as ModeTitle, t.Title as TypeTitle, c.Title as classTitle, f.DocumentCode as docoumentcode
        from main_Fee f
        left join main_Student s on s.StudentCode = f.StudentCode
        left join main_Class c on c.id = s.Class
        left join main_PaymentMode m on m.id = f.Mode
        left join main_FeeType t on t.id = f.Type
        where f.Deleted = 0 and s.FullName like %s and f.SessionId=%s""", ['%'+search+'%', sessionid])

        alldata = parse_curser(cursor)
    return JsonResponse(alldata, safe=False)

@csrf_exempt
def get_faculty_detail(request):
    faculty = Faculty.objects.filter(FacultyCode = request.POST.get("facultycode"))
    dt = parse_data(faculty)[0]
    subjects = []
    with connection.cursor() as cursor:
            cursor.execute('''SELECT s.* FROM main_Faculty f
            left join main_FacultySubject fs on f.FacultyCode=fs.FacultyCode
            left join main_Subject s on s.id = fs.SubjectId
            WHERE f.FacultyCode=%s''', [request.POST.get('facultycode')])

            subjects = parse_curser(cursor)
    return JsonResponse({"data":dt, "subjects":subjects})

@csrf_exempt
def get_expense_detail(request):
    expense = Expense.objects.filter(ExpenseCode = request.POST.get("expensecode"))
    dt = parse_data(expense)[0]
    return JsonResponse({"data":dt})

@csrf_exempt
def get_paper_detail(request):
    paper = ExamPaper.objects.filter(id = request.POST.get("paperid"))
    alldata = parse_data(paper)[0]

    return JsonResponse(alldata, safe=False)

@csrf_exempt
def get_paper_list(request):
    alldata = None
    with connection.cursor() as cursor:
        cursor.execute("""select p.*, s.Title as Subject, c.Title as Class,
        ' - '||t.Title as Section, e.Title as Exam, (case when p.paperdate < CURRENT_DATE then '1' else '0' end) as Finished
        from main_ExamPaper p
        left join main_Subject s on s.id = p.subjectid
        left join main_Class c on c.id = p.ClassId
        left join main_Section t on t.id = p.SectionId
        left join main_Exam e on e.id = p.ExamId
        where p.Deleted = 0 order by paperdate desc""")

        alldata = parse_curser(cursor)

    return JsonResponse(alldata, safe=False)

@csrf_exempt
def get_expense_list(request):
    search = request.POST.get("search")
    sessionid = request.POST.get("sessionid")
    alldata = []
    with connection.cursor() as cursor:
            cursor.execute('''SELECT e.*, t.Title as typetitle FROM main_Expense e
            left join main_ExpenseType t on e.Type = t.id
            WHERE e.Sessionid = %s and e.Deleted=0 and (e.expensecode like %s or t.Title like %s)''',
            [sessionid,"%"+search+"%", "%"+search+"%"])

            alldata = parse_curser(cursor)
    return JsonResponse(alldata, safe=False)


@csrf_exempt
def get_student_detail(request):
    student = Student.objects.filter(StudentCode = request.POST.get("studentcode"))
    dt = parse_data(student)[0]
    return JsonResponse({"data":dt})

@csrf_exempt
def get_fee_detail(request):
    fee = Fee.objects.filter(id = request.POST.get("feeid"))
    dt = parse_data(fee)[0]
    return JsonResponse({"data":dt})

@csrf_exempt
def save_file(request):
    if "myfile" in request.FILES:
        myfile = request.FILES["myfile"]
        fs = FileSystemStorage(location=django_settings.STATIC_ROOT + '/uploads')
        newname = generate_id(15)+"."+myfile.name.split(".")[-1]
        filename = fs.save(newname, myfile)
        # file = request.FILES["myfile"]
        # newname = generate_id(15)+"."+file.name.split(".")[-1]

        # file_path = os.path.join('uploads', newname)
        # with open(file_path, 'wb+') as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)
        return JsonResponse({"name":newname})
    else:
        return JsonResponse({"name":"Not Found"})

@csrf_exempt
def change_faculty_status(request):
    code = request.POST.get("facultycode")
    status = request.POST.get("status")

    faculty=Faculty.objects.filter(FacultyCode = code)
    if len(faculty) > 0:
        faculty = faculty[0]
        faculty.Status = status
        faculty.save()

    return JsonResponse({"status":"success"})

@csrf_exempt
def change_student_status(request):
    code = request.POST.get("studentcode")
    status = request.POST.get("status")

    faculty=Student.objects.filter(StudentCode = code)
    if len(faculty) > 0:
        faculty = faculty[0]
        faculty.Status = status
        faculty.save()

    return JsonResponse({"status":"success"})

@csrf_exempt
def get_status(request):
    type = request.POST.get("type")
    status = StatusMaster.objects.filter(Type = type)
    table = None
    data = []
    if type == "FACULTY":
        table = Faculty.objects.filter(Deleted = False)
    elif type == "STUDENT":
        table = Student.objects.filter(Deleted = False)

    for s in status:
        count = 0
        for f in table:
            if f.Status == s.StatusCode:
                count+=1

        data.append([s.StatusCode, s.Title, count])

    return JsonResponse({"data":data})

@csrf_exempt
def fee_expense_summary(request):
    month = request.POST.get("month")

    allfee = []
    with connection.cursor() as cursor:
        cursor.execute('''select cast(f.DocumentDate as varchar(30)) as newdate, f.Amount from main_Fee f''')
        allfee = parse_curser(cursor)

    totalfee = 0
    for data in allfee:
        if data["newdate"][:7] == month:
            am = float(data["amount"])
            totalfee  = totalfee + am

    allexpense = []
    with connection.cursor() as cursor:
        cursor.execute('''select cast(f.DocumentDate as varchar(30)) as newdate, f.Amount from main_Expense f''')
        allexpense = parse_curser(cursor)

    totalexpense = 0
    for data in allexpense:
        if data["newdate"][:7] == month:
            am = float(data["amount"])
            totalexpense  = totalexpense + am

    return JsonResponse({"fee":totalfee, "expense":totalexpense})

@csrf_exempt
def get_people_count(request):
    dt = request.POST.get("date")

    fac = Faculty.objects.filter(Deleted = False, Status= 'A')
    staff = Staff.objects.filter(Deleted = False, Status= 'A')
    student = Student.objects.filter(Deleted = False, Status= 'A')

    return JsonResponse({"totalfaculty": len(fac) ,"totalstudent": len(student), "totalstaff": len(staff)})

@csrf_exempt
def load_monthwise_expense(request):
    allexpense = []
    
    with connection.cursor() as cursor:
        cursor.execute('''select *, cast(DocumentDate as varchar(30)) as newdate from main_Expense
        where Deleted = 0''')
        
        expense = parse_curser(cursor)

        for i in range(1,13):
            mn = "2023-"+'{:02d}'.format(i)
            monthdata = 0
            for e in expense:
                if e["newdate"][:7] == mn:
                    am = float(e["amount"])
                    monthdata += am

            allexpense.append(monthdata)

    return JsonResponse({"data":allexpense})

@csrf_exempt
def delete_item(request):
    id = request.POST.get("id")
    table = request.POST.get("table")
    with connection.cursor() as cursor:
        sql = "UPDATE main_{} SET Deleted = 1 WHERE id = %s".format(table)
        cursor.execute(sql, [id])

    return JsonResponse({"status": "success"})

@csrf_exempt
def permanent_delete(request):
    id = request.POST.get("id")
    table = request.POST.get("table")

    with connection.cursor() as cursor:
        sql = "delete from main_{} WHERE id = %s".format(table)
        cursor.execute(sql, [id])

    return JsonResponse({"status": "success"})