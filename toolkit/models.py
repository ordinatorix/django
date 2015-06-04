from django.db import models

class Category(models.Model):
    """
    The Category is ..
    """
    title        = models.CharField(max_length=20)
    description  = models.TextField()

    def __unicode__(self):
        return self.title

class System(models.Model):
    """
    A system is a single unit that has a single function
    """

    purpose_choices = ( ('pg', 'power generation'), ('ps','power storage'))

    method_choices = (  ('mv', 'mechanical vibration'), ('mr','mechanical rotation'))

    title        = models.CharField(max_length=30)
    description  = models.TextField()
    categories   = models.ForeignKey('Category') #--> one system does not only belong to one category <--#
    subsystem    = models.ManyToManyField('self', null=True, blank=True) #this needs to be ManyToManyField('self', blank=True, null=True)

    purpose      = models.CharField(max_length=20, choices=purpose_choices)
    method       = models.CharField(max_length=30, choices=method_choices)

    def __unicode__(self):
        return self.title

class Scalar(models.Model):
    """
    """
    UNIT_CHOICES    = (   ('power','W'),
                          ('meters','m'),
                          ('kilograms','kg'),
                          ('voltage','V'),
                          ('volume', 'V'),
                          ('frequency','Hz')
                      )

    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    value = models.DecimalField(max_digits=5, decimal_places=3)

    def __unicode__(self):
        return self.value

class Vector(models.Model):
    """
    """
    UNIT_CHOICES    = (   ('force','F'),
                          ('amperage','Amps')
                      )

    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
 
    #Rectangular/Cartesian Coords
    x_value = models.DecimalField(max_digits=5, decimal_places=3)
    x_angle = models.DecimalField(max_digits=5, decimal_places=3)

    y_value = models.DecimalField(max_digits=5, decimal_places=3)
    y_angle = models.DecimalField(max_digits=5, decimal_places=3)

    z_value = models.DecimalField(max_digits=5, decimal_places=3)
    z_angle = models.DecimalField(max_digits=5, decimal_places=3)

    #Polar Coords
#    r = models.DecimalField(max_digits=5, decimal_places=3)
#    phi = models.DecimalField(max_digits=5, decimal_places=3)
#    theta = models.DecimalField(max_digits=5, decimal_places=3)

    #Cylindrical Coords
#    s = models.DecimalField(max_digits=5, decimal_places=3)
#    z = models.DecimalField(max_digits=5, decimal_places=3)
#    theta = models.DecimalField(max_digits=5, decimal_places=3)

    def __unicode__(self):
        return


class Mechanical_Vibration(models.Model):
    """
    The Mechanical Vibration class ..
    """
    type_title    = models.CharField(max_length=30)
    description   = models.TextField()

    initial_force = models.ForeignKey('Vector', related_name='+', null=True)
    frequency     = models.ForeignKey('Scalar', related_name='+', null=True)
    mass          = models.ForeignKey('Scalar', related_name='+', null=True)
    damping_ratio = models.ForeignKey('Scalar', related_name='+', null=True)
    amplitude     = models.ForeignKey('Scalar', related_name='+', null=True)
    mode         = models.DecimalField(max_digits=5, decimal_places=3)
    system        = models.ForeignKey('System', related_name='+', null=True)

    def __unicode__(self):
        return type_title

class Mechanical_Rotation(models.Model):
    """
    The Mechanical Vibration class ..
    """
    type_title       = models.CharField(max_length=30)
    description      = models.TextField()
    torque           = models.ForeignKey('Vector', related_name='+', null=True)
    angular_velocity = models.ForeignKey('Vector', related_name='+', null=True)
    system           = models.ForeignKey('System', null=True)

class Assembly

'''
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
