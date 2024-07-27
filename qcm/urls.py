
# from django.contrib import admin
# from django.urls import path
# from main.views import accueil, corriger

# urlpatterns = [
#     path("", accueil, name="accueil"),
#     path("correction/", corriger, name="corriger"),
#     path('admin/', admin.site.urls),
# ]

##############################################


from django.contrib import admin
from django.urls import path, include
from main.views import DomaineViewset, BrancheViewset, QcmViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('domaine', DomaineViewset, basename='domaine')
router.register('branche', BrancheViewset, basename='branche')
router.register('qcm', QcmViewset, basename='qcm')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]