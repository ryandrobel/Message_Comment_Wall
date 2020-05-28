from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Post, Comment
from login . models import User



# Create your views here.
def wall(request):
    context = {
        'all_posts': Post.objects.all()
    }

    return render(request, 'wall.html', context)

def post_message(request):
    errors = Post.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/wall')

    else:
        user = User.objects.get(id = request.session['user_id'])
        post = Post.objects.create(
            body = request.POST['message'],
            user = user
        )
        return redirect('/wall')

def post_comment(request, post_id):
    errors = Comment.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
        return redirect('/wall')

    else:
        post = Post.objects.get(id = post_id)
        user = User.objects.get(id = request.session['user_id'])
        comment = Comment.objects.create(
            content = request.POST['comment'],
            post = post,
            user = user
        )
        return redirect('/wall')