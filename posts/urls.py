from django.urls import path
from posts import views

urlpatterns = [
    path('',views.index,name='home_page'),
    path('all-courses/',views.get_courses,name='all_courses'),
    path('posts/<slug:course_slug>',views.get_course_details,name = 'course-details'),
    path('form/',views.PostFormView.as_view(),name='form'),
    # path('Thankyou',views.Thankyouview.as_view())
    # path('post/<slug:slug>',views.get_course_details,name = 'course-details')
]