
def parking_garage():  # function declaration
    # Constant Variable declarations
    standard_hours = 3
    standard_charge = 2
    max_hours = 24
    max_charge = 40
    loop_exit = 'P'
    while loop_exit.lower() == 'p':  # loops the program until condition is false

        try:
            hours_parked = float(input("Enter the number of hours you Parked your car:\n"))

            while hours_parked < 0 or hours_parked > max_hours:
                hours_parked = float(input("Enter the number of hours you Parked your car:\n"))
            # calculating charged price conditions
            if 0 < hours_parked <= standard_hours:
                charged_price = standard_charge

            elif standard_hours < hours_parked < max_hours:
                excess_hours = float(hours_parked - standard_hours)
                charged_price = (excess_hours * 0.5) + standard_charge

            elif hours_parked == max_hours:
                charged_price = max_charge

            print("The total charge is:${:.2f}".format(charged_price))

        except ValueError:  # catching the invalid inputs
            print('Invalid input!! Please try again\n')
        # exit condition
        loop_exit = input('Enter P to continue or any key other to terminate the program :')


parking_garage()  # invoking the function
