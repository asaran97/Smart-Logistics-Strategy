from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from smarthub import map
from .models import Hub, orders

# Create your views here.

@login_required
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        deliver = Hub.objects.all()
        start = request.POST.get('start')
        end = request.POST.get('end')
        (lat1, lon1) = map.get_coordinates(start)
        (lat2, lon2) = map.get_coordinates(end)
        for locs in deliver:
            if not map.within(lat1, lon1, lat2, lon2, locs.lat, locs.long):
                locs.lat = ""
                locs.long = ""
        content = {
            "lat1": lat1,
            "lon1": lon1,
            "lat2": lat2,
            "lon2": lon2,
            "lats": deliver,
        }
        return render(request, "Map.html", content)

@login_required
def show_hub(request, lat, long):
    hub = Hub.objects.get(lat=lat, long=long)
    toBeDelivered = orders.objects.filter(hub=hub, status=False, dstatus=False)
    count = len(toBeDelivered)
    content={}
    content['count'] = count
    content['tobedelivered'] = toBeDelivered
    return render(request, 'hub.html', content)
