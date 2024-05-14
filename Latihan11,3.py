totaljam = dict()
with open('mbox-short.txt', 'r') as file:
    for i in file:
        if i.startswith("From "):
            jam = i.split()
            jam1 = jam[5].split(":")[0]
            totaljam[jam1] = totaljam.get(jam1, 0) + 1

    for jam2, hitung in sorted(totaljam.items()):
        print(jam2, hitung)
