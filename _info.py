#

class Info():
    def __init__(self):
        self.email = "0xtz.52@mail.com"
        self.github = "https://github.com/0xtz"
        self.twitter = "https://twitter.com/0xtz"
        self.website = "COMMING SOON"
        self.description = "FAST Multithreaded port scanner written in Python3"
        self.version = "0.0.2"
        self.date = "2020-05-20"
        self.usage = "python3 pscanner.py -t <host> [-p <port>] # -t is the target host, -p is the port"
        self.author = "0xtz"
        self.license = "MIT"
        self.credits = "Rich"
        self.banner = f"""                                                       
    .oOo. O   o .oOo  .oOo  .oOoO' 'OoOo. 'OoOo. .oOo. `OoOo. 
    O   o o   O `Ooo. O     O   o   o   O  o   O OooO'  o     
    o   O O   o     O o     o   O   O   o  O   o O      O     
    oOoO' `OoOO `OoO' `OoO' `OoO'o  o   O  o   O `OoO'  o     
    O         o                                               
    o'     OoO' - by : [bold]{self.author}[/bold], v : {self.version} \n"""
        self.top_ports = [1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37, 39, 42, 43, 49, 50, 53, 67, 68, 69, 70, 71, 79, 80, 81, 82, 88, 101, 102, 105, 107, 110, 111, 113, 117, 119, 123, 137, 138, 139, 143, 161, 162, 177, 179, 194, 199, 201, 209, 210, 213, 220, 369, 370, 389, 427, 443, 444, 445, 464, 500, 512, 513, 513, 514, 515, 517, 518, 520,
                          521, 525, 531, 532, 533, 543, 544, 546, 547, 548, 554, 556, 563, 587, 631, 631, 636, 674, 694, 749, 750, 873, 992, 993, 995, 1080, 1433, 1434, 1494, 1512, 1524, 1701, 1719, 1720, 1812, 1813, 1985, 2008, 2010, 2049, 2102, 2103, 2104, 2401, 2809, 3306, 4321, 5999, 6000, 11371, 13720, 13721, 13724, 13782, 13783, 22273, 23399, 25565, 26000, 27017, 33434]


pyscanners = Info()
