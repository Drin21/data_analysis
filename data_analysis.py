from statistics import stdev

## open and read file
f = open('results.txt', 'r+')

## Stores data in jan_data
jan_data = []
for line in f:
    jan_data.append([float(x) for x in line.split()])

## Data information
experiment_number = jan_data[0]
experiment_date   = jan_data[1]
experiment_time   = jan_data[2]
experiment_data   = jan_data[3]


## Data processing/ calculation: max&min, average, std dev, greater than values,acending and decending
class Basic_data_processing:
    def all_data(self, value):
        print("experiment_number: ")
        print (value[0], "\n")
        print("experiment_date: ")
        print (value[1], "\n")
        print("experiment_time: ")
        print (value[2], "\n")
        print("experiment_data: ")
        print (value[3], "\n")

    def min_max(self, value):
        print(value, "\n")
        value.sort()
        print (value)
        return "the maximum value is {0} and the minimum value is {1}".format(value[-1], value[0])

    def average(self, value):
        return "The Average value of the results is: ", sum(value)/ len(value)

    def standard_dev(self, value):
        return "The Standard Deviation of the results is: ", stdev(value)

    def greater_less_than(self, value):
        print(value)
        user_input = int(input("Enter a number: "))
        list = [i/i for i in value if user_input<i]
        return("There are {0} that is greather than {1} ".format(sum(list), user_input) )

    def acending_decending():
        pass




## Main Program
data_processing = Basic_data_processing()
while True:
    print("""
    hi, there!

    choose your program:

    a = shows all data
    b = Find the maximum and minimum of data
    c = Find standard deviation and average results of data
    d = Find the calculated results
    e = exit program
    """)

    '''
    This section of the code are the user's choices

    '''
    ## Ask user their choices
    user_input = input("enter choice: ")


    ## display all data
    if user_input == 'a':
        while True:
            print(data_processing.all_data(jan_data))
            user = input("enter '0' to close program or press any key to go back to the main menu: ")
            if user == "0":
                exit()
            else:
                break

    ## display max and min of the results in the data
    elif user_input == 'b':
        while True:
            print(data_processing.min_max(experiment_data))
            user = print("enter your next move: ")
            if user == "0":
                exit()
            else:
                break

    ## Average value and Standard Deviation result of the data
    elif user_input == 'c':
        while True:
            print(data_processing.average(experiment_data))
            print(data_processing.standard_dev(experiment_data))
            user = input("enter '0' to close program or press any key to go back to the main menu: ")
            if user == "0":
                exit()
            else:
                break
    ## Sort experiment data in Acending and descending order
    elif user_input == 'd':
        print(data_processing.greater_less_than(experiment_data))

    ## new User Menu for Medium Data Processing
    elif user_input == 'e':
        print(data_processing.min_max(data_average))


    elif user_input == 'f':
        print(data_processing.min_max(data_average))


