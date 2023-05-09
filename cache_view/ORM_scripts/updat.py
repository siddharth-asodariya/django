from django.db import connections, reset_queries
from cache_view.models import Restaurant, Place

p = Place.objects.create(
    name="temp", address="simform sol", city="ahm", state="guj", email="s@gmail.com"
)
print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))
print()
reset_queries()

p.address = "Simfrom solutions"
p.save()
p.address = "Simform solutions"
p.save(update_fields=["address"])

print("\n\n".join(query.get("sql") for c in connections.all() for query in c.queries))

p = Place.objects.filter(name="tmp")
del p
