def calculate_bill_for_each_person(bill, people, tip_percentage):
    total, people_count, percentage = float(bill), float(people), float(tip_percentage)
    tip = ((total / 100) * percentage) / 5
    return round((total / people_count) + tip, 2)


def main():
    print("Welcome to the tip calculator!")
    bill = input("What was the total bill ? ")
    people = input("How many people to split the bill ? ")
    tip_percentage = input("What percentage tip would you like to give ? 10, 12 or 15 ? ")
    each_person_bill = calculate_bill_for_each_person(bill, people, tip_percentage)
    print(f'Each person should pay : {each_person_bill}')


main()
