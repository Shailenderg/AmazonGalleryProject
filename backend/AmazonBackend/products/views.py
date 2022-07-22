from django.shortcuts import render
from numpy import product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status,exceptions
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

class ProductsList(APIView):
    '''
    List all products or create new one
    '''
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductAllInfoSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)  


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_fields = (
        'category__id',
    )
    search_fields = (
        'title',
    )

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SellerViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Seller.objects.all()
        