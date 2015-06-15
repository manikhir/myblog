from celery.task.schedules import crontab
# from celery.decorators import periodic_task


# # this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
# @periodic_task(run_every=crontab(minute=1))
# def test():
#     print "MANISHA123456789"

from celery.decorators import periodic_task
from datetime import timedelta
from blogs.models import Blog

# @periodic_task(run_every=timedelta(seconds=30))
# def manisha():
#     print("Running periodic task!")


@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    try:
	    N = datetime.today()
	    date_N_days_ago = N - timedelta(days=15)
	    # blog = Blog.objects.filter(date__range=(N,date_N_days_ago) ).delete()
	    log.objects.filter(date__lt=date_N_days_ago).delete()
	    print("Delete Data Succefully")
    except:
        print("there are no record")