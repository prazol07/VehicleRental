from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from statistics import mode
from django.http import QueryDict
from django.shortcuts import redirect, render,reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin#restricting pages and allowingg only authenticated users
from django.contrib.auth import login
from Booking.forms import VehicleBookForm, VehicleRentForm
from .models import VehicleBook, VehicleRent


# Create your views here.
class BookerLogin(LoginView):
    template_name="login_logout/login.html"
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('home')
    
class Register(generic.FormView):
    template_name="login_logout/register.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

class VehicleRentCreate(LoginRequiredMixin,generic.CreateView):
    model = VehicleRent
    form_class = VehicleRentForm
    template_name ="renter_booker/rentcreate.html"

    def get_success_url(self):
        return reverse('home')

class VehicleBookCreate(LoginRequiredMixin,generic.CreateView):
    model= VehicleBook
    form_class = VehicleBookForm
    template_name="renter_booker/bookcreate.html"
    
    def post(self, request, pk, *args, **kwargs):
        user_request_obj = VehicleRent.objects.get(pk=pk)
        forms = VehicleBookForm(request.POST)
        if forms.is_valid():
            status = forms.save()
            status.user = request.user
            status.save()
            if status is not None:
                user_request_obj.is_booked = True
                user_request_obj.save()

        return redirect("home")

class UserRentList(LoginRequiredMixin,generic.ListView):
    model=VehicleRent
    context_object_name= 'rentinglist'
    template_name="user_profile/myrentings.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rentinglist']= context['rentinglist'].filter(user=self.request.user)
        return context

class UserBookList(LoginRequiredMixin,generic.ListView):
    model=VehicleBook
    context_object_name= 'bookinglist'
    template_name="user_profile/mybookings.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['bookinglist']= context['bookinglist'].filter(user=self.request.user)
        return context
    
class LandingPage(generic.TemplateView):
    template_name ="home.html"

class AboutPage(generic.TemplateView):
    template_name="about.html"

class ServicePage(generic.TemplateView):
    template_name="services.html"

class CarPage(generic.ListView):
    template_name="car.html"
    queryset=VehicleRent.objects.all()
    context_object_name ="object"
    
class RentUpdate(generic.UpdateView):
    model = VehicleRent
    form_class = VehicleRentForm
    template_name = "renter_booker/rent_update.html"
    queryset = VehicleRent.objects.all()

    def get_success_url(self):
        return reverse("home")

class DeleteRentings(generic.DeleteView):
    model= VehicleRent
    template_name="renter_booker/rent_delete.html"
    success_url="/home"

class DeleteBookings(generic.DeleteView):
    model= VehicleBook
    template_name="renter_booker/book_delete.html"
    success_url="/home"

    def post(self,request,*args,**kwargs):
        obj = VehicleBook.objects.get(pk=kwargs.get("pk"))
        vehicle = obj.rent_info
        obj.delete()
        vehicle.is_booked = False
        vehicle.save()
        return redirect("home")




