

def main():
    try:
        from soil import sample
        moisture = sample()
        days = 0
        print(f"Days {days}: Moisture {moisture}")

        while moisture>20:
            moisture = sample()
            days += 1
            print(f"Days {days}: Moisture {moisture}")

        print("Time to water! ")
    except ModuleNotFoundError:
        print("No module named 'soil'")


main()