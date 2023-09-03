from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializers
# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset=Category.objects.order_by('-created_at').all()
    serializer_class=CategorySerializers