document.getElementById('grafico').addEventListener('click', function () {
    // Obter valores do formulário
    const criancas = parseInt(document.getElementById('criancas').value) || 0;
    const jovens = parseInt(document.getElementById('jovens').value) || 2000; // Exemplo fornecido
    const adultos = parseInt(document.getElementById('adultos').value) || 0;
    const idosos = parseInt(document.getElementById('idosos').value) || 0;

    const criancasMulheres = parseInt(document.getElementById('criancas_mulheres').value) || 0;
    const criancasHomens = parseInt(document.getElementById('criancas_homens').value) || 0;
    const jovensMulheres = parseInt(document.getElementById('jovens_mulheres').value) || 0;
    const jovensHomens = parseInt(document.getElementById('jovens_homens').value) || 0;
    const adultosMulheres = parseInt(document.getElementById('adultos_mulheres').value) || 0;
    const adultosHomens = parseInt(document.getElementById('adultos_homens').value) || 0;
    const idososMulheres = parseInt(document.getElementById('idosos_mulheres').value) || 0;
    const idososHomens = parseInt(document.getElementById('idosos_homens').value) || 0;

    const regiaoLeste = parseInt(document.getElementById('regiao_leste').value) || 0;
    const regiaoOeste = parseInt(document.getElementById('regiao_oeste').value) || 0;
    const regiaoNorte = parseInt(document.getElementById('regiao_norte').value) || 0;
    const regiaoSul = parseInt(document.getElementById('regiao_sul').value) || 0;

    const formacaoSem = parseInt(document.getElementById('formacao_sem').value) || 0;
    const formacaoFundamental = parseInt(document.getElementById('formacao_fundamental').value) || 0;
    const formacaoMedio = parseInt(document.getElementById('formacao_medio').value) || 0;
    const formacaoSuperior = parseInt(document.getElementById('formacao_superior').value) || 0;

    const formacaoEnfermagem = parseInt(document.getElementById('formacao_enfermagem').value) || 0;
    const formacaoPedagogia = parseInt(document.getElementById('formacao_pedagogia').value) || 0;
    const formacaoTi = parseInt(document.getElementById('formacao_ti').value) || 0;

    const pop2022 = parseInt(document.getElementById('pop_2022').value) || 0;
    const pop2027 = parseInt(document.getElementById('pop_2027').value) || 0;

    // Criar elementos canvas dinamicamente
    const sectionDados = document.querySelector('.dados');
    const canvases = [
        { id: 'chartFaixaEtaria', title: 'Faixa Etária (Total)' },
        { id: 'chartFaixaEtariaSexo', title: 'Faixa Etária por Sexo' },
        { id: 'chartRegioes', title: 'Regiões' },
        { id: 'chartFormacao', title: 'Formação' },
        { id: 'chartFormacaoSuperior', title: 'Formação Superior Específica' },
        { id: 'chartPopulacao', title: 'População por Ano' }
    ];

    canvases.forEach(chart => {
        const canvas = document.createElement('canvas');
        canvas.id = chart.id;
        const title = document.createElement('h3');
        title.textContent = chart.title;
        sectionDados.appendChild(title);
        sectionDados.appendChild(canvas);
    });

    // Gráfico 1: Faixa Etária (Total) - Barras
    ```chartjs
    {
        "type": "bar",
        "data": {
            "labels": ["Crianças", "Jovens", "Adultos", "Idosos"],
            "datasets": [{
                "label": "População",
                "data": [criancas, jovens, adultos, idosos],
                "backgroundColor": ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9"],
                "borderColor": ["#D64550", "#483C67", "#5A7F3C", "#D8A7B1"],
                "borderWidth": 1
            }]
        },
        "options": {
            "scales": {
                "y": {
                    "beginAtZero": true
                }
            },
            "plugins": {
                "legend": {
                    "display": false
                }
            }
        }
    }