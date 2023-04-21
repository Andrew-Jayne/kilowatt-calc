def get_battery_capacity():
    print("Enter Battery Capacity in kWh")
    battery_capacity = int(input())

def get_power_needed():
    #operate in varibles
    percent_needed = target_percent - starting_percent
    target_kwh = (battery_capacity / 100) * percent_needed

def complete_cost_by_kwh():
    # Cost for per KWH
    by_kwh_cost = kwh_cost * target_kwh
    print(f"Your Cost to charge to {target_percent}% ({target_kwh} kWh) is:")
    print("${:0.2f}\n".format(by_kwh_cost))

def complete_cost_by_time():
    # Cost for by Time
    time_needed = target_kwh / charge_rate
    by_time_cost = (time_needed * per_min_cost) * 60
    print(f"Your Cost to charge to {target_percent}% ({target_kwh} kWh) is:")
    print("${:0.2f}\n".format(by_time_cost))


print("How Does the Charge charge for Power?")
print("By kWh or By Time")
charger_type = input().lower

match charger_type:
    case "time":
        print("Enter Target Battery Charge")
        target_percent = int(input())
        print("Enter Current Battery Charge")
        starting_percent = int(input())
        print("Enter Cost Per Min")
        per_min_cost = float(input())
        print("Enter Charger Charge Rate in kWh")
        charge_rate = int(input())
        get_battery_capacity
        complete_cost_by_time
    case "kwh":
        print("Enter Target Battery Charge")
        target_percent = int(input())
        print("Enter Current Battery Charge")
        starting_percent = int(input())
        print("Enter Cost Per kWh")
        kwh_cost = float(input())
        get_battery_capacity
        complete_cost_by_kwh
    case "free":
        print("then why are you asking...")
        exit()
    case "*":
        print("Your Choice was invalid. Please try again")
