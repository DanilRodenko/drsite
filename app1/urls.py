from django.urls import path
from app1.views import  main_page, login_user, do_logout, registration, users_login,\
    ajax_path, check_login, check_mail, register,register_with_ajax, news_page, trading_pairs
urlpatterns = [
    path('users_name', users_login),
    path('trading_pairs', trading_pairs),
    path('main_page', main_page),
    path('login', login_user),
    path('logout', do_logout),
    path('register', register),
    path('registration', registration),
    path('ajax_path', ajax_path),
    path('check_login', check_login),
    path('check_mail', check_mail),
    path('register_with_ajax', register_with_ajax),
    path('news', news_page)
]