import psutil
import time
import csv
from pynvml import *

def get_gpu_info():
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    util = nvmlDeviceGetUtilizationRates(handle)
    return util.gpu, info.used // 1024**2  # Uso em % e VRAM em MB

# Inicializa NVML (NVIDIA Management Library)
nvmlInit()

filename = "squad_performance_log.csv"
print(f"Monitorando... Pressione Ctrl+C para parar e salvar no {filename}")

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Header do CSV
    writer.writerow(["Timestamp", "CPU_Total_%", "RAM_Used_GB", "GPU_Load_%", "VRAM_Used_MB"])

    try:
        while True:
            t = time.strftime("%H:%M:%S")
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().used // 1024**3
            gpu_load, vram_used = get_gpu_info()

            writer.writerow([t, cpu, ram, gpu_load, vram_used])
            
            # Print rápido para você acompanhar no segundo monitor se tiver
            print(f"[{t}] CPU: {cpu}% | GPU: {gpu_load}% | VRAM: {vram_used}MB | RAM: {ram}GB", end='\r')
            
            time.sleep(1) 
    except KeyboardInterrupt:
        print(f"\nMonitoramento finalizado. Dados salvos em {filename}")
    finally:
        nvmlShutdown()