# Program make a simple calculator
import calculator as cc
import logging_config as lg
import term_loop as tl
import initial

initial.init()

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            str = "%.1f + %.1f = %.1f" % (num1, num2, cc.add(num1,num2))

        elif choice == '2':
            str = "%.1f - %.1f = %.1f" % (num1, num2, cc.subtract(num1,num2))

        elif choice == '3':
            str = "%.1f * %.1f = %.1f" % (num1, num2, cc.multiply(num1,num2))

        elif choice =='4':
            if(num2 == 0):
              lg.logging.warning("Division by Zero")
              print("You can't divide by zero.")
              continue
            else:
              str = "%.1f / %.1f = %.1f" % (num1, num2, cc.divide(num1,num2))
      
        print(str)
        lg.logging.info(str)

        flag = False
        flag = tl.term(flag)
        
        if flag == False:
          break
        else:
          continue

    else:
        lg.logging.warning("Invalid Input")
        print("Invalid Input")
        