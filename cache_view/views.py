import time

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.db import reset_queries 
from .utils import query_count_all, create_or_increment_site_count
from .constant import IMAGE_NAME_LIST
from .models import SiteVisit, Restaurant, Place


# Create your views here.
def home(request):
    """home page"""
    context = {
    }
    return render(request, 'base.html', context=context)


# Note: Overuse of Data Caching can cause memory issues if data is constantly added and removed to and from the cache.
#server-side cache-----Data Caching
@cache_page(60 * 2)
def test_cache(request):
    """test cache in browser"""
    print("Comes to test_cache view")
    visited_count = create_or_increment_site_count(request.path)
    context = {
        "visited_count": visited_count
    }
    return render(request, 'site_visit_count.html',context=context)


def test_fragment_cache(request):
    """test cache in browser"""
    # {% cache my_timeout sidebar %} ... {% endcache %}
    # section will be cached and db queries can be avoided
    visited_count = create_or_increment_site_count(request.path)
    image_name = IMAGE_NAME_LIST[visited_count % 6]
    print(image_name)

    context = {
        "visited_count": visited_count,
        "image_name": image_name
    }
    return render(request, 'site_visit_fragment_cache.html',context=context)


# As the accepted answer says you must consume the queryset first since it's lazy (e.g. list(qs)).
# Another reason can be that you must be in DEBUG mode (see FAQ):
# connection.queries is only available if Django DEBUG setting is True.
def db_call_count(request):
    """test cache in browser"""
    visited_count = create_or_increment_site_count(request.path)
    restaurant = Restaurant.objects.all()[0]
    for waiter in restaurant.waiters.all():
        print(waiter.restaurant.place.name)
    queries_count = query_count_all()
    context = {
        "visited_count": visited_count,
        "queries_count": queries_count,
        "restaurant_object": restaurant,
        "query_func": query_count_all,
    }
    # {% load cache %}
    # {% cache 60 user_details user_instance %}
    #     <p>First name: {{ user_instance.first_name }}</p>
    #     <p>Last name: {{ user_instance.last_name }}</p>
    # {% endcache %}
    # In above example, user's first name and last name details will be cached but,
    # here multiple cache copies will be created based on the user_instance value.
    # Better performance can be seen once caching is applied at multiple templates and bigger chunks of templates.

    return render(request, 'queries_count.html',context=context)


#iterator
# A QuerySet typically caches its results internally so that repeated evaluations do not result in additional queries. In contrast, iterator() will 
# read results directly, without doing any caching at the QuerySet level (internally, the default iterator calls iterator() and caches the return 
# value). For a QuerySet which returns a large number of objects that you only need to access once, this can result in better performance and a 
# significant reduction in memory.


def use_iterator(request):
    """use iterator in query"""
    # visited_count = create_or_increment_site_count(request.path)

    # reset_queries()
    restaurants = Restaurant.objects.filter(serves_pizza=True).iterator()
    # print(restaurants)
    for restaurant in restaurants:
    #     print("----------------")
        print(restaurant.place.name)
        print(restaurant.place.city)
    # # queries_count = query_count_all()
    print(query_count_all())
    # reset_queries()
    
    # restaurants = Restaurant.objects.filter(serves_pizza=True).iterator()
    # print(type(restaurants))
    # for restaurant in restaurants:
    #     print(restaurant.serves_pizza)
    # queries_count1 = query_count_all()


    # context = {
    #     "visited_count": visited_count,
    #     "queries_count": queries_count,
    #     "queries_count1": queries_count1,
    #     "restaurant_object": restaurant,
    #     "query_func": query_count_all,
    # }
    # return render(request, 'queries_count.html',context=context)
    return HttpResponse("NOthignn")


# Restaurant.objects.in_bulk([1])
# {1: <Restaurant: gvalia purani delhi the restaurant>}
# >>> Restaurant.objects.in_bulk([2])
# {2: <Restaurant: saffron the restaurant>}
# >>> type(Restaurant.objects.in_bulk([2]))
# <class 'dict'>
# >>> Restaurant.objects.in_bulk()
# {1: <Restaurant: gvalia purani delhi the restaurant>, 2: <Restaurant: saffron the restaurant>, 3: <Restaurant: TORITOS the restaurant>, 4: <Restaurant: From the north the restaurant>}
# >>> Restaurant.objects.in_bulk(field_name="place")
# {<Place: gvalia purani delhi the place>: <Restaurant: gvalia purani delhi the restaurant>, <Place: saffron the place>: <Restaurant: saffron the restaurant>, <Place: TORITOS the place>: <Restaurant: TORITOS the restaurant>, <Place: From the north the place>: <Restaurant: From the north the restaurant>}
# >>> from cache_view.models import Restaurant, Place
# >>> p = Place.objects.first()
# >>> Restaurant.objects.in_bulk(field_name="place")[p]
# <Restaurant: gvalia purani delhi the restaurant>

