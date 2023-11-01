# monitoramento-ups
Projeto para uso na CM Jahu, com a finalidade de monitorar os equipamentos UPS, enviar mensagens para um servidor gerenciador de fila de mensagem, consumir a mensagem e realizar o desligamento automático de todas as VMs, containers e Servidores físicos quando a falta energética atingir um tempo pré-definido.

## Como Usar

Para usar o aplicativo, siga estas etapas:

1. **Requisitos**: Você precisará ter o Python3 instalado em seu sistema.

2. **Bibliotecas**: Instale as bibliotecas `PySNMP` (biblioteca para o protocolo snmp). Para instalar:

    pip3 install pysnmp 

3. Para correto funciomento da biblioteca PySNMP, é necessário instalar a biblioteca pyasn1 na versao 0.4.8

    pip3 install pyasn1=0.4.8