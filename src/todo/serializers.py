from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def destroy(self, instance):
        raise MethodNotAllowed('DELETE')
