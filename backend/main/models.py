from django.db import models

BLOCKS = [
    ("A","Bloco A"),
    ("B","Bloco B"),
    ("C","Bloco C")
]

class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30,choices=BLOCKS)

    def __str__(self):
        return self.name
    

class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
TASKS_TYPE = [
    ('MA','Manutenção'),
    ('ME','Melhoria')    
]

TASKS_STATUS = [
    ('AB','Aberta'),
    ('EA','Em Andamento'),
    ('CA','Cancelada'),
    ('CO','Concluída'),
    ('EN','Encerrada')
]

class Tasks(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='tasksEnvironments', on_delete=models.CASCADE)
    #reporterFK = models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=30,choices=TASKS_TYPE)
    status = models.CharField(max_length=30,choices=TASKS_STATUS)

    def __str__(self):
        return self.title

