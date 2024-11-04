from django.shortcuts import redirect
from social_core.exceptions import AuthCanceled


class HandleAuthCanceledMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, AuthCanceled):
            return redirect('/')
        return None
