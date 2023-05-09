from django.db import connections, reset_queries
from cache_view.models import Restaurant, Place

print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
print()
reset_queries()

restaurants = Restaurant.objects.filter(serves_pizza=True).iterator()
# print(restaurants)
# for restaurant in restaurants:
#     #     print("----------------")
#     print(restaurant.place.name)
#     print(restaurant.place.city)


print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
reset_queries()
print("------------")

restaurants = Restaurant.objects.filter(serves_pizza=True)
# print(restaurants)
# for restaurant in restaurants:
#     #     print("----------------")
#     print(restaurant.place.name)
#     print(restaurant.place.city)
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
