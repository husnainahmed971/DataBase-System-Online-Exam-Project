from django import forms
# provides classes and functions for working with HTML forms in Django.
from django.contrib.auth.models import User
#class is a built-in Django model that represents a user account. 
# It provides fields such as username, password, email, etc., to store user authentication information.
from . import models
# is a custom module containing Django models that define the structure and behavior of your application's data.
# Form for the Contact Us page
class ContactusForm(forms.Form):

    Name = forms.CharField(max_length=30)  # Field for name input
    Email = forms.EmailField()  # Field for email input
    
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    # Field for message input

# Form for Teacher Salary
class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()  # Field for salary input

# Form for Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course  # Model associated with the form
        fields = ['course_name', 'question_number', 'total_marks']
        # Fields to be displayed in the form

# Form for Question
class QuestionForm(forms.ModelForm):
    courseID = forms.ModelChoiceField(queryset=models.Course.objects.all(), empty_label="Course Name", to_field_name="id")
    # Dropdown field to select a course from the available options

    class Meta:
        model = models.Question  # Model associated with the form
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        # Fields to be displayed in the form

        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})  # Textarea widget for the 'question' field
        }
