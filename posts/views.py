from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
from django.views import View
from posts.forms import PostReview
from django.views.generic.base import TemplateView
from .models import Post

# Create your views here.


def index(request):
    courses = Post.objects.all()
    latest_courses = courses[0:3]
    return render(request,'posts/homepage.html',{
        'courses' : latest_courses
    })


def get_courses(request):
    courses = Post.objects.all()
    return render(request, 'posts/all-course.html',{
        "courses" : courses
    })

def get_course_details(request,course_slug):
    Courses_details = Post.objects.get(course_slug=course_slug)

    return render(request,'posts/courses-details.html',{
        "course" : Courses_details
    })



class PostFormView(View):
    def get(self,request):
        form = PostReview()
        return render(request, 'posts/post-form.html',{'hasError':False,'form':form})

    def post(self,request):
        form = PostReview(request.POST,request.FILES)

        if form.is_valid():
            print(form)
            form.save() # django model form

            return HttpResponseRedirect('/running/all-courses')
        # return render(request, "posts/thank-you.html")

            




            
        


    




