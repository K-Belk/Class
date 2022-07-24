from .views import PostViewSet, CommentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentsViewSet)

urlpatterns = router.urls