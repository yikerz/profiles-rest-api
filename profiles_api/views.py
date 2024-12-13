from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
          "message 1",
          "message 2",
          "message 3",
          "message 4",
        ]
        
        return Response({'message':'Hello!', 'an_apiview':an_apiview})