from django import forms
from app1.models import Course

#create your forms here

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cname','dur','fee']