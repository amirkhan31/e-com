from .models import Category,Vendor,Product,ProductImges,CartOrder,CartOrderItems,ProductReview,Wishlist,Address 
from django.contrib.auth.models import AnonymousUser

def custom(request):
    hello = Category.objects.all()

    address = None
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None

    return {
        "hello" : hello,
        "add" :address
    }