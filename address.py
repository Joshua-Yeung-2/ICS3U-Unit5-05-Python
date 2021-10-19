# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to procedure that accepts an address and then prints it again


def address(
    full_name,
    apartment,
    street_number_int,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):
    # This function is to procedure that accepts an address and then prints it again

    # process
    full_name = full_name.upper()
    street_name = street_name.upper()
    city = city.upper()
    province = province.upper()
    if apartment_number != None:
        address = (
            full_name
            + "\n"
            + str(apartment_number)
            + "-"
            + str(street_number_int)
            + street_name
            + "\n"
            + city
            + " "
            + province
            + "  "
            + postal_code
        )
    else:
        address = (
            full_name
            + "\n"
            + str(street_number_int)
            + " "
            + street_name
            + "\n"
            + city
            + " "
            + province
            + "  "
            + postal_code
        )

    return address


def main():
    # this function gets the the address
    apartment_number = None

    # input
    full_name = input("Enter your full_name: ")
    apartment = input("Do you live in apartment? (y/n): ")
    if apartment.upper() == "Y":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street_number: ")
    street_name = input("Enter your street_name and type (Main St, Express Pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC...): ")
    postal_code = input("Enter your postal code (A12 3B4): ")
    print("")

    # process
    try:
        street_number_int = int(street_number)
        if apartment == "y":
            apartment_number_int = int(apartment_number)

        # call functions
        address_2 = address(
            full_name,
            apartment,
            street_number_int,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )

        print("{}".format(address_2))

    except Exception:
        print("sorry, this is not a number")
        print("please try again")

    print("\nDone")


if __name__ == "__main__":
    main()
