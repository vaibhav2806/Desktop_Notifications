import time
#Plyer is a Python library for accessing features of your hardware / platforms.
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "** Please drink water! ",
            message = "Drink water and keep yourself hydrated",
            #app_icon = "D:\desktop_notifications",
            timeout = 5
        )
        time.sleep(6)
