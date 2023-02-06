"""ORM scripts"""
from django.db import connections, reset_queries
from cache_view.models import Restaurant
r =Restaurant.objects.all()
r[0].place.amenities.all()
sum(len(c.queries) for c in connections.all())

# 1. caceh
# 2. fragment cache
# 3. db count
# 4. setting debug app append
# 5. ORM query iterator
