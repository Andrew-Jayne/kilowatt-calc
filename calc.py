#!/opt/homebrew/bin/python3.11
charger_type = str(input("How Does the Charge charge for Power?: By kWh or By Time ").lower())
lap = 0
is_valid = False

while is_valid != True:
    if charger_type not in ("time","kwh","free"):
        lap += 1
        if lap == 10:
            print()
            print("You're really bad at this, just type 'time' or 'kwh'")
            print("I'm surprised you can tie your shoes")
            exit()
        print("That is not a valid choice try again")
        charger_type = str(input("How Does the Charge charge for Power?: By kWh or By Time ").lower())
    else:
        is_valid = True

match charger_type:
    case "time":
        target_percent = int(input("Enter Target Battery Charge "))
        starting_percent = int(input("Enter Current Battery Charge "))
        per_min_cost = float(input("Enter Cost Per Min in $ "))
        charge_rate = int(input("Enter Charger Charge Rate in kWh "))
        battery_capacity = int(input("Enter Battery Capacity in kWh "))
        percent_needed = target_percent - starting_percent
        target_kwh = (battery_capacity / 100) * target_percent
        time_needed = target_kwh / charge_rate
        pretty_time = time_needed * 60
        by_time_cost = (time_needed * per_min_cost) * 60
        print()
        print(f"Your Cost to charge to {target_percent}% ({target_kwh} kWh) over ~{pretty_time} Minutes is:")
        print("${:0.2f}\n".format(by_time_cost))

    case "kwh":
        target_percent = int(input("Enter Target Battery Charge "))
        starting_percent = int(input("Enter Current Battery Charge "))
        kwh_cost = float(input("Enter Cost Per kWh in $ "))
        battery_capacity = int(input("Enter Battery Capacity in kWh"))
        percent_needed = target_percent - starting_percent
        target_kwh = (battery_capacity / 100) * target_percent
        by_kwh_cost = kwh_cost * target_kwh
        print()
        print(f"Your Cost to charge to {target_percent}% ({target_kwh} kWh) is:")
        print("${:0.2f}\n".format(by_kwh_cost))

    case "free":
        print("then why are you asking... ")