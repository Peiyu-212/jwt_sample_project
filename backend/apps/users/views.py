from rest_framework import status, generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer

#Register API
class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return None

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User created successfully! Please try to login again.",
        }, status=status.HTTP_201_CREATED)