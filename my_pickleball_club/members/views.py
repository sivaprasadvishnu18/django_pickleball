from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Member
import uuid

def members(request):
  mymembers = Member.objects.all().values()

  if(mymembers):
    return JsonResponse(list(mymembers), safe=False)
  else:
    return JsonResponse()

  
def details(request, id):
  mymember = Member.objects.get(memberId=id)

  data = {
    'memberId': mymember.memberId,
    'first_name': mymember.first_name,
    'last_name': mymember.last_name,
    'email': mymember.email,
    'phone': mymember.phone,
    'date_joined': mymember.date_joined,
    'active': mymember.active
  }

  if(mymember):
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse()
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render()) 