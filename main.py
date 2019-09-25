import os
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

   import os
import statistics
TEMPERATURE_ID = 1
HUMIDITY_ID = 2
PRESSURE_ID = 3
class TimeSeriesDatum:
   id = 0 # 1=TEMP, 2=HUMID, 3=PRESS, etc.
   value = 0
   time = 0
   def __init__(self, id, value, time):
       self.id = id
       self.value = value
       self.time = time
class Instrument:
   # Member variables
   data = []
   def get_values_by_id(self, id):
       values = []
       for datum in self.data:
           if datum.id == id:
               values.append(datum.value)
       return values
   def get_mean_by_id(self, id):
       values = self.get_values_by_id(id)
       mean = statistics.mean(values)
       return mean
   def get_median_by_id(self, id):
       values = self.get_values_by_id(id)
       median = statistics.median(values)
       return median
   def print_calculation_by_id(self, id):
       if id == TEMPERATURE_ID:
           print("Temperature")
       if id == HUMIDITY_ID:
           print("Humidity")
       mean = self.get_mean_by_id(id)
       median = self.get_median_by_id(id)
       print("Mean:", mean)
       print("Median:", median)
       print("\n")
   def add_datum(self, id, value, time):
       datum = TimeSeriesDatum(id, value, time)
       self.data.append(datum)
tool = Instrument()
tool.add_datum(TEMPERATURE_ID, 25, 1)
tool.add_datum(TEMPERATURE_ID, 26, 2)
tool.add_datum(TEMPERATURE_ID, 29, 3)
tool.add_datum(HUMIDITY_ID, 80, 1)
tool.add_datum(HUMIDITY_ID, 75, 2)
tool.add_datum(HUMIDITY_ID, 50, 3)
tool.print_calculation_by_id(TEMPERATURE_ID)
tool.print_calculation_by_id(HUMIDITY_ID)

def get_commmand():
    print("Indoor Air Quality Monitoring Command Console")
    print("Please select from the following options:")
    print("1 - Add reading")
    print("2 - List readings")
    print("3 - Calculate")
    print("4 - Exit")
    command = int(input("Choose option: "))
    os.system("clear")
    return command
is_running = True

while is_running:
    command = get_commmand()
    if command == 1:
        print("add")

    if command == 2:
            print("list")

    if command == 3:
        print("calc")

    if command == 4:
        is_running = False
