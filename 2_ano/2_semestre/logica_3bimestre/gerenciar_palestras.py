def Palestrando(palestrante_nivel, tipo):
    print("Você está palestrando!")
    print("Você está falando sobre um assunto interessante!")

    recursos = {
        ('NOVATO', 'WORKSHOP'): "3 horas e bastante equipamentos",
        ('NOVATO', 'PALESTRA'): "1 hora e equipamentos básicos",
        ('NOVATO', 'DEMONSTRAÇÃO'): "30 minutos e equipamentos básicos",
        ('EXPERIENTE', 'WORKSHOP'): "4 horas e equipamentos intermediarios",
        ('EXPERIENTE', 'DEMONSTRAÇÃO'): "1 hora e equipamentos intermediarios",
        ('EXPERIENTE', 'PALESTRA'): "3 horas e bastante equipamentos",
        ('PROFISSIONAL', 'WORKSHOP'): "5 minutos e equipamentos avançados",
        ('PROFISSIONAL', 'PALESTRA'): "4 horas e equipamentos avançados",
        ('PROFISSIONAL', 'DEMONSTRAÇÃO'): "2 horas e equipamentos básicos",
    }

    print(f"Vc precisara de {recursos.get((palestrante_nivel, tipo), '2 horas e equipamentos básicos')}")

def imprimir_fim():
    print("Você está terminando sua palestra!")
    print("FIM")

palestrante_nivel = input("Qual o seu nivel de experiencia? ").upper()
tipo = input("Qual tipo de palestra? ").upper()

Palestrando(palestrante_nivel, tipo)
imprimir_fim()