# 🎬 Movie Ticket Booking System

# Movies and timings
movies = {
    1: "Dhurandhar",
    2: "Max",
    3: "Toxic"
}

timings = {
    1: "Morning (10 AM)",
    2: "Afternoon (2 PM)",
    3: "Evening (6 PM)"
}

PRICE = 150
GST = 0.18  # 18%

# Create seating (5x5)
seats = [[0 for _ in range(5)] for _ in range(5)]


# Function to display movies
def display_movies():
    print("\n🎬 Available Movies:")
    for key, value in movies.items():
        print(f"{key}. {value}")


# Function to display timings
def display_timings():
    print("\n⏰ Show Timings:")
    for key, value in timings.items():
        print(f"{key}. {value}")


# Function to display seats
def display_seats():
    print("\n🪑 Seat Layout (0 = Available, 1 = Booked)")
    for i, row in enumerate(seats):
        print(f"Row {i}: {row}")


# Function to book seats
def book_seats():
    count = int(input("\nHow many seats do you want to book? "))
    booked = 0

    while booked < count:
        try:
            r = int(input("Enter row (0-4): "))
            c = int(input("Enter column (0-4): "))

            if seats[r][c] == 0:
                seats[r][c] = 1
                print("✅ Seat booked!")
                booked += 1
            else:
                print("❌ Seat already booked. Choose another.")
        except:
            print("⚠️ Invalid input. Try again.")

    return count


# Function to calculate price
def calculate_price(num_seats):
    total = num_seats * PRICE
    tax = total * GST
    final = total + tax

    print("\n💰 Billing Details:")
    print("Ticket Price:", total)
    print("GST (18%):", round(tax, 2))
    print("Total Amount:", round(final, 2))


# Main program
def main():
    print("🎉 Welcome to Movie Ticket Booking System 🎉")

    display_movies()
    movie_choice = int(input("Select movie: "))

    display_timings()
    time_choice = int(input("Select timing: "))

    display_seats()

    seats_booked = book_seats()

    calculate_price(seats_booked)

    print("\n🎟️ Booking Confirmed!")
    print("Enjoy your movie 🍿")


# Run program
main()