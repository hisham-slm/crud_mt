from django.shortcuts import render,redirect
from common.models import User

from user.models import Post , LikedPosts

# Create your views here.

def home(request):
    post = Post.objects.filter(status = 'approve')
    return render(request, 'user_temp/home.html',{'post':post})


def create_post(request):
    msg = ''
    if request.method == 'POST':
        post = request.POST['post']
        userid = request.session['user']


        new_post = Post(
            user = User.objects.get(id = userid),
            post = post,
            votes = 0,
            status = 'pending'
        )
        msg = 'Uploaded Succesfully'

        new_post.save()
    return render(request, 'user_temp/create_post.html',{'msg':msg})


def uploaded_post(request):
    return render(request, 'user_temp/uploaded_post.html')


def like_post(request,pid):
    post_id = pid
    user_id = request.session['user']
    
    liked_user = LikedPosts.objects.filter(user_id=user_id, post_id = post_id).exists()
    post = Post.objects.get(id = pid)
    if liked_user == False:
        new_liked_post = LikedPosts(
            post_id = post_id,
            user_id = user_id

        )
        print(pid)
        
        new_liked_post.save()

        post.votes = post.votes + 1
        post.save()

    else:
        post.votes = post.votes - 1
        post.save()
        liked_post = LikedPosts.objects.get(user_id = request.session['user'], post_id = pid)
        liked_post.delete()
        print('true')
    
    return redirect('user:user_home')

def logout(request):
    del request.session['user']
    request.session.flush()
    
    return redirect('common:home')

