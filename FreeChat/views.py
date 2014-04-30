
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from FreeChat.settings import DEFAULT_TORNADO_PORT


@login_required(login_url="/signin/")
def default(request):
    return render_to_response('index.html',
                              dict(port=DEFAULT_TORNADO_PORT),
                              context_instance=RequestContext(request))


def signIn(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        error = ''
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            #Trying to create new user with given username and password
            try:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
            #Mistake means, that user with uch username already exits
            except:
                pass
            #Trying lo authenticate user
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
            #In case of fail, returning mistake
                error = "Wrong password or such user doesn't exist"
        return render_to_response('auth.html', {'error': error},
                                  context_instance=RequestContext(request))


def signOut(request):
    auth.logout(request)
    return HttpResponseRedirect("/")