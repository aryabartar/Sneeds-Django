from rest_framework import generics, permissions

from . import models
from . import serializers
from .models import StudentDetailedInfo
from .permissions import StudentDetailedInfoListCreatePermission, StudentDetailedInfoRetrieveUpdatePermission
from .serializers import StudentDetailedInfoSerializer


class CountryDetail(generics.RetrieveAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    lookup_field = 'slug'


class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class UniversityDetail(generics.RetrieveAPIView):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    lookup_field = 'slug'


class UniversityList(generics.ListAPIView):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class FieldOfStudyDetail(generics.RetrieveAPIView):
    queryset = models.FieldOfStudy.objects.all()
    serializer_class = serializers.FieldOfStudySerializer
    lookup_field = 'slug'


class FieldOfStudyList(generics.ListAPIView):
    queryset = models.FieldOfStudy.objects.all()
    serializer_class = serializers.FieldOfStudySerializer


class StudentDetailedInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentDetailedInfo.objects.all()
    serializer_class = StudentDetailedInfoSerializer
    permission_classes = (permissions.IsAuthenticated, StudentDetailedInfoListCreatePermission)

    def get_queryset(self):
        user = self.request.user
        qs = StudentDetailedInfo.objects.filter(user=user)
        return qs


class StudentDetailedInfoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = StudentDetailedInfo.objects.all()
    serializer_class = StudentDetailedInfoSerializer
    permission_classes = (permissions.IsAuthenticated, StudentDetailedInfoRetrieveUpdatePermission)
