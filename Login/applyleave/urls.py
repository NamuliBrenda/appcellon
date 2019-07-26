from applyleave.views import ApplyLeaveView
from django.urls import path

urlpatterns = [
	path('apply/', ApplyLeaveView, name='appyforleave'),
]