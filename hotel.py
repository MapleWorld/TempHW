from enum import Enum
from datetime import date
import time

'''
Rules:
    Never use confusing variable names like a, c, coo, rc, p, because nobody know what they mean besides you
    
Note: enum class is only available in python3, check if you guys are using python2 of python3
'''

class Hotel:
    def __init__(self):
        self.booking_lst = []
        self.available_room_num_lst = [x for x in range(0, 30)]
        self.total_room_capacity = 30
        self.total_guest_capacity = 100

    def home_menu(self):
        print("\n1 Booking")
        print("2 Look Up Booking")
        print("3 Check Capacity")
        print("4 Check Booking Cost")
        print("5 Check Income")
        print("ANY OTHER NUMBER Exit")

        option = int(input("->"))
        if option == 1:
            print(" ")
            self.book_room()
        elif option == 2:
            print(" ")
            self.look_up()
        elif option == 3:
            print(" ")
            self.check_capacity()
        elif option == 4:
            self.check_booking_cost()
        elif option == 5:
            print(" ")
            #self.check_income()
        else:
            exit()
            
        self.home_menu()

    def _is_valid_date(self, date):
        day, month, year = date.split('/')[:3]
        day, month, year = int(day), int(month), int(year)
        if year >= 2022 and year <= 2024:
            if month != 0 and month <= 12:
                if month == 2 and day != 0 and day <= 31:
                    if year % 4 == 0 and day <= 29:
                        pass
                    elif day < 29:
                        pass
                    else:
                        return False
                elif month <= 7 and month % 2 != 0 and day <= 31:
                    pass
                elif month <= 7 and month % 2 == 0 and day <= 30 and month != 2:
                    pass
                elif month >= 8 and month % 2 == 0 and day <= 31:
                    pass
                elif month >= 8 and month % 2 != 0 and day <= 30:
                    pass
                else:
                    return False
            else:
                return False
        else:
            return False
        return True

    def _is_valid_string_input(self, input):
        input_is_not_empty = input != ""
        return input_is_not_empty
    
    def book_room(self):
        print(" BOOKING ROOMS")
        print(" ")
        
        while True:
            num_guest = int(input("Enter the number of people staying\n"))
            if num_guest < self.total_guest_capacity:
                break
            else:
                print("There is not enough capacity for the guest")
    
        while True:
            guest_name = str(input("Name: "))
            guest_phone_num = str(input("Phone No.: "))
            guest_address = str(input("Address: ")) 
            if self._is_valid_string_input(guest_name) and self._is_valid_string_input(guest_phone_num) and self._is_valid_string_input(guest_address):
                break
            else:
                print("Name, Phone no. & Address cannot be empty")

        while True:
            check_in_date = str(input("Check-In (DD/MM/YYYY): "))
            check_out_date = str(input("Check-Out (DD/MM/YYYY): "))
            if self._is_valid_date(check_in_date) and self._is_valid_date(check_out_date):
                check_in_date_time = time.strptime(check_in_date, "%d/%m/%Y")
                check_out_date_time = time.strptime(check_out_date, "%d/%m/%Y")
                if check_in_date_time < check_out_date_time:
                    break
                else:
                    print("Check in date must occur before check out date")
            else:
                print("Invalid check in and check out date")
        
        if len(self.available_room_num_lst) > 0:
            room_num = self.available_room_num_lst.pop()
            booking = Booking(self.booking_id, guest_name, guest_address, guest_phone_num, check_in_date, check_out_date, num_guest, room_num)
            self.booking_lst.append(booking)
            self.booking_id += 1
            self.total_room_capacity -= 1
            self.total_guest_capacity -= num_guest
            print("")
            print("ROOM BOOKED SUCCESSFULLY\n")
            print("Room No. - ", room_num)
        else:
            print("There is not enough room")

    def look_up(self):
        booking_id = int(input("Enter the booking id\n"))
        for booking in self.booking_lst:
            if booking.booking_id == booking_id:
                print ("We found your booking, below is the detail of your booking:")
                booking.display_info()
                return
            
        print ("There is no such booking")

    def check_capacity(self):
        print ("Number of room available for booking: ", self.total_room_capacity)
        print ("Number of guest the hotel can support: ", self.total_guest_capacity)

    def check_booking_cost(self):
        booking_id = int(input("Enter the booking id\n"))
        for booking in self.booking_lst:
            if booking.booking_id == booking_id:
                print ("We found your booking, below is the detail of your booking:")
                print ("The cost of the booking is: ", booking.total_cost)
                return
            
        print ("There is no such booking")

class MEAL_PRICE(Enum):
    NO_MEAL = 0
    BREAKFAST_PRICE = 5
    DINNER_PRICE = 10
    BREAKFAST_AND_DINNER_PRICE = 12
    
