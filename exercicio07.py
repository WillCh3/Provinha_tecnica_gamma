"""7 - Crie uma API Rest em Python, que responda à seguinte chamada:
curl -X POST 'http://localhost:5000/soma' -H 'Content-type:
application/json' -d '{"x": 1, "y"; 2}'
A API /soma irá receber o valor x e somar com o valor y e retorná-lo em JSON no
seguinte formato:
{
"resultado": <valor do resultado>
}
Para o exemplo, acima iremos retornar:
{
"resultado": 3
}
Os valores de entrada, x e y são obrigatórios e devem ser números.
Tempo estimado: 6-8 minutos. Dificuldade: Fácil."""

#---------------------------------- FastAPI -----------------------------------------#
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Soma(BaseModel):
    x: int
    y: int

@app.post("/soma")
async def soma(soma: Soma):
    total = soma.x + soma.y
    return {"resultado": total}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("exercicio07:app", port=8000, reload=True)

##-------------------------------------- Flask -------------------------------------------#

from flask import Flask, request

app = Flask(__name__)

@app.post('/soma')
def soma():
    number = request.get_json()
    total = number.get("x") + number.get("y")

    return {"Total": total}


if __name__ == '__main__':
    app.run(debug=True)