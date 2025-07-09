
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '').lower()

    respostas = {
        "ed": "ED significa Educativos de corrida. São exercícios técnicos que simulam gestos da corrida e ajudam a ativar a musculatura e melhorar a técnica. Estão disponíveis em 'Rotinas de Treino'.",
        "aq": "O aquecimento deve ser feito em ritmo leve, próximo do seu ritmo de corrida longa. Serve para preparar o corpo e a mente para o treino principal.",
        "plano": "Temos dois planos: R$ 85 com planilha de corrida + educativos + alongamento dinâmico. R$ 110 é o plano completo, com treinos de força e periodização detalhada.",
        "feedback": "O feedback é essencial! Após cada treino, finalize na plataforma MFit, descreva o esforço, cole link do Strava ou Garmin, e como se sentiu. Isso ajuda a ajustar os treinos.",
        "desmotivado": "Lembre-se dos treinos que já fez e superou. Você não está sozinho. Pode me chamar direto se precisar ajustar algo. Bora pra cima!",
        "não treinei": "Se não conseguiu treinar, tudo bem. Pode seguir o próximo ou me chamar no WhatsApp que ajusto pra você. O importante é continuar o processo."
    }

    for chave, resposta in respostas.items():
        if chave in message:
            return jsonify({"reply": resposta})

    return jsonify({"reply": "Fala, atleta! Aqui é o CoachBot. Manda sua dúvida que eu te ajudo!"})
