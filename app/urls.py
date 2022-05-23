from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('faq', faq, name="faq"),
    path('register', register, name="register"),
    path('contact', contact, name="contact"),
    path('partner', partner, name="partner"),
    path('signin', signin, name="signin"),
    path('blog', blog, name="blog"),

]
