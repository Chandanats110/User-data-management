from django.shortcuts import render
from userapp.models import status
from userapp.serializers import statusserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import mixins





# class status_api_view(APIView):
#     def get(self,request):
#         status_data= status.objects.all()
#         status_serializer = statusserializer(status_data,many=True)
#         return Response(status_serializer.data)

# class ListAllStatus(generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = status.objects.all()
#     serializer_class = statusserializer
    

# class AddNewData(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = status.objects.all()
#     serializer_class = statusserializer

# class updatedata(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = status.objects.all()
#     serializer_class = statusserializer
#     lookup_field ='id'

# class UserDetailAPIView(RetrieveAPIView):
#     queryset = status.objects.all()
#     serializer_class = statusserializer 
#     lookup_field = 'id'  
        
class  statuslistadd(generics.ListAPIView,mixins.CreateModelMixin):
    permission_classes = []
    authentication_classes = []
    queryset = status.objects.all()
    serializer_class = statusserializer



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class statusupdatedeleteretrieve(generics.RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes = []
    authentication_classes = []
    queryset = status.objects.all()
    serializer_class = statusserializer
    lookup_field ='id'


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request.user, *args, **kwargs)
    

