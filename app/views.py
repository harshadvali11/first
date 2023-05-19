from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<marquee><h1>Srujana Tinnavara, Eera Vadilestunnava Bla blaaaaa.....</h1></marquee>')


def revi(request):
    return HttpResponse('<marquee><b>Mama Kutti, Long Drive Polaamaa</b></marquee>')