from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenWithUserObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {'first_name': self.user.first_name, 'last_name': self.user.last_name}
        data['permissions'] = self.user.get_permission_table()
        return data


class TokenWithUserObtainPairView(TokenObtainPairView):
    serializer_class = TokenWithUserObtainPairSerializer
