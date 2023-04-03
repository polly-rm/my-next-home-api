from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from mynexthome.comments.models import Comment
from mynexthome.comments.serializers import CommentSerializer
from mynexthome.properties.models import Property


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class CommentCreate(APIView):
    def post(self, request):
        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            user_id = int(request.data['user_id'])
            user = User.objects.get(id=user_id)

            property_id = int(request.data['property_id'])
            property = Property.objects.get(id=property_id)
            comment_serializer.save(user=user, property=property)

            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)

        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CommentUpdate(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"
        

class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"
