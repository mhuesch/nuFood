from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Hour(models.Model):
    MEAL_TYPES = (
        ('BRK', 'Breakfast'),
        ('BRU', 'Brunch'),
        ('LUN', 'Lunch'),
        ('DIN', 'Dinner'),
        ('LAT', 'Late Night'),
    )

    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )

    host_hall = models.ForeignKey(Hall)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=3, choices=MEAL_TYPES)
    start_hour = models.IntegerField()
    start_minute = models.IntegerField()
    end_hour = models.IntegerField()
    end_minute = models.IntegerField()
    def __unicode__(self):
        return u'%s hours on %s for %s' % (self.host_hall, self.day, self.meal_type)




'''
class Meal(models.Model):
    MEAL_TYPES = (
        ('BRK', 'Breakfast'),
        ('BRU', 'Brunch'),
        ('LUN', 'LUNCH'),
        ('DIN', 'Dinner'),
        ('LAT', 'Late Night'),
    )

    host_hall = models.ForeignKey(Hall)
    meal_type = models.CharField(max_length=3, choices=MEAL_TYPES)
    day = models.CharField(max_length=10, )
    '''