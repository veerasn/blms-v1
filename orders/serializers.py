from rest_framework import serializers
from orders.models import Person, HumanName


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class HumanNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanName
        fields = '__all__'
