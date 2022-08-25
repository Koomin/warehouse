from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenWithUserObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user'] = {'tralala': 'starara'}
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {'first_name': self.user.first_name, 'last_name': self.user.last_name}
        data['permissions'] = self.permissions_table()
        return data

    def permissions_table(self):
        permissions = {}
        return permissions


class TokenWithUserObtainPairView(TokenObtainPairView):
    serializer_class = TokenWithUserObtainPairSerializer
