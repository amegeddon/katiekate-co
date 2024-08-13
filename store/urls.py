from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.ProductViewSet)
router.register( 'collections', views.CollectionViewSet)
router.urls

urlpatterns = router.urls