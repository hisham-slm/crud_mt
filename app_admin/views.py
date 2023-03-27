from django.shortcuts import render , redirect

from user.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.filter(status = 'pending')

    return render(request, 'admin_temp/home.html',{'post':posts})

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('common:home')

def approve(request,pid):
    post = Post.objects.get(id = pid)
    post.status = 'approve'

    post.save()
    return redirect('admin:home')

def reject(request,pid):
    post = Post.objects.get(id = pid)
    post.delete()

    return redirect('admin:home')