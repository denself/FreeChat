from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext


def default(request):
    return render_to_response('index.html',
                               context_instance=RequestContext(request))