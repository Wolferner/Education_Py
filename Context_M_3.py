
class open_manual:
    def __init__(self, adres:str):
        self.adres = adres

    def __enter__(self):
        self.file = open(self.adres,)
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()



if __name__ == '__main__':
    try:
        with open_manual("text.txt") as txt:
            txt.write('hui')
    except:
        FileNotFoundError("Faila ne sushestvuet!!!")