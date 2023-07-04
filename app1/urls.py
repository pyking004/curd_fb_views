from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('addcourse',views.addcourse,name='addcourse'),
    path('courses',views.courses,name='courses'),
    path('updatecourse/<int:id>',views.updatecourse,name='updatecourse'),
    path('deletecourse/<int:id>',views.deletecourse,name='deletecourse'),
]