import datetime

current_year = datetime.datetime.now().year  
type_cars=input("'Εσωτερικής καύσης'ή 'Υβριδικό':")
year = int(input(f"Είσαγεται την χρονολογία του οχήματος σας(1900-{current_year}):"))

cubic_capacity = int(input("Εισάγεται τα κυβικά του οχήματος σας:(500-9000): "))

current_year = datetime.datetime.now().year  

def calculate_year_difference(year, current_year):    ### vivliotihiki gia na travaei se real time thn xronia
 year = int(year)
 return year
calculate_year_difference(year,current_year)
dif_years=current_year-year

def calculate_teloi(year, cubic_capacity):  #ews to etos 2011
        
        if year >= 1900 and year <= 2000:
            if cubic_capacity >= 0 and cubic_capacity <= 300:
                return 22
            elif cubic_capacity > 300 and cubic_capacity <= 785:
                return 55
            elif cubic_capacity > 786 and cubic_capacity <= 1071:
                return 120
            elif cubic_capacity > 1072 and cubic_capacity <= 1357:
                return 135
            elif cubic_capacity > 1358  and cubic_capacity <= 1548:
                return 225
            elif cubic_capacity > 1549 and cubic_capacity <= 1738:
                return 250
            elif cubic_capacity > 1738 and  cubic_capacity <= 1928:
                return 280
            elif   cubic_capacity > 1928  and cubic_capacity <= 2357:
                return 615
            elif  cubic_capacity >  2358 and cubic_capacity <= 3000:
                return 820
            elif  cubic_capacity > 3000 and cubic_capacity <= 4000:
                return 1025
            elif cubic_capacity > 4001:
                return 1230
            
        elif year > 2000 and year <= 2005:
            if cubic_capacity >= 0 and cubic_capacity <= 300:
                return 22
            elif cubic_capacity > 300 and cubic_capacity <= 785:
                return 55
            elif cubic_capacity > 786 and cubic_capacity <= 1071:
                return 120
            elif cubic_capacity > 1072 and cubic_capacity <= 1357:
                return 135
            elif cubic_capacity > 1358  and cubic_capacity <= 1548:
                return 240
            elif cubic_capacity > 1549 and cubic_capacity <= 1738:
                return 265
            elif cubic_capacity > 1738 and  cubic_capacity <= 1928:
                return 300
            elif   cubic_capacity > 1928  and cubic_capacity <= 2357:
                return 630
            elif  cubic_capacity >  2358 and cubic_capacity <= 3000:
                return 840
            elif  cubic_capacity > 3000 and cubic_capacity <= 4000:
                return 1050
            elif cubic_capacity > 4001:
                return 1260
            
        elif year > 2005 and year <= 2010:
            if cubic_capacity >= 0 and cubic_capacity <= 300:
                return 22
            elif cubic_capacity > 300 and cubic_capacity <= 785:
                return 55
            elif cubic_capacity > 786 and cubic_capacity <= 1071:
                return 120
            elif cubic_capacity > 1072 and cubic_capacity <= 1357:
                return 135
            elif cubic_capacity > 1358  and cubic_capacity <= 1548:
                return 255
            elif cubic_capacity > 1549 and cubic_capacity <= 1738:
                return 280
            elif cubic_capacity > 1738 and  cubic_capacity <= 1928:
                return 320
            elif   cubic_capacity > 1928  and cubic_capacity <= 2357:
                return 690
            elif  cubic_capacity >  2358 and cubic_capacity <= 3000:
                return 920
            elif  cubic_capacity > 3000 and cubic_capacity <= 4000:
                return 1150
            elif cubic_capacity > 4001:
                return 1380
            
def calculate_teloi_2011(year,co2_emission):  # apo to etos noemvrio 2011 ews 2020
   # if year >= 2011 and year <= 2020:
            if co2_emission >= 0 and co2_emission <= 90:
                return 0
            elif co2_emission > 90 and co2_emission <= 100 :
                return 0.90 * co2_emission
            elif co2_emission < 100 and co2_emission <=120 :
                return 0.98 * co2_emission 
            elif co2_emission > 120 and co2_emission <=140 : 
                return 1.20 * co2_emission
            elif co2_emission > 140 and co2_emission <=160 : 
                return 1.85 * co2_emission
            elif co2_emission > 160 and co2_emission <=180 :
                return 2.45 * co2_emission
            elif co2_emission > 180 and co2_emission <=200 :
                return 2.78 * co2_emission
            elif co2_emission > 200 and  co2_emission <=250 :
                return 3.05 * co2_emission
            else:
                return 3.72 * co2_emission
            
