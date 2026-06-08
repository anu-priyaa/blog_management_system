from django.shortcuts import render, redirect
from blogApp.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib.auth.models import User, Group

def home(request):
    return render(request,"home.html")

def get_login(request):
    return render(request,'login.html')

def post_login(request):
    email = request.POST['email']
    password = request.POST['password']

    authuser = User.objects.filter(username=email).first()

    if authuser is not None and authuser.is_active == False:
        return HttpResponse(
            "<script>alert('Your account has been blocked');window.location='/blogApp/get_login/'</script>"
        )

    user = authenticate(username=email, password=password)

    if user is not None:
        login(request, user)

        if user.groups.filter(name="admin").exists():
            return render(request, "adminmodule/adminhome.html")

        elif user.groups.filter(name="users").exists():
            return render(request, "usermodule/userhome.html")

    return HttpResponse(
        "<script>alert('Invalid Username or Password');window.location='/blogApp/get_login/'</script>"
    )

def logout_user(request):

    logout(request)

    return redirect('/blogApp/get_login/')
def get_register(request):
    return render(request,"usermodule/signup.html")

def post_register(request):
    fullname = request.POST['fullname']
    email = request.POST['email']
    phone=request.POST['phone']
    password = request.POST['password']
    biopic = request.FILES['biopic']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%y%m%d%H%M%S') + '.jpg'
    fs.save(date, biopic)
    path = fs.url(date)

    authuser = User.objects.create_user(
    username=email,
    email=email,
    password=password
)

    group = Group.objects.get(name="users")
    authuser.groups.add(group)


    obj = Users()
    obj.fullname = fullname
    obj.email = email
    obj.phone = phone
    obj.biopic = path
    obj.AUTHUSER = authuser
    obj.save()

    return HttpResponse(
        '''<script>alert('Registration Successful');window.location="/blogApp/get_login/"</script>'''
    )

def viewdata(request):
    a = Users.objects.all()

    for i in a:
        print(i.fullname)
        print(i.phone)
        print(i.biopic)

    return render(request, 'adminmodule/viewusers.html', {'data': a})

def get_changepassword(request):
    return render(request,'changepassword.html')

from django.contrib.auth import authenticate

def post_changepassword(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']

    user = request.user

    check = authenticate(
        username=user.username,
        password=oldpassword
    )

    if check is not None:

        if newpassword == confirmpassword:

            user.set_password(newpassword)
            user.save()

            return HttpResponse(
                '''<script>alert("Password Changed Successfully");window.location="/blogApp/get_login/"</script>'''
            )

        else:
            return HttpResponse(
                '''<script>alert("Passwords do not match");history.back()</script>'''
            )

    else:
        return HttpResponse(
            '''<script>alert("Old Password Incorrect");history.back()</script>'''
        )


def viewprofile(request):
    data=Users.objects.get(AUTHUSER=request.user)
    return render(request,"usermodule/viewprofile.html",{'data':data})
    
def get_editprofile(request):
    data=Users.objects.get(AUTHUSER=request.user)
    return render(request,"usermodule/editprofile.html",{'data':data})

def post_editprofile(request):
    obj = Users.objects.get(AUTHUSER=request.user)

    obj.fullname = request.POST['fullname']
    obj.phone = request.POST['phone']

    if 'biopic' in request.FILES:

        photo = request.FILES['biopic']

        fs = FileSystemStorage()

        filename = fs.save(photo.name, photo)

        obj.biopic = fs.url(filename)

    obj.save()

    return redirect('/blogApp/viewprofile/')

def userhome(request):
    return render(request, "usermodule/userhome.html")


def block_user(request, id):
    user = Users.objects.get(id=id)

    user.AUTHUSER.is_active = False
    user.AUTHUSER.save()

    return redirect('/blogApp/viewdata/')

def unblock_user(request, id):
    user = Users.objects.get(id=id)

    user.AUTHUSER.is_active = True
    user.AUTHUSER.save()

    return redirect('/blogApp/viewdata/')

def get_addblog(request):
    return render(request,"usermodule/addblog.html")

def post_addblog(request):

    title = request.POST['title']
    content = request.POST['content']
    image = request.FILES['image']

    fs = FileSystemStorage()

    filename = datetime.now().strftime('%y%m%d%H%M%S') + '.jpg'

    fs.save(filename, image)

    path = fs.url(filename)

    user = Users.objects.get(AUTHUSER=request.user)

    obj = Blog()
    obj.title = title
    obj.content = content
    obj.image = path
    obj.status = "pending"
    obj.USER = user
    obj.save()

    return HttpResponse(
        '''<script>alert("Blog Created Successfully");
        window.location="/blogApp/userhome/"</script>'''
    )

def view_myblogs(request):

    user = Users.objects.get(AUTHUSER=request.user)

    blogs = Blog.objects.filter(USER=user)

    return render(
        request,
        "usermodule/viewmyblogs.html",
        {'blogs': blogs}
    )

def get_editblog(request,id):

    user = Users.objects.get(AUTHUSER=request.user)

    data = Blog.objects.get(
        id=id,
        USER=user
    )

    return render(
        request,
        "usermodule/editblog.html",
        {'data':data}
    )

def post_editblog(request,id):

    user = Users.objects.get(AUTHUSER=request.user)

    obj = Blog.objects.get(
        id=id,
        USER=user
    )

    obj.title = request.POST['title']
    obj.content = request.POST['content']

    if 'image' in request.FILES:

        image = request.FILES['image']

        fs = FileSystemStorage()

        filename = fs.save(image.name,image)

        obj.image = fs.url(filename)

    obj.save()

    return redirect('/blogApp/view_myblogs/')

def delete_blog(request,id):

    user = Users.objects.get(AUTHUSER=request.user)

    obj = Blog.objects.get(
        id=id,
        USER=user
    )

    obj.delete()

    return redirect('/blogApp/view_myblogs/')

def view_allblogs(request):

    blogs = Blog.objects.filter(status="approved")

    return render(
        request,
        "usermodule/viewallblogs.html",
        {'blogs': blogs}
    )

def view_blog(request,id):

    blog = Blog.objects.get(id=id)

    comments = comment.objects.filter(BLOG=blog)

    return render(
        request,
        "usermodule/viewblog.html",
        {
            'blog': blog,
            'comments': comments
        }
    )

def add_comment(request,id):

    blog = Blog.objects.get(id=id)

    user = Users.objects.get(
        AUTHUSER=request.user
    )

    text = request.POST['comment']

    obj = comment()

    obj.BLOG = blog
    obj.USER = user
    obj.comment = text

    obj.save()

    return redirect(
        f'/blogApp/view_blog/{id}/'
    )

def adminhome(request):
    return render(request, "adminmodule/adminhome.html")

def viewallblogs_admin(request):

    blogs = Blog.objects.all()

    return render(
        request,
        "adminmodule/viewallblogs_admin.html",
        {'blogs':blogs}
    )

def approve_blog(request,id):

    blog = Blog.objects.get(id=id)

    blog.status = "approved"

    blog.save()

    return redirect('/blogApp/viewallblogs_admin/')

def reject_blog(request,id):

    blog = Blog.objects.get(id=id)

    blog.status = "rejected"

    blog.save()

    return redirect('/blogApp/viewallblogs_admin/')

def delete_blog_admin(request,id):

    blog = Blog.objects.get(id=id)

    blog.delete()

    return redirect('/blogApp/viewallblogs_admin/')