from django.db import models
from django.db import Manager

class SystemManager(models.Manager):
    """
    The System Manager handles processing multiple rows and creation, deletion, 
    etc of rows
    """
    
    def create_system(self):
        """
        Create system with appropriate constraints
        """
        pass
    
    def list_subsystems(self):
        """
        Returns a list of the subsystems of the current system
        """
        #return self.filter(subsystem != null)
        pass
    
    
    def list_system_materials(self):
        """
        Returns a list of the material objects that belong to a system and 
        its subsystems
        """
        pass
    
    def list_component_materials(self):
        """
        Returns a list of the material objects that belong to the components of
        a system and its subsystems
        """
        pass
    
    def list_questions(self):
        """
        Returns a list of question objects that belong to a system and its 
        subsystems
        """
        pass

class System(models.Model):
    """
    A System is a single unit that has a single function/purpose
    """

    title            = models.CharField(max_length=30)
    description      = models.TextField()
    subsystem        = models.ManyToManyField('self', null=True, blank=True)
    purpose          = models.ManyToManyField('Purpose', help_text="Each system has a single purpose object", null=True, blank=True)
    component        = models.ManyToManyField('Component', null=True, blank=True)
    #assembly         = #a system belongs to 1 or many assemblies
    #inpt  = #is an assembly input
    #outpt = #is an assembly output
    systems          = SystemManager()

    def __unicode__(self):
        return self.title

class AssemblyManager(models.Manager):
    """
    """
    #only create an assembly if it is valid
    #only create an assembly if it contains >1 system
    
    def list_systems(self):
        pass
    
    def get_assembly_directions(self):
        pass

class Assembly(models.Model):
    """
    An Assembly contains many systems and component
    """

    valid_assembly = models.BooleanField(default=False)
    #direction = models.
    
    def is_a_valid_assembly(self):
        """
        If for all systems in the assembly 
        """
        pass
        
class QuantityManager(models.Manager):
    """
    The Quantity Manager controls the creation and representation of quantities
    """
    
    def create_quantity(self, usr_val_list, usr_unit_list):
        """
        Create a Quantity
        
        Ex. CreateQuantity([23.4], ['m'])
        Ex. CreateQuantity([23.4], ['m'])
        Ex. CreateQuantity([22, 32.2, 2], ['N'])
        Ex. CreateQuantity([5], ['Hz'])
        
        **Need to rewrite code but you get the idea
        
        """
        # if usr_unit in SCALAR_CHOICES:
        #     if len(usr_val) > 1:
        #         raise ValidationError("The length of your list of values should be 1 for a scalar")
        #     else:
        #         scalar      = True
        #         scalar_unit = usr_unit
        #         value_type  = SCALAR_CHOICES[0]
        #         value  = usr_val[0]
            
        # else
        #     vector = True
        #     vector_unit = usr_unit
        #     for val in usr_val_list:
        #         #Construct a quantity object
        #         #bla bla
        pass
    
    def balance_2_units(self, operator, quantity_objectA, quantity_objectB):
        """
        Balance Units takes 2 quantity objects and and operator and returns
        the missing unit
        
        Ex. balance_units('*', <quantityA>, <quantityB>)
        """
        pass

