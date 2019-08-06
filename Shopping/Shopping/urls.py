from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from cart import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
router.register('ruleset',views.RulesetView)
router.register('allowuser',views.AllowedUsersRuleView)
router.register('maxuser',views.MaxUsesRuleView)
router.register('validity',views.ValidityRuleView)
router.register('couponuser',views.CouponUserView)
router.register('discount',views.DiscountView)
router.register('coupon',views.CouponView)
# router.register('user-detail',views.UserList)

router.register('category',views.CatgoryView)
router.register('subcatetgory',views.SubCatView)
router.register('product',views.ProductView)
router.register('shoppingcart',views.ShoppingCartView)


# router.register('user-detail',views.UserList)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('cart.urls')),  
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include((router.urls))),
    # path('category/',include(router1.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    # path('user/',views.UserView,name='allowuser'),
    path('cate/',views.CatgoryView),
    path('cate/<int"pk>/',views.CatgoryViewDelete)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