def calculate_teloi_2024(year,co2_emission): #2020 ews simera 
    if co2_emission >= 0 and co2_emission <= 122:
        return 0
    elif co2_emission > 122 and co2_emission <= 139:
        return 0.64 * co2_emission
    elif co2_emission > 139 and co2_emission <= 166:
        return 0.70 * co2_emission
    elif co2_emission > 166 and co2_emission <=208:
        return 0.85 * co2_emission
    elif co2_emission > 209 and co2_emission <= 224:
        return 1.87 * co2_emission
    elif co2_emission > 225 and co2_emission <=240 :
        return 2.20 * co2_emission 
    elif co2_emission > 240 and co2_emission <= 260:
        return 2.50 * co2_emission
    elif co2_emission > 260 and  co2_emission <=280 :
        return 2.70 * co2_emission
    elif co2_emission > 280:
        return 2.85 * co2_emission
    



def politelia(year,cubic_capacity):
    #δηλαδή 5ετία (τρέχον έτος 2024)θα αλλάζει μόνο λόγω της βιβλιοθήκης

    if cubic_capacity >= 1929 and cubic_capacity <= 1949:
        return 410
    elif cubic_capacity > 1950 and cubic_capacity <= 2049:
        return 440
    elif cubic_capacity > 2049 and cubic_capacity <= 2149:
        return 485
    elif cubic_capacity > 2149 and cubic_capacity  <= 2249:
        return 530
    elif cubic_capacity > 2249 and cubic_capacity <= 2949:
        return 575
    elif cubic_capacity > 2349 and cubic_capacity  <= 2449:
        return 620
    elif cubic_capacity > 2450 and cubic_capacity <= 2500 :
        return 665
    elif cubic_capacity > 2501 and cubic_capacity  <= 2549:
        return 1330
    elif cubic_capacity > 2550 and cubic_capacity <= 2649 :
        return 1420
    elif cubic_capacity > 2650 and cubic_capacity <= 2749:
        return 1510
    elif cubic_capacity > 2750 and cubic_capacity <= 2849: 
        return 1600
    elif cubic_capacity > 2850 and cubic_capacity <= 2949:
        return 1690
    elif cubic_capacity > 2950 and cubic_capacity <= 3049:
        return 1780
    elif cubic_capacity > 3050  and cubic_capacity <= 3149:
        return 1900
    elif cubic_capacity > 3150 and cubic_capacity  <= 3249:
        return 2020
    elif cubic_capacity > 3250 and cubic_capacity <= 3349:
        return 2140
    elif cubic_capacity > 3350 and cubic_capacity <= 3449:
        return 2260
    elif cubic_capacity > 3450 and cubic_capacity <= 3549:
        return 2380
    elif cubic_capacity > 3550 and cubic_capacity <= 3649:
        return 2500
    elif cubic_capacity > 3650 and cubic_capacity <= 3749:
        return 2620
    elif cubic_capacity > 3750 and cubic_capacity <= 3849:
        return 2740
    elif cubic_capacity > 3850 and cubic_capacity <= 3949:
        return 2860
    elif cubic_capacity > 3950 and cubic_capacity <= 4049:
        return 2980
    elif cubic_capacity > 4050 and cubic_capacity <= 4149:
        return 3100
    elif cubic_capacity > 4150 and cubic_capacity <= 4249:
        return 3220
    elif cubic_capacity > 4250 and cubic_capacity <= 4349:
        return 3340
    elif cubic_capacity > 4350 and cubic_capacity <= 4449:
        return 3460
    elif cubic_capacity > 4450 and cubic_capacity <= 4549:
        return 3580
    elif cubic_capacity > 4550 and cubic_capacity <= 4649:
        return 3700
    elif cubic_capacity > 4650 and cubic_capacity <= 4749:
        return 3820

    else:
        return "Δεν υπάρχει φόρος πολυτελίας"

 #elif  dif_years >5 and dif_years <= 10:
