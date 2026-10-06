def daily_pay(wage, hours, shift):
    if shift == "day":
        return wage * hours
    else:
        return wage * hours * 125 // 100
wage = int(input())
transport_allowance = int(input())
days = int(input())
total_hours = 0
total_wages = 0
for i in range(days):
    hours = int(input())
    while hours < 1 or hours > 12:
        print("Invalid hours")
        hours = int(input())
    shift = input().strip().lower()
    while shift not in ("day", "night"):
        print("Invalid shift")
        shift = input().strip().lower()
    pay = daily_pay(wage, hours, shift)
    total_hours += hours
    total_wages += pay
    print(f"Day {i + 1}: {hours} hours ({shift}) ¥{pay}")
total_transport = transport_allowance * days
total_pay = total_wages + total_transport
print(f"Total hours: {total_hours}")
print(f"Total wages: ¥{total_wages}")
print(f"Transport: ¥{total_transport}")
print(f"Total pay: ¥{total_pay}")
if total_hours > 28:
    print("Warning: over 28 hours.")
else:
    print("Within 28-hour limit")