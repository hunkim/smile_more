from apscheduler.schedulers.blocking import BlockingScheduler
import main_job as mj
import settings

def main_job():
    mj.main_job()

scheduler = BlockingScheduler()
scheduler.add_job(main_job, 'interval',
                  minutes=settings.CAMERA_INTERVAL)
scheduler.start()