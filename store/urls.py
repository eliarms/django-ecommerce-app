from django.urls import path
from django.urls.conf import include
from rest_framework  import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)

# URLConf
urlpatterns = router.urls