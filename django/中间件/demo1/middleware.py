from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class ForbiddenIpsMiddleware(MiddlewareMixin):
    EXCLUDE_IPS = ['127.0.0.1']

    def process_view(self, request, callback, callback_args, callback_kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in ForbiddenIpsMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        return None