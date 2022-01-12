from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import random
from myapp.models import Otp, UserType
from django.conf import settings
from django.core.mail import send_mail


def generateOTP():  # funtion for otp generation
    OTP = ""
    for i in range(6):
        OTP += str(random.randint(1, 9))
    return OTP


def landing(request):
    return render(request, 'landing.html')


def signup(request):  # signup funtion take input name ,email, passord
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():  # error if user already exists
            return HttpResponse("user exists try to login")
        else:
            user = User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()  # new user register
            user = User.objects.get(email=email)
            get_otp = generateOTP()
            otp = Otp.objects.create(user=user, otp=get_otp)
            otp.save()  # otp generated and saved in db
            subject = 'Thank you for registering to Upcloud helthcare'  #subjet of email verification
            message = f'Congratulations on successfully creating your account on Upcloud tech. Use the OTP {get_otp} to verify your details.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            context = {"email": email}
            return render(request, 'otp.html', context)


def otp_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = request.POST['otp']
        user = User.objects.get(email=email)
        if Otp.objects.filter(user=user, otp=otp).exists(): # if email verified
            user_type = UserType.objects.create(user=user, is_verified=True)
            user_type.save()
            context = {"email": email}
            return render(request, 'index.html', context)

        else:
            return HttpResponse("error")


def index(request):
    return render(request, 'index.html')
