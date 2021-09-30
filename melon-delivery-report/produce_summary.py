def delivery_report(day, data_file):
    print("Day", day)
    print("File",data_file)
    the_file = open(data_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    the_file.close()

delivery_report(1, "um-deliveries-20140519.txt")
delivery_report(2, "um-deliveries-20140520.txt")
delivery_report(3, "um-deliveries-20140521.txt")






