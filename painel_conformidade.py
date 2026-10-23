"""Um painel web simples que exibe o status de controles de segurança. Você roda o script, abre o navegador num endereço local, e vê uma página com os controles listados com status colorido — verde pra conforme, amarelo pra atenção, vermelho pra não conforme."""

from flask import Flask, render_template

#Classe Controle
class Controle:
    def __init__(self, nome, categoria, status):
        self.nome = nome
        self.categoria = categoria
        self.status = status

#Lista de controles
controles = [
    Controle("MFA habilitado", "Acesso", "conforme"),
    Controle("Política de senhas aplicada", "Acesso", "atenção"),
    Controle("Privilégio mínimo configurado", "Acesso", "não conforme"),
    Controle("Backup diário ativo", "Backup", "conforme"),
    Controle("Teste de restore realizado", "Backup", "não conforme"),
    Controle("Retenção de 90 dias configurada", "Backup", "atenção"),
    Controle("Firewall perimetral ativo", "Rede", "conforme"),
    Controle("Segmentação de rede aplicada", "Rede", "atenção"),
    Controle("VPN corporativa obrigatória", "Rede", "conforme"),
]

app = Flask(__name__)

@app.route("/")
def painel():
    return render_template("painel.html", controles=controles)

#Programa principal
if __name__ == "__main__":
    app.run(debug=True)