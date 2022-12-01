UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, val=0, unit='ml'):

        if unit not in UNITS:
            self.val, self.unit = None, None
            val, unit = None, None   


        try: 
            if float(val) < 0:
                val = 0
                self.val = 0
                unit = None
                self.unit = None  
        except:
            if val != None:
                self.val = 0
                self.unit = None
        else:
            if val != 0 and val != None and unit != None:
                self.val = val
                self.unit = unit
        
        
    def __str__(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if Volume.is_valid(self):
            return f"{self.val:.3f} {self.unit}"
        else:
            return "Not a Volume"

    def __repr__(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if Volume.is_valid(self):
            return f"{self.val:.6f} {self.unit}"
        else:
            return "Not a Volume"
        
    def is_valid(self):     # this line is incomplete: parameters needed
        if self.unit not in UNITS:
            return False  


        try: 
            if float(self.val) < 0:
                return False 
        except:
            return False 
        else:
            if self.val != 0 and self.unit != None:
                return True
    
    def get_units(self):     # this line is incomplete: parameters needed
        '''Docstring'''
        if Volume.is_valid(self):
            return self.unit
        else:
            return None
    def get_magnitude(self):  # this line is incomplete: parameters needed
        '''Docstring'''
        return self.val
        
        
    
    def metric(self):      # this line is incomplete: parameters needed
        '''Docstring'''
        if Volume.is_valid(self):
            if self.unit == "ml":
                return Volume(self.val, self.unit)
            else:
                return Volume(self.val*MLperOZ, "ml")
        
    def customary(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if Volume.is_valid(self):
            if self.unit == "oz":
                return Volume(self.val, self.unit)
            else:
                return Volume(self.val/MLperOZ, "oz")
        
    def __eq__(v1, v2):  # this line is incomplete: parameters needed
        '''Docstring'''
        if v1.get_units() == v2.get_units():
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
        elif v1.get_units() == 'oz':
            v2 = v2.customary()
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
        elif v1.get_units() == 'ml':
            v2 = v2.metric()
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
       
    def add(self, v):  # this line is incomplete: parameters needed
        '''Docstring'''
        
        if isinstance(v, float) or isinstance(v, int):
            return Volume(self.val+v, self.unit)

        if Volume.is_valid(self) == False or Volume.is_valid(v) == False:
            return Volume(-1,'oz')

        if self.unit == v.get_units():
            return Volume(self.val + v.get_magnitude(), self.unit)
        elif self.unit == 'oz':
            v = v.customary()
            return Volume(self.val + v.get_magnitude(), self.unit)
        elif self.unit == 'ml':
            v = v.metric()
            return Volume(self.val + v.get_magnitude(), self.unit)


    
    def sub(self, v): # this line is incomplete: parameters needed
        '''Docstring'''
        if isinstance(v, float) or isinstance(v, int):
            return Volume(self.val-v, self.unit)

        if Volume.is_valid(self) == False or Volume.is_valid(v) == False:
            return Volume(-1,"oz")

        if self.unit == v.get_units():
            return Volume(self.val - v.get_magnitude(), self.unit)
        elif self.unit == 'oz':
            v = v.customary()
            return Volume(self.val - v.get_magnitude(), self.unit)
        elif self.unit == 'ml':
            v = v.metric()
            return Volume(self.val - v.get_magnitude(), self.unit)

v1 = Volume(2.5, "tsp")
print(v1.get_magnitude())

