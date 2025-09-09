from locust import HttpUser, between
from tasks.booking_tasks import BookingTasks

class NormalLoadUser(HttpUser):
    tasks = [BookingTasks]
    wait_time = between(0,1)