from django.db import models

class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
   
    class Meta:  
        db_table = "tblemployee"




class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    cust_id = models.IntegerField()
    invoice_date = models.CharField(max_length=10)
    due_date = models.CharField(max_length=10)
    total_amt = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    pay_id = models.IntegerField()
    
    class Meta:
        db_table = "invoices"

