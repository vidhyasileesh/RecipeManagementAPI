from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import mixins, generics, viewsets, status

from recipie.models import Recipie,Review_or_Comment

from recipie.serializer import RecipieSerializer,ReviewSerializer

from recipie.serializer import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# class Recipiedetail(generics.ListCreateAPIView):
#     queryset = Recipie.objects.all()
#     serializer_class = RecipieSerializer


class Recipiedetail(viewsets.ModelViewSet):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer

class Reviewrating(viewsets.ModelViewSet):
    permission_classes = [ IsAuthenticated ]
    queryset = Review_or_Comment.objects.all()
    serializer_class = ReviewSerializer

class CreateUser(viewsets.ModelViewSet):         #  --------By using  Viewset Function
    queryset = User.objects.all()
    serializer_class = UserSerializer




class search(APIView):
    def get(self,request):
        #to get the keyword for search from request query parameters send from client
        query=self.request.query_params.get('search')   #{params:{'search':'carrot}} default search key
        if query:
            # Perform search based on the query parameter
            b = Recipie.objects.filter(Q(name__icontains=query) |Q(ingredients__icontains=query) | Q(cuisine__icontains=query) | Q(meal_type__icontains=query ))
            r=RecipieSerializer(b,many=True)
            return Response(data=r.data, status=status.HTTP_200_OK)

        else:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

