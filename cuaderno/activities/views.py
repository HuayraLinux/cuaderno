from django.http import Http404
from django.shortcuts import render_to_response
from activities.models import Activity

def index(request):
    q = request.GET.get('q', None)
    activities = Activity.objects.all()

    if q:
        activities = activities.filter(name__icontains=q)

    return render_to_response('activities/index.html', {'activities': activities})

def show(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        raise Http404

    return render_to_response('activities/show.html', {'activity': activity})
