from django.contrib.auth.backends import ModelBackend

from .decorators import protect_and_serve

class BruteBusterModelBackend(ModelBackend):
  
    @protect_and_serve
    def authenticate(self, *args, **kwargs):
        print 'huh?'
        return super(BruteBusterModelBackend, self).authenticate(*args, **kwargs)

