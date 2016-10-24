from django.shortcuts import render_to_response


# Create your views here.


def fb_view(request):
    return render_to_response('facebook.html')
