import psutil


def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        print("Battery information not available")
        return
    percent = battery.percent
    charging = battery.power_plugged
    if charging:
        print(f"Laptop is charging: AND charging percent is: {percent}%")
    else:
        print(f"Laptop is not charging: AND charging percent is: {percent}%")


get_battery_status()
