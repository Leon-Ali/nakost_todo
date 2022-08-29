from django.http import JsonResponse

from django.conf import settings


class ApiTokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('X-API-KEY')

        if not api_key or api_key != settings.API_KEY:
            return JsonResponse({'error': 'Invalid Api Key'}, status=403)

        response = self.get_response(request)

        return response
