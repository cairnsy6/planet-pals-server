from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer, CompetitionSerializer, ScoreSerializer
from .models import User, Competition, Score
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     id = self["id"]
    #     user = get_object_or_404(User, id=id)
    #     user.delete()
    #     return Response(status=204)


    

class CompetitionView(viewsets.ModelViewSet):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class ScoreView(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()