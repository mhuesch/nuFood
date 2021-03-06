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
        ('RET', 'Retail'),
    )

    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    host_hall = models.ForeignKey(Hall)
    day = models.IntegerField(choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=3, choices=MEAL_TYPES)
    start_hour = models.IntegerField()
    start_minute = models.IntegerField()
    end_hour = models.IntegerField()
    end_minute = models.IntegerField()
    def __unicode__(self):
        return u'%s hours on %s for %s' % (self.host_hall, self.day, self.meal_type)


class MealMenu(models.Model):
    meal_time = models.ForeignKey(Hour)
    date = models.DateField()
    def __unicode__(self):
        return u'%s on day %s' % (self.meal_time, self.date)

class FoodAttribute(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __unicode__(self):
        return u'Food attribute: %s' % (self.name)

class FoodItem(models.Model):
    meal_menu = models.ManyToManyField(MealMenu)
    name = models.CharField(max_length=80, unique=True)
    attributes = models.ManyToManyField(FoodAttribute, blank=True, null=True, default=None)
    def __unicode__(self):
        return u'Food item: %s' % (self.name)


