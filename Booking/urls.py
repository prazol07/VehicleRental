from django.contrib import admin
from django.urls import path  
from .views import BookerLogin, DeleteBookings, Register, LandingPage, AboutPage,ServicePage, VehicleRentCreate, CarPage,VehicleBookCreate, UserRentList, UserBookList, RentUpdate, DeleteRentings
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login', BookerLogin.as_view(), name="login"),
    path('logout', LogoutView.as_view(next_page="home"), name="logout"),
    path('register', Register.as_view(), name="register"),
    path('rentcreate', VehicleRentCreate.as_view(), name="rentcreate"),
    path('bookcreate/<int:pk>', VehicleBookCreate.as_view(), name="bookcreate"),
    path('', LandingPage.as_view(), name="root"),
    path('home', LandingPage.as_view(), name="home"),
    path('about', AboutPage.as_view(), name="about"),     
    path('service', ServicePage.as_view(), name="service"),
    path('car', CarPage.as_view(), name="cars"),
    path('userrentings', UserRentList.as_view(), name="rentinglist"),
    path("userbookings",UserBookList.as_view(), name="bookinglist"),
    path("update/<int:pk>",RentUpdate.as_view(), name="rentupdate"),
    path("deleterentings/<int:pk>",DeleteRentings.as_view(), name="rentdelete"),
    path("deletebookings/<int:pk>",DeleteBookings.as_view(), name="bookdelete"),
]
    