def politelia_5_10(year,cubic_capacity):

    if cubic_capacity >= 1929 and cubic_capacity <= 1949:
        return 287
    elif cubic_capacity > 1950 and cubic_capacity <= 2049:
        return 308
    elif cubic_capacity > 2049 and cubic_capacity <= 2149:
        return 340
    elif cubic_capacity > 2149 and cubic_capacity  <= 2249:
        return 371
    elif cubic_capacity > 2249 and cubic_capacity <= 2949:
        return 403
    elif cubic_capacity > 2349 and cubic_capacity  <= 2449:
        return 434
    elif cubic_capacity > 2450 and cubic_capacity <= 2500 :
        return 466
    elif cubic_capacity > 2501 and cubic_capacity  <= 2549:
        return 931
    elif cubic_capacity > 2550 and cubic_capacity <= 2649 :
        return 994
    elif cubic_capacity > 2650 and cubic_capacity <= 2749:
        return 1057
    elif cubic_capacity > 2750 and cubic_capacity <= 2849: 
        return 1120
    elif cubic_capacity > 2850 and cubic_capacity <= 2949:
        return 1183
    elif cubic_capacity > 2950 and cubic_capacity <= 3049:
        return 1246
    elif cubic_capacity > 3050  and cubic_capacity <= 3149:
        return 1330
    elif cubic_capacity > 3150 and cubic_capacity  <= 3249:
        return 1414
    elif cubic_capacity > 3250 and cubic_capacity <= 3349:
        return 1498
    elif cubic_capacity > 3350 and cubic_capacity <= 3449:
        return 1582
    elif cubic_capacity > 3450 and cubic_capacity <= 3549:
        return 1666
    elif cubic_capacity > 3550 and cubic_capacity <= 3649:
        return 1750
    elif cubic_capacity > 3650 and cubic_capacity <= 3749:
        return 1834
    elif cubic_capacity > 3750 and cubic_capacity <= 3849:
        return 1918
    elif cubic_capacity > 3850 and cubic_capacity <= 3949:
        return 2002
    elif cubic_capacity > 3950 and cubic_capacity <= 4049:
        return 2086
    elif cubic_capacity > 4050 and cubic_capacity <= 4149:
        return 2170
    elif cubic_capacity > 4150 and cubic_capacity <= 4249:
        return 2254
    elif cubic_capacity > 4250 and cubic_capacity <= 4349:
        return 2338
    elif cubic_capacity > 4350 and cubic_capacity <= 4449:
        return 2422
    elif cubic_capacity > 4450 and cubic_capacity <= 4549:
        return 2506
    elif cubic_capacity > 4550 and cubic_capacity <= 4649:
        return 2590
    elif cubic_capacity > 4650 and cubic_capacity <= 4749:
        return 2674
    else:
        return "Δεν υπάρχει φόρος πολυτελίας"
 
  
#############################      YVRIDIKA         #########################################

def taxes_hybr(year,cubic_capacisity):

  if  year <= 2010:    #Εχω εφαρμοσει ειδη το πολλαπλασιασμο με το 60%, οι τιμες ειναι ετοιμες!
       
        if cubic_capacisity >= 0 and cubic_capacisity <= 1549:
         return 0
        elif cubic_capacisity > 1549 and  cubic_capacity <= 1738:
         return 168
        elif cubic_capacisity > 1738 and cubic_capacity <= 1928:
          return 192
        elif cubic_capacity > 1928 and cubic_capacisity <= 2357:
          return 414
        elif cubic_capacity > 2357 and cubic_capacisity  <= 3000:
         return 552
        elif cubic_capacisity > 3000 and cubic_capacity <= 4000:
          return 690
        else:
         return 828

def taxes_hybr_2011(year,co2_emission):
    if year > 2010 and year <= 2019:                        #Για τα υβριδικα ισχυει η ιδια φορολογια οπως για τα εσωτερικης καυσης.

        if co2_emission >= 0 and co2_emission <= 90:
          return 0
        elif co2_emission > 90 and co2_emission <= 100 :
          return 0.90 * co2_emission
        elif co2_emission > 100 and co2_emission <= 120 :
         return 0.98 * co2_emission
        elif co2_emission > 120 and co2_emission <= 140 :
          return 1.20 * co2_emission
        elif co2_emission >140 and co2_emission <= 160 :
          return 1.85 * co2_emission
        elif co2_emission > 160 and co2_emission <= 180:
         return 2.45 * co2_emission
        elif co2_emission > 180 and co2_emission <= 200:
          return 2.78 * co2_emission
        elif  co2_emission > 200 and co2_emission <= 250:
          return 3.05 * co2_emission
        else:
          return 3.72 * co2_emission
        
