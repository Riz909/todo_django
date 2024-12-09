from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    # Adding a computed 'complete' field
    complete = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'complete']

    def get_complete(self, obj):
        # Get the current date
        today = datetime.today().date()

        # Compare 'today' with the task's 'due_date'
        if today == obj.due_date:
            return "Today"
        elif today > obj.due_date:
            return "Overdue"
        elif today < obj.due_date:
            return "Incoming"