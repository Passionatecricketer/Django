from django.db import models
from django_simple_coupons.models import Ruleset, AllowedUsersRule, MaxUsesRule, ValidityRule, Coupon,CouponUser,Discount

# Create your models here.
class Category(models.Model):
  Cat_id = models.IntegerField()
  cat_name = models.CharField(max_length=300)

  def __str__(self):
    return self.cat_name

class SubCategory(models.Model):
  cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
  Sub_cat_id = models.IntegerField()  
  Sub_cat_name = models.CharField(max_length=300)
  Sub_image = models.URLField(blank=True,max_length=250)

  def __str__(self):
    return self.Sub_cat_name

class Product(models.Model):
  #subcat_id = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
  P_id = models.IntegerField()
  P_name = models.CharField(max_length=300)
  P_code = models.IntegerField()
  P_price = models.IntegerField()
  P_image = models.URLField(blank=True,max_length=250)

  def __str__(self):
    return self.P_name

class ShoppingCart(models.Model):
  P_id = models.ForeignKey(Product,on_delete=models.CASCADE)
  User_id = models.IntegerField()
  qty = models.FloatField() 
  Total = models.FloatField()
