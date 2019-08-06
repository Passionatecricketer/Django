from rest_framework import serializers
from .models import Category, SubCategory,Product, ShoppingCart
from django_simple_coupons.models import Ruleset, AllowedUsersRule, MaxUsesRule, ValidityRule, Coupon,CouponUser,Discount
from django.contrib.auth import get_user_model 

User = get_user_model()

class RulesetSerailizer(serializers.ModelSerializer):
  class Meta:
    model = Ruleset
    fields= '__all__'

class AllowedUsersRuleSerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(view_name='cart:allowuser-detail',)

  class Meta:
    model = AllowedUsersRule
    fields= '__all__'

    

class MaxUsesRuleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = MaxUsesRule
    fields = '__all__'

class ValidityRuleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ValidityRule
    fields ='__all__'

class CouponSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Coupon
    fields = '__all__'

class CouponUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CouponUser    
    fields = '__all__'

class DiscountSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Discount
    fields = '__all__'             

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'       

class SubCatSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubCategory
    fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields='__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoppingCart
    fields = '__all__'    

# class UserSerializer(serializers.ModelSerializer): 
#   class Meta:
#     model = User
#     fields = ('email','name')
#     read_only_fields = ('name',)    

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="cart:user-detail")

#     class Meta:
#         model = User
#         fields = ('url', 'username')