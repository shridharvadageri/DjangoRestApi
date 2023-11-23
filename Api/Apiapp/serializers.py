from rest_framework import serializers
from .models import Allotment

class AllotmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allotment
        fields = ('tag_id', 'employee_id', 'action')
