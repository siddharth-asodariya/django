from django.db import connections, reset_queries
from cache_view.models import Restaurant

print([r.place for r in Restaurant.objects.all()])
reset_queries()

a = Restaurant.objects.filter(serves_pizza=True).count()
b = Restaurant.objects.all().exists()

print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))


# [<Place: gwalia purani delhi the place>, <Place: saffron the place>, <Place: TORITOS the place>, <Place: From the north the place>]
# SELECT COUNT(*) AS "__count" FROM "cache_view_restaurant" WHERE "cache_view_restaurant"."serves_pizza"

# SELECT 1 AS "a" FROM "cache_view_restaurant" LIMIT 1
