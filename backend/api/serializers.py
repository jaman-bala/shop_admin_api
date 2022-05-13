from rest_framework import serializers
from apps.models import Product, Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'category']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'subcategory',
            'description',
            'price',
            'image',
            'created',
            'updated',
        ]


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('created', 'updated', 'id', 'image')