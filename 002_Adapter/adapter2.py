class Banner:
    def __init__(self, str):
        self.__str = str
    def get_str(self):
        return self.__str
    def set_str(self, str):
        self.__str = str
    str = property(get_str, set_str)

    def show_with_paren(self):
        print("(" + self.__str + ")")
    def show_with_aster(self):
        print("*" + self.__str + "*")
         

class PrintBanner:
    def __init__(self, str):
        self.__banner = Banner(str)
    def print_weak(self):
        self.__banner.show_with_paren()
    def print_strong(self):
        self.__banner.show_with_aster()

p = PrintBanner("Hello")
p.print_strong()
p.print_weak()
    