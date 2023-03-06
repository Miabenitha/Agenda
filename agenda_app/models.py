from django.db import models
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
 
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class agendalist (models.Model):

    Tilte=models.CharField(max_length=200 ,unique=True)
    
    def get_absolute_url(self):
        return reverse("list" , args=[self.id])
    
    def __str__(self):
        return self.Tilte
    
class agendaItems(models.Model):

    Tilte=models.CharField(max_length=200 ,unique=True)
    Discription=models.TextField(null=True ,blank= True)
    Createdate=models.DateTimeField(auto_now_add=True)
    Duedate=models.DateTimeField(default=one_week_hence)
    agenda_list=models.ForeignKey(agendalist ,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("item_update" ,args=[str(self.agenda_list.id) ,str(self.id)])
    
    def __str__(self):
        return f"{self.Tilte} : Due{self.Duedate}"
    
    class  Meta:
      ordering = ["Duedate"]
    
        

    
    