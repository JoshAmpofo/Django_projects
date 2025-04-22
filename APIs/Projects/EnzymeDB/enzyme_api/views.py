from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Enzyme
from .serializers import EnzymeSerializer, UserSerializer
from .permissions import IsOwnerOrSuperuser, IsSuperuserOrReadOnly

# Create your views here.
class EnzymeViewSet(viewsets.ModelViewSet):
    serializer_class = EnzymeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSuperuser]

    def get_queryset(self):
        """
        Return enzymes based on user permissions:
        - Superusers see all enzymes
        - Regular users only see their own enzymes
        """
        if self.request.user.is_superuser:
            return Enzyme.objects.all()
        return Enzyme.objects.filter(curator=self.request.user)

    def perform_create(self, serializer):
        """Automatically associate the enzyme with the current user"""
        serializer.save(curator=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def get_queryset(self):
        """
        Return users based on permissions:
        - Superusers see all users
        - Regular users only see their own profile
        """
        if self.request.user.is_superuser:
            return get_user_model().objects.all()
        return get_user_model().objects.filter(id=self.request.user.id)

    def get(self, request):
        """Get current user's information"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def list(self, request):
        """List all users (only for superusers)"""
        if not request.user.is_superuser:
            return Response(
                {'error': 'Only superusers can list all users'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().list(request)

    def retrieve(self, request, pk=None):
        """Retrieve a specific user"""
        try:
            user = self.get_queryset().get(pk=pk)
        except get_user_model().DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if not request.user.is_superuser and request.user.id != user.id:
            return Response(
                {'error': 'You can only view your own profile'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(user)
        return Response(serializer.data)