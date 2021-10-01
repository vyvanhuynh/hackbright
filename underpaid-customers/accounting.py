

def customer_report(data_file,melon_cost):
    
    the_file = open(data_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        name = words[1]
        melons = words[2]
        paid = float(words[3])
        expected = int(melons) * int(melon_cost)

        if expected != paid:
            print(f"{name} paid ${paid:.2f}, expected ${expected}")


    the_file.close()

customer_report("customer-orders.txt", 1.00)