
from django.urls import path
#from apps.users.api.api import UserAPIView
from .api import permiso_api_view, permiso_detalle_api_view

urlpatterns = [
    path('datos/', permiso_api_view, name='permiso'),
    path('datos/<int:pk>', permiso_detalle_api_view, name='permiso_detalle')
    #path('usuario/', UserAPIView.as_view(), name='usuario_api')
]
