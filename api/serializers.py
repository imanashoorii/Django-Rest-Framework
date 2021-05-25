from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Article
from rest_framework.authtoken.views import Token


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('createdAt', 'updatedAt')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.createdAt = timezone.now()
        obj.save()
        return obj

    def update(self, instance, validated_data):
        created_at = instance.createdAt
        obj = super().update(instance, validated_data)
        obj.createdAt = created_at
        obj.updatedAt = timezone.now()
        obj.save()
        return obj


class UserSerializer(serializers.ModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
