from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',views.languageview)
router.register('paradigm',views.paradigmview)
router.register('programmer',views.programmerview)

urlpatterns = [
    path('',include(router.urls))

    
]