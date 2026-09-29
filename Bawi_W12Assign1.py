bawipatients = {
    "ana": (80, 50, 150, 90, 140, 170, 180),
    "ben": (130, 140, 135, 90, 140, 150, 160),
    "carlo": (90, 100, 95, 90, 140, 180, 120)
}

for patient, bawireadings in bawipatients.items():
    print("Patient:", patient)

    bawi_high_count = 0

    for bawireading in bawireadings:
        if bawireading >= 120:
            bawistatus = "High"
            bawi_high_count += 1
        else:
            bawistatus = "Normal"

        print(bawireading, "-", bawistatus)

    print("Number of High Readings:", bawi_high_count)
    print()

    #max min average diff

    bawimax = max(bawireadings)
    bawimin = min(bawireadings)
    bawiaverage = sum(bawireadings) / len(bawireadings)
    bawidiff = bawimax - bawimin

    print(f"Number of High Readings: ", bawi_high_count)
    print()
    print("Highest Blood Sugar: ", bawimax)
    print("Lowest Blood Sugar: ", bawimin)
    print("Average Blood Sugar: ", bawiaverage)
    print("Difference in Blood Sugar: ", bawidiff)
    print()


