from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, get_backends

from django.contrib.auth.models import User

from fileauth.utils import salted_hash

from fileauth.models import AuthenticationKey

def file_login_view(request):
    key = request.POST.get("key", "")

    try:
        ak = AuthenticationKey.objects.get(key=salted_hash(key))
    except AuthenticationKey.DoesNotExist:
        return HttpResponse("Invalid key")

    if not ak.active:
        return HttpResponse("Inactive key")

    user = ak.user

    # In lieu of a call to authenticate()
    backend = get_backends()[0]
    user.backend = "%s.%s" % (
        backend.__module__,
        backend.__class__.__name__
    )
    login(request, user)

    return HttpResponseRedirect("/")
