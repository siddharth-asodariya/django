from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class SiteVisit(models.Model):
    """count site visist of given site"""
    path = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)

    def increment_view_count(self):
        self.view_count += 1
        self.save()
        return self.view_count

    def __str__(self) -> str:
        return str(self.path) + "  Count = " + str(self.view_count)


class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)

    @admin.display(description="Name and State", ordering="name")
    def colored_name_state(self):
        return format_html(
            '<span style="color: #{};">{} --{}</span>',
            '{:02X}{:02X}{:02X}'.format(2*self.id, 45*self.id, 87*self.id),
            self.name,
            self.state,
        )

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.email

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="waiters")
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)

    class Meta:
        ordering = ("name",)
        # Adding the ordering attribute will default all queries on Person to be ordered by last_name then first_name. Django will respect this default order both in the 
        # admin and when fetching objects.
    #     indexes = [
    #         models.Index(fields=['last_name', 'first_name']),
    #         models.Index(fields=['first_name'], name='first_name_idx'),
    #     ]



# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.db import models

# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     courses = models.ManyToManyField("Course", blank=True)

#     class Meta:
#         verbose_name_plural = "People"

# class Course(models.Model):
#     name = models.TextField()
#     year = models.IntegerField()

#     class Meta:
#         unique_together = ("name", "year", )

# class Grade(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     grade = models.PositiveSmallIntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(100)])
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)





# from django.contrib.con

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, ReverseGenericManyToOneDescriptor
"""
    Provide a generic many-to-one relation through the ``content_type`` and
    ``object_id`` fields.

    This class also doubles as an accessor to the related object (similar to
    ForwardManyToOneDescriptor) by adding itself as a model attribute.
"""
# GenericForeignKey tries to give you a ForeignKey behavior but instead to be against one type of object, 
# they do it for a set of object types (that's why they are defined with 2 columns, 
# 1 to keep the primary_key and another to keep the content_type).
# https://stackoverflow.com/a/40150127/19526287


# from django.db import models

# class Image(models.Model):
#     image = models.ImageField(upload_to="images")
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey("content_type", "object_id")

# class Product(models.Model):
#     name = models.CharField(max_length=100)