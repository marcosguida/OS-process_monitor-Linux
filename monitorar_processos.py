import psutil
cpu_percent_limit = 0.0
memory_percent_limit = 0.0

def monitorar_processos():
    # Obter uma lista de todos os processos em execução
    for processo in psutil.process_iter():
        try:
            
            nome_processo = processo.name()
            uso_cpu = processo.cpu_percent()
            uso_memoria = processo.memory_percent()

           
            if uso_cpu > cpu_percent_limit or uso_memoria > memory_percent_limit:
                
                print(f"Processo: {nome_processo}")
                print(f"Recurso CPU: {uso_cpu}%")
                print(f"Memória = {uso_memoria}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
monitorar_processos()

