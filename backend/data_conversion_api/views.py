# data_inference/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .data_processing import read_and_infer_data_types

class InferDataTypesView(APIView):
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data_types_list=read_and_infer_data_types(file_obj)
                
            return Response({'data_types': data_types_list}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
