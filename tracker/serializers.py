from rest_framework.serializers import ModelSerializer
from .models import Alert


class AlertSerializer(ModelSerializer):
	class Meta:
		model = Alert
		fields = ['id', 'price','triggered', 'created_at', 'triggered_at']
