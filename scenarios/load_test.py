from tasks.booking_tasks import BookingTasks
from locust import HttpUser, between

class LoadTestUser(HttpUser):
    tasks = [BookingTasks]
    wait_time = between(1,2)