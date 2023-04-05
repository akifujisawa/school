class vehicle:
    def __init__(self, name, topspeed, mileage):
        self.name = name
        self.topspeed = topspeed
        self.mileage = mileage

    def details(self):
        print( f"Name:        {self.name}\n" \
               f"Topspeed:    {self.topspeed}\n" \
               f"Mileage:     {self.mileage}")

motocompo = vehicle("Honda Motocompo", "30-50 km/h", "70 km/L @ 30 km/h")
motocompo.details()

class classes:
    pass

class computer:
    def __init__(self, host, cpu, gpu, mem, storage, usr):
        self.host = host
        self.cpu = cpu
        self.gpu = gpu
        self.mem = mem
        self.storage = storage
        self.usr = usr

    def specs(self):
        print(f"\n{self.usr}\n"
              f"-----------------------------\n"
              f"HOST:   {self.host}\n"
              f"CPU:    {self.cpu}\n"
              f"GPU:    {self.gpu}\n"
              f"MEM:    {self.mem}\n"
              f"SPACE:  {self.storage}\n"
              f"USR:    {self.usr}")

anko = computer("Thinkpad X1 Carbon 6th Gen", "Intel i7-8650U (8) @ 4.2GHz", "Intel UHD Graphics 620", "16GB @ 2133MHz", "512GB Samsung PM981 M.2 SSD", "autumn@anko")
anko.specs()

