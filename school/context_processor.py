from main.models import *
from main.helper import *
from django.db import connection

def get_active_session(request):
    ses = SchoolSession.objects.filter(Deleted = False, Active=True)
    activesession = ""
    activesessionid = ""
    if len(ses) > 0:
        activesession = ses[0].Title
        activesessionid = ses[0].id

    return {"activesession":activesession, "activesessionid":activesessionid}

def get_menu(request):
    menu = None
    if "USERID" in request.session:
        if request.session["SUPERADMIN"] == True:
            with connection.cursor() as cursor:
                cursor.execute("""select m.* from main_Menu m
                where ((m.Desktop=1 and 'D'=%s) or (m.Mobile=1 and 'M'=%s)) and m.Visible = 1 and m.ForAdmin = 1
                order by SortOrder desc""", 
                [request.session["LOGINFROM"], request.session["LOGINFROM"]])
                menu = parse_curser(cursor)
        else:
            with connection.cursor() as cursor:
                cursor.execute("""select m.* from main_Menu m
                inner join main_UserPrivilege p on p.UserId = %s and m.PageCode = p.PrivilegeCode 
                where ((m.Desktop=1 and 'D'=%s) or (m.Mobile=1 and 'M'=%s))  and m.Visible = 1
                order by SortOrder desc""", 
                [request.session["USERID"], request.session["LOGINFROM"], request.session["LOGINFROM"]])
                menu = parse_curser(cursor)

    return {"menu": menu}

def get_mobile_menu(request):
    menu = Menu.objects.filter(Visible=True, Mobile=True).order_by("-SortOrder")
    menu = parse_data(menu)

    return {"mobilemenu": menu}

def get_settings(request):
    set = AppSetting.objects.filter()[:1].get()

    request.session["HasSection"] = set.HasSection
    request.session["LateFee"] = set.LateFee
    request.session["FeeDate"] = set.FeeDate
    request.session["FacultyAttendanceDirect"] = set.FacultyAttendanceDirect
    request.session["generalfee"] = set.GeneralFee
    request.session["faceid"] = set.FaceId
    request.session["discussion"] = set.Discussion
    
    return {"latefee":set.LateFee, "feedate":set.FeeDate, "hassection":set.HasSection, 
            "facultydirect":set.FacultyAttendanceDirect, "generalfee":set.GeneralFee, "faceid":set.FaceId, "discussion":set.Discussion}

def get_company_detail(request):
    if "COMPANY" in request.session:
        companycode = request.session["COMPANY"]

        comp = Company.objects.filter(CompanyCode = companycode)

        if len(comp) > 0:
            comp = comp[0]
            request.session["complatitude"] = comp.Latitude
            request.session["complatitude"] = comp.Longitude
            request.session["radius"] = comp.Radius

            return {"complatitude":comp.Latitude, "complongitude":comp.Longitude, "radius": comp.Radius}
        else:
            return {"testdata":""}
    else:
        return {"testdata":""}

def unread_message(request):
    if "USERID" in request.session:
        msg = FacultyRemark.objects.filter(Receiver = request.session["USERID"], Read = False)
        if len(msg) > 0:
            return {"unread":"1"}
        else:
            return {"unread":"0"}
    else:
        return {"unread" : "0"}
    
def get_company(request):
    comp = Company.objects.filter(Deleted = False, Active=True)
    return {'companies':comp}