from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout as auth_logout

from secrets import token_urlsafe, compare_digest
from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)


def start(request):
    request.session['next'] = request.GET.get('next')

    state = token_urlsafe(64)
    request.session['state'] = state

    params = urlencode({'client_id': settings.UCLAPI_CLIENT_ID, 'state': state})

    url = settings.UCLAPI_URL + '/oauth/authorise?' + params
    return redirect(url)


def callback(request):
    try:
        state = request.GET.get('state')
        if not compare_digest(state, request.session['state']):
            raise Exception

        code = request.GET.get('code')
        user = authenticate(request, code=code)

        if user:
            login(request, user)
        else:
            raise Exception

        request.session['state'] = None
        return redirect(request.session['next'])
    except Exception:
        logger.exception('authentication failed')
        request.session['state'] = None
        return render(request, 'auth_failed.html')


def logout(request):
    auth_logout(request)
    return redirect('index')
