from django.contrib import admin
from django.urls import path, include
from hotel_home import views as home_view
from rooms import views as rooms_view
from reservations import views as reservation_view
from Info import views as info_views
from user_auth import views as auth_views
from django.contrib.auth import views as django_auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home, name="home"),
    path('rooms/', rooms_view.rooms, name="rooms"),
    path('rooms/reservation/', reservation_view.reservation, name="reservation"),
    path('info/', info_views.about_us, name="about_us"),
    path('contact_us/', info_views.contact_us, name="contact_us"),
    # authentication (login and sign up)
    path('login/', auth_views.login, name="login"),
    path('sign_up/', auth_views.sign_up, name="sign_up"),
    path('logout/', auth_views.logout, name="logout"),
    path('profile/', auth_views.profile, name="profile"),
    path('password/', auth_views.passwordChange, name='change_password'),



]
