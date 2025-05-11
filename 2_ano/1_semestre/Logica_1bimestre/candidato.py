candidato = {
    1: {"nome":"Cleiton", "partido": "F", "vice":"Renatão", "cargo":"Financeiro", "idade":30},
    2: {"nome":"Matheus", "partido": "D", "vice":"Gabriel", "cargo":"Educação", "idade":32},
    3: {"nome":"Fernanda", "partido": "C", "vice":"Jéssica", "cargo":"Saúde", "idade":35},
    4: {"nome":"Lucas", "partido": "B", "vice":"Pedro", "cargo":"Infraestrutura", "idade":28},
    5: {"nome":"Maria", "partido": "A", "vice":"Ana", "cargo":"Cultura", "idade":40},
    6: {"nome":"João", "partido": "F", "vice":"José", "cargo":"Segurança", "idade":38},
    7: {"nome":"Camila", "partido": "D", "vice":"Bruna", "cargo":"Meio Ambiente", "idade":33},
    8: {"nome":"Rafael", "partido": "C", "vice":"Thiago", "cargo":"Esportes", "idade":36},
    9: {"nome":"Roberta", "partido": "B", "vice":"Luana", "cargo":"Assistência Social", "idade":29},
    10: {"nome":"Paulo", "partido": "A", "vice":"Marcos", "cargo":"Desenvolvimento Econômico", "idade":42}
    
}

numero = int(input("Digite seu numero de candidato: "))

if numero in candidato:
    candidato = candidato[numero]
    print(f"Seu nome é {candidato["nome"]}")
    print(f"Seu partido {candidato["partido"]}")
    print(f"Seu vice é o {candidato["vice"]}")
    print(f"Seu cargo é {candidato["cargo"]}")
    print(f"Sua idade é {candidato["idade"]}")

else:
    print("Numero não encontrado, tente novamente")