from django.db import models
from colorfield.fields import ColorField
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField




def user_directory_path(instance,filename):
    return f'user_{instance.user.id}/{filename}'


STATUS_CHOICE = (
    ("process","process"),
    ("shipped","shipped"),
    ("delivered","delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("in_review", "In Review"),
    ("rejected", "Rejected"),
    ("published", "Published"),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)



# amir start 


# amir end


class Tags(models.Model):
    pass



class Category(models.Model):
    cid = ShortUUIDField(unique=True, max_length=20, length=10, prefix="cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />') 

    
    def __str__(self):
        return self.title
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, max_length=20, length=10, prefix="ven",alphabet="abcdefgh12345")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=user_directory_path)
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    # description = models.TextField(null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)

    address = models.CharField(max_length=100, default="123 New Delhi")
    contact = models.CharField(max_length=100, default="7678501657")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    date = models.DateField(auto_now_add=True, null=True, blank=True)
     
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />') 

    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=20, length=10, alphabet="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="vendor")



    title = models.CharField(max_length=50, default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    # description = models.TextField(null=True, blank=True, default="This is the Product")
    description = RichTextUploadingField(null=True, blank=True, default="This is the Product")

    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="2.99")

    # specification = models.TextField(null=True, blank=True) 
    specification = RichTextUploadingField(null=True, blank=True)

    type = models.CharField(max_length=100, default="Organic", null=True, blank=True)
    stock_count = models.CharField(max_length=100, default=10, null=True, blank=True)
    life = models.CharField(max_length=100, default="100 Days", null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    tags = TaggableManager(blank=True)


    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, max_length=10, length=4, prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />') 

    
    def __str__(self):
        return self.title
    
    def get_precentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    

class ProductImges(models.Model):
    images = models.ImageField(upload_to="Multi_Img_Pro", default="product_list.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="p_image")
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Products Image"
    

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    Product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Order"

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="1.99")
    
    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % {self.image}) 


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="review")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products Reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"



