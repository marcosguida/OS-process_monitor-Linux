# Monitor de Processos com Python

Este é um script em Python que possui o objetivo de monitorar os processos em execução em sistema operacional Linux e alertar sobre aqueles que excedem determinados limites de utilização de CPU e memória.

## Comportamento

O script utiliza a biblioteca `psutil`, que fornece uma interface para recuperar informações do sistema operacional, incluindo informações sobre processos em execução, uso de CPU e memória.

Ao executar o script, ele itera sobre todos os processos em execução e verifica o uso de CPU e memória de cada um. Se o uso de CPU ou memória de um processo exceder os limites definidos, o script exibe informações sobre esse processo, incluindo seu nome, uso de CPU e uso de memória.

## Requisitos

- Python
- Biblioteca `psutil`

Instalar python:

```
sudo apt install python3
```

```
sudo apt install python3-pip
```

Instalar a biblioteca utilizando o pip:

```
pip install psutil
```

## Como Usar

1. Fazer o download do script e salvar com a extensão `.py` (por exemplo, `monitorar_processos.py`).
2. Abrir um terminal ou prompt de comando e navegar até o diretório onde o script está localizado.
3. Executar o script digitando no terminal `$ python3 monitorar_processos.py`.

O script começará a monitorar os processos em execução no sistema.

## Contribuições

Este projeto foi desenvolvido por mim. Contribuições adicionais são bem-vindas.

