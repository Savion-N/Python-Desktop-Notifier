from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "./clock.ico",
        timeout = 15,
    )


if __name__ == '__main__':
    while True:
        notifyMe("Hey Savion, take a break now!", "You should use your device for only 20 miniutes at a time to keep your eyes healthy")
        time.sleep(1200)
        # Use pythonw and your files name in the terminal to make the program run automatically in the background.