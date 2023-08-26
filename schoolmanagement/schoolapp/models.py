from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherDT(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    salary=models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    phone=models.IntegerField()
    status=models.BooleanField(default=False)
    def __str__(self): #__str__ used to convert the object into string
        return self.user.first_name
    @property #used to get direct access to get, set and delete
    def get_id(self):
        return self.user.id 
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name



classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]

class StudentDT(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no=models.IntegerField()
    phone=models.IntegerField()
    fee=models.PositiveIntegerField(null=True)
    cl=models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    def __str__(self): #__str__ used to convert the object into string
        return self.user.first_name
    @property #used to get direct access to get, set and delete
    def get_id(self):
        return self.user.id 
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




class Attendance(models.Model):
    roll_no=models.IntegerField(null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status=models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True) # auto_now will update the field every time the save method is called
    by=models.CharField(max_length=30,null=True,default='school')
    message=models.CharField(max_length=500)