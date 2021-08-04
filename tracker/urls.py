from django.urls import path
from .views import AlertList, AlertListCreateApiView, AlertDetailApiView, AlertTriggeredApiView

urlpatterns = [
	path('', AlertList.as_view(), name="alert-list"),
	path('create',AlertListCreateApiView.as_view(), name="alert-create"),
	path('triggered', AlertTriggeredApiView.as_view(), name="alert-triggered"),
	path('delete/<int:id>', AlertDetailApiView.as_view(), name='alert-detail'),
]