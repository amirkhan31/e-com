from django.shortcuts import render,get_object_or_404
from taggit.models import Tag
from .forms import ProductReviewForms
from django.http import JsonResponse
from django.db.models import Count, Avg
from .models import Category,Vendor,Product,ProductImges,CartOrder,CartOrderItems,ProductReview,Wishlist,Address 


def home(request):
    # product = Product.objects.all()
    product = Product.objects.filter(product_status="published", featured=True)
    context = {
       'product' : product 
    }
    return render(request,'index.html',context)

def product_list_view(request):
    # product = Product.objects.all()
    product = Product.objects.filter(product_status="published")
    context = {
       'product' : product 
    }
    return render(request,'product-list.html',context)

def category_list_view(request):
    category = Category.objects.all()
    context = {
        'category' : category

    }
    return render(request,'category_list.html',context)

def category_view_list(request,cid):
    category = Category.objects.get(cid=cid)
    product = Product.objects.filter(product_status="published", category=category)
    context = {
       "category" : category,
       "product" : product
    }
    return render (request,"category_view_list.html",context)

def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors" : vendors
    }
    return render(request,"vendor-list.html",context)

def vendor_detail_view(request,vid):
    vendor = Vendor.objects.get(vid=vid)
    prod  = Product.objects.filter(vendor=vendor,product_status="published")
    context = {
        "vendor" : vendor,
        "prod" : prod
    }
    return render(request,"vendor-detail.html",context)


def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    r_image = product.p_image.all()
    products = Product.objects.filter(category=product.category).exclude(pid=pid)[:4]
    print(product.pid)

    # getting all review 
    review = ProductReview.objects.filter(product=product).order_by("-date")

    # getting average review 

    avg_ratting = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # product Review form 

    review_form = ProductReviewForms()


    context = {
        "p" : product,
        "r_image" : r_image,
        "review" : review,
        "products" : products,
        "review_form" : review_form,
        "avg_ratting" : avg_ratting
    }
    return render(request,"product-details.html",context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None
    if tag_slug:
        # tag = Product.objects.get(slug=tag_slug)
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag
    }
    # print(tag.name)
    return render(request,"tag.html",context)


def ajax_add_review(request,pid):
    product = Product.objects.get(pid=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user' : user.username,
        'review' : request.POST['review'],
        'rating' : request.POST['rating']
    }

    average_review = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context' : context,
            'average_review' : average_review
        }

    )


def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context =  {
        "products" : products,
        "query" : query
    }

    return render(request,"search.html",context)



 










# amir start 

def deal(request):
    return render(request, 'shop-grid-right.html')

def about(request):
    return render(request, "page-about.html")

def vendor(request):
    return render(request, "vendors-grid.html")

def product(request):
    return render(request, 'shop-product-right.html')

def blog_list(request):
    return render(request, "blog-category-list.html")

def blog_details(request):
    return render(request, "blog-post-right.html")

def contact(request):
    return render(request, "page-contact.html")

# amir end function 
# Create your views here.



# amir comment 

# home start

#     imagesdata = BannerImage.objects.all()
#     FeaturedCategorie = FeaturedCategories.objects.all()
#     slider = FeaturedCategorieSlider.objects.all()
#     menu = FeaturedCategorieMenu.objects.all()
#     product_details = ProductCards.objects.all()[:10]
#     categories = [
#     {'id': 'one', 'name': 'All'},
#     {'id': 'two', 'name': 'Milks & Dairies'},
#     {'id': 'three', 'name': 'Coffees & Teas'},
#     {'id': 'four', 'name': 'Pet Foods'},
#     {'id': 'five', 'name': 'Meats'},
#     {'id': 'six', 'name': 'Vegetables'},
#     {'id': 'seven', 'name': 'Fruits'},
# ]
#     context = {
#         "imagesdata" : imagesdata,
#         "FeaturedCategorie" : FeaturedCategorie,
#         "slider" : slider,
#         "menu":menu,
#         "product_details":product_details,
#         "categories": categories
#     }


# home end 
