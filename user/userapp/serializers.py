from rest_framework import serializers
from userapp.models import status,userdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userdata
        fields = '__all__' 
class statusserializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model =status
        fields ='__all__'

