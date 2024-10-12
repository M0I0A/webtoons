from django.shortcuts import render
from django.http import JsonResponse
from api.models import User

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import  viewsets,permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from .models import webtoons,Comment,Favorite
from .serializer import WebtoonsSerializer,CommentSerializer,FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Get the user ID from the URL
        return Favorite.objects.filter(user_id=user_id)  # Filter favorites by user ID

    serializer_class = FavoriteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        webtoon_id = self.kwargs['webtoon_id']
        return Comment.objects.filter(webtoon_id=webtoon_id)

    def perform_create(self, serializer):
        print(self.request.data)  # Log the incoming data
        webtoon_id = self.kwargs['webtoon_id']
        webtoon = webtoons.objects.get(id=webtoon_id)
        serializer.save(webtoon=webtoon)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class WebtoonsList(generics.ListAPIView):
    queryset = webtoons.objects.all()
    serializer_class = WebtoonsSerializer

class WebtoonDetail(RetrieveAPIView):
    queryset = webtoons.objects.all()
    serializer_class = WebtoonsSerializer    


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)