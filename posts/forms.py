from django import forms
from posts.models import Post

class PostReview(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'course_name',
            'develop_by',
            # 'course_title',
            'excerpt',
            'content',
            'course_image',
            
        ]

        labels = {
            "course_name" : "Course Name",
            "develop_by" : "Developed By",
            # "course_title" : "Course Title",
            "excerpt" : "Excerpt",
            "content" : "Content",
            "course_image" : "Image"
        }

        error_messages = {
            'course_name':{
                'required':'course_name must not be empty',
                'max_length':'course_name should not be greater than 50 characters'
            }
        }