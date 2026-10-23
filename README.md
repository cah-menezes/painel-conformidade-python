# 🛡️ Painel de Conformidade

Script Python com Flask que exibe um painel web de controles de segurança com status colorido — útil para visualização rápida de conformidade em contextos de GRC.

## O que o script faz
- Modela controles de segurança com nome, categoria e status
- Sobe um servidor web local com Flask
- Exibe os controles numa página HTML com status verde, amarelo ou vermelho

## Como executar
```
python painel_conformidade.py
```
Acesse no navegador: `http://127.0.0.1:5000`