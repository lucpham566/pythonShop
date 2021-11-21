from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from article.models import New, NewCate
# Create your views here.

class NewsPage(View):
    def get(self,request):
        new_cates = NewCate.objects.all()
        new_list = New.objects.all().order_by('-id')
        new_specials = New.objects.filter(special = True).order_by('-id')
        paginator = Paginator(new_list, 6)
        
        page_number = request.GET.get("page")
        try:
            news = paginator.page(page_number)
        except PageNotAnInteger:
            # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
            news = paginator.page(1)
        except EmptyPage:
            # Nếu page không có item nào, trả về page cuối cùng
            news = paginator.page(paginator.num_pages)
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