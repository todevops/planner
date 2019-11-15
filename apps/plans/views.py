from rest_framework import viewsets
from plans.models import Plan, Todo
from plans.serializers import PlanSerializer, TodoSerializer
import logging


logger = logging.getLogger(__file__)

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all().order_by('created_time')
    serializer_class = PlanSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('created_time')
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
