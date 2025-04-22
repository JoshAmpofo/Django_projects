from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet #PostList, PostDetail, UserList, UserDetail

# using routers
router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path("", PostList.as_view()),
# ]