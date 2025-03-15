from django.http import JsonResponse
from rest_framework.views import APIView
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

User = get_user_model()

class ReceiveDataView(APIView):

    @method_decorator(ratelimit(key='ip', rate='5/s', method='POST', block=True))
    def post(self, request, *args, **kwargs):
        if 'CL-X-TOKEN' not in request.headers:
            return JsonResponse({'success': False, 'message': 'Unauthenticated'}, status=401)
        
        return JsonResponse({'success': True, 'message': 'Data Received'})
