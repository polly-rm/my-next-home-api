from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    floor = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    storey = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    area = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    yardArea = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    bedroom = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    bathroom = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    storage = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    parking = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    basement = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
        
    class Meta:
        model = Property
        fields = '__all__'


    def validate_field(self, value):
        if not value:
            return None
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError('Valid number is required')
        
    def validate_floor(self, value):
         return self.validate_field(value)
    
    def validate_storey(self, value):
         return self.validate_field(value)

    def validate_area(self, value):
         return self.validate_field(value)
    
    def validate_yardArea(self, value):
         return self.validate_field(value)
    
    def validate_bedroom(self, value):
         return self.validate_field(value)
    
    def validate_bathroom(self, value):
         return self.validate_field(value)
    
    def validate_storage(self, value):
         return self.validate_field(value)
    
    def validate_parking(self, value):
        if value == '-Select-':
            return None
    
    def validate_basement(self, value):
        if value == '-Select-':
            return None