def taxes_hybr_2019(year,co2_emission): #dif_years <= 5:                        #Για τα υβριδικα ισχυει η ιδια φορολογια οπως για τα εσωτερικης καυσης.
       #co2_emission = int(input("Εισάγετε τις εκπομπές Co2 του οχήματος σας: ")) 
        if co2_emission >= 0 and co2_emission <= 122:
                return 0
        elif co2_emission > 122 and co2_emission <= 139:
                return 0.64 * co2_emission
        elif co2_emission > 139 and co2_emission <= 166:
                return 0.70 * co2_emission
        elif co2_emission > 166 and co2_emission <= 208:
                return 0.85 * co2_emission
        elif co2_emission > 208 and co2_emission <= 224:
                return 1.87 * co2_emission
        elif co2_emission > 224 and co2_emission <= 240:
                return 2.20 * co2_emission
        elif co2_emission > 240 and co2_emission <= 260:
                return 2.50 * co2_emission
        elif co2_emission > 260 and co2_emission <= 280:
                return 2.70 * co2_emission
        else:
                return 2.85 * co2_emission
        #else:
         #       return "Μη έγκυρη αποδεκτή τιμή"


def hybrid_politelia_5(year,cubic_capacity):
   #if dif_years <=5 :    #δηλαδή 5ετία (τρέχον έτος 2024)θα αλλάζει μόνο λόγω της βιβλιοθήκης

    if cubic_capacity >= 1929 and cubic_capacity <= 1949:
        return 410
    elif cubic_capacity > 1950 and cubic_capacity <= 2049:
        return 440
    elif cubic_capacity > 2049 and cubic_capacity <= 2149:
        return 485
    elif cubic_capacity > 2149 and cubic_capacity  <= 2249:
        return 530
    elif cubic_capacity > 2249 and cubic_capacity <= 2949:
        return 575
    elif cubic_capacity > 2349 and cubic_capacity  <= 2449:
        return 620
    elif cubic_capacity > 2450 and cubic_capacity <= 2500 :
        return 665
    elif cubic_capacity > 2501 and cubic_capacity  <= 2549:
        return 1330
    elif cubic_capacity > 2550 and cubic_capacity <= 2649 :
        return 1420
    elif cubic_capacity > 2650 and cubic_capacity <= 2749:
        return 1510
    elif cubic_capacity > 2750 and cubic_capacity <= 2849: 
        return 1600
    elif cubic_capacity > 2850 and cubic_capacity <= 2949:
        return 1690
    elif cubic_capacity > 2950 and cubic_capacity <= 3049:
        return 1780
    elif cubic_capacity > 3050  and cubic_capacity <= 3149:
        return 1900
    elif cubic_capacity > 3150 and cubic_capacity  <= 3249:
        return 2020
    elif cubic_capacity > 3250 and cubic_capacity <= 3349:
        return 2140
    elif cubic_capacity > 3350 and cubic_capacity <= 3449:
        return 2260
    elif cubic_capacity > 3450 and cubic_capacity <= 3549:
        return 2380
    elif cubic_capacity > 3550 and cubic_capacity <= 3649:
        return 2500
    elif cubic_capacity > 3650 and cubic_capacity <= 3749:
        return 2620
    elif cubic_capacity > 3750 and cubic_capacity <= 3849:
        return 2740
    elif cubic_capacity > 3850 and cubic_capacity <= 3949:
        return 2860
    elif cubic_capacity > 3950 and cubic_capacity <= 4049:
        return 2980
    elif cubic_capacity > 4050 and cubic_capacity <= 4149:
        return 3100
    elif cubic_capacity > 4150 and cubic_capacity <= 4249:
        return 3220
    elif cubic_capacity > 4250 and cubic_capacity <= 4349:
        return 3340
    elif cubic_capacity > 4350 and cubic_capacity <= 4449:
        return 3460
    elif cubic_capacity > 4450 and cubic_capacity <= 4549:
        return 3580
    elif cubic_capacity > 4550 and cubic_capacity <= 4649:
        return 3700
    elif cubic_capacity > 4650 and cubic_capacity <= 4749:
        return 3820

    else:
        return "Δεν υπάρχει φόρος πολυτελίας"
    