class Quantity(models.Model):
    """
    A measureable quantity that goes into or comes out of something
    """
    
    SCALAR_CHOICES = (
                            ('power'                ,  (   ('watt', 'W') ),
                            ('work'                 ,  (   ('joule', 'J') ),
                            ('length'               ,  (   ('meter', 'm') ),
                            ('mass'                 ,  (   ('kilogram', 'kg') ),
                            ('volume'               ,  (   ('liter', 'l') ),
                            ('electric charge'      ,  (   ('coulomb', 'C') ),
                            ('electric potential'   ,  (   ('voltage', 'v') ),
                            ('resistance'           ,  (   ('ohm', u'U+2126') ),
                            ('electric conductance' ,  (   ('siemens', 'S') ),
                            ('capacitance'          ,  (   ('Farad', 'F') ),
                            ('inductance'           ,  (   ('Henry', 'H') ),
                            ('frequency'            ,  (   ('hertz', 'Hz') ),
                            ('time'                 ,  (   ('second', 's') ),
                            ('luminous intensity'   ,  (   ('candela', 'cd') ),
                            ('illuminance'          ,  (   ('lux', 'lx') ),
                            ('luminous flux'        ,  (   ('lumen', 'lm') ),
                            ('pressure'             ,  (   ('pascal', 'Pa') ),
                            ('magnetic flux'        ,  (   ('weber', 'Wb') ),
                            ('magnetic flux density',  (   ('tesla', 'T') ),
                            ('activity'             ,  (   ('bequerel', 'Bq') ),
                            ('amount of substance'  ,  (   ('mole', 'mol') ),
                            ('absorbed dose'        ,  (   ('gray', 'Gy') ),
                            ('dose equivalent'      ,  (   ('sievert', 'Sv') ),
                            ('catalyctic activity'  ,  (   ('katal', 'kat') )
                     )
    
    VECTOR_CHOICES = (   
                             ('force',  (   ('newton', 'N') ),
                             ('current',  (   ('amperage', 'amps') ),
                             #('velocity',  (   ('meters per second', 'm/s') ),# warning!!!
                             #('current',  (   ('amperage', 'amps') ),
                     )
    
    TYPE_CHOICES   = (        
                            ('none','no-coord-system'), 
                            ('x','rect-x-dir'), 
                            ('y','rect-y-dir'),
                            ('z','rect-z-dir'),
                            ('r','polar-radius'),
                            ('phi','polar-phi-angle'),
                            ('theta','polar-theta-angle'),
                            ('s','cylin-length-dir'),
                            ('z','cylin-length-dir'),
                            ('phi','cylin-phi-angle')
                     )

    vector           = models.BooleanField(default=False)
    scalar           = models.BooleanField(default=False)
    scalar_unit      = models.CharField(max_length=30, choices=SCALAR_CHOICES)
    vector_unit      = models.CharField(max_length=30, choices=VECTOR_CHOICES)
    value_type       = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
    value            = models.DecimalField(max_digits=24, decimal_places=24)
    
    system           = models.ForeignKey('System', null=True, blank=True)
    component        = models.ForeignKey('Component', null=True, blank=True)
    material         = models.ForeignKey('Material', null=True, blank=True)
    
    quantity         = QuantityManager()

    
class ComponentManager():
    
    def get_dimentions():
        return dims

class Component(models.Model):
    """
    """
    title        = models.CharField(max_length=30)
    description  = models.TextField()
    weigth       = models.DecimalField(max_digits=10,decimal_places=3)
    life_time    = models.DateTimeField()
    systems      = models.ManyToManyField('System')
    
    def __unicode__(self):
        return self.title

class Direction(models.Model):
    title        = models.CharField(max_length=30)
    systems      = models.ManyToManyField('System')
    def __unicode__(self):
        return self.title
'''

class Purpose(models.Model):
    """
    The Purpose class defines the purpose or function of a system. Each system has a single purpose.
    
    Each Purpose has a single method 
    """
    
    VERBS = 
    
    purp_verb   = models.CharField(max_length=20, choices=VERBS)
    purp_object = #purpose object is a quantity or material 
    method      = models.ForeignKey('Method', null=True, blank=True)

class Method (models.Model):
    """
    The method for accomplishing a purpose
    
    Ex. vibrate metal, rotate blades, etc
    """
    
    VERBS = (vibrate, rotate, mix, )
    
    method_verb   = models.CharField(max_length=30, choices=VERBS)
    method_object =
    


class Mechanical_Vibration(Method):
    """
    The Mechanical Vibration is a method object represents mechanical vibrational motion
    """

    initial_force     = models.ForeignKey('Quantity', related_name='+', null=True)
    frequency         = models.ForeignKey('Quantity', related_name='+', null=True)
    mass              = models.ForeignKey('Quantity', related_name='+', null=True)
    damping_ratio     = models.ForeignKey('Quantity', related_name='+', null=True)
    amplitude         = models.ForeignKey('Quantity', related_name='+', null=True)
    mode              = models.DecimalField(max_digits=5, decimal_places=3)
    system            = models.ForeignKey('System', related_name='+', null=True)
    natural_frequency = models.ForeignKey('Quantity', related_name='+', null= True)

    def __unicode__(self):
        return type_title

class Mechanical_Rotation(models.Model):
    """
    The Mechanical Vibration class ..
    """
    type_title       = models.CharField(max_length=30)
    description      = models.TextField()
    torque           = models.ForeignKey('Quantity', related_name='+', null=True)
    angular_velocity = models.ForeignKey('Quantity', related_name='+', null=True)
    system           = models.ForeignKey('System', null=True)
"""