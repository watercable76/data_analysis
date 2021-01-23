"""
Author: Nicholas Cable, el cablecito
Date Created: 1/13/2021
Purpose: Work with an example data set using matplotlib,
        and display some graphs with the data.
Last updated: 1/23/2021
"""

"""
Work with the data here
Options for the user:
1) Find high and low of life expect
2) Find all data for a certain country - high and low, and average
3) Find average for each country. Store in dictionary, if country code exists
   then set that as key.

"""


def options():
    """Print out the options for the user to input. """
    print('Here are some options to see trends within the data: \n\
        \t1) Check a certain year.\n\
        \t2) Find the high, low and average for a certain country.\n\
        \t3) Find the average for all countries.\n')
    print("\nIf you do not care to see about these options, you can \
        \nenter '9' or any number besides 1, 2 or 3 and we will display \
        \nthe highest life expectancy, with the associated country and year,\
        \nand the lowest life expectancy, with the associated country and year.\
        \n".expandtabs(4))


def print_set(a_set, num):
    """
    Print out the countries from the set, and specify how many
    countries to be printed out.
    """
    print("Here are some countries that you could check.\n")
    stop = num
    for i in a_set:
        print(f'{i}, ', end='')
        stop -= 1
        if stop <= 0:
            print(f'{i}\n')
            break


"""
Next chunk of code validates the input from the user, from getting the input
to getting the option choice they choose.
"""

choice_prompt = 'What would you like to do? (type 0 to see the options again) '
year_prompt = 'Please enter a year you would like to check. Please note,\
                \nthe valid years are from 1543 up to 2019. '
all_prompt = 'How many averages do you want to see? '

options()

# Make sure the user inputs a whole number
while True:
    choice = input(choice_prompt)
    try:
        choice = int(choice)
    except ValueError:
        print("That is not a whole number!")
    else:
        break

# if the user types 0, they will see the options again.
while choice == 0:
    options()
    choice = int(input(choice_prompt))

if choice not in [1, 2, 3]:
    choice = 9


"""
Open the file once to get country names in order to allow the user to have some options
if they decide to choose option 2.
"""
with open('life-expectancy.csv') as information:
    next(information)

    # store all of the codes and country names here
    my_set = set()

    # get the country names in a set to show some options for the user
    for stuff in information:
        info = stuff.strip().split(',')
        c_name = info[0]

        my_set.add(c_name)

# Prompt the user for the year or country or how many country avgs they want to see
# Do try/except for each of the values
if choice == 1:
    # Prompt the user for a year
    # valid year is from 1543 to 2019
    while True:
        year_choice = input(year_prompt)
        try:
            year_choice = int(year_choice)
        except ValueError:
            print("That is not a year value.\n")
        else:
            if year_choice < 1543 or year_choice > 2019:
                print("That is an invalid year.\n")
            else:
                break
elif choice == 2:
    while True:
        print_set(my_set, 10)
        coun_choice = input("What country would you like to check: ")
        if coun_choice not in my_set:
            print("I'm sorry, but you input a country that does not exist or you mistyped the name.")
        else:
            break
elif choice == 3:
    while True:
        all_choice = input(all_prompt)
        try:
            all_choice = int(all_choice)
        except ValueError:
            print("That is not a valid number.\n")
        else:
            if all_choice < 1 or all_choice > 100:
                print("That is an invalid number of averages.\n")
            else:
                break

# Open the file
with open('life-expectancy.csv') as data:
    # Skip the header line
    next(data)

    # Data to be used in comparisons and outputs
    h_lf = 0
    l_lf = 999
    hc = ''
    lc = ''
    hy = 0
    ly = 0

    # set the first country value
    old_country = 'AFG'

    # hold the country names in a list
    country_list = ['Afghanistan']

    # var to find averages
    avg = 0
    count = 0

    # find the oldest year in the records
    lowest = 1800

    # dic declaration to hold all countries values.
    all_countries = dict()

    for line in data:
        cl = line.strip().split(',')
        country = cl[0]
        code = cl[1]
        year = int(cl[2])
        life_expec = float(cl[3])

        # find the oldest year in the records
        if year < lowest:
            lowest = year

        # default choice. Find high/low w/country+year and average
        if choice == 9:
            avg += life_expec
            count += 1

            # find new life expect high
            if life_expec > h_lf:
                h_lf = life_expec
                hc = country
                hy = year
            # find new life expect low
            if life_expec < l_lf:
                l_lf = life_expec
                lc = country
                ly = year

        # Find the high/low for a specific year and average of all data
        elif choice == 1:
            # check to see if the year input is the year in the database
            if year_choice == year:

                avg += life_expec
                count += 1

                # find new life expect high
                if life_expec > h_lf:
                    h_lf = life_expec
                    hc = country
                    hy = year
                # find new life expect low
                if life_expec < l_lf:
                    l_lf = life_expec
                    lc = country
                    ly = year

        # find the average for a certain country
        elif choice == 2:
            # check to see if the year input is the year in the database
            if coun_choice.lower() == country.lower():

                avg += life_expec
                count += 1

                # find new life expect high
                if life_expec > h_lf:
                    h_lf = life_expec
                    hc = country
                    hy = year
                # find new life expect low
                if life_expec < l_lf:
                    l_lf = life_expec
                    lc = country
                    ly = year

        # find the average of all the countries
        elif choice == 3:
            # check to see if country code is in the dictionary
            if code in all_countries:
                all_countries[code] += [life_expec]
            else:
                all_countries[code] = [life_expec]

            if old_country != country:
                old_country = country
                all_choice -= 1
                # add country names to list
                country_list.append(country)
            if all_choice <= 0:
                break

    print('\n')

    # print out the high/low if use did not choose country option.
    if choice == 9 or choice == 1:
        print(f'The highest life expectancy was {h_lf} in the year {hy} in the country {hc}.')
        print(f'The lowest life expectacny was {l_lf} in the year {ly} in the country {lc}.')

    # print out average for all years - option 9/default
    if choice == 9:
        print(f'The average was {avg/count:.2f} for all the years.')

    # print out average for specific year.
    if choice == 1:
        print(f'The average was {avg/count:.2f} for the year {year_choice}.')

    # print out the average for the certain country.
    if choice == 2:
        print(f'The highest life expectancy for {coun_choice} was {h_lf} in the year {hy}.')
        print(f'The lowest life expectacny for {coun_choice} was {l_lf} in the year {ly}.')
        print(f'The average was {avg/count:.2f} for {coun_choice}.')

    # print out the average of the countries and their names.
    if choice == 3:
        strt = 1
        for i in all_countries:
            print(f'The average of {country_list[strt]} is: {sum(all_countries[i])/len(all_countries[i]):.3f}')
            strt += 1
