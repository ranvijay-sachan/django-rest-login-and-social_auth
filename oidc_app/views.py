from django.shortcuts import render_to_response


def oidc_view(request):
    return render_to_response('openind_connect.html')
