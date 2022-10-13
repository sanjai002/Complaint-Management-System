from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    catname = models.CharField(max_length=100)
    catdes = models.CharField(max_length=300)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.catname

class SubCategory(models.Model):
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategoryname = models.CharField(max_length=100)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subcategoryname

class State(models.Model):
    statename = models.CharField(max_length=100)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.statename

class tblUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=300,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=20,null=True)
    userimage = models.FileField(null=True)
    regdate = models.DateField()
    def __str__(self):
        return self.user.username


class Complaint(models.Model):
    userid = models.ForeignKey(tblUser, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100,null=True)
    subcategory = models.CharField(max_length=100,null=True)
    complainttype = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    noc = models.CharField(max_length=200, null=True)
    complaintdetail = models.CharField(max_length=300,null=True)
    complaintfile = models.FileField(null=True,blank=True)
    regdate = models.DateField()
    status = models.CharField(max_length=50, null=True)
    lastupdationdate = models.DateField(null=True)
    remark = models.CharField(max_length=200, null=True)
    remarkdate = models.DateField(null=True)
    def __str__(self):
        return self.id


class ComplaintRemark(models.Model):
    complaintid = models.ForeignKey(Complaint, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=200, null=True)
    remarkdate = models.DateField(null=True)
    def __str__(self):
        return self.id