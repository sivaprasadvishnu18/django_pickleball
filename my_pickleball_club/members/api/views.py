from django.http import JsonResponse
from members.models import Member
from members.api.serializers import MemberSerializer

def members(request):
  mymembers = Member.objects.all()
  serializer = MemberSerializer(mymembers, many=True)
  return JsonResponse(serializer.data, safe=False)
  
def details(request, id):
  mymember = Member.objects.get(memberId=id)
  serializer = MemberSerializer(mymember, many=False) 
  return JsonResponse(serializer.data, safe=False)
  