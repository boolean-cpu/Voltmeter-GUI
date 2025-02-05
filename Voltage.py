
from ModelPredictor import ModelPredictor
class Voltage:
    def __init__(self):
        self.model = ModelPredictor("linear_regression_model.pkl")
    def Read(self, track,filename):
        c=''
        with open(filename, "r") as file1:
            c = file1.readlines()[1:]      
        if len(c)<= track:
            return 1000           
        else:
            try:
                return self.model.Predict(float(c[track-1]))
            except:
                return self.model.Predict(float(c[track-3]))
if __name__ == "__main__":
    # This code will only run if the file is executed directly,
    # not when imported as a module
    pass