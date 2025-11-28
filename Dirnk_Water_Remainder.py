import time
from win10toast import ToastNotifier

toast=ToastNotifier()

while True:
    toast.show_toast(
        #  Title
        "Drink Water Remainder",
        "Hey its time to drink water",
        duration=20,
        threaded=True
    )
    time.sleep(7200)
