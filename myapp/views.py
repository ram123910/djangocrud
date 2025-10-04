# from django.shortcuts import render

from django.shortcuts import render, redirect


from .models import *

# Create your views here.


# def IndexView(request):                 # Index.html View
#     return render(request, "app/index.html")


# def htmlform(request):
#     return render(request,"app/Forms.html")

def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):

    # Data come from HTML to View
    
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

# Creating object of Model class

#  Inserting Data into Table
    newuser = Student.objects.create(Firstname=fname , Lastname=lname , Email=email , Contact=contact)

# After Insert render on Show.html  
    
    # return render(request,"app/show.html")
# After Insert render on ShowPage View
    return redirect('showpage')

# SHOW PAGES View


def ShowPage(request):
    # Select * from tablename
    # For fetching all the data of the table

    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

# Edit Page View
# Fetching the data of particular ID

def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})


# Update Data View

def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

# Query for Update

    udata.save()
    # Render to Show Page
    return redirect('showpage')

# Delete Data View

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)

    # Query For Delete
    
    ddata.delete()
    return redirect('showpage')


