class AbstractDisplay:
    def open_display(self):
        print("")
    def print_display(self):
        print("")
    def close_display(self):
        print("")

    def display(self):
        self.open_display()
        i = 0
        while i < 5:
            self.print_display()
            i += 1
        self.close_display()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.__ch = ch
    def open_display(self):
        print("<<", end='')
    def print_display(self):
        print(self.__ch, end='')
    def close_display(self):
        print(">>")
    def get_ch(self):
        return self.__ch
    def set_ch(self, ch):
        self.__ch = ch
    ch = property(get_ch, set_ch)

class StringDisplay(AbstractDisplay):
    def __init__(self, str):
        self.__str = str
        self.__width = len(str)
    def get_str(self):
        return self.__str
    def set_str(self, str):
        self.__str = str
        self.__width = len(str)
    str = property(get_str, set_str)

    def open_display(self):
        self.print_line()
    
    def print_display(self):
        print("|" + self.str + "|")
    
    def close_display(self):
        self.print_line()
    
    def print_line(self):
        print("+", end='')
        i = 0
        while i < self.__width:
            print("-", end='')
            i += 1
        print("+")

d1 = CharDisplay('H')
d2 = StringDisplay("Hello, world.")
d3 = StringDisplay("こんにちは")
d1.display()
d2.display()
d3.display()