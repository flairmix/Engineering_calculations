from enum import Enum

class PIPE_TYPE(Enum):
    PIPE_STELL_NEW = 1



#constants
G = 9.81 # м/с2 




class Pipe():

    def __init__(self,  pipe_type: PIPE_TYPE):
        
        self.pipe_type = pipe_type
        self.diameter: int # диаметр трубы 
        self.velocity: float # скорость м/с 
        self.s_lambda: float # коэффициент сопротивления трения по длине
        self.i: float  # гидравлический уклон

        #new steel pipes 


    def pipe_calculation(self):

        if self.pipe_type == "PIPE_STELL_NEW": 
            self.i = self.s_lambda * (1 / self.diameter) * (self.velocity**2 / (2 * G))
