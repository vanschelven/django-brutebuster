# brutebuster by Cyber Security Consulting (www.csc.bg)

"""
brutebuster needs access to the REMOTE_IP of the incoming request. We're doing
this by adding the request object to the thread_local space
"""

try:
    from threading import local
except ImportError:
    from django.utils.threading_local import local

_thread_locals = local()

def set_request(request):
    _thread_locals.request = request

def get_request():
    # In cases where the request is non-existent (i.e. testing, shell), this
    # returns None. Callers are responsible for checking this condition, and
    # adapting as necessary.
    return getattr(_thread_locals, 'request', None)


class RequestMiddleware(object):
    """Provides access to the request object via thread locals"""

    def process_request(self, request):
        # the cleanup (for tests only) is done in LSTestCaseMixin
        # since there is no easy, always called, mirror-image of 'process_request'

        set_request(request)

    def process_response(self, request, response):
        # we cannot rely on process_request being succesful, so doublecheck w/ hasattr

        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request

        return response


