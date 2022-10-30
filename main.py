# Program make a simple calculator

#logging 설정
import logging

Log_Format = "%(levelname)s %(asctime)s     %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

# Program make a simple calculator

op = ['','+', '-', '*', '/']

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    return x/y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            str = "%d + %d = %d" % (num1, num2, add(num1,num2))
            print(str)
            logging.info(str)

        elif choice == '2':
            str = "%d - %d = %d" % (num1, num2, subtract(num1,num2))
            print(str)
            logging.info(str)

        elif choice == '3':
            str = "%d * %d = %d" % (num1, num2, multiply(num1,num2))
            print(str)
            logging.info(str)

        elif choice =='4':
            if(num2 == 0):
              logging.warning("Division by Zero")
              print("You can't divide by zero.")
            else:
              str = "%d / %d = %d" % (num1, num2, divide(num1,num2))
              print(str)
              logging.info(str)


        # check if user wants another calculation
        # break the while loop if answer is no
        flag = False

        while True:
          next_calculation = input("Let's do next calculation? (yes/no): ")
          next_calculation = next_calculation.lower()

          if next_calculation == "yes":
              flag = True
              break
          elif next_calculation == "no":
              confirm = input("Are you sure? (yes/no): ")
              confirm = confirm.lower()
              
              if confirm == "yes":
                break
              elif confirm == "no":
                continue
              else:
                print("Invalid Input. Please answer yes or no.")
                #로깅?
                continue
          else:
            print("Invalid Input. Please answer yes or no.")
            #로깅?
            continue
        
        if flag == False:
          break

    else:
        logging.warning("Invalid Input")
        print("Invalid Input")
        