import matplotlib.pyplot as plt

rides = []

def add_ride():
    try:
        distance = float(input("Enter distance (km): "))
        hrs = int(input("Enter time (hours): "))
        mins = int(input("Enter time (minutes): "))
        secs = int(input("Enter time (seconds): "))
        total_time = hrs * 60 + mins + (secs / 60)   # convert into minutes

        avg_speed = float(input("Enter average speed (km/h): "))

        # If avg speed entered > 0, override time with distance/speed
        if avg_speed > 0:
            total_time = (distance / avg_speed) * 60

        rides.append((distance, total_time, avg_speed))
        print("✅ Ride saved!")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
    input("\nPress Enter to continue...")

def show_summary():
    if not rides:
        print("⚠ No rides added yet!")
    else:
        total_distance = sum(r[0] for r in rides)
        total_time = sum(r[1] for r in rides)
        avg_speed = (total_distance / (total_time / 60)) if total_time > 0 else 0

        print("\n📊 Ride Summary 📊")
        print(f"Total Rides: {len(rides)}")
        print(f"Total Distance: {total_distance:.2f} km")
        print(f"Total Time: {total_time/60:.2f} hrs")
        print(f"Average Speed: {avg_speed:.2f} km/h")

        # Prepare data
        distances = [r[0] for r in rides]
        avg_speeds = [r[2] for r in rides]
        x = range(1, len(rides) + 1)

        # Single Graph with Bars + Line
        fig, ax1 = plt.subplots()

        # Bar chart for distance
        ax1.bar(x, distances, color="skyblue", label="Distance (km)")
        ax1.set_xlabel("Ride Number")
        ax1.set_ylabel("Distance (km)", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        # Line chart for avg speed (secondary axis)
        ax2 = ax1.twinx()
        ax2.plot(x, avg_speeds, color="red", marker="o", label="Avg Speed (km/h)")
        ax2.set_ylabel("Avg Speed (km/h)", color="red")
        ax2.tick_params(axis="y", labelcolor="red")

        # Title + Legend
        plt.title("Cycle Ride Tracker: Distance & Avg Speed")
        fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

    input("\nPress Enter to continue...")

while True:
    print("\n🚴 Cycle Ride Tracker 🚴")
    print("1. Add Ride")
    print("2. Show Summary")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_ride()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("👋 Goodbye! Keep riding 🚴💨")
        break
    else:
        print("❌ Invalid choice!")
        input("\nPress Enter to continue...")