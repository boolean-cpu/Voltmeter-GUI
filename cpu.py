class CPU:
    def __init__(self):
        pass



    def Log(self, time):
        self.file = open("cpu.txt",'a')
        self.file.write(time+"\n")
        self.file.close()

if __name__ == "__main__":
    # This code will only run if the file is executed directly,
    # not when imported as a module
    pass