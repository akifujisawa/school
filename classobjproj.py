# Aki Fujisawa and Katherine Zeng

# defining master class
class template:
    def __init__(self, manufacturer, type, name, cost, cpu, gpu, mem, storage):
        self.manufacturer = manufacturer
        self.type = type
        self.name = name
        self.cost = cost
        self.cpu = cpu
        self.gpu = gpu
        self.mem = mem
        self.storage = storage

    def details(self):
        print(f"\nMANUFACTURER:   {self.manufacturer}\n"
              f"NAME:           {self.name}\n"
              f"COST:           {self.cost}\n"
              f"CPU:            {self.cpu}\n"
              f"GPU:            {self.gpu}\n"
              f"MEM:            {self.mem}\n"
              f"STORAGE:        {self.storage}\n")
    def __repr__(self):
        return str(self)

# different sub-classes for each manufacturer
class Lenovo(template):
    def init(self, manufacturer, type, name, cost, cpu, gpu, mem, storage):
        template.__init__(manufacturer, type, name, cost, cpu, gpu, mem, storage)

class Apple(template):
    def init(self, manufacturer, type, name, cost, cpu, gpu, mem, storage):
        template.__init__(manufacturer, type, name, cost, cpu, gpu, mem, storage)

class Dell(template):
    def init(self, manufacturer, type, name, cost, cpu, gpu, mem, storage):
        template.__init__(manufacturer, type, name, cost, cpu, gpu, mem, storage)

class HP(template):
    def init(self, manufacturer, type, name, cost, cpu, gpu, mem, storage):
        template.__init__(manufacturer, type, name, cost, cpu, gpu, mem, storage)

# child classes
LenovoComputers = [
    Lenovo("Lenovo", "Desktop Computer", "Legion 5i Gen 6", "699.99", "Core i5-11400F 2.6GHz", "NVIDIA GeForce RTX 3050", "8GB DDR4-3200", "512GB"),
    Lenovo("Lenovo", "Desktop Computer", "IdeaCentre 5 17ACN7", "899.99", "AMD Ryzen 7 5700G 3.8GHz", "NVIDIA GeForce RTX 3060", "16GB DDR4-3200", "512GB SSD + 1TB HDD"),
    Lenovo("Lenovo", "Desktop Computer", "Legion Tower 5i", "1,499.99", "Intel Core i7-12700 1.6GHz", "NVIDIA GeForce RTX 3060", "32GB DDR-5-4800", "1TB SSD"),
    Lenovo("Lenovo", "All-in-One", "IdeaCentre 5i 27IAH7", "1,299.99", "Intel Core i7-12700H 1.7GHz", "Intel Iris Xe Graphics", "16GB DDR5-4800", "512GB SSD"),
    ]

DellComputers = [
    Dell("Dell", "SFF Desktop Computer", "OptiPlex 3000", "649.99", "Intel Core i5-12500 3.0GHz", "Intel UHD Graphics 770", "8GB DDR4-3200", "256GB SSD"),
    Dell("Dell", "Desktop Computer", "Inspiron 3910", "629.99", "Intel Core i5-12400 2.5GHz", "Intel UHD Graphics 730", "8GB DDR4-3200", "512GB SSD"),
    Dell("Dell", "Laptop Computer", "Latitude 5530", "1,699.99", "Intel Core i7-1265U 1.3GHz", "Intel Iris Xe Graphics", "16GB DDR4-3200", "512GB SSD"),
    Dell("Dell", "Laptop Computer", "XPS 13 9315", "1,699.99", "Intel Core i7-1250U 0.8GHz", "Intel Iris Xe Graphics", "16GB-3200", "1TB SSD")
    ]

HPComputers = [
    HP("HP", "Laptop Computer", "OMEN 17-CK1020NR", "1,199.99", "Intel Core i7-12700H 1.7 GHz", "NVIDIA GeForce RTX 3070 Ti", "16GB DDR4-4800", "512GB SSD"),
    HP("HP", "Laptop Computer", "ProBook 450 G9", "999.99", "Intel Core i7-1255U 1.7GHz", "Intel Iris Xe Graphics", "16GB DDR4-3200", "1TB SSD"),
    HP("HP", "All-in-One", "24-CB1021", "429.99", "AMD Ryzen 3 5425U 2.7GHz", "AMD Radeon RX Vega 6", "8GB DDR4-3200", "256GB SSD"),
    HP("HP", "SFF Desktop Computer", "ProDesk 600 G2", "199.99", "Intel Core i5-6500 3.2GHz", "Intel HD Graphics 530", "16GB DDR4-2133", "256GB SSD")
    ]

