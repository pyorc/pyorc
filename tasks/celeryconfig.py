# -*- coding: utf-8 -*-


from celery import Celery


def my_on_failure(self, exc, task_id, args, kwargs, einfo):
    print('Oh no! Task failed: {0!r}'.format(exc))


app = Celery(broker='amqp://guest@localhost//',
             backend='amqp://',
             include=['tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_IGNORE_RESULT=True,
    CELERYD_MAX_TASKS_PER_CHILD=300,
    CELERY_TASK_SERIALIZER='json'
)

# CELERY_ANNOTATIONS = {
#     '*': {
# i        'rate_limit': '10/s',
#         'on_failure': my_on_failure
#     }
# }
