import psutil

def check_battery_health():
    battery = psutil.sensors_battery()
    
    if battery is None:
        return "Battery information not available. Make sure you're running this on a laptop."

    percent = battery.percent
    plugged = battery.power_plugged
    time_left = battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "N/A"

    status = "Charging 🔌" if plugged else "On Battery 🔋"
    
    return f"🔋 Battery: {percent}% | Status: {status} | Estimated Time Left: {time_left} seconds"

# Run the function and display the battery info
print(check_battery_health())
