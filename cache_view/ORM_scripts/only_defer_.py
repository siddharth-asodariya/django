from django.db import connections, reset_queries
from cache_view.models import Restaurant, Place

print(Place.objects.all())  # queryset
print("Place.objects.all()  # queryset")
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("\n\n")


print(Place.objects.values("name", "city"))  # dict
print('Place.objects.values("name", "city")  # dict')
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("\n\n")


print(Place.objects.values_list("name", "city"))  # tuple
print('Place.objects.values_list("name", "city")  # tuple')
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("\n\n")


print(Place.objects.all().defer("name", "city")[0].name)
print('Place.objects.all().defer("name", "city")[0].name')
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("\n\n")


print(Place.objects.all().only("name", "city")[0].address)
print('Place.objects.all().only("name", "city")[0].address')
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("\n\n")
