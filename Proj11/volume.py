###########################################################
#   Computer Project #11
#   Algorithm
#       Define constructor function    
#       Define the str method to represent the values in a specific way
#       Define repr method to represent the values in a specific way
#       Define the is valid method to make sure the parameters are valid
#       Define all other functions based on their main fucntion
#############################################################
UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, val=0, unit='ml'):
        '''sets the value of the magnitude and unit parameter depending on the inputed parameters when the Volume class is called'''
        if unit not in UNITS:
            self.val, self.unit = None, None
            val, unit = None, None
            #makes sure val is none so that it doesnt turn self.val into a value other than None


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
        
        
    def __str__(self):    
        '''represents the volume magnitude rounded to three decimal places'''
        if Volume.is_valid(self):
            return f"{self.val:.3f} {self.unit}"
            # returns self.val rounded to three decimal places  
        else:
            return "Not a Volume"

    def __repr__(self):    
        '''represents the volume magnitude rounded to three decimal places'''
        if Volume.is_valid(self):
            return f"{self.val:.6f} {self.unit}"
            # returns self.val rounded to six decimal places
        else:
            return "Not a Volume"
        
    def is_valid(self):    
        '''returns true if the volume obeject is valid; false otherwise''' 
        if self.unit not in UNITS:
        # if units not oz or ml
            return False  


        try: 
            if float(self.val) < 0:
                return False 
        except:
            return False 
        else:
            if self.val != 0 and self.unit != None:
                return True
    
    def get_units(self):     
        '''returns the unit of the volume'''
        if Volume.is_valid(self):
            return self.unit
        else:
            return None
    def get_magnitude(self):  
        '''returns the magnitude of the volume'''
        return self.val
        
        
    
    def metric(self):      
        '''returns a volume object in metric units'''
        if Volume.is_valid(self):
            if self.unit == "ml":
                return Volume(self.val, self.unit)
            else:
                return Volume(self.val*MLperOZ, "ml")
                #converts oz to ml
        
    def customary(self):    
        '''returns a volume object in customary units'''
        if Volume.is_valid(self):
            if self.unit == "oz":
                return Volume(self.val, self.unit)
            else:
                return Volume(self.val/MLperOZ, "oz")
                #converts ml to oz
        
    def __eq__(v1, v2):  
        '''checks if two volume objects are equal'''
        if v1.get_units() == v2.get_units():
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
            #if the abs value of the diff of the magnitude is less than delta then it is equal
        elif v1.get_units() == 'oz':
            v2 = v2.customary()
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
        elif v1.get_units() == 'ml':
            v2 = v2.metric()
            return abs(v1.get_magnitude() - v2.get_magnitude()) < DELTA
       
    def add(self, v):  
        '''adds constant values and volume objects to existing volume object'''
        
        if isinstance(v, float) or isinstance(v, int):
            return Volume(self.val+v, self.unit)

        if Volume.is_valid(self) == False or Volume.is_valid(v) == False:
            return Volume(-1,'oz')
            # returns invalid volume object if one of the volume objects are not valid

        if self.unit == v.get_units():
            return Volume(self.val + v.get_magnitude(), self.unit)
        elif self.unit == 'oz':
            v = v.customary()
            return Volume(self.val + v.get_magnitude(), self.unit)
        elif self.unit == 'ml':
            v = v.metric()
            return Volume(self.val + v.get_magnitude(), self.unit)


    
    def sub(self, v): 
        '''subtracts constant values and volume objects to existing volume object'''
        if isinstance(v, float) or isinstance(v, int):
            return Volume(self.val-v, self.unit)

        if Volume.is_valid(self) == False or Volume.is_valid(v) == False:
            return Volume(-1,"oz")
            # returns invalid volume object if one of the volume objects are not valid
        if self.unit == v.get_units():
            return Volume(self.val - v.get_magnitude(), self.unit)
        elif self.unit == 'oz':
            v = v.customary()
            return Volume(self.val - v.get_magnitude(), self.unit)
        elif self.unit == 'ml':
            v = v.metric()
            return Volume(self.val - v.get_magnitude(), self.unit)



