from django.shortcuts import render
from .forms import NewPostForm
from .models import Post

# Create your views here.
def NewPost(request):
    return(render(request,'repo/newpost.html', {'newpostform':NewPostForm}))
    
def ListPosts(request):
    posts = Post.objects.all().order_by('submitted')
    return render(request,'repo/postlist.html',{'posts':posts})