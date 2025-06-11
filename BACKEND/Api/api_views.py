# api/views.py
'''from rest_framework.views import APIView  # Correct import
from rest_framework.response import Response
from base.models import UserProfile
from base.Api.serializers import UserProfileSerializer

class UserProfileList(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)'''
