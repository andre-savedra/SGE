from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    #objects = CustomUserManager()

    def __str__(self):
        return self.email


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
    reporterFK = models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=30,choices=TASKS_TYPE)
    status = models.CharField(max_length=30,choices=TASKS_STATUS)

    def __str__(self):
        return self.title

class TasksAssignees(models.Model):
    assigneeFK = models.ForeignKey(CustomUser, related_name='tasksAssigneesCustomUser', on_delete=models.CASCADE)
    taskFK = models.ForeignKey(Tasks, related_name='tasksAssigneesTask', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskFK.title
    

class TasksStatus(models.Model):    
    taskFK = models.ForeignKey(Tasks, related_name='tasksStatusTask', on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=TASKS_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)    
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.status

class TasksEquipments(models.Model):    
    taskFK = models.ForeignKey(Tasks, related_name='tasksEquipmentsTask', on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name='tasksEquipmentsEquipment', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskFK.title

FILE_TYPE = [
    ('D','Document'),
    ('P','Photo')
]
    
class FileTasksStatus(models.Model):    
    taskStatusFK = models.ForeignKey(TasksStatus, related_name='fileTasksStatusTask', on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    fileType = models.CharField(max_length=15,choices=FILE_TYPE)    
        
    def __str__(self):
        return self.fileType


class EnvironmentsAssignees(models.Model):    
    environmentFK = models.ForeignKey(Environments, related_name='environmentsAssigneesEnv', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='environmentsAssigneesUser', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.assigneeFK.email
