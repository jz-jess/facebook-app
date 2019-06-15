import base64
import hashlib
import hmac
import json

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Profile


class DeAuthUser(APIView):

    def post(self, request, format=None):
        signed_request = request.data.get('signed_request', None)

        if signed_request:
            encoded_sig, encoded_envelope = signed_request.split('.', 1)
            envelope = json.loads(self._base64_url_decode(encoded_envelope))
            algorithm = envelope['algorithm']

            if algorithm != 'HMAC-SHA256':
                return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)

            if self._base64_url_decode(encoded_sig) != hmac.new(
                    settings.SOCIAL_AUTH_FACEBOOK_SECRET, msg=encoded_envelope, digestmod=hashlib.sha256).digest():
                return Response('Invalid signature', status=status.HTTP_400_BAD_REQUEST)

            profile = Profile.objects.filter(facebook_user_id=envelope['user_id']).first()

            if profile:
                user = profile.user
                user.is_active = False
                user.save()
                return Response({'success': 'User deauthorized'}, status=status.HTTP_200_OK)
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def _base64_url_decode(self, input):
        input = input.encode(u'ascii')
        input += '=' * (4 - (len(input) % 4))
        return base64.urlsafe_b64decode(input)
