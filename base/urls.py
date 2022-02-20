from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
from django.http import HttpResponse
from django.conf import settings


AdminSite.site_header = 'Hardik Api Section'
AdminSite.site_title = 'Hardik Api Section'
AdminSite.index_title = ''


schema_view = get_swagger_view(title='HARDIK API VIEW')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


def home(request):
    return HttpResponse('<h1></h2>')


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # swagger
    path('', schema_view) if settings.DEBUG else path('', home),

    # all path
    path('app/', include('home.urls'))
]
