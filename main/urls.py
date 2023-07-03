from django.urls import path
from . import views

app_name = 'main'
 
urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path("dashboard", views.dashboard, name="dashboard"),
    path("faculty_list", views.faculty_list, name="faculty_list"),
    path("student_list", views.student_list, name="student_list"),
    path("settings", views.settings, name="settings"),
    path("expense", views.expense, name="expense"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("fee_collection", views.fee_collection, name="fee_collection"),
    path("class_routine", views.class_routine, name="class_routine"),
    path("faculty_routine", views.faculty_routine, name="faculty_routine"),
    path("save_faculty", views.save_faculty, name="save_faculty"),
    path("save_student", views.save_student, name="save_student"),
    path("report_card", views.report_card, name="report_card"),
    path("save_expense", views.save_expense, name="save_expense"),
    path("save_routine", views.save_routine, name="save_routine"),
    path("get_faculty_list", views.get_faculty_list, name="get_faculty_list"),
    path("get_student_list", views.get_student_list, name="get_student_list"),
    path("get_fee_list", views.get_fee_list, name="get_fee_list"),
    path("get_member_fee_list", views.get_member_fee_list, name="get_member_fee_list"),
    path("get_faculty_detail", views.get_faculty_detail, name="get_faculty_detail"),
    path("get_expense_detail", views.get_expense_detail, name="get_expense_detail"),
    path("get_expense_list", views.get_expense_list, name="get_expense_list"),
    path("get_fee_detail", views.get_fee_detail, name="get_fee_detail"),
    path("get_student_detail", views.get_student_detail, name="get_student_detail"),
    path("get_student_profile", views.get_student_profile, name="get_student_profile"),
    path("get_member_profile", views.get_member_profile, name="get_member_profile"),
    path("save_file", views.save_file, name="save_file"),
    path("change_faculty_status", views.change_faculty_status, name="change_faculty_status"),
    path("change_student_status", views.change_student_status, name="change_student_status"),
    path("get_status", views.get_status, name="get_status"),
    path("save_class", views.save_class, name="save_class"),
    path("save_section", views.save_section, name="save_section"),
    path("save_exam", views.save_exam, name="save_exam"),
    path("save_subject", views.save_subject, name="save_subject"),
    path("get_all_class", views.get_all_class, name="get_all_class"),
    path("get_all_section", views.get_all_section, name="get_all_section"),
    path("get_all_subject", views.get_all_subject, name="get_all_subject"),
    path("save_fee", views.save_fee, name="save_fee"),
    path("get_class_fee", views.get_class_fee, name="get_class_fee"),
    path("get_class_routine", views.get_class_routine, name="get_class_routine"),
    path("get_faculty_routine", views.get_faculty_routine, name="get_faculty_routine"),
    path("exam_list", views.exam_list, name="exam_list"),
    path("get_exam_list", views.get_exam_list, name="get_exam_list"),
    path("paper_list", views.paper_list, name="paper_list"),
    path("save_paper", views.save_paper, name="save_paper"),
    path("get_paper_detail", views.get_paper_detail, name="get_paper_detail"),
    path("get_paper_list", views.get_paper_list, name="get_paper_list"),
    #path("get_report_card", views.get_report_card, name="get_report_card"),
    path("save_class_subject", views.save_class_subject, name="save_class_subject"),
    path("get_class_subject", views.get_class_subject, name="get_class_subject"),
    path("save_report_card", views.save_report_card, name="save_report_card"),
    path("get_student_marks", views.get_student_marks, name="get_student_marks"),
    path("delete_item", views.delete_item, name="delete_item"),
    path("permanent_delete", views.permanent_delete, name="permanent_delete"),
    path("fee_expense_summary", views.fee_expense_summary, name="fee_expense_summary"),
    path("get_people_count", views.get_people_count, name="get_people_count"),
    path("get_member_count", views.get_member_count, name="get_member_count"),
    path("load_monthwise_expense", views.load_monthwise_expense, name="load_monthwise_expense"),
    path("attendance", views.attendance, name="attendance"),
    path("facultyattendance", views.facultyattendance, name="facultyattendance"),
    path("get_student_by_class", views.get_student_by_class, name="get_student_by_class"),
    path("save_attendance", views.save_attendance, name="save_attendance"),
    path("get_fee_detail_show", views.get_fee_detail_show, name="get_fee_detail_show"),
    path("syllabus", views.syllabus, name="syllabus"),
    path("get_syllabus", views.get_syllabus, name="get_syllabus"),
    path("save_syllabus", views.save_syllabus, name="save_syllabus"),
    path("save_chapter", views.save_chapter, name="save_chapter"),
    path("delete_chapter", views.delete_chapter, name="delete_chapter"),
    path("mark_chapter_done", views.mark_chapter_done, name="mark_chapter_done"),
    path("salary", views.salary, name="salary"),
    path("get_faculty_for_salary", views.get_faculty_for_salary, name="get_faculty_for_salary"),
    path("get_faculty_attendance", views.get_faculty_attendance, name="get_faculty_attendance"),
    path("save_faculty_attendance", views.save_faculty_attendance, name="save_faculty_attendance"),
    path("save_salary", views.save_salary, name="save_salary"),
    path("print_receipt", views.print_receipt, name="print_receipt"),
    path("faculty_dashboard_mobile", views.faculty_dashboard_mobile, name="faculty_dashboard_mobile"),
    path("attendancemobile", views.attendancemobile, name="attendancemobile"),
    path("get_student_attendance", views.get_student_attendance, name="get_student_attendance"),
    path("mark_individual_attendance", views.mark_individual_attendance, name="mark_individual_attendance"),
    path("mark_self_attendance", views.mark_self_attendance, name="mark_self_attendance"),
    path("get_faculty_dashboard", views.get_faculty_dashboard, name="get_faculty_dashboard"),
    path("print_report_card", views.print_report_card, name="print_report_card"),
    path("dashboard_mobile", views.dashboard_mobile, name="dashboard_mobile"),
    path("get_main_dashboard", views.get_main_dashboard, name="get_main_dashboard"),
    path("receipt_template/<id>", views.receipt_template, name="receipt_template"),
    path("mark_sheet", views.mark_sheet, name="mark_sheet"),
    path("mobilesyllabus", views.mobilesyllabus, name="mobilesyllabus"),
    path("get_salary_history", views.get_salary_history, name="get_salary_history"),
    path("VerifyLogin", views.VerifyLogin, name="VerifyLogin"),
    path("logmeout", views.logmeout, name="logmeout"),
    path("parent_dashboard_mobile", views.parent_dashboard_mobile, name="parent_dashboard_mobile"),
    path("get_faculty_remarks", views.get_faculty_remarks, name="get_faculty_remarks"),
    path("parent_attendance", views.parent_attendance, name="parent_attendance"),
    path("get_parent_attendance", views.get_parent_attendance, name="get_parent_attendance"),
    path("parent_syllabus", views.parent_syllabus, name="parent_syllabus"),
    path("get_parent_syllabus", views.get_parent_syllabus, name="get_parent_syllabus"),
    path("parent_report_card", views.parent_report_card, name="parent_report_card"),
    path("get_exam_by_session", views.get_exam_by_session, name="get_exam_by_session"),
    path("get_parent_report_card", views.get_parent_report_card, name="get_parent_report_card"),
    path("parent_payment", views.parent_payment, name="parent_payment"),
    path("get_parent_payment", views.get_parent_payment, name="get_parent_payment"),
    path("home_work", views.home_work, name="home_work"),
    path("get_class_section", views.get_class_section, name="get_class_section"),
    path("save_homework", views.save_homework, name="save_homework"),
    path("load_homework", views.load_homework, name="load_homework"),
    path("staff_list", views.staff_list, name="staff_list"),
    path("save_staff", views.save_staff, name="save_staff"),
    path("get_staff_list", views.get_staff_list, name="get_staff_list"),
    path("get_staff_detail", views.get_staff_detail, name="get_staff_detail"),
    path("change_staff_status", views.change_staff_status, name="change_staff_status"),
    path("faculty_homework_mobile", views.faculty_homework_mobile, name="faculty_homework_mobile"),
    path("parent_homework", views.parent_homework, name="parent_homework"),
    path("get_parent_homework", views.get_parent_homework, name="get_parent_homework"),
    path("discussion_board", views.discussion_board, name="discussion_board"),
    path("discussion_page/<otherparty>", views.discussion_page, name="discussion_page"),
    path("get_parent_faculty", views.get_parent_faculty, name="get_parent_faculty"),
    path("send_message", views.send_message, name="send_message"),
    path("load_chats", views.load_chats, name="load_chats"),
    path("get_discus_parent", views.get_discus_parent, name="get_discus_parent"),
    path("save_message_id", views.save_message_id, name="save_message_id"),
    path("get_message_token", views.get_message_token, name="get_message_token"),
    path("permission", views.permission, name="permission"),
    path("load_users", views.load_users, name="load_users"),
    path("get_user_detail", views.get_user_detail, name="get_user_detail"),
    path("save_user", views.save_user, name="save_user"),
    path("block_user", views.block_user, name="block_user"),
    path("load_privileges", views.load_privileges, name="load_privileges"),
    path("load_role_privileges", views.load_role_privileges, name="load_role_privileges"),
    path("save_permissions", views.save_permissions, name="save_permissions"),
    path("save_role_permissions", views.save_role_permissions, name="save_role_permissions"),
    path("mobile_faculty_list", views.mobile_faculty_list, name="mobile_faculty_list"),
    path("mobile_student_list", views.mobile_student_list, name="mobile_student_list"),
    path("exam_paper_mobile", views.exam_paper_mobile, name="exam_paper_mobile"),
    path("mobileattendance_faculty", views.mobileattendance_faculty, name="mobileattendance_faculty"),
    path("mobileattendance_member", views.mobileattendance_member, name="mobileattendance_member"),
    path("mobileattendance_faculty/<type>", views.mobileattendance_faculty, name="mobileattendance_faculty"),
    path("get_faculty_list_attendance", views.get_faculty_list_attendance, name="get_faculty_list_attendance"),
    path("get_staff_list_attendance", views.get_staff_list_attendance, name="get_staff_list_attendance"),
    path("mark_faculty_attendance", views.mark_faculty_attendance, name="mark_faculty_attendance"),
    path("faculty_profile", views.faculty_profile, name="faculty_profile"),
    path("faculty_profile/<faculty_id>", views.faculty_profile, name="faculty_profile"),
    path("student_profile", views.student_profile, name="student_profile"),
    path("student_profile/<student_id>", views.student_profile, name="student_profile"),
    path("faculty_routine_mobile", views.faculty_routine_mobile, name="faculty_routine_mobile"),
    path("face_test", views.face_test, name="face_test"),
    path("encrypt_face", views.encrypt_face, name="encrypt_face"),
    path("recognize_face", views.recognize_face, name="recognize_face"),
    path("get_face_data", views.get_face_data, name="get_face_data"),
    path("clear_old_face", views.clear_old_face, name="clear_old_face"),
    path("roles", views.roles, name="roles"),
    path("load_roles", views.load_roles, name="load_roles"),
    path("announcement", views.announcement, name="announcement"),
    path("send_notice", views.send_notice, name="send_notice"),
    path("get_announcements", views.get_announcements, name="get_announcements"),
    path("get_notice_detail", views.get_notice_detail, name="get_notice_detail"),
    path("mobile_notice",views.mobile_notice, name="mobile_notice"),
    path("get_user_notice", views.get_user_notice, name="get_user_notice"),
    path("calendar", views.calendar, name="calendar"),
    path("save_calendar_event", views.save_calendar_event, name="save_calendar_event"),
    path("load_calendar_events", views.load_calendar_events, name="load_calendar_events"),
    path("load_month_event", views.load_month_event, name="load_month_event"),
    path("member", views.member, name="member"),
    path("save_member", views.save_member, name="save_member"),
    path("get_member_list", views.get_member_list, name="get_member_list"),
    path("get_member_detail", views.get_member_detail, name="get_member_detail"),
    path("member_attendance", views.member_attendance, name="member_attendance"),
    path("get_member_by_batch", views.get_member_by_batch, name="get_member_by_batch"),
    path("save_member_attendance", views.save_member_attendance, name="save_member_attendance"),
    path("member_fee_collection", views.member_fee_collection, name="member_fee_collection"),
    path("change_member_status", views.change_member_status, name="change_member_status"),
    path("get_member_fee_detail_show", views.get_member_fee_detail_show, name="get_member_fee_detail_show"),
    path("mobile_member_list", views.mobile_member_list, name="mobile_member_list"),
    path("member_profile/<member_id>", views.member_profile, name="member_profile"),
    path("mobile_fee_collection", views.mobile_fee_collection, name="mobile_fee_collection"),
    path("get_member_list_attendance", views.get_member_list_attendance, name="get_member_list_attendance"),
    path("library_dashboard",views.library_dashboard, name="library_dashboard"),
    path("load_monthwise_library_revenue", views.load_monthwise_library_revenue, name="load_monthwise_library_revenue"),
    path("load_member_graph", views.load_member_graph, name="load_member_graph"),
    path("library_dashboard_mobile", views.library_dashboard_mobile, name="library_dashboard_mobile"),
    path("member_payment_record", views.member_payment_record, name="member_payment_record"),
    path("get_fee_item_detail", views.get_fee_item_detail, name="get_fee_item_detail"),
    path("member_dashboard_mobile", views.member_dashboard_mobile, name="member_dashboard_mobile"),
    path("get_member_dashboard", views.get_member_dashboard, name="get_member_dashboard"),
    path("mark_member_self_attendance", views.mark_member_self_attendance, name="mark_member_self_attendance"),    
    path("block_unblock_user", views.block_unblock_user, name="block_unblock_user"),
    path("update_member_user", views.update_member_user, name="update_member_user"),
    path("student_payment_record", views.student_payment_record, name="student_payment_record"),
]