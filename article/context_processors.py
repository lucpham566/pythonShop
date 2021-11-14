from article.models import New, NewCate


# def get_product_cate(request):
#     product_cates =  ProductCate.objects.all()
#     return {
#         'common_product_cates': product_cates,
#     }

def get_new_special(request):
    new_specials =  New.objects.filter(special = True)
    return {
        'common_new_specials': new_specials,
    }