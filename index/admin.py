from django.contrib import admin
from .models import Category,Vendor,Product,ProductImges,CartOrder,CartOrderItems,ProductReview,Wishlist,Address 


# import list BannerImage, FeaturedCategories, FeaturedCategorieSlider, FeaturedCategorieMenu,ProductCards, 

# amir start 

# @admin.register(BannerImage)
# class BannerImageAdmin(admin.ModelAdmin):
#     list_display = ['name','description','image',]

# @admin.register(FeaturedCategories)
# class FeaturedCategoriesAdmin(admin.ModelAdmin):
#     list_display = [
#         'fruit_name',
#         'color',
#         'total_item',
#         'frtimage',
#     ]

# @admin.register(FeaturedCategorieSlider)
# class FeaturedCategorieSliderAdmin(admin.ModelAdmin):
#     list_display = ['slogan','featured_image_slider',]

# @admin.register(FeaturedCategorieMenu)
# class FeaturedCategorieMenuAdmin(admin.ModelAdmin):
#     list_display = ['name']
    

# @admin.register(ProductCards)
# class ProductCardsAdmin(admin.ModelAdmin):
#     list_display = [
#         'vendorName',
#         'FrontImage',
#         'SecondImage',
#         'status',
#         'status_tittle',
#         'Type_food',
#         'ProductTittle',
#         'old_price',
#         'current_Price',
#         'category',
#     ]

# amir end 

    
class ProductImgesAdmin(admin.TabularInline):
    model = ProductImges


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']


@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price','paid_status','order_date','Product_status']


@admin.register(CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no','item','image','qty','price','total']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','date']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status',]












    


# Register your models here.
