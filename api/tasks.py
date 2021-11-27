from university.celery import app


@app.task
def send_schedule_to_email():
    print("------TASK DONE------")
