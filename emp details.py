from django.db import models  
class Employee(models.Model):  
    firstname = models.CharField(max_length=100)    
    lastname = models.CharField(max_length=100)  
    empid = models.CharField(max_length=20)   
    email = models.EmailField()
    contact =models.CharField(max_length=10)  
    class Meta:  
        db_table = "employee"  
