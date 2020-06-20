from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.

def homepage(request):
	objs=Post.objects.order_by('Date_Added')
	return render(request,'app/index.html',{'objs':objs})

def vrform(request):
	form =PostForm()
	return render(request,'app/vrform.html',{'form':form})

def addpost(request):
	form =PostForm(request.POST or None )
	obj=Post()
	if form.is_valid():
		obj.PostName=form.cleaned_data['PostName']
		obj.Post=form.cleaned_data['Post']
		obj.save()
		return redirect('/VideoRequest')
	return redirect('/VideoRequest')



