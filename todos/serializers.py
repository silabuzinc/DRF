from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
            "created_at",
            "done_at",
            "updated_at",
            "deleted_at",
            "status",
        )
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at'


class TestTodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 100, allow_blank=True)
    body = serializers.CharField()

    def validate_title(self, value):
        # Validación customizada
        if "$" in value:
            raise serializers.ValidationError("Error, el título no puede tener el símbolo de $")
        return value
    
    def validate_body(self, value):
        # Validación customizada
        if "$" in value:
            raise serializers.ValidationError("Error, el cuerpo no puede tener el símbolo de $")
        return value
    
