from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from core.models import Banner, Subscriber, Video, ShopService, Reviewer
# Create your views here.

class HomeView(View):
    def get(self,request):
        banners = Banner.objects.all()
        videos = Video.objects.all()
        shopservices = ShopService.objects.all()
        reviewers = Reviewer.objects.all()
        context = {"banners" : banners,"videos" : videos, "shopservices":shopservices, 'reviewers':reviewers}
        return render(request,'index.html',context)

def addSubscriber(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    subscriber = Subscriber.objects.create(name=name, email=email, phone=phone, address=address)
    subscriber.save()
    # return JsonResponse({"success":"thành công"})
    
    return JsonResponse({"success":"thành công"})