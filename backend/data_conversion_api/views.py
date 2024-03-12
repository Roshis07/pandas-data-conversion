from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .data_processing import read_and_infer_data_types


class InferDataTypesView(APIView):
    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            dataframe = read_and_infer_data_types(file_obj)
            dataframe_dtypes_str = {column: str(dtype) for column, dtype in dataframe.dtypes.items()}

            return Response(dataframe_dtypes_str, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
