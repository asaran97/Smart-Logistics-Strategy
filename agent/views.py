from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponse
from hubdata.models import orders,Hub
from django.shortcuts import render
from agent.models import agentMapping

# Create your views here.


@login_required
def add_delivery(request, id):
    order = orders.objects.get(pk=id)
    if not order.status and not order.dstatus:
        order.status = True
        mail = 'Dear Customer,\n\n your order'+id+' will be arriving shortly.\n\nWarm Regards,\nTeam Zeus'
        subject = "Smart Hub Notification"
        to = [order.email]
        order.save()
        msg = EmailMessage(subject, mail, to=to, from_email="admin@smart.in")
        msg.send()
        a = agentMapping(agent=request.user, hub=order.hub)
        a.save()
        return HttpResponse("Package Successfully Delivered!!")


def deliver(request):
    content = {}
    order = {}
    tobe = agentMapping.objects.filter(agent=request.user, status=False)
    for i in tobe:
        shub = Hub.objects.get(name=i.hub.name)
        order = orders.objects.filter(hub=shub)
    content['tobedelivered'] = order
    return render(request, "deliver.html", content)


