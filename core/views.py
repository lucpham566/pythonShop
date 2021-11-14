from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from core.models import Banner, Video
# Create your views here.

class HomeView(View):
    def get(self,request):
        banners = Banner.objects.all()
        videos = Video.objects.all()
        context = {"banners" : banners,"videos" : videos}
        return render(request,'index.html',context)