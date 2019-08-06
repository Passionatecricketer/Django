from django.shortcuts import render,redirect
from .models import Category,ShoppingCart,SubCategory,Product
from django_simple_coupons.models import Coupon,CouponUser,Discount,Ruleset,ValidityRule,AllowedUsersRule,MaxUsesRule
from django.http import HttpResponse  
from .serializers import CouponSerializer,CouponUserSerializer,DiscountSerializer,RulesetSerailizer,ValidityRuleSerializer,AllowedUsersRuleSerializer,MaxUsesRuleSerializer,CategorySerializer,SubCatSerializer,ProductSerializer,ShoppingCartSerializer
from django.contrib import messages
from django.contrib.auth import get_user_model  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework import viewsets,permissions
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django_simple_coupons.validations import validate_coupon
#Create your views here.

class CouponView(viewsets.ModelViewSet):
  queryset = Coupon.objects.all()
  serializer_class = CouponSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CouponUserView(viewsets.ModelViewSet):
  queryset = CouponUser.objects.all()
  serializer_class = CouponUserSerializer

class DiscountView(viewsets.ModelViewSet):
  queryset = Discount.objects.all()
  serializer_class = DiscountSerializer

class RulesetView(viewsets.ModelViewSet):
  queryset = Ruleset.objects.all()
  serializer_class = RulesetSerailizer 
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  

class ValidityRuleView(viewsets.ModelViewSet):
  queryset = ValidityRule.objects.all()
  serializer_class = ValidityRuleSerializer

class AllowedUsersRuleView(viewsets.ModelViewSet):
  queryset = AllowedUsersRule.objects.all()
  serializer_class = AllowedUsersRuleSerializer
  

class MaxUsesRuleView(viewsets.ModelViewSet):
  queryset = MaxUsesRule.objects.all()
  serializer_class = MaxUsesRuleSerializer

class CatgoryView(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CatgoryViewDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CouponSerializer  

class SubCatView(viewsets.ModelViewSet):
  queryset = SubCategory.objects.all()
  serializer_class = SubCatSerializer

class SubCatViewDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = SubCategory.objects.all()
  serializer_class = SubCatSerializer


class ProductView(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductViewdelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ShoppingCartView(viewsets.ModelViewSet):
  queryset = ShoppingCart.objects.all()
  serializer_class = ShoppingCartSerializer 

class ShpoingCartViewDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = ShoppingCart.objects.all()
  serializer_class = ShoppingCartSerializer 
  
  coupon_code = "COUPONTEST01"
  User = get_user_model()
  user = User.objects.get(username="rishabh")

  status = validate_coupon(coupon_code=coupon_code, user=user)
  if status['valid']:
    coupon = Coupon.objects.get(code=coupon_code)
    coupon.use_coupon(user=user)

class UseCouponView(View):
    def get(self, request, *args, **kwargs):
        coupon_code = request.GET.get("coupon_code")
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        
        status = validate_coupon(coupon_code=coupon_code, user=user)
        if status['valid']:
            coupon = Coupon.objects.get(code=coupon_code)
            coupon.use_coupon(user=user)
        
            return HttpResponse("OK")
        
        return HttpResponse(status['message'])


'''class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")'''


# User = get_user_model()

# class UserList(viewsets.generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserViewSet(viewsets.generics.ListCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# def index(request):
#   return render(request,'index.html')    

# def register(request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       form.save()
#       username = form.cleaned_data['username']
#       password = form.cleaned_data['password1']

#       user = authenticate(username=username,password=password)
#       login(request,user)
#       return redirect('index')
#   else:
#     form = UserCreationForm()    
#   context = {'form':form}
#   return render(request,'registration/register.html',context)

# class UserView(APIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)  