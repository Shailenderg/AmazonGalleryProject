from django import views
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

category_list = CategoryViewSet.as_view({
    'get':'list',
    'post':'create'

})
category_detail = CategoryViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delate':'destroy'

})
router = DefaultRouter(trailing_slash=False)
router.register('sellers',SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductsList.as_view(), name='products'),
    path('products-filter/', ProductListAPIView.as_view()),

    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>', category_detail, name='category_detail'),

]
