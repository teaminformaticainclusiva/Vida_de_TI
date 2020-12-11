import psutil
from datetime import datetime

#By izaias de oliveira elias
#Fonte de pesquisa-0 (https://pypi.org/project/psutil/)
#Fonte de pesquisa-1 (https://psutil.readthedocs.io/en/latest/)

#Head
x = datetime.now()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print('\n'"Hoje é", dias[x.weekday()])
print("Data",x.day,"/", x.month,"/", x.year)
print("Horas",x.hour ,":",x.minute,":",x.second, '\n')

#Cpu
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()
cpu_percent = psutil.cpu_percent(interval=1)
cpu_stats = psutil.cpu_stats()
cpu_times = psutil.cpu_times()
cpu_times_percent = psutil.cpu_times_percent()

#Temperature
temp = psutil.sensors_temperatures()

#Memory
mem = psutil.virtual_memory()
swap = psutil.swap_memory()

#Disck
disck = psutil.disk_partitions()
disck_io = psutil.disk_io_counters(perdisk=True)
disck_usage = psutil.disk_usage('/')

#Users
users = psutil.users()

#Time
time_usage = psutil.boot_time()

#Network
net = psutil.net_io_counters(pernic=True)
conect = psutil.net_connections()
adress_if = psutil.net_if_addrs()
stats_net = psutil.net_if_stats()

print("Cores:", cpu_count,'\n')
print("Frequence:", cpu_freq,'\n')
print("Usage percent:", cpu_percent,'%''\n')
print("Estate:", cpu_stats,'\n')
print("Time:", cpu_times,'\n')
print("Time percent:", cpu_times_percent,'\n')
print("Temperature", temp,'c°' '\n')
print("Memory", mem,'\n')
print("Memory swap", swap,'\n')
print("Disck mount point", disck,'\n')
print("Dis")
print("Disck usage", disck_usage,'\n')
print("Users", users,'\n')
print("Time online", time_usage,'\n')
print("Network", net,'\n')
print("Network conect", conect,'\n')
print("Network adress", adress_if,'\n')
print("Network stats", stats_net,'\n')
