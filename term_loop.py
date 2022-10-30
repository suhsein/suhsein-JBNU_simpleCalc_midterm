def term(flag):
        # check if user wants another calculation
        # break the while loop if answer is no

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
                continue
          else:
            print("Invalid Input. Please answer yes or no.")
            continue

        return flag