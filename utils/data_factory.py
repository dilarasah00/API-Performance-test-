import random
import datetime

def random_booking_data():
    return {
    "firstname" : random.choice(["John","Jim","Bob","Kevin","Alice"]),
    "lastname" : "Tester",
    "totalprice" : random.randint(100,500),
    "depositpaid" : random.choice([True,False]),
    "bookingdates" : {
        "checkin" : str(datetime.date.today()),
        "checkout" : str(datetime.date.today() + datetime.timedelta(days=5))
    },
    "additionalneeds" : random.choice(["breakfast","lunch","None"])
}