from plans.models import Plan, Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['todo_title', 'is_done']


class PlanSerializer(serializers.ModelSerializer):
    plan_todo = TodoSerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.username', read_only=True)

    class Meta:
        model = Plan
        # fields = '__all__'
        fields = ['plan_title', 'plan_start_time', 'plan_finish_time', 'priority', 'owner', 'plan_todo', 'is_finish']
