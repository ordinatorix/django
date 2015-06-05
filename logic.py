"""

    File: logic.py
    
    Description: the logic.py file is the logic unit or processing unit for 
    processing what data to get from from models.py, then processing it
    and sending it to views.py
    
    What does it do????
    
    It turns user quesitons into information

"""

how do I build/assemble <system>
    whats the next step
    
what materials do I need 

get appropriate questions for user in appropriate order

##### LOGIC UNIT FOR System Design ###########
USER: Give me a system design that GENERATES POWER
    how much power do you need?
    where are you located?
    

USER: Give me a system design that GENERATES HEAT
    What temperature do you wish to acheive?
    Where are you located?
    
USER: Give me a system design that IRRIGATES my garden
    how much water do you need over what time period?
    what water resources do you have available?
    
USER: Give me a system design that 

##########LOGIC UNIT FOR System Creation ##############
1) I have a system that GENERATES POWER via MECHANICAL VIBRATION.  
When you take two metal sheets and subject them to an external vibrational 
force, the electrons jump back and forth generating a current and thus power.
    CATEGORY: Energy
    PURPOSE: generates power
    COMPONENT: metal sheets
        SIZE: null
        QUANTITY: 2
        MATERIAL: metal
            type: null
    METHOD: mechanical vibration
    MATERIAL: metal
    INPUT: vibrational force
        QUANTITY: null
    OUTPUT: power
        QUANTITY: null
    DIRECTIONS: null
    
2) The energy in the wind turns two or three propeller-like blades around a rotor. 
The rotor is connected to the main shaft, which spins a generator to create electricity.
    CATEGORY:Energy
    PURPOSE: generates electricity
    COMPONENT: Propeller
        SIZE: null
        QUANTITY: 2-3
        MATERIAL: null
    SUBSYSTEM: Main shaft
        SIZE: null
        QUANTITY: 1
        MATERIAL: null
    METHOD: mechanical rotatation
    MATERIAL: metal
    INPUT: air flow
        SCALAR: null
            UNIT: null
        VECTOR: True
            UNIT: m/s #default
        QUANTITY: null
    OUTPUT: power
        QUANTITY: null
    DIRECTIONS: null
    ASSEMBLY: null
    
3) Tesla turbine consists of a set of smooth disks, with nozzles applying a moving gas to the edge of the disk.
The gases drag on the disk by means of viscosity and the adhesion of the surface layer of the gas.
As the gas slows and adds energy to the disks, it spirals into the center exhaust.    

CATEGORY: Energy
    PURPOSE: null
    COMPONENT: smooth disks
        SIZE: null
        QUANTITY: null
        MATERIAL: null
    SUBSYSTEM: nozzles
        SIZE: null
        QUANTITY: 1
        MATERIAL: null
    METHOD: mechanical rotatation
    MATERIAL: null
    INPUT: gas flow
        SCALAR: null
            UNIT: null
        VECTOR: True
            UNIT: m/s #default
        QUANTITY: null
    OUTPUT: power
        QUANTITY: null
    DIRECTIONS: null
    ASSEMBLY: null
---------
matplotlib
numpy
scipy
pyGTS

class Units():
    """
    """
    
    def balance_units():
        """
        Get the result of operations with units
        Ex. balance_units( [(m/s)*(N/m)] ) gives N/s
        """
        pass
    
-----------------

EPA Q&A:
    Find a system that will generate 200kWh of power
    Find a system that will power my house
    Find a system to water my garden
    
    Convert my results in metric to X
    
    What is the name of the tool that X
    What materials do I need to X
    
    How do I build X
    How can I generate power
    How much power can I get from X
    How strong is X
    
    If I have a ball rolling at X, what is the X
    what will it cost to build x
    