def hybrid_5_10(year,cubic_capacity):
#elif  dif_years >5 and dif_years <= 10:
    
    if cubic_capacity >= 1929 and cubic_capacity <= 1949:
        return 287
    elif cubic_capacity > 1950 and cubic_capacity <= 2049:
        return 308
    elif cubic_capacity > 2049 and cubic_capacity <= 2149:
        return 340
    elif cubic_capacity > 2149 and cubic_capacity  <= 2249:
        return 371
    elif cubic_capacity > 2249 and cubic_capacity <= 2949:
        return 403
    elif cubic_capacity > 2349 and cubic_capacity  <= 2449:
        return 434
    elif cubic_capacity > 2450 and cubic_capacity <= 2500 :
        return 466
    elif cubic_capacity > 2501 and cubic_capacity  <= 2549:
        return 931
    elif cubic_capacity > 2550 and cubic_capacity <= 2649 :
        return 994
    elif cubic_capacity > 2650 and cubic_capacity <= 2749:
        return 1057
    elif cubic_capacity > 2750 and cubic_capacity <= 2849: 
        return 1120
    elif cubic_capacity > 2850 and cubic_capacity <= 2949:
        return 1183
    elif cubic_capacity > 2950 and cubic_capacity <= 3049:
        return 1246
    elif cubic_capacity > 3050  and cubic_capacity <= 3149:
        return 1330
    elif cubic_capacity > 3150 and cubic_capacity  <= 3249:
        return 1414
    elif cubic_capacity > 3250 and cubic_capacity <= 3349:
        return 1498
    elif cubic_capacity > 3350 and cubic_capacity <= 3449:
        return 1582
    elif cubic_capacity > 3450 and cubic_capacity <= 3549:
        return 1666
    elif cubic_capacity > 3550 and cubic_capacity <= 3649:
        return 1750
    elif cubic_capacity > 3650 and cubic_capacity <= 3749:
        return 1834
    elif cubic_capacity > 3750 and cubic_capacity <= 3849:
        return 1918
    elif cubic_capacity > 3850 and cubic_capacity <= 3949:
        return 2002
    elif cubic_capacity > 3950 and cubic_capacity <= 4049:
        return 2086
    elif cubic_capacity > 4050 and cubic_capacity <= 4149:
        return 2170
    elif cubic_capacity > 4150 and cubic_capacity <= 4249:
        return 2254
    elif cubic_capacity > 4250 and cubic_capacity <= 4349:
        return 2338
    elif cubic_capacity > 4350 and cubic_capacity <= 4449:
        return 2422
    elif cubic_capacity > 4450 and cubic_capacity <= 4549:
        return 2506
    elif cubic_capacity > 4550 and cubic_capacity <= 4649:
        return 2590
    elif cubic_capacity > 4650 and cubic_capacity <= 4749:
        return 2674
    else:
        return "Δεν υπάρχει φόρος πολυτελίας"

if type_cars == 'Εσωτερικής καύσης' :

 if year >= 1900 and year <=2011:
  print("Τέλη κυκλοφορίας:",calculate_teloi(year, cubic_capacity))
 elif year>=2011 and year <2020:
  co2_emission = int(input("Εισάγεται τις εκπομπές διοξειδίου του άνθρακα(Co2) (0-700): "))
  print("Τέλη κυκλοφορίας:",calculate_teloi_2011(year, co2_emission))

 elif year >=2020:
  co2_emission = int(input("Εισάγεται τις εκπομπές διοξειδίου του άνθρακα(Co2) (0-700): "))
  print("Τέλη κυκλοφορίας:",calculate_teloi_2024(year, co2_emission))


 if dif_years <=5 :
  print("Φόρος πολυτελέιας¨:", politelia(year,cubic_capacity)) 
 elif  dif_years >5 and dif_years <= 10:
  print("Φόρος πολυτελέιας:", politelia_5_10(year,cubic_capacity))
 

if type_cars == 'Υβριδικά' :
 if  year <= 2010:
  print("Τέλη κυκλοφορίας:",taxes_hybr(year,cubic_capacity))

 elif year >2010 and year <= 2019:
  co2_emission = int(input("Εισάγεται τις εκπομπές διοξειδίου του άνθρακα(Co2) (0-700): "))
  print("Τέλη κυκλοφορίας:", taxes_hybr_2011(year,co2_emission))

 elif dif_years <= 5: 
  co2_emission = int(input("Εισάγεται τις εκπομπές διοξειδίου του άνθρακα(Co2) (0-700): "))
  print("Τέλη κυκλοφορίας:", taxes_hybr_2019(year,co2_emission))

 if dif_years <=5: 
  print("Φόρος πολυτελείας:", hybrid_politelia_5(year,cubic_capacity))

 elif  dif_years >5 and dif_years <= 10: 
  print("Φόρος πολυτελείας:",hybrid_5_10(year,cubic_capacity))


