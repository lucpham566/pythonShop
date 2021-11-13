from product.models import Product, ProductCate


def get_product_cate(request):
    product_cates =  ProductCate.objects.all()
    return {
        'common_product_cates': product_cates,
    }

def get_product_special(request):
    product_specials =  Product.objects.filter(special = True)
    return {
        'product_specials': product_specials,
    }