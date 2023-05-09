# If some request is going to take couple of seconds to return then better to use background works such as celery.
# Celery is a background worker and has support for multiple messaging brokers for the communication.
# djcelery is the well mantained package to use the celery with Django.
# celery communicaty also has celery-beat to run cronjobs or periodic background jobs.
# celery also supports various conditional parameters to retry, alerting, chain of task executions.
# celery can have multiple machines attached to single cluster. Therefore, based on the more load, more computing power can be added.
# celery also has rich dashboard support to visulize the working of workers.
# celery should be used with the messaging broker which provides better persistance and resillent.
