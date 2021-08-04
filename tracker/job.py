from pycoingecko import CoinGeckoAPI
from django.utils import timezone
from schedule import Scheduler
import threading
import time
from django.core.mail import EmailMessage


class EmailTread(threading.Thread):
    def __init__(self, email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send(fail_silently=False)    


def my_tracker_job():
	cg = CoinGeckoAPI()
	bitcoin = cg.get_price(ids='bitcoin', vs_currencies='usd')
	name = [i for i in bitcoin.keys()][0]
	price_in_usd = bitcoin['bitcoin']['usd']
    
	qs = Alert.objects.filter(alert_owner=self.request.user)
	triggered_at = timezone.now()
	if price_in_usd <= qs.price:
		qs.update(triggered=True, triggered_at=triggered_at)
		for alert in qs:
			alert.save()
    #send email
    email_ids = [i.alert_owner.email for i in qs]
    email_subject = 'Bitcoin price is lower than your set alert price'
    email_message = EmailMessage(
                    email_subject,
                    'Hi '+qalert.alert_owner + ', Bitcoin price is lower than your set alert price \n',
                    '<from email-id>',
                    email_ids,
                )
    EmailTread(email_message).start()


def run_continuously(self, interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously				

def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(10).minutes.do(my_tracker_job)
    scheduler.run_continuously()
 	  