from main.models import *
from main.helper import *

def get_active_session(request):
    ses = SchoolSession.objects.filter(Deleted = False, Active=True)
    activesession = ""
    activesessionid = ""
    if len(ses) > 0:
        activesession = ses[0].Title
        activesessionid = ses[0].id

    return {"activesession":activesession, "activesessionid":activesessionid}

def get_menu(request):
    menu = Menu.objects.filter(Visible=True).order_by("-SortOrder")
    menu = parse_data(menu)

    return {"menu": menu}
