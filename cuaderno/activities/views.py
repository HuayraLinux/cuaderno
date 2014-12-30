from django.http import Http404
from django.shortcuts import render_to_response
from activities.models import Activity

def index(request):
    q = request.GET.get('q', '')
    activities = Activity.objects.filter(is_published=True)

    if q:
        activities = activities.filter(name__icontains=q)

    return render_to_response('activities/index.html', {'activities': activities, 'q': q})

def show(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        raise Http404

    values = {
        'activity': activity,
        'members': [str(m) for m in activity.staff.all()],
        'attachments': activity.activityattachment_set.filter(is_published=True),
    }
    return render_to_response('activities/show.html', values)
