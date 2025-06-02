current_time = int(input("Enter current time in 24-hour format (0–23): "))

wait_hours = int(input("Enter number of hours to wait for alarm: "))

alarm_time = (current_time + wait_hours) % 24

print(f"The alarm will go off at: {alarm_time}:00")
