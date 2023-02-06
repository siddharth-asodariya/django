# # https://pypi.org/project/django-query-profiler/

# django-query-profile can be used if want to check the sql query performance.

# This is a query profiler for Django applications, for helping developers answer the question “My Django code/page/API is 
# slow, How do I find out why?”

# Below are some of the features of the profiler:

# Shows code paths making N+1 sql calls: Shows the sql with stack_trace which is making N+1 calls, along with sql count

# Shows the proposed solution: If the solution to reduce sql is to simply apply a select_related or a prefetch_related, this 
# is highlighted as a suggestion

# Shows exact sql duplicates: Count of the queries where (sql, parameters) is exactly the same. This is the kind of sql 
# where implementing a query cache would help

# Flame Graph visualisation: Collects all the stack traces together to allow quickly identifying which area(s) of code is 
# causing the load to the database

# Command line or chrome plugin: The profiler can be called from command line via context manager, or can be invoked via a 
# middleware, and output shown in a chrome plugin

# Super easy to configure in any application: The only changes are in settings.py file and in urls.py file