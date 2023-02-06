from django.contrib import admin
from django.contrib.admin.sites import AdminSite, site
from .models import SiteVisit, Amenity, Place, Restaurant, Waiter
from django.urls import reverse
from django.utils.http import urlencode

# Register your models here.
admin.site.register((SiteVisit))

class AmenityAdmin(admin.ModelAdmin):
    """Amenity admin"""
    # ERRORS:<class 'cache_view.admin.PlaceAdmin'>: (admin.E040) ModelAdmin must define "search_fields", because it's referenced by PlaceAdmin.
    # autocomplete_fields.
    exclude = ()
    search_fields = ("name",)


class WaiterAdmin(admin.ModelAdmin):
    """receipt admin"""
    # inlines = [PlaceInline]
    # exclude = ('birth_date',)
    # list_select_related = ('author', 'category') tell Django to use select_related() in retrieving the list of objects on the admin change list page

    list_display = ("restaurant", "name", "show_use_case")
    
    search_fields = ("name",)
    list_filter = ("restaurant", )


    # fieldsets = (
    #     (None, {
    #         'fields': ('url', 'title', 'content', 'sites')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('registration_required', 'template_name'),
    #     }),
    # )

    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }

    def show_use_case(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html
        result = SiteVisit.objects.filter(path__icontains="/cache/").aggregate(Avg("view_count"))
        return format_html("<b><i>{}</i></b>", result["view_count__avg"])
    
    show_use_case.short_description = "Average of site count"

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("place", "serves_hot_dogs", "serves_pizza", "view_waiters_link")
    search_fields = ("place",)
    # list_select_related = ('place',)# 'place_')
    # radio_fields = {"group": admin.VERTICAL}
    
    def view_waiters_link(self, obj):
        from django.utils.html import format_html
        count = obj.waiters.count()
        url = (
            reverse("admin:cache_view_waiter_changelist")
            + "?"
            + urlencode({"restaurant__place__exact": f"{obj.pk}"})
        )
        return format_html('<a href="{}">{} Waiters</a>', url, count)


class PlaceAdmin(admin.ModelAdmin):
    """Place admin"""
    list_display = ('name', 'address', 'city', 'state', 'email', 'colored_name_state')
    search_fields = ("name",)
    # <class 'cache_view.admin.PlaceAdmin'>: (admin.E038) The value of 'autocomplete_fields[0]' must be a foreign key or a many-to-many field.
    autocomplete_fields = ['amenities']
    # raw_id_fields = ("amenities",)

    # readonly_fields = ('address_report',)

    # def clean_name(self):
    #     # do something that validates your data
    #     return self.cleaned_data["name"]
    



admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Amenity, AmenityAdmin)



# """receipt model register to admin """
# from django.contrib import admin

# from .models import ReceiptFile, Receipt, ReceiptUser, Item, Vendor, VendorAddress, CardDetail
# from .services import run_mapper_and_extractor_on_receipt_file


# class ReceiptFileAdmin(admin.ModelAdmin):
#     """Receipt model admin"""

#     def save_model(self, request, obj, form, change):
#         """managing custom save"""
#         super().save_model(request, obj, form, change)
#         job_id = run_mapper_and_extractor_on_receipt_file.delay(receipt_file_pk=obj.pk)


# admin.site.register(ReceiptFile, ReceiptFileAdmin)
# admin.site.register(VendorAddress)
# admin.site.register([ReceiptUser, Item, Vendor])
# admin.site.register(CardDetail)


# class ItemInline(admin.TabularInline):
#     """item inline for receipt"""
#     model = Item

#     def has_add_permission(self, request, obj=None):
#         """add permission"""
#         return False

#     def has_delete_permission(self, request, obj=None):
#         """delete permission"""
#         return False

#     def has_change_permission(self, request, obj=None):
#         """remove change the permission"""
#         return False


# class ReceiptAdmin(admin.ModelAdmin):
#     """receipt admin"""
#     inlines = [ItemInline]


# admin.site.register(Receipt, ReceiptAdmin)


# """register models here"""
# from django.contrib import admin
# from .models import User, MailDetail, MailAttachment, NotificationLog, EmailAccount

# # Register your models here.
# admin.site.register(User)


# class EmailAccountAdmin(admin.ModelAdmin):
#     list_display = ["user", "email", 'email_provider']


# admin.site.register(EmailAccount, EmailAccountAdmin)
# admin.site.register(MailDetail)
# admin.site.register(MailAttachment)
# admin.site.register(NotificationLog)



# If you wanted to display an inline on the Person admin add/change pages you need to explicitly define the foreign key since it is unable to do so
#  automatically:

# from django.contrib import admin
# from myapp.models import Friendship

# class FriendshipInline(admin.TabularInline):
#     model = Friendship
#     fk_name = "to_person"

# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         FriendshipInline,
#     ]





# ------------------many to many
# from django.db import models

# class Person(models.Model):
#     name = models.CharField(max_length=128)

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, related_name='groups')
# If you want to display many-to-many relations using an inline, you can do so by defining an InlineModelAdmin object for the relationship:

# from django.contrib import admin

# class MembershipInline(admin.TabularInline):
#     model = Group.members.through

# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]

# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)