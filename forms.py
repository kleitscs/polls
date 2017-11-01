
from django import forms
from .models import Measurementunit, Threaddiameter, Pitch2Threaddiameter, Threaddesignation, Partnumber

tpdid = Partnumber.objects.values('threaddesignationid').distinct()
p2did = Threaddesignation.objects.filter(pk__in=tpdid).values('pitch2threaddiameterid').distinct()
thdid = Pitch2Threaddiameter.objects.filter(pk__in=p2did).values('threaddiameterid').distinct()
untid = Threaddiameter.objects.filter(pk__in=thdid).values('measurementunitid').distinct()

PARTSLIST = Partnumber.objects.distinct()
