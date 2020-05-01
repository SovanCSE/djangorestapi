from rest_framework import serializers
from .models import Student

#normal serializer class
class Studenterializer(serializers.Serializer):
    level_choice = [('Senior', 'level1'),
                    ('Sub Senior', 'level2'),
                    ('Junior', 'level3'),
                    ]
    first_name = serializers.CharField(max_length=1000)
    last_name = serializers.CharField(max_length=1000)
    class_level = serializers.CharField(max_length=20)
    total_marks = serializers.FloatField()
    roll_no = serializers.IntegerField()
    phone_no = serializers.CharField(max_length=17)
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.class_level = validated_data.get('class_level', instance.class_level)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.email = validated_data.get('email', instance.email)
        return instance

#model based serializer class
class StudenterializerModel(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields = ("id", "first_name", "last_name", "class_level", "total_marks", "roll_no",
        #           "phone_no", "email", "created_date", "updated_date")
        fields = '__all__'
