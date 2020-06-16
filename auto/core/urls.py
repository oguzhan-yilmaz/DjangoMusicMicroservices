from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
# router.register(r'songs', SongModelList)
# router.register(r'groups', SongModelList)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', SongUploadView.as_view()),
    path('login/', auth_views.LoginView.as_view()),
    # path('', include(router.urls)),
    path('api/songs/', SongModelListView.as_view()),
    path('api/users/', UserApiView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)