class Booking:
    ROOM_PRICE = 50
    
    def __init__(self, booking_id, guest_name, guest_address, guest_phone_num, check_in_date, check_out_date, num_guest, room_num):
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.guest_address = guest_address
        self.guest_phone_num = guest_phone_num
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guest = num_guest
        self.room_num = room_num
        self.meal_plan = MEAL_PRICE.NO_MEAL
        self._pick_meal_plan()
        self.total_cost = self._calculate_cost()
    
    def display_info(self):
        print("| Name    | Phone No. | Address   | Check-In | Check-Out  | Meal Plan | Total Price     |")
        print("----------------------------------------------------------------------------------------------------------------------")
        print("|", self.guest_name, "\t |", self.guest_phone_num, "\t|", self.guest_address, "\t|",
                    self.check_in_date, "\t|", self.check_out_date, "\t|", self.meal_plan.name, "\t|", self.total_cost)
        print("----------------------------------------------------------------------------------------------------------------------") 
            
    def _calculate_cost(self):
        count_days = self._count_difference_between_dates(self.check_in_date, self.check_out_date)
        total_meal_cost = count_days * self.num_guest * self.meal_plan.value
        total_guest_room_cost = count_days * self.num_guest * self.ROOM_PRICE
        total_cost = total_meal_cost + total_guest_room_cost
        return total_cost

    def _pick_meal_plan(self):
        meal_option = int(input("Do you want breakfast for $5 (1), evening meal for $10 (2), both for $12 (3), or no meal at all (0)?\n"))

        while meal_option < 0 or meal_option > 3:
            meal_option = int(input("Invalid meal option, please pick 0/1/2/3\n"))
            
        if meal_option == 1:
            self.meal_plan = MEAL_PRICE.BREAKFAST_PRICE
        if meal_option == 2:
            self.meal_plan = MEAL_PRICE.DINNER_PRICE
        if meal_option == 3:
            self.meal_plan = MEAL_PRICE.BREAKFAST_AND_DINNER_PRICE
        
    def _count_difference_between_dates(self, check_in, check_out):
        check_in_day, check_in_month, check_in_year = check_in.split('/')[:3]
        check_in_day, check_in_month, check_in_year = int(check_in_day), int(check_in_month), int(check_in_year)
        
        check_out_day, check_out_month, check_out_year = check_out.split('/')[:3]
        check_out_day, check_out_month, check_out_year = int(check_out_day), int(check_out_month), int(check_out_year)
        
        check_in_date = date(check_in_year, check_in_month, check_in_day)
        check_out_date = date(check_out_year, check_out_month, check_out_day)
        delta = check_out_date - check_in_date
        return delta.days
        
hotel = Hotel()
hotel.home_menu()

# def payment(self):

    #     ph = str(input("Phone Number: "))
    #     global i
    #     f = 0

    #     for n in range(0, i):
    #         if ph == phno[n]:

    #             if p[n] == 0:
    #                 f = 1
    #                 print(" Payment")
    #                 print(" --------------------------------")
    #                 print(" MODE OF PAYMENT")

    #                 print(" 1- Credit/Debit Card")
    #                 print(" 2- Paytm/PhonePe")
    #                 print(" 3- Using UPI")
    #                 print(" 4- Cash")
    #                 x = int(input("-> "))
    #                 print("\n Amount: ", (price[n]*day[n])+rc[n])
    #                 print("\n        Pay")
    #                 print(" (y/n)")
    #                 ch = str(input("->"))

    #                 if ch == 'y' or ch == 'Y':
    #                     print(" --------------------------------")
    #                     print("          Bill")
    #                     print(" --------------------------------")
    #                     print(" Name: ", name[n], "\t\n Phone No.: ",
    #                         phno[n], "\t\n Address: ", add[n], "\t")
    #                     print("\n Check-In: ",
    #                         guest_check_in_date_lst[n], "\t\n Check-Out: ", checkout[n], "\t")
    #                     print("\n Room Type: ",
    #                         room[n], "\t\n Room Charges: ", price[n]*day[n], "\t")
    #                     print(" Restaurant Charges: \t", rc[n])
    #                     print(" --------------------------------")
    #                     print("\n Total Amount: ", (price[n]*day[n])+rc[n], "\t")
    #                     print(" --------------------------------")
    #                     print("      Thank You")
    #                     print("      Visit Again :)")
    #                     print(" --------------------------------\n")
    #                     p.pop(n)
    #                     p.insert(n, 1)

    #                     roomno.pop(n)
    #                     roomno.insert(n, 0)

    #             else:

    #                 for j in range(n+1, i):
    #                     if ph == phno[j]:
    #                         if p[j] == 0:
    #                             pass

    #                         else:
    #                             f = 1
    #                             print("Payment has been Made\n\n")
    #     if f == 0:
    #         print("Invalid Customer Id")
