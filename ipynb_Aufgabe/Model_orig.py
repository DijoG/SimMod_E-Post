
class Battery:
    """a simple battery class with the following default parameters:
    capacity_kWh= 1000
    charge_kW   = 200
    discharge_kW= 200
    current_kWh = capacity_kWh
    """

    @property
    def SoC(self):
        """returns the State of Charge als Wert zwischen [0 - 1]"""
        pass # replace pass with the code

    @property
    def max_charge(self):
        """returns the maximum possible charge to the battery 
        limited by the maximum charging power and the current battery charge 
        for a given hour in [kWh]"""
        pass
    
    @property
    def max_discharge(self):
        """returns the maximum possible DIScharge FROM the battery 
        limited by the maximum DIScharging power and the current battery charge 
        for a given hour in [kWh]"""
        pass

    def charge(self, amount):
        """charges the battery by the maximum possible amount, 
        up to the requested parameter [amount] 
        and RETURNS the actual amount charged (which is <= the [amount] requested)"""
        pass

    def discharge(self, amount):
        """DIScharges the battery by the maximum possible amount, 
        up to the requested parameter [amount] 
        and RETURNS the actual amount charged (which is <= the [amount] requested)"""
        pass

    
class Etruck(Battery):
    """represents an Etruck,
    inheriting all Properties of the Battery:
    capacity_kWh = 400     
    charge_kW = 100
    discharge_kW = 150
    consumption = 0.85 # kWh/km
    """

    def __init__(self, 
                 schedule = "workday", #workday, worknight
                 avg_km_per_h = 15,
                 ):
        """initializes a truck with a schedule string, and an avg_km_per_h mileage when the schedule is 'offsite'"""
        
        pass # replace pass with the code


    def status(self, hour_of_day, day_of_week): #hour_of_day [0-23], day_of_week [0-4 workday, 5,6 weekend] 
        """if the trucks's schedule parameter is 'workday', 
        it should return the string 'onsite' on weekends and on workdays from 3:00 unti 6:00 AM
        otherwise 'offsite'
        if the trucks's schedule parameter is 'worknight', 
        it should return the string 'onsite' on weekends and on workdays from 7:00 unti 19:00 AM,
        otherwise 'offsite'
        """
        pass # replace pass with the code

    @property
    def chargeable(self, hour_of_day, day_of_week):
        """returns True if the Truck is currently chargeable"""
        pass # replace pass with the code

    @property
    def hourly_demand(self):
        """returns the hourly energy demand in [kWh] of a typical hour"""
        pass # replace pass with the code
    
    @property
    def weekly_energy_demand(self):
        """returns the WEEKLy energy demand in [kWh] of the car"""
        pass # replace pass with the codde
        
    def __repr__(self):
        """should return the string:
        Etruck(schedule='schedulestring')
        """
        pass # replace pass with the code






