# data_inference/urls.py

from django.urls import path
from .views import InferDataTypesView

urlpatterns = [
    path('infer/', InferDataTypesView.as_view(), name='infer_data_types'),
]
