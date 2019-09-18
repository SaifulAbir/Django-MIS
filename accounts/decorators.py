from django.contrib.auth.decorators import user_passes_test, login_required


adm_login_required = user_passes_test(lambda u: True if u.is_admin else False, login_url='/')
head_login_required = user_passes_test(lambda u: True if u.is_headmaster else False, login_url='/')
ment_login_required = user_passes_test(lambda u: True if u.is_mentor else False, login_url='/')
sklead_login_required = user_passes_test(lambda u: True if u.is_skleader else False, login_url='/')


def admin_login_required(view_func):
    decorated_view_func = login_required(adm_login_required(view_func), login_url='/')
    return decorated_view_func

def headmaster_login_required(view_func):
    decorated_view_func = login_required(head_login_required(view_func), login_url='/')
    return decorated_view_func

def mentor_login_required(view_func):
    decorated_view_func = login_required(ment_login_required(view_func), login_url='/')
    return decorated_view_func

def skleader_login_required(view_func):
    decorated_view_func = login_required(sklead_login_required(view_func), login_url='/')
    return decorated_view_func