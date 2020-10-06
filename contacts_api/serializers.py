from rest_framework import serializers 
from .models import Contact 

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'contact_detail'
    )

    class Meta:
        model = Contact
        fields = ('id', 'contact_url', 'name', 'age',)