from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

#Session related section
class Regime(models.TextChoices):
        ONLINE = 'O', gettext_lazy('Online')
        PRESENCIAL = 'P', gettext_lazy('Presencial')
        MISTO = 'M', gettext_lazy('Misto')


class Session(models.Model):

    number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(14), MinValueValidator(1)])
    duration = models.SmallIntegerField()
    theme = models.CharField(max_length=225)
    regime = models.CharField(max_length=1, choices=Regime.choices)

    def __str__(self):
        return f"Session nº: {self.number} | Theme: {self.theme} | Duration: {self.duration}"


class Phase(models.Model):
    
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    duration = models.SmallIntegerField()
    topic = models.CharField(max_length=225)
    content = models.CharField(max_length=225)
    regime = models.CharField(max_length=1, choices=Regime.choices)

    def __str__(self):
        return f"Phase nº: {self.number} From session: {self.session.number}| Topic: {self.topic} | Duration: {self.duration}"

#Group related section
class Cog_Group(models.Model):

    def __str__(self):
        return f"Group id: {self.id}"

#User related section
class User(models.Model):

    name = models.CharField(max_length= 26)
    email = models.EmailField()
    class Meta:
        abstract = True 
    def __str__(self):
        return f"User name: {self.name} | User id: {self.id}"

    

class Facilitator(User):

    grupo_cog = models.ManyToManyField(Cog_Group, blank = True, related_name ="facilitator")

    def __str__(self):
        return f"Facilitator name: {self.name} | Facilitator id: {self.id}"

    
class Participant(User):

    grupo_cog = models.ManyToManyField(Cog_Group, blank= True, related_name="participant")

    def __str__(self):
        return f"Participant name: {self.name} | Participant id: {self.id}"