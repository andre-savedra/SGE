from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
from django.utils import timezone
import pandas as pd

def StartChatBotScheduler():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(ChatBotJob, 'interval', seconds=2)
    scheduler.start()


#1 -) PROCURAR NO BANCO DE DADOS NA TABELA CHATBOT QUAIS DADOS
#     ESTÃO DONE=FALSE E SCHEDULED_DATE <= NOW() -->timezone

#2 -) EXECUTAR UM FOR PARA CADA ITEM RETORNADO E LER O ARQUIVO FILE
#     USANDO O PANDAS (pip install pandas)

#3 -) FAÇA UM FOR DE CADA LINHA DO EXCEL E CHAME A FUNÇÃO 
#     sendMessage()  ONDE NESTA FUNÇÃO VOCÊ VAI DAR
#     UM PRINT NO TERMINAL DO NÚMERO DE TELEFONE E DO NOME E 
#     A MENSAGEM A SER ENVIADA

#4 -) APÓS EXECUTAR O ARQUIVO INTEIRO, SALVE O MODEL DO CHATBOT PARA DONE=TRUE
#pip install pandas openpyxl
def SendMessage(message, phone):
    print('Message: ', message, phone)

def ChatBotJob():
    print('Running ChatBot Job...')
    chatBots = ChatBot.objects.filter(done=False).filter(scheduledDate__lte=timezone.now())
    for bot in chatBots:
        file = pd.read_excel(bot.file.path)
        for index,row in file.iterrows():
            if row['Telefone'] is not None:
                SendMessage(bot.message.replace('{name}',row['Nome']),row['Telefone'])
        bot.done = True
        bot.save()
    


    