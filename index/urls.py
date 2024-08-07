from django.urls import path
from .views import home,deal,about,vendor,product,blog_list,blog_details,contact,product_list_view,category_list_view,category_view_list,vendor_list,vendor_detail_view,product_detail_view,tag_list,ajax_add_review,search_view

app_name = "core"

urlpatterns = [
    # Homepage 
    path('',home, name="home"),
    path('product-list',product_list_view, name="product-list"),

    # product detail view 
    path('product-detail/<pid>',product_detail_view,name="product-details"),

    # Category 
    path('category',category_list_view, name="category-list"),
    path('category/<cid>',category_view_list, name="category-view-list"),

    # vendor-list 

    path('vendors/',vendor_list,name='vendor-list'),
    path('vendor/<vid>',vendor_detail_view,name='vendor-detail'),

    # add review path 

    path('ajax-add-review/<slug:pid>/',ajax_add_review,name='ajax-add-review'),

    # search product 

    path('search_view',search_view,name="search"),


    # Tags 
    path('products/tag/<slug:tag_slug>',tag_list,name="tags"),



    path('deal',deal,name="deal"),
    path('about',about,name='about'),
    path('vendor',vendor,name='vendor'),
    path('product',product,name="product"),
    path('blog',blog_list,name="blog"),
    path('blog-details',blog_details,name="blog-details"),
    path('contact',contact,name="contact")
]


