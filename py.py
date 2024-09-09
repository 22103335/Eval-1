movies = {
    'Joker': {'available': 5, 'rented_by': []},
    'Deadpool': {'available': 3, 'rented_by': []},
    'Avengers': {'available': 4, 'rented_by': []},
    'Taxi Driver': {'available': 2, 'rented_by': []}
}
customers = {}
def rent_movie(user, mname):
    if mname not in movies:
        print(f"Movie '{mname}' does not exist.")
        return
    if movies[mname]['available'] <= 0:
        print(f"Sorry, '{mname}' is currently out of stock.")
        return
    if user not in customers:
        customers[user] = []
    if mname in customers[user]:
        print(f"{user} already rented '{mname}'.")
        return
    movies[mname]['available'] -= 1
    movies[mname]['rented_by'].append(user)
    customers[user].append(mname)
    print(f"{user} has rented '{mname}'.")
def return_movie(user, mname):
    if user not in customers or mname not in customers[user]:
        print(f"{user} did not rent '{mname}'.")
        return
    movies[mname]['available'] += 1
    movies[mname]['rented_by'].remove(user)
    customers[user].remove(mname)
    if not customers[user]:
        del customers[user]
    print(f"{user} has returned '{mname}'.")
def rental_report():
    print("\nRental Report:")
    print("Available Movies:")
    for movie, info in movies.items():
        print(f"{movie}: {info['available']} available, rented by {', '.join(info['rented_by']) if info['rented_by'] else 'none'}")
    
    print("\nCustomer Rentals:")
    for customer, rentals in customers.items():
        print(f"{customer} has rented: {', '.join(rentals) if rentals else 'none'}")
while True:
    print("\nMovie Rental Service")
    print("1. Rent a movie")
    print("2. Return a movie")
    print("3. Generate rental report")
    print("4. Exit")
    c = input("Enter your c: ").strip()
    if c == '1':
        user = input("Enter customer name: ").strip()
        mname = input("Enter movie title: ").strip()
        rent_movie(user, mname)
    elif c == '2':
        user = input("Enter customer name: ").strip()
        mname = input("Enter movie title: ").strip()
        return_movie(user, mname)
    elif c == '3':
        rental_report()
    elif c == '4':
        print("Exiting...")
        break
    else:
        print("Invalid c. Please try again.")