import csv
from collections import defaultdict, Counter
from datetime import datetime, timedelta

# Simulação de base de dados de bugs reportados
bugs_reportados = [
    {"id": 1, "descricao": "Erro de conexão", "gravidade": "Alta", "data_de_reporte": "2024-09-01"},
    {"id": 2, "descricao": "Falha no login", "gravidade": "Média", "data_de_reporte": "2024-09-02"},
    {"id": 3, "descricao": "Erro de exibição", "gravidade": "Baixa", "data_de_reporte": "2024-09-07"},
    {"id": 4, "descricao": "Bug de segurança", "gravidade": "Alta", "data_de_reporte": "2024-09-05"},
    {"id": 5, "descricao": "Erro no cálculo", "gravidade": "Média", "data_de_reporte": "2024-09-08"},
    {"id": 1, "descricao": "Erro de conexão", "gravidade": "Alta", "data_de_reporte": "2024-09-09"},
    {"id": 1, "descricao": "Erro de conexão", "gravidade": "Alta", "data_de_reporte": "2024-09-10"},
    {"id": 4, "descricao": "Bug de segurança", "gravidade": "Alta", "data_de_reporte": "2024-09-07"},
    {"id": 1, "descricao": "Erro de conexão", "gravidade": "Alta", "data_de_reporte": "2024-09-11"},
    {"id": 3, "descricao": "Erro de exibição", "gravidade": "Baixa", "data_de_reporte": "2024-09-08"},
    {"id": 1, "descricao": "Erro de conexão", "gravidade": "Alta", "data_de_reporte": "2024-09-12"},
    {"id": 4, "descricao": "Bug de segurança", "gravidade": "Alta", "data_de_reporte": "2024-09-12"},
    {"id": 5, "descricao": "Erro no cálculo", "gravidade": "Média", "data_de_reporte": "2024-09-06"},
    {"id": 2, "descricao": "Falha no login", "gravidade": "Média", "data_de_reporte": "2024-09-10"}
]

# Função para converter data em objeto datetime
def str_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

# Filtrar bugs reportados na última semana
hoje = datetime.now()
uma_semana_atras = hoje - timedelta(days=7)

bugs_ultima_semana = [
    bug for bug in bugs_reportados if str_to_date(bug["data_de_reporte"]) >= uma_semana_atras
]

# Contar frequências de bugs reportados na última semana
frequencia_bugs = Counter(bug["id"] for bug in bugs_ultima_semana)

# Filtrar bugs reportados mais de 5 vezes
bugs_prioritarios = {bug_id: count for bug_id, count in frequencia_bugs.items() if count > 5}

# Classificar bugs por gravidade
bugs_por_gravidade = defaultdict(list)
for bug in bugs_ultima_semana:
    bugs_por_gravidade[bug["gravidade"]].append(bug)

# Gerar e exportar relatório para CSV
def gerar_relatorio_csv(bugs_prioritarios, bugs_por_gravidade, arquivo_csv):
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["==== RELATÓRIO SEMANAL DE BUGS ===="])
        writer.writerow([])  # linha em branco
        
        # Bugs prioritários
        writer.writerow(["Bugs com mais de 5 reportagens na última semana:"])
        if bugs_prioritarios:
            for bug_id, count in bugs_prioritarios.items():
                bug = next(b for b in bugs_reportados if b["id"] == bug_id)
                writer.writerow([f"- {bug['descricao']} (ID: {bug_id}) - Reportado {count} vezes"])
        else:
            writer.writerow(["Nenhum bug reportado mais de 5 vezes."])
        
        writer.writerow([])  # linha em branco
        
        # Bugs por gravidade
        writer.writerow(["Bugs por gravidade:"])
        for gravidade, bugs in bugs_por_gravidade.items():
            writer.writerow([f"Gravidade: {gravidade}"])
            for bug in bugs:
                writer.writerow([f"- {bug['descricao']} (Data: {bug['data_de_reporte']})"])
            writer.writerow([])  # linha em branco entre categorias de gravidade

# Chamar a função de geração de relatório CSV
gerar_relatorio_csv(bugs_prioritarios, bugs_por_gravidade, "relatorio_semanal_bugs.csv")

print("Relatório gerado com sucesso e salvo como 'relatorio_semanal_bugs.csv'.")
