from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about', views.about, name="about-page"),
    path('service', views.service, name="service-page"),
    path('why', views.whyus, name="why-page"),
    path('login', views.userLogin, name="login-page"),
    path('logout', views.usrLogout, name="logout-page"),
    path('profile', views.allMechanics, name='profile-page'),
    path('registration', views.userRegistration, name="registration-page"),
    path('contact', views.contact, name="contact-page"),
    path('book/<int:mid>', views.bookMechanic, name='book-page'),
    path('history', views.bookHistory, name='history-page'),
]