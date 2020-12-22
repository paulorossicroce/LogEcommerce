from numpy import random
def input_csv():
   import csv
   f = open('input.csv')
   csv_f = csv.reader(f)
   tw = []

   i = int(0)
   tw1 = int(0)
   tw2 = int(0)
   tw3 = int(0)
   tw4 = int(0)
   tw5 = int(0)

   for row in csv_f:
     tw.append(int(row[1]))
   for i in range(360):
     if tw[i] == 1:
       tw1 = int(tw1 + 1)
     if tw[i] == 2:
       tw2 = int(tw2 + 1)
     if tw[i] == 3:
       tw3 = int(tw3 + 1)
     if tw[i] == 4:
       tw4 = int(tw4 + 1)
     if tw[i] == 5:
       tw5 = int(tw5 + 1)

   return tw1, tw2, tw3, tw4, tw5


input_csv()

def day1():

    # ===============================================SETUP====================================


    tw = input_csv()
    tw1 = tw[0]
    tw2 = tw[1]
    tw3 = tw[2]
    tw4 = tw[3]
    tw5 = tw[4]
    cl = int(9)
    max_vehicles = int(8)
    fleet_vehicles = int(0)
    extra_vehicles = int(0)
    total_packages = int(0)
    total_extra_packages = int(0)
    total_fleet_packages = int(0)
    total_mileage = int(0)
    total_mileage_fleet = int(0)
    total_mileage_extra = int(0)
    mileage = int(0)
    packages = []
    extra_packages = []
    packages_of_the_day = int(0)
    km = []
    km_extra = []
    overall_packages = int(0)

    for a in range(max_vehicles):  # defines the array of packages of a car
        packages.append(int(0))
        km.append(int(0))


    fleet = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}
    extra = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}

    # ======================================================COUNTERS=================================
    a = int(0)  # Fleet car number
    vehicle_used = 0
    b = int(0)  #extra fleet package counter

    # ============================LOADING THE FLEET=======================================================================

    for a in range(max_vehicles):  # TIME WINDOW 1
        while (tw1 > 0) and (packages[a] < cl):
            tw1 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 2
        while (tw2 > 0) and (packages[a] < cl):
            tw2 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 3
        while (tw3 > 0) and (packages[a] < cl):
            tw3 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 4
        while (tw4 > 0) and (packages[a] < cl):
            tw4 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 5
        while (tw5 > 0) and (packages[a] < cl):
            tw5 -= 1
            total_packages += 1
            packages[a] += 1

#===============================================SETS THE NUMBER OF USED VEHICLES=============================

    if (total_packages % max_vehicles) > 0:
        vehicle_used = (total_packages / max_vehicles) +1
    else:
        vehicle_used = total_packages / max_vehicles



#=========================================CHECKS IF IT NECESSARY TO USE EXTRA VEHICLES=======================
    if tw1 > 0:

        if tw1 % cl > 0:                            # CALCULATE HOW MANY EXTRA CARS WILL BE NEEDED
            extra_vehicles = int((tw1 / cl) + 1)

        else:
            extra_vehicles = int((tw1/cl))


        for a in range(int(extra_vehicles)):  # defines the array of extra packages of an extra car
            extra_packages.append(0)
            km_extra.append(0)



#======================================LOADS EXTRA VEHICLES==========================================================================

        for a in range(int(extra_vehicles)):
            while (tw1 > 0) and (extra_packages[a] < cl):
                tw1 -= 1
                total_packages += 1
                extra_packages[a] += 1
                total_extra_packages +=1


#=========================================CALCULATES THE MILIAGE OF EACH VEHICLE OF THE FLEET=====================================

    for a in range (len(km)):

        if packages[a] >0 :
            fleet_vehicles += 1


