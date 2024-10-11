from groq import Groq
from api_senha import API_KEY
import json

class Kevin():
    def __init__(self):
        self.client = Groq(
            api_key=API_KEY,
        )

    def Debate(self, tese):
        self.chat_sinistro = self.client.chat.completions.create(
            messages=[

                {
                    "role": "system",
                    "content": f"Você é uma IA que está em um debate, Você deve defender fortemente que discorda. Mostre por que sua opinião é a correta e não se deixe abalar por perguntas ou contra-argumentos, mas esteja pronto para ceder caso o argumento o convença, não escreva de forma muito curta mas tambpm não escreva mais de dois paragrafos"
                },
                {
                    "role": "user",
                    "content": f"Resposta: {tese}. "
                }

            ],
            model="llama3-70b-8192",
            #model="llama3-8b-8192",
        )
        return self.chat_sinistro.choices[0].message.content