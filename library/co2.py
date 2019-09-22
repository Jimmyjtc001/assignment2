CO2 = 500
if CO2 <= 2100 and CO2 >= 1600:
    print("Air Quality is BAD")
    print("Heavily contaminated indoor air")
    print("Ventailation required")
if CO2 <=1600 and CO2 >=1100:
    print("MEDIOCRE")
    print("contamated indoor air")
    print("Ventailation recom")
if CO2 <=1000 and CO2 >=700:
    print("GOOD")
if CO2 <=600 and CO2 >=400:
    print("EXCELLENT")
