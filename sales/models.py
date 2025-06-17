from django.db import models

class SalesRecord(models.Model):
    
    order_id=models.CharField(max_length=20)
    category =models.CharField(max_length=50)
    price =models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    order_date = models.DateField()
    
    def __str__(self):
        return self.order_id
    