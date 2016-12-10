#class Print:
#    def print_weak(self):
#    def print_strong(self):

class Banner:
    def __init__(self, str):
        self.str = str
    def show_with_paren(self):
        print("(" + self.str + ")")
    
    def show_with_aster(self):
        print("*" + self.str + "*")

class PrintBanner(Banner):
    def __init__(self, str):
        self.str = str 
    def print_weak(self):
        self.show_with_paren()
    def print_string(self):
        self.show_with_aster()
            
p = PrintBanner("Hello")
p.print_weak()
p.print_string()