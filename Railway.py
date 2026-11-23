
import random
def calculate_fare(seats, fare_per_seat):
    if seats <= 0:
        raise ValueError("Seats must be greater than zero")

    if fare_per_seat <= 0:
        raise ValueError("Fare must be greater than zero")

    return seats * fare_per_seat
def generate_pnr():
    return random.randint(100000, 999999)
if __name__ == "__main__":
    print("===== RAILWAY TICKET BOOKING SYSTEM =====")
    name = input("Enter Passenger Name: ")
    age = int(input("Enter Passenger Age: "))
    train_no = input("Enter Train Number: ")
    train_name = input("Enter Train Name: ")
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")
    journey_date = input("Enter Journey Date: ")
    seats = int(input("Enter Number of Seats: "))
    fare = float(input("Enter Fare Per Seat: "))
    total_fare = calculate_fare(seats, fare)
    pnr = generate_pnr()
    print("\n===== TICKET DETAILS =====")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Train Number:", train_no)
    print("Train Name:", train_name)
    print("Source:", source)
    print("Destination:", destination)
    print("Journey Date:", journey_date)
    print("Number of Seats:", seats)
    print("Fare Per Seat: Rs.", fare)
    print("Total Fare: Rs.", total_fare)
    print("PNR Number:", pnr)
    print("Booking Status: CONFIRMED")
    print("===== HAPPY JOURNEY =====")
