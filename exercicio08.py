"""8. Crie um programa que seja uma API de um contador de números. Esta API irá
manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
Para o programa teremos as seguinte chamadas:
● POST /contador
{
"numero": <numero>
}
Irá definir um novo número para o nosso contador. O método irá retornar um
HTTP 201.
● GET /contador
Retorna o número que foi guardado na memória, em um JSON no formato:
{
"numero": <numero guardado>
}
E também um HTTP 200.
● PUT /contador/incrementa

Irá incrementar o valor do número em 1 e retornar um HTTP 202.
● DELETE /contador
Irá zerar o valor do contador. A API irá retornar um HTTP 202.
Seguem algumas chamadas que fizemos no terminal, para mostrar o
comportamento de nosso programa, considere que iniciamos o programa agora e
executamos os testes na ordem apresentada:
1) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 0}
2) curl -X POST 'http://localhost:5000/contador’ -d
'{"numero": 123}'
Retornou um HTTP 201.
3) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 123}
4) curl -X PUT 'http://localhost:5000/contador/incrementa’
Retornou um HTTP 202.
5) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 124}
6) curl -X DELETE 'http://localhost:5000/contador’
Retornou um HTTP 202.
7) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 0}
Dificuldade: Média. Tempo: 9-17 minutos. Tempo para pensar no número na
memória, e fazer cada método."""

#-------------------------------- FastAPI -----------------------------------#

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Contador_base(BaseModel):
    numero: int

memoria = {"numero": 0}


@app.post("/contador")
async def contador_save(contadorBase: Contador_base):
    memoria["numero"] = contadorBase.numero
    raise HTTPException(status_code=201, detail="Created")

@app.get("/contador")
async def contador_return():
    print(memoria)
    return memoria

@app.put("/contador/incrementa")
async def contador_add():
    memoria["numero"] += 1
    raise HTTPException(status_code=202)

@app.delete("/contador")
async def contador_delete():
    memoria["numero"] = 0
    raise HTTPException(status_code=202)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("exercicio08:app", port=8000, reload=True)



#------------------------------------ Flask -------------------------------------#

from flask import Flask, request

app = Flask(__name__)

memoria = {"numero": 0}

@app.post('/contador')
def contador_add():
    number = request.get_json()
    memoria["numero"] = number.get("numero")
    return "", 201


@app.get('/contador')
def contador_get():
    return memoria, 200


@app.put('/contador/incrementa')
def contador_increment():
    memoria["numero"] += 1
    return "", 202


@app.delete('/contador')
def contador_del():
    memoria["numero"] = 0
    return "", 202


if __name__ == '__main__':
    app.run(debug=True)