AppleComputers = [
    Apple("Apple", "Desktop Computer", "Mac Mini MMFJ3LL/A Early 2023", "579.99", "Apple M2", "10 Core GPU/16 Core Neural Engine", "8GB Unified", "256GB SSD"),
    Apple("Apple", "All-in-One", "iMac MGTF3LL/A Mid 2021", "1,249.99", "Apple M1", "7 Core GPU/16 Core Neural Engine", "8GB Unified", "256GB SSD"),
    Apple("Apple", "Laptop Computer", "Macbook Pro Z17400180 Early 2023", "4,499.99", "Apple M2 Max", "38 Core GPU/16 Core Neural Engine", "96GB Unified", "2TB SSD"),
    Apple("Apple", "Desktop Computer", "Mac Studio Z14K0007J Early 2022", "5,599.99", "Apple M1 Ultra", "64 Core GPU/32 Core Neural Engine", "128GB Unified", "1TB SSD")
]

# actual shopping
customername = input("What is your name?\n")
print(f"\nWelcome to the store, {customername.capitalize()}.")
while True:
    while True:
        #ask for manufacturer
        choicemanufacturertype = input("\nAre you looking for a specific manufacturer?\n"
                                       "Choices: Lenovo, Apple, Dell, or HP\n")
        if choicemanufacturertype.lower() in {"lenovo", "apple", "dell", "hp"}:
            choicemanufacturertype = choicemanufacturertype.lower()
            break
        else:
            print("Sorry, that isn't a option")
    while True:
        if choicemanufacturertype == "lenovo":
            # print list of names of lenovo computers from list
            print(f"\n{[Lenovo.name for Lenovo in LenovoComputers]}")
            information = input("What item would you like to see? Input is CASE SENSITIVE\n")
            # if input is in list run function
            if information in (Lenovo.name for Lenovo in LenovoComputers):
                for index, Lenovo in enumerate(LenovoComputers):
                    if Lenovo.name == information:
                        LenovoComputers[index].details()
                        while True:
                            # ask to keep browsing
                            cont = input("Would you like to keep browsing? Yes or No\n")
                            if cont.capitalize() == "Yes":
                                break
                            elif cont.capitalize() == "No":
                                print("Thank you for browsing today!")
                                exit()
                            else:
                                print("That isn't an option.\n")
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                print("We don't seem to have that.")
        elif choicemanufacturertype == "apple":
            # print list of names of apple computers from list
            print(f"\n{[Apple.name for Apple in AppleComputers]}")
            information = input("What item would you like to see? Input is CASE SENSITIVE\n")
            # if input is in list run function
            if information in (Apple.name for Apple in AppleComputers):
                for index, Apple in enumerate(AppleComputers):
                    if Apple.name == information:
                        AppleComputers[index].details()
                        while True:
                            # ask to keep browsing
                            cont = input("Would you like to keep browsing? Yes or No\n")
                            if cont.capitalize() == "Yes":
                                break
                            elif cont.capitalize() == "No":
                                print("Thank you for browsing today!")
                                exit()
                            else:
                                print("That isn't an option.\n")
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                print("We don't seem to have that.")
        elif choicemanufacturertype == "dell":
            # print list of dell computers from list
            print(f"\n{[Dell.name for Dell in DellComputers]}")
            information = input("What item would you like to see? Input is CASE SENSITIVE\n")
            # if input is in list run function
            if information in (Dell.name for Dell in DellComputers):
                for index, Dell in enumerate(DellComputers):
                    if Dell.name == information:
                        DellComputers[index].details()
                        while True:
                            # ask to keep browsing
                            cont = input("Would you like to keep browsing? Yes or No\n")
                            if cont.capitalize() == "Yes":
                                break
                            elif cont.capitalize() == "No":
                                print("Thank you for browsing today!")
                                exit()
                            else:
                                print("That isn't an option.\n")
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                print("We don't seem to have that.")
        elif choicemanufacturertype == "hp":
            # print list of hp computers from list
            print(f"\n{[HP.name for HP in HPComputers]}")
            information = input("What item would you like to see? Input is CASE SENSITIVE\n")
            # if input is in list run function
            if information in (HP.name for HP in HPComputers):
                for index, HP in enumerate(HPComputers):
                    if HP.name == information:
                        HPComputers[index].details()
                        while True:
                            # ask to keep browsing
                            cont = input("Would you like to keep browsing? Yes or No\n")
                            if cont.capitalize() == "Yes":
                                break
                            elif cont.capitalize() == "No":
                                print("Thank you for browsing today!")
                                exit()
                            else:
                                print("That isn't an option.\n")
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                print("We don't seem to have that.")
