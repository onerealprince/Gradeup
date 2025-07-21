from rest_framework import viewsets, permissions
from .models import StudyEvent
from .serializers import StudyEventSerializer

class StudyEventViewSet(viewsets.ModelViewSet):
    serializer_class = StudyEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyEvent.objects.filter(user=self.request.user).order_by('date', 'time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
