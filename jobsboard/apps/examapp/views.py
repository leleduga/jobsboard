from __future__ import unicode_literals
from django.shortcuts import render,redirect

from .models import User,Job

from django.contrib import messages

import bcrypt

def index(request):
    if "errors" in request.session:
        errors=request.session["errors"]
        del request.session["errors"]
    else:
        errors=[]    
    context={
        "errors":errors
    }
    return render(request, 'exam/index.html', context)

def create(request):
    data_is_valid, errors = User.objects.basic_validator(request.POST)
    print ('data is valid',data_is_valid)
    print (errors)
    if  data_is_valid:    
        examapp= User.objects.create(
            firstname=request.POST["firstname"],
            lastname=request.POST["lastname"],
            email=request.POST["email"],
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
        )
        request.session['firstname'] = request.POST['firstname']
        request.session['lastname']=request.POST['lastname']
        request.session['email']=request.POST['email']
    
        return redirect('/dashboard')
    else:
        request.session["errors"]=errors
        return redirect('/') 
    if User.objects.filter(email=request.POST['email']).count()>0:
        request.session["errors"]=errors
        print("Duplicate Email")   
        return redirect('/')   
    else:
        redirect('/dashboard')     
#fix this
def create_job(request):
    return render(request, "exam/add.html")

def add(request):
    data_is_valid, errors = Job.objects.basic_validator(request.POST)
    print ('data is valid',data_is_valid)
    print (errors)
    if  data_is_valid:    
        job= Job.objects.create(
            title=request.POST["title"],
            desc=request.POST["desc"],
            location=request.POST["location"],
        )
    
        return redirect('/dashboard')
    else:
        request.session["errors"]=errors
        return redirect('/') 

def dashboard(request):
    if "email" not in request.session:
        return redirect("/")
    else:    
        job = Job.objects.all()
        user = User.objects.get(email=request.session["email"])
        #add in avail jobs and my jobs
        print(user.email)
        context = {
            "job":job,
            "user":user,
            
        }
        return render(request, 'exam/dashboard.html', context)

def viewjob(request, id):
    if "email" not in request.session:
        return redirect('/')
    else:
        job = Job.objects.get(id=id) 
        context = {
            "job":job,
        }   
        return render(request, 'exam/viewjob.html', context)

def logout(request):
    del request.session["email"]
    return redirect( "/logout")    

def edit(request, id):
    job = Job.objects.filter(id=id)

    context = {
        "job":job
    }
    return render(request, 'exam/edit.html', context)
    
def delete(request, id):
    job=Job.objects.filter(id=id).delete()
    return redirect("/dashboard")

def validate_login(request):
    try:
        user = User.objects.get( email=request.POST["email"] )

        isValid = bcrypt.checkpw( request.POST["password"].encode() , user.password.encode() )

        print(isValid)
 
        if isValid:
            print("PASSWORDS MATCH")
            return redirect("/dashboard")
        else:
            print("NO MATCH")
            messages.add_message( request, messages.ERROR, "Invalid Credentials!" )
            return redirect("/")
    except:
        messages.add_message( request, messages.ERROR, "No user with this email was found!" )
        return redirect("/")

                




