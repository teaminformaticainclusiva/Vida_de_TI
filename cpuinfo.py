import psutil

#by python_genius
#cores 
print("Physical core:", psutil.cpu_count(logical=False))
print("Total core:", psutil.cpu_count(logical=True))

#Frequence
cpufreq = psutil.cpu_freq()
print(f"Max frequency: {cpufreq.max:.2f}Mhz")
print(f"Min frequency: {cpufreq.min:.2f}Mhz")
print(f"Corrent frequency: {cpufreq.current:.2f}Mhz")

#Cpu uso
print("CPU Usage core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core{i}: {percentage}%")

print(f"Total CPU Usage: {psutil.cpu_percent()}%")
