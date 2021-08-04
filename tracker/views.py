from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView
from .models import Alert
from .serializers import AlertSerializer
from rest_framework import permissions 


class AlertList(ListAPIView):
	serializer_class = AlertSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def get_queryset(self):
		return Alert.objects.filter(alert_owner=self.request.user)

class AlertListCreateApiView(ListCreateAPIView):
	serializer_class = AlertSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(alert_owner=self.request.user)

	def get_queryset(self):
		return Alert.objects.filter(alert_owner=self.request.user)


class AlertDetailApiView(RetrieveDestroyAPIView):
	serializer_class = AlertSerializer
	permission_classes = (permissions.IsAuthenticated,)
	lookup_field = 'id'

	def get_queryset(self):
		return Alert.objects.filter(alert_owner=self.request.user)		

class AlertTriggeredApiView(ListAPIView):
	serializer_class = AlertSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def get_queryset(self):
		return Alert.objects.filter(alert_owner=self.request.user, triggered=True)