# def bulk_query(request):
#     """run query in bulk"""
#     from datetime import datetime
#     start_time = datetime.now()
#     for i in range(100):
#         SiteVisit.objects.create(
#             path="/"+str(i)+"/"
#         )
#     print("time before---", datetime.now()-start_time)

#     start_time1 = datetime.now()
#     sitevisit_instances = []
#     for i in range(100):
#         sitevisit_instances.append(SiteVisit(path="/"+str(i)+"/"))
#     SiteVisit.objects.bulk_create(sitevisit_instances)
#     print("time using bulk---", datetime.now()-start_time1)

#     # 10x faster
#     # time before------- 0:00:00.236880
#     # time using bulk--- 0:00:00.006943

#     sitevisit_instances_delete = SiteVisit.objects.exclude(id__in=[1, 2, 3, 4])
#     sitevisit_instances_delete.delete()

#     return HttpResponse("query bulk has beeen created and deleted.")


# def bulk_query(request):
#     """select_related"""
#     restaurants = Restaurant.objects.all().iterator()
#     for restaurant in restaurants:
#         print(restaurant.place.name)
#     print(query_count_all())
#     before_query_count = query_count_all()

#     restaurants = Restaurant.objects.select_related('place')
#     for restaurant in restaurants:
#         print(restaurant.place.name)
#     print("after--", before_query_count - query_count_all())


#     # """prefetcg related"""
#     # restaurants = Restaurant.objects.all() #prefetch_related('place__amenities')
#     # for restaurant in restaurants:
#     #     print(restaurant.place.amenities.all())


#     # places = Place.objects.all()#.prefetch_related('amenities')
#     # print([[print(i) for i in place.amenities.all()] for place in places])

#     return HttpResponse("select related and prefetch related.")


def bulk_query(request):
    """small learning"""
    Place.objects.all() #queryset
    Place.objects.values('name', 'city') # dict
    # >>> Place.objects.all()
    # <QuerySet [<Place: gvalia purani delhi the place>, <Place: saffron the place>, <Place: TORITOS the place>, <Place: From the north the place>]>
    # >>> Place.objects.values('name', 'city')
    # <QuerySet [{'name': 'gvalia purani delhi', 'city': 'ahmedabad'}, {'name': 'saffron', 'city': 'Ahmedabad'}, {'name': 'TORITOS', 'city': 'Ahmedabad'}, {'name': 'From the north', 'city': 'Ahmedabad'}]>

    # avoid the unnecessary overhead of fetching and mapping the extra columns with the queryset

    Place.objects.values_list('name', 'city') # tuple
    # <QuerySet [('gvalia purani delhi', 'ahmedabad'), ('saffron', 'Ahmedabad'), ('TORITOS', 'Ahmedabad'), ('From the north', 'Ahmedabad')]>
    # Whenever, we try to access the other column from the queryset, that column details will be fetched from the database on that specific instance.

    Place.objects.all().defer('name', 'city')[0].name
    # 'gvalia purani delhi'
    # >>> connections.all()[0].queries
    # [{'sql': 'SELECT "cache_view_place"."id", "cache_view_place"."address", "cache_view_place"."state", "cache_view_place"."email" FROM "cache_view_place" LIMIT 1', 'time': '0.000'}, {'sql': 'SELECT "cache_view_place"."id", "cache_view_place"."name" FROM "cache_view_place" WHERE "cache_view_place"."id" = 1 LIMIT 21', 'time': '0.000'}]

    Place.objects.all().only('name', 'city')[0].address
    # >>> Place.objects.all().only('name', 'city')[0].address
    # 'south bopal'
    # >>> connections.all()[0].queries
    # [{'sql': 'SELECT "cache_view_place"."id", "cache_view_place"."name", "cache_view_place"."city" FROM "cache_view_place" LIMIT 1', 'time': '0.000'}, {'sql': 'SELECT "cache_view_place"."id", "cache_view_place"."address" FROM "cache_view_place" WHERE "cache_view_place"."id" = 1 LIMIT 21', 'time': '0.000'}]

    return HttpResponse("select related and prefetch related.")



# Use Redis for caching as it is blazzingly faster. It stores all the data into RAM.
# Redis support lots of data structures which can be helpful to store various kind of data. Make sure to check time complexity of each operation on data structure 
# before using any data structure.
# Always try to choose the data structure whose operations we are going to perform are not proposonal to data size. As an example, fetching the value by the 
# key has always O(1) complexity in Redis. It's performance will be consistant in case of any volume.
# If achieving O(1) is not possible then we can go with the other data structures with nearby lesser complexities. In any case, we should have the fair idea 
# of the worst case complexities.


import csv
from django.http import StreamingHttpResponse
def csv_response(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    writer =csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

from django.utils.functional import lazy
def delaying_fun(sec: int):
    time.sleep(sec)
    return f"Slept enough for {sec} seconds"

def lazy_example(request):
    return HttpResponse(str(lazy(delaying_fun(10))))

# Use lazy for the variables which can take time to evalute.
# lazy function in the django will only evalute the variable value whenever they are being used.
# Follow the great article to better understand the concept.




def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")



def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")