#============================================SAVES RESULTS IN CSV==================================================================



    import csv
    with open('day1_results.csv', mode='w') as csv_file:

        fieldnames = ["vehicle", "packages", "km", "total fleet mileage", "total extra fleet mileage", "overall milage", "packages delivered"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv.writer(csv_file, delimiter=';')
        write.writeheader()

        dist = -1
        while dist < 0:
            dist = (float(random.normal(loc=2.21, scale=1, size=(1, 1))))


        for i in range(fleet_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (packages[i] - 1) )
            write.writerow({"vehicle" : i+1, "packages" : packages[i], "km" : mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_fleet + mileage
            overall_packages = overall_packages + packages[i]


        for i in range(extra_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (extra_packages[i] - 1))
            write.writerow({"vehicle": ('extra {}'.format(i + 1)), "packages": extra_packages[i], "km": mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_extra + mileage
            overall_packages = overall_packages + extra_packages[i]

        write.writerow({"total fleet mileage" : total_mileage_fleet, "total extra fleet mileage" : total_mileage_extra, "overall milage": total_mileage, "packages delivered" : overall_packages})


#==========================================ADJUST THE TIME WINDOWS==========================================


    tw1 = tw2
    tw2 = tw3
    tw3 = tw4
    tw4 = tw5
    tw5 = 0
    #PRINT VARIABLE FOR TESTS

    return tw1, tw2, tw3, tw4, tw5, cl, max_vehicles

def day2():

    # ===============================================SETUP====================================


    tw = day1()
    tw1 = tw[0]
    tw2 = tw[1]
    tw3 = tw[2]
    tw4 = tw[3]
    tw5 = tw[4]
    cl = tw[5]
    max_vehicles = tw[6]
    fleet_vehicles = int(0)
    extra_vehicles = int(0)
    total_packages = int(0)
    total_extra_packages = int(0)
    total_fleet_packages = int(0)
    total_mileage = int(0)
    total_mileage_fleet = int(0)
    total_mileage_extra = int(0)
    mileage = int(0)
    packages = []
    extra_packages = []
    packages_of_the_day = int(0)
    km = []
    km_extra = []
    overall_packages = int(0)

    for a in range(max_vehicles):  # defines the array of packages of a car
        packages.append(int(0))
        km.append(int(0))


    fleet = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}
    extra = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}

    # ======================================================COUNTERS=================================
    a = int(0)  # Fleet car number
    vehicle_used = 0
    b = int(0)  #extra fleet package counter

    # ============================LOADING THE FLEET=======================================================================

    for a in range(max_vehicles):  # TIME WINDOW 1
        while (tw1 > 0) and (packages[a] < cl):
            tw1 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 2
        while (tw2 > 0) and (packages[a] < cl):
            tw2 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 3
        while (tw3 > 0) and (packages[a] < cl):
            tw3 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 4
        while (tw4 > 0) and (packages[a] < cl):
            tw4 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 5
        while (tw5 > 0) and (packages[a] < cl):
            tw5 -= 1
            total_packages += 1
            packages[a] += 1

#===============================================SETS THE NUMBER OF USED VEHICLES=============================

    if (total_packages % max_vehicles) > 0:
        vehicle_used = (total_packages / max_vehicles) +1
    else:
        vehicle_used = total_packages / max_vehicles



#=========================================CHECKS IF IT NECESSARY TO USE EXTRA VEHICLES=======================
    if tw1 > 0:

        if tw1 % cl > 0:                            # CALCULATE HOW MANY EXTRA CARS WILL BE NEEDED
            extra_vehicles = int((tw1 / cl) + 1)

        else:
            extra_vehicles = int((tw1/cl))


        for a in range(int(extra_vehicles)):  # defines the array of extra packages of an extra car
            extra_packages.append(0)
            km_extra.append(0)



#======================================LOADS EXTRA VEHICLES==========================================================================

        for a in range(int(extra_vehicles)):
            while (tw1 > 0) and (extra_packages[a] < cl):
                tw1 -= 1
                total_packages += 1
                extra_packages[a] += 1
                total_extra_packages +=1


#=========================================CALCULATES THE MILIAGE OF EACH VEHICLE OF THE FLEET=====================================

    for a in range (len(km)):

        if packages[a] >0 :
            fleet_vehicles += 1


#============================================SAVES RESULTS IN CSV==================================================================



    import csv
    with open('day2_results.csv', mode='w') as csv_file:

        fieldnames = ["vehicle", "packages", "km", "total fleet mileage", "total extra fleet mileage", "overall milage", "packages delivered"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv.writer(csv_file, delimiter=';')

        write.writeheader()

        dist = -1
        while dist < 0:
            dist = (float(random.normal(loc=2.21, scale=1, size=(1, 1))))


        for i in range(fleet_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (packages[i] - 1) )
            write.writerow({"vehicle" : i+1, "packages" : packages[i], "km" : mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_fleet + mileage
            overall_packages = overall_packages + packages[i]


        for i in range(extra_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (extra_packages[i] - 1))
            write.writerow({"vehicle": ('extra {}'.format(i + 1)), "packages": extra_packages[i], "km": mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_extra + mileage
            overall_packages = overall_packages + extra_packages[i]

        write.writerow({"total fleet mileage" : total_mileage_fleet, "total extra fleet mileage" : total_mileage_extra, "overall milage": total_mileage, "packages delivered" : overall_packages})


#==========================================ADJUST THE TIME WINDOWS==========================================


    tw1 = tw2
    tw2 = tw3
    tw3 = tw4
    tw4 = tw5
    tw5 = 0
    #PRINT VARIABLE FOR TESTS

    return tw1, tw2, tw3, tw4, tw5, cl, max_vehicles

def day3():

    # ===============================================SETUP====================================

    tw = day2()
    tw1 = tw[0]
    tw2 = tw[1]
    tw3 = tw[2]
    tw4 = tw[3]
    tw5 = tw[4]
    cl = tw[5]
    max_vehicles = tw[6]
    fleet_vehicles = int(0)
    extra_vehicles = int(0)
    total_packages = int(0)
    total_extra_packages = int(0)
    total_fleet_packages = int(0)
    total_mileage = int(0)
    total_mileage_fleet = int(0)
    total_mileage_extra = int(0)
    mileage = int(0)
    packages = []
    extra_packages = []
    packages_of_the_day = int(0)
    km = []
    km_extra = []
    overall_packages = int(0)

    for a in range(max_vehicles):  # defines the array of packages of a car
        packages.append(int(0))
        km.append(int(0))


    fleet = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}
    extra = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}

    # ======================================================COUNTERS=================================
    a = int(0)  # Fleet car number
    vehicle_used = 0
    b = int(0)  #extra fleet package counter

    # ============================LOADING THE FLEET=======================================================================

    for a in range(max_vehicles):  # TIME WINDOW 1
        while (tw1 > 0) and (packages[a] < cl):
            tw1 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 2
        while (tw2 > 0) and (packages[a] < cl):
            tw2 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 3
        while (tw3 > 0) and (packages[a] < cl):
            tw3 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 4
        while (tw4 > 0) and (packages[a] < cl):
            tw4 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 5
        while (tw5 > 0) and (packages[a] < cl):
            tw5 -= 1
            total_packages += 1
            packages[a] += 1

#===============================================SETS THE NUMBER OF USED VEHICLES=============================

    if (total_packages % max_vehicles) > 0:
        vehicle_used = (total_packages / max_vehicles) +1
    else:
        vehicle_used = total_packages / max_vehicles



#=========================================CHECKS IF IT NECESSARY TO USE EXTRA VEHICLES=======================
    if tw1 > 0:

        if tw1 % cl > 0:                            # CALCULATE HOW MANY EXTRA CARS WILL BE NEEDED
            extra_vehicles = int((tw1 / cl) + 1)

        else:
            extra_vehicles = int((tw1/cl))


        for a in range(int(extra_vehicles)):  # defines the array of extra packages of an extra car
            extra_packages.append(0)
            km_extra.append(0)



#======================================LOADS EXTRA VEHICLES==========================================================================

        for a in range(int(extra_vehicles)):
            while (tw1 > 0) and (extra_packages[a] < cl):
                tw1 -= 1
                total_packages += 1
                extra_packages[a] += 1
                total_extra_packages +=1


#=========================================CALCULATES THE MILIAGE OF EACH VEHICLE OF THE FLEET=====================================

    for a in range (len(km)):

        if packages[a] >0 :
            fleet_vehicles += 1


#============================================SAVES RESULTS IN CSV==================================================================



    import csv
    with open('day3_results.csv', mode='w') as csv_file:

        fieldnames = ["vehicle", "packages", "km", "total fleet mileage", "total extra fleet mileage", "overall milage", "packages delivered"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv.writer(csv_file, delimiter=';')
        write.writeheader()

        dist = -1
        while dist < 0:
            dist = (float(random.normal(loc=2.21, scale=1, size=(1, 1))))


        for i in range(fleet_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (packages[i] - 1) )
            write.writerow({"vehicle" : i+1, "packages" : packages[i], "km" : mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_fleet + mileage
            overall_packages = overall_packages + packages[i]


        for i in range(extra_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (extra_packages[i] - 1))
            write.writerow({"vehicle": ('extra {}'.format(i + 1)), "packages": extra_packages[i], "km": mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_extra + mileage
            overall_packages = overall_packages + extra_packages[i]

        write.writerow({"total fleet mileage" : total_mileage_fleet, "total extra fleet mileage" : total_mileage_extra, "overall milage": total_mileage, "packages delivered" : overall_packages})


#==========================================ADJUST THE TIME WINDOWS==========================================


    tw1 = tw2
    tw2 = tw3
    tw3 = tw4
    tw4 = tw5
    tw5 = 0
    #PRINT VARIABLE FOR TESTS

    return tw1, tw2, tw3, tw4, tw5, cl, max_vehicles

def day4():

    # ===============================================SETUP====================================


    tw = day3()
    tw1 = tw[0]
    tw2 = tw[1]
    tw3 = tw[2]
    tw4 = tw[3]
    tw5 = tw[4]
    cl = tw[5]
    max_vehicles = tw[6]
    fleet_vehicles = int(0)
    extra_vehicles = int(0)
    total_packages = int(0)
    total_extra_packages = int(0)
    total_fleet_packages = int(0)
    total_mileage = int(0)
    total_mileage_fleet = int(0)
    total_mileage_extra = int(0)
    mileage = int(0)
    packages = []
    extra_packages = []
    packages_of_the_day = int(0)
    km = []
    km_extra = []
    overall_packages = int(0)

    for a in range(max_vehicles):  # defines the array of packages of a car
        packages.append(int(0))
        km.append(int(0))


    fleet = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}
    extra = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}

    # ======================================================COUNTERS=================================
    a = int(0)  # Fleet car number
    vehicle_used = 0
    b = int(0)  #extra fleet package counter

    # ============================LOADING THE FLEET=======================================================================

    for a in range(max_vehicles):  # TIME WINDOW 1
        while (tw1 > 0) and (packages[a] < cl):
            tw1 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 2
        while (tw2 > 0) and (packages[a] < cl):
            tw2 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 3
        while (tw3 > 0) and (packages[a] < cl):
            tw3 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 4
        while (tw4 > 0) and (packages[a] < cl):
            tw4 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 5
        while (tw5 > 0) and (packages[a] < cl):
            tw5 -= 1
            total_packages += 1
            packages[a] += 1

#===============================================SETS THE NUMBER OF USED VEHICLES=============================

    if (total_packages % max_vehicles) > 0:
        vehicle_used = (total_packages / max_vehicles) +1
    else:
        vehicle_used = total_packages / max_vehicles



#=========================================CHECKS IF IT NECESSARY TO USE EXTRA VEHICLES=======================
    if tw1 > 0:

        if tw1 % cl > 0:                            # CALCULATE HOW MANY EXTRA CARS WILL BE NEEDED
            extra_vehicles = int((tw1 / cl) + 1)

        else:
            extra_vehicles = int((tw1/cl))


        for a in range(int(extra_vehicles)):  # defines the array of extra packages of an extra car
            extra_packages.append(0)
            km_extra.append(0)



#======================================LOADS EXTRA VEHICLES==========================================================================

        for a in range(int(extra_vehicles)):
            while (tw1 > 0) and (extra_packages[a] < cl):
                tw1 -= 1
                total_packages += 1
                extra_packages[a] += 1
                total_extra_packages +=1


#=========================================CALCULATES THE MILIAGE OF EACH VEHICLE OF THE FLEET=====================================

    for a in range (len(km)):

        if packages[a] >0 :
            fleet_vehicles += 1


#============================================SAVES RESULTS IN CSV==================================================================



    import csv
    with open('day4_results.csv', mode='w') as csv_file:

        fieldnames = ["vehicle", "packages", "km", "total fleet mileage", "total extra fleet mileage", "overall milage", "packages delivered"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv.writer(csv_file, delimiter=';')
        write.writeheader()

        dist = -1
        while dist < 0:
            dist = (float(random.normal(loc=2.21, scale=1, size=(1, 1))))


        for i in range(fleet_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (packages[i] - 1) )
            write.writerow({"vehicle" : i+1, "packages" : packages[i], "km" : mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_fleet + mileage
            overall_packages = overall_packages + packages[i]


        for i in range(extra_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (extra_packages[i] - 1))
            write.writerow({"vehicle": ('extra {}'.format(i + 1)), "packages": extra_packages[i], "km": mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_extra + mileage
            overall_packages = overall_packages + extra_packages[i]

        write.writerow({"total fleet mileage" : total_mileage_fleet, "total extra fleet mileage" : total_mileage_extra, "overall milage": total_mileage, "packages delivered" : overall_packages})


#==========================================ADJUST THE TIME WINDOWS==========================================


    tw1 = tw2
    tw2 = tw3
    tw3 = tw4
    tw4 = tw5
    tw5 = 0
    #PRINT VARIABLE FOR TESTS

    return tw1, tw2, tw3, tw4, tw5, cl, max_vehicles

def day5():

    # ===============================================SETUP====================================


    tw = day4()
    tw1 = tw[0]
    tw2 = tw[1]
    tw3 = tw[2]
    tw4 = tw[3]
    tw5 = tw[4]
    cl = tw[5]
    max_vehicles = tw[6]
    fleet_vehicles = int(0)
    extra_vehicles = int(0)
    total_packages = int(0)
    total_extra_packages = int(0)
    total_fleet_packages = int(0)
    total_mileage = int(0)
    total_mileage_fleet = int(0)
    total_mileage_extra = int(0)
    mileage = int(0)
    packages = []
    extra_packages = []
    packages_of_the_day = int(0)
    km = []
    km_extra = []
    overall_packages = int(0)

    for a in range(max_vehicles):  # defines the array of packages of a car
        packages.append(int(0))
        km.append(int(0))


    fleet = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}
    extra = {0: {'packages': 0, 'cd': 0, 'dist': 0, 'km': 0}}

    # ======================================================COUNTERS=================================
    a = int(0)  # Fleet car number
    vehicle_used = 0
    b = int(0)  #extra fleet package counter

    # ============================LOADING THE FLEET=======================================================================

    for a in range(max_vehicles):  # TIME WINDOW 1
        while (tw1 > 0) and (packages[a] < cl):
            tw1 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 2
        while (tw2 > 0) and (packages[a] < cl):
            tw2 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 3
        while (tw3 > 0) and (packages[a] < cl):
            tw3 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 4
        while (tw4 > 0) and (packages[a] < cl):
            tw4 -= 1
            total_packages += 1
            packages[a] += 1

    for a in range(max_vehicles):  # TIME WINDOW 5
        while (tw5 > 0) and (packages[a] < cl):
            tw5 -= 1
            total_packages += 1
            packages[a] += 1

#===============================================SETS THE NUMBER OF USED VEHICLES=============================

    if (total_packages % max_vehicles) > 0:
        vehicle_used = (total_packages / max_vehicles) +1
    else:
        vehicle_used = total_packages / max_vehicles



#=========================================CHECKS IF IT NECESSARY TO USE EXTRA VEHICLES=======================
    if tw1 > 0:

        if tw1 % cl > 0:                            # CALCULATE HOW MANY EXTRA CARS WILL BE NEEDED
            extra_vehicles = int((tw1 / cl) + 1)

        else:
            extra_vehicles = int((tw1/cl))


        for a in range(int(extra_vehicles)):  # defines the array of extra packages of an extra car
            extra_packages.append(0)
            km_extra.append(0)



#======================================LOADS EXTRA VEHICLES==========================================================================

        for a in range(int(extra_vehicles)):
            while (tw1 > 0) and (extra_packages[a] < cl):
                tw1 -= 1
                total_packages += 1
                extra_packages[a] += 1
                total_extra_packages +=1


#=========================================CALCULATES THE MILIAGE OF EACH VEHICLE OF THE FLEET=====================================

    for a in range (len(km)):

        if packages[a] >0 :
            fleet_vehicles += 1


#============================================SAVES RESULTS IN CSV==================================================================



    import csv
    with open('day5_results.csv', mode='w') as csv_file:

        fieldnames = ["vehicle", "packages", "km", "total fleet mileage", "total extra fleet mileage", "overall milage", "packages delivered"]
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv.writer(csv_file, delimiter=';')
        write.writeheader()

        dist = -1
        while dist < 0:
            dist = (float(random.normal(loc=2.21, scale=1, size=(1, 1))))


        for i in range(fleet_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (packages[i] - 1) )
            write.writerow({"vehicle" : i+1, "packages" : packages[i], "km" : mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_fleet + mileage
            overall_packages = overall_packages + packages[i]


        for i in range(extra_vehicles):
            mileage = ((float(random.normal(loc=23, scale=5, size=(1, 1)))) * 2) + (dist * (extra_packages[i] - 1))
            write.writerow({"vehicle": ('extra {}'.format(i + 1)), "packages": extra_packages[i], "km": mileage })
            total_mileage = total_mileage + mileage
            total_mileage_fleet = total_mileage_extra + mileage
            overall_packages = overall_packages + extra_packages[i]

        write.writerow({"total fleet mileage" : total_mileage_fleet, "total extra fleet mileage" : total_mileage_extra, "overall milage": total_mileage, "packages delivered" : overall_packages})


#==========================================ADJUST THE TIME WINDOWS==========================================


    tw1 = tw2
    tw2 = tw3
    tw3 = tw4
    tw4 = tw5
    tw5 = 0
    #PRINT VARIABLE FOR TESTS

    return tw1, tw2, tw3, tw4, tw5, cl, max_vehicles

day1()
day2()
day3()
day4()
day5()

