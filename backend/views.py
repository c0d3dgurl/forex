# from django.shortcuts import render
# from rest_framework import generics
from django.db.models.query import QuerySet
from django.http import request
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Signal
from . serializers import SignalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
import json
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

# ViewSets define the view behavior.
# class SignalViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated)
#     queryset = Signal.objects.all()
#     serializer_class = SignalSerializer



schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]

class SignalGetterView(APIView):
    permission_classes=[IsAuthenticated]
    # permission_classes = (IsAuthenticated,ReadPermission)
    def get(self,request,id,*args,**kwargs):
        obj=Signal.objects.get(id=id)
       
        self.check_object_permissions(request,obj)
        return Response({'data':list(obj)})


class CheckUser(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        
        return Response(data={"email":request.user.email,"name":request.user.first_name})
        

# class SignalList(APIView):
#     def post (self, request):
#         body = json.loads(request.body)
#         print(body)
#         serializer = SignalSerializer(data=body)
#         if serializer.is_valid():
#             serializer.save()
#             return Response()

#         else:
#             print(serializer.errors)
#             return Response(serializer.errors,status=400)
            
