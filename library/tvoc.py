TVOC =2300
if TVOC <=2500 and TVOC >=2000:
    print("Level-5", "Unhealty")
    print("Hygienic Rating - Situation not acceptable")
    print("Recommendation - Use only if unavoidable/Intense ventilation necessary")
    print("Exposure Limit - Hours")

TVOC =2100
if TVOC <2200 and TVOC >=660:
    print("Level-4", "Poor")
    print("Hygienic Rating - Major objections")
    print("Recommendation - Intensitied ventilation/airing necessary - Seach for sources")
    print("Exposure Limit - <1 month")

TVOC =230
if TVOC <660 and TVOC >=220:
    print("Level-3", "Moderate")
    print("Hygienic Rating - Some objections")
    print("Recommendation - Intensitied ventilation/airing recommended - Seach for sources")
    print("Exposure Limit - <12 month")

TVOC =69
if TVOC < 220 and TVOC >=65:
    print("Level-2", "Good")
    print("Hygienic Rating - No relevant objections")
    print("Recommendation - Ventilation/airing recommended")
    print("Exposure Limit - no limit")

TVOC =55
if TVOC < 65 and TVOC >=0:
    print("Level-4", "Excellend")
    print("Hygienic Rating - No objections")
    print("Recommendation - Target value")
    print("Exposure Limit - no limit")
