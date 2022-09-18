from rest_framework import viewsets, parsers, permissions
from .. import serializers, models
from base.permissions import IsAuthor

class UserView(viewsets.ModelViewSet):
    """User uchun view
    """
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()

class AuthorView(viewsets.ReadOnlyModelViewSet):
    """Mualliflar ro`yhati
    """
    queryset = models.AuthUser.objects.all().prefetch_related('social_links')
    serializer_class = serializers.AuthorSerializer

class SocialLinkView(viewsets.ModelViewSet):
    """CRUD
    """
    serializer_class = serializers.SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)