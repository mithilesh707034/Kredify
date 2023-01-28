from django.db import models

class contact(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField( max_length=50)
    description=models.TextField()
    
    def __str__(self):
        return self.first_name +' '+ self.last_name
    
class loanRequest(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    employment=models.CharField(max_length=30)
    company_name=models.CharField( max_length=100)
    email=models.EmailField( max_length=50)
    phone=models.CharField(max_length=12)
    salary=models.IntegerField()
    loan_type=models.CharField(max_length=30)
    aadhar_card=models.FileField(default='' ,null=True,blank=True)
    pan_card=models.FileField(default='' ,null=True,blank=True)
    salary_sleep=models.FileField(default='' ,null=True,blank=True)
    photo=models.ImageField(default='' ,null=True,blank=True)


    def __str__(self):
        return self.first_name+' '+self.last_name