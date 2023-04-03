from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from mynexthome.properties.models import Property
from mynexthome.properties.serializers import PropertySerializer


class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetails(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = "id"


class PropertyCreate(APIView):
    def post(self, request):
        property_serializer = PropertySerializer(data=request.data)

        if property_serializer.is_valid():
            user_id = int(request.data['user_id'])
            user = User.objects.get(id=user_id)
            property_serializer.save(user=user)

            return Response(property_serializer.data, status=status.HTTP_201_CREATED)

        return Response(property_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PropertyUpdate(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = "id"
        

class PropertyDelete(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = "id"
