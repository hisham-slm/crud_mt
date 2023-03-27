from django.http import JsonResponse
from django.shortcuts import redirect, render

from common.models import Admin, User

# Create your views here.
def home(request):
    return render(request,"common_temp/home.html")

def login(request):
    msg = ''
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username, password = password)
            request.session['user'] = user.id
            return redirect('user:user_home')
        except:
            msg = "Invalid User Id or Password"
    return render(request, "common_temp/login.html",{'msg':msg})

def signup(request):
    if request.method == 'POST':
            username = request.POST['username']
            password =  request.POST['repassword']
            name = request.POST['name']


            new_user = User(
                username = username,
                password = password,
                name = name
            )
            new_user.save()
            return redirect('common:login')
    
    return render(request, 'common_temp/signup.html')

def username_exist(request):
    username = request.POST['username']
    status = User.objects.filter(username=username).exists()
    return JsonResponse({'status': status})

def admin_login(request):
    msg = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            admin = Admin.objects.get(username = username, password = password)
            request.session['admin'] = admin.id

            return redirect('admin:home')
        except:
            msg = 'Invalid ID or Password'
    return render(request, 'common_temp/admin_login.html',{'msg': msg})