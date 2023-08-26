from django import forms
from django.contrib.auth.models import User
from . import models


# for admin
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentDTForm(forms.ModelForm):
    class Meta:
        model=models.StudentDT
        fields=['roll_no','cl','phone','fee','status']



# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class TeacherDTForm(forms.ModelForm):
    class Meta:
        model=models.TeacherDT
        fields=['salary','phone','status']






# for attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField(choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()






#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'