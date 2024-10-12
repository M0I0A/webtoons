# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FavoriteViewSet
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('webtoons/', views.WebtoonsList.as_view(), name='webtoons-list'),
    path('webtoons/<int:pk>/', views.WebtoonDetail.as_view(), name='webtoon-detail'),

    # User-specific favorites endpoint
    path('users/<int:user_id>/favorites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-favorites'),

    # Manually define the route for comments
    path('webtoons/<int:webtoon_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
