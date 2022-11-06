from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import TgUser
from .serializers import TgUserUpdateSerializer


class TgUserUpdateView(GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserUpdateSerializer
    queryset = TgUser.objects.all()

    def update(self, request, *args, **kwargs):
        instance = TgUser.objects.filter(
            verification_code=request.data.get('verification_code')
        ).first()
        if not instance:
            return Response(
                data={'verification_code': ['Invalid code']}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance.user = request.user
        instance.save()

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
