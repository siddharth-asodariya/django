# Profile the code
# Code profiler is a tool which can showcase each and every function call along with time it took to execute. Mordern profilers also showcase insightful visulizations.
# Django profiler can give the good insight on each function call time and tree of exection of function.
# Profiling helps to find out what lib or snippet of the code is creating roadblock. Later, it can be fixed by the developer.
# Profiling should be scheduled at regular intervals and while doing the development django-silk can be used. It can profile the each and every request and can visulize it.
# Python also has built in profiling support.
# Python call graphs can be generated with tools tuna and pycallgraph.


# Django silk stores response time, route, call profile, sql queries details for each request.
# should enabled only for needed time only, because it stores the request data into database which over the time creates 
# lots of data blot into database.
# On production environment we should not use the django silk.

import cProfile
import re
cProfile.run('re.compile("foo|bar")')

# python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)


# pip install pycallgraph

# pip install tuna  