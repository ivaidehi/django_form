from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from app.models import form_data

# Create your views here.
def login(req):
      if req.method == 'POST': 
            username = req.POST['unL']
            password = req.POST['pwL']
            logStudent = auth.authenticate(username=username, password=password)
            if logStudent is None:
                  print(username+"Username not found.")
                  messages.warning(req, "Username not found.")
                  return redirect('login')
            else:
                  print(username+"Login successful.")
                  messages.success(req,"Login successful.")
                  return render(req, 'form.html')
      return render(req, 'login.html')
      
def register(req):
      if req.method == 'POST': 
            email = req.POST['email']
            username = req.POST['unR']
            password = req.POST['pwR']

            if User.objects.filter(email=email).exists():
                  messages.info(req,"Email already exists.")
            elif User.objects.filter(username=username).exists():
                  messages.info(req,"Username already exists.")
            else:
                  regStudent = User.objects.create_user(username=username, password=password, email=email)
                  regStudent.save()
                  print("User Registered Successfully.")
                  messages.info(req,"User Registered Successfully.")
      return render(req,'register.html')      

def form(req):
      if req.method == 'POST':
            emailF = req.POST['emailF']
            studentName = req.POST['sname']
            collegeName = req.POST['cname']
            websiteUsername = req.POST['websiteUn']
            tasks = req.POST['task']
            percent = req.POST['percentage']
            date = req.POST['datE']

            totalData = form_data(emailF,studentName,collegeName,websiteUsername,tasks,percent,date)
            totalData.save()
      return render(req, 'home.html')