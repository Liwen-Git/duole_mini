from django.utils.deprecation import MiddlewareMixin


class SignatureVerificationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return None