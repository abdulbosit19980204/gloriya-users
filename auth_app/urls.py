from django.urls import path
from .views import login_view, signup_view, lock_screen_view, logout_view, user_setting_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('lock-screen/', lock_screen_view, name='lock_screen'),
    path('user-settings/', user_setting_view, name='user_settings'),
    path('logout/', logout_view),
]
