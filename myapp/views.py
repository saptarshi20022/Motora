from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm, BookingForm
from .models import Mechanic, Booking

# Create your views here.

def home(request):
   return render(request, 'myapp/index.html')

def about(request):
   return render(request, 'myapp/about.html')

def service(request):
   return render(request, 'myapp/service.html')

def whyus(request):
   return render(request, 'myapp/why.html')

def contact(request):
   return render(request, 'myapp/contact.html')

def userRegistration(request):
   if request.POST:
      form = SignUpForm(request.POST)
      if form.is_valid():
         try:
            form.save()
            messages.success(request, 'Registration is successful')
         except Exception as e:
            messages.error(request, 'Registration is unsuccessful')
   else:
      form = SignUpForm()
   context = {'form': form}
   return render(request, 'myapp/signUp.html', context)

def userLogin(request):
   if request.user.is_authenticated:
      return HttpResponseRedirect('/profile')
   else:
      if request.method == "POST":
         form = SignInForm(request=request, data=request.POST)
         if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
               login(request, user)
               return HttpResponseRedirect('/profile')
      else:
         form = SignInForm()
      return render(request, 'myapp/signIn.html', {'form': form})


def usrLogout(request):
   logout(request)
   return HttpResponseRedirect('/login')

def allMechanics(request):
   if request.user.is_authenticated:
      mechanics=Mechanic.objects.all()
      return render(request, 'myapp/profile.html', {'mechanics':mechanics})
   else:
      return HttpResponseRedirect('/login')

def bookMechanic(request, mid):
   if request.user.is_authenticated:
      if request.POST:
         frm=BookingForm(request.POST)
         if frm.is_valid():
            try:
               instance=frm.save(False)
               instance.user_id=request.user.id
               instance.mechanic_id=mid
               instance.save()
               messages.success(request, 'Booking has been completed')
               frm = BookingForm()
            except Exception as e:
               messages.error(request, 'Booking is not complete please try again')
      else:
         frm=BookingForm()
      return render(request, 'myapp/booking.html', {'form':frm})
   else:
      return HttpResponseRedirect('/login')

def bookHistory(request):
   if request.user.is_authenticated:
      allBook=Booking.objects.raw("SELECT b.*, m.name, m.mobile as m_mobile FROM myapp_booking b INNER JOIN myapp_mechanic m ON b.mechanic_id=m.mid WHERE b.user_id={} ORDER BY b.servicingDate DESC".format(request.user.id))
      return render(request, 'myapp/bookHistroy.html', {'allBook':allBook})
   else:
      return HttpResponseRedirect('/login')
