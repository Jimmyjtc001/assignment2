  import os
from library.temperature import c_to_f
def main():
   # This variable controls the main runtime loop
   # of our application. If this variable is False
   # then our application should terminal.
   main_loop_is_running = True
   while main_loop_is_running:
       print("Indoor Air Quality Monitoring Command Console\n")
       print("Please select from the following options:")
       print("(A) Add reading")
       print("(B) List readings")
       print("(C) Calculate")
       print("(D) Exit\n")
       command = input("Input: ")
       os.system("clear")
       if command == "A":
           print("TODO: Add readings GUI page")
       elif command == "B":
           print("TODO: List readings GUI page")
       elif command == "C":
           print("TODO: Calculate")
       elif command in ["D", "d", "(D)", "(d)"]:
           main_loop_is_running = False
if __name__ == "__main__":
   main()

  from library.temperature import c_to_f
def get_command_input():
   print("Indoor Air Quality Monitoring Command Console\n")
   print("Please select from the following options:")
   print("(A) Add reading")
   print("(B) List readings")
   print("(C) Calculate")
   print("(D) Exit\n")
   command = input("Input: ")
   os.system("clear")
   return command
def get_readings():
   print("Please input")
   temperature = input("Temperature (degrees): ")
   humidity = input("Humidity (%): ")
   readings = {
       "temperature": temperature,
       "humidity": humidity
   }
   os.system("clear")
   print("* * * * * * * * * * * * * *")
   print("Successfully saved reading")
   print("* * * * * * * * * * * * * *")
   print("\nHit enter key to return to the menu")
   input()
   os.system("clear")
   return readings
def main():
   # This variable controls the main runtime loop
   # of our application. If this variable is False
   # then our application should terminal.
   main_loop_is_running = True
   while main_loop_is_running:
       command = get_command_input()
       if command == "A":
           readings = get_readings()
       elif command == "B":
           print("TODO: List readings GUI page")
       elif command == "C":
           print("TODO: Calculate")
       elif command in ["D", "d", "(D)", "(d)"]:
           main_loop_is_running = False
if __name__ == "__main__":
   main()

 from library.temperature import c_to_f
def get_command_input():
   print("Indoor Air Quality Monitoring Command Console\n")
   print("Please select from the following options:")
   print("(A) Add reading")
   print("(B) List readings")
   print("(C) Calculate")
   print("(D) Exit\n")
   command = input("Input: ")
   os.system("clear")
   return command
def get_readings():
   print("Please input")
   temperature = input("Temperature (degrees): ")
   humidity = input("Humidity (%): ")
   readings = {
       "temperature": temperature,
       "humidity": humidity
   }
   os.system("clear")
   print("* * * * * * * * * * * * * *")
   print("Successfully saved reading")
   print("* * * * * * * * * * * * * *")
   print("\nHit enter key to return to the menu")
   input()
   os.system("clear")
   return readings
def main():
   # This variable controls the main runtime loop
   # of our application. If this variable is False
   # then our application should terminal.
   main_loop_is_running = True
   readings = []
   while main_loop_is_running:
       command = get_command_input()
       if command == "A":
           data_reading = get_readings()
           readings.append(data_reading)
       elif command == "B":
           print("TODO: List readings GUI page")
       elif command == "C":
           print("TODO: Calculate")
       elif command in ["D", "d", "(D)", "(d)"]:
           main_loop_is_running = False
if __name__ == "__main__":
   main()
