import requests

#res_get = requests.get("http://localhost:5000/hello/hellojson")

Dadosjson = ({
  "Integração de Sistemas": {
    "Código da disciplina": "BLU3024",
    "Ano e semestre de oferta": "2020.1",
    "Turma": "9743",
    "Nome do professor": "Maiquel de Brito",
    "Email do professor":"maiquel.b@ufsc.br",
    "Horário e local das aulas":"A305",
    "Horário e local de atendimento ao aluno":"Sala de atendimento",
    "Metodologia de ensino":"Descrição da metodologia",
    "Metodo de Avaliação":"Descrição da Avaliação",
    "Metodo de Recuperação":"Descrição da Recuperação",
    "Cronograma de aulas":"",
    "Observações":"Descrição observações"
  },
  
  "Algoritmos e estrutura de dados": {
    "Código da disciplina": "BLU3202",
    "Ano e semestre de oferta": "2017.2",
    "Turma": "02754A",
    "Nome do professor": "Mauri Ferrandin",
    "Email do professor":"mauri.f@ufsc.br",
    "Horário e local das aulas":"A301",
    "Horário e local de atendimento ao aluno":"Sala de atendimento 2",
    "Metodologia de ensino":"Descrição da metodologia 2",
    "Metodo de Avaliação":"Descrição da Avaliação 2",
    "Metodo de Recuperação":"Descrição da Recuperação 2",
    "Cronograma de aulas":"",
    "Observações":"Descrição observações 2"
  }
})

res_post = requests.post('http://localhost:5000/service/planos', json = Dadosjson)
if res_post.ok:
    print(" Requisição POST recebida pelo servidor, conteudo enviado: ", res_post.json(), "\n URL: ", res_post.url, "\n STATUS: ", res_post.headers)
else:
  print(str(res_post.status_code))
