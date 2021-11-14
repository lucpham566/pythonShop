from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from article.models import New, NewCate
# Create your views here.

class NewsPage(View):
    def get(self,request):
        new_cates = NewCate.objects.all()
        news = New.objects.all()
        new_specials = New.objects.filter(special = True)
        context = {'new_cates':new_cates, 'news':news, 'new_specials':new_specials}
        return render(request,'news.html', context)


class NewDetail(View):
    def get(self,request,id):
        # return HttpResponse(id)
        thisnew = New.objects.get(pk = id)
        new_specials = New.objects.filter(special=True)
        newcates = NewCate.objects.all()
        context = {'thisnew':thisnew, 'newcates':newcates, 'new_specials':new_specials}
        return render(request,'new-detail.html', context)