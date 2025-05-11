# Inoformações de numero do trabalhador, horas trabalhadas e o quantidade q ganha por horas trablhadas
number = int(input())
hours = int(input())
valor_hora = float(input())

salary = valor_hora * hours

print(f"NUMBER: {number}")
print(f"SALARY: U$ {salary:.2f}")  