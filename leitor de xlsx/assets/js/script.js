document.addEventListener('DOMContentLoaded', function() {
    // Adiciona os eventos via JavaScript em vez de onclick no HTML
    document.getElementById('processarBtn').addEventListener('click', processarArquivo);
    document.getElementById('resetarBtn').addEventListener('click', resetarFiltros);
});

let alunosGlobal = [];

function normalizarCabecalho(cabecalho) {
    if (!cabecalho) return '';
    return cabecalho.toString().toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .trim();
}

function encontrarColuna(chaves, possiveisNomes) {
    const normalizadas = chaves.map(normalizarCabecalho);
    for (const nome of possiveisNomes) {
        const idx = normalizadas.indexOf(normalizarCabecalho(nome));
        if (idx !== -1) return chaves[idx];
    }
    return null;
}

function processarArquivo() {
    try {
        const input = document.getElementById("arquivo");
        if (!input) throw new Error("Elemento de upload não encontrado!");

        const file = input.files[0];
        if (!file) throw new Error("Selecione um arquivo XLSX primeiro.");

        // Verifica se a biblioteca XLSX está carregada
        if (typeof XLSX === 'undefined') {
            throw new Error("Biblioteca XLSX não carregada. Verifique o script.");
        }

        const reader = new FileReader();
        
        reader.onload = function(e) {
            try {
                const data = new Uint8Array(e.target.result);
                const workbook = XLSX.read(data, { type: "array" });
                
                if (!workbook.SheetNames || workbook.SheetNames.length === 0) {
                    throw new Error("O arquivo não contém planilhas!");
                }

                const firstSheetName = workbook.SheetNames[0];
                const sheet = workbook.Sheets[firstSheetName];
                const json = XLSX.utils.sheet_to_json(sheet, { defval: "", raw: false });

                if (json.length === 0) {
                    throw new Error("A planilha está vazia!");
                }

                const chaves = Object.keys(json[0]);
                
                // Busca as colunas (note que usamos "série" para manter compatibilidade com seu HTML)
                const campoNome = encontrarColuna(chaves, ["nome", "nome completo", "aluno"]);
                const campoEscola = encontrarColuna(chaves, ["escola"]);
                const campoCurso = encontrarColuna(chaves, ["curso"]);
                const campoSerie = encontrarColuna(chaves, ["série", "serie", "sala", "turma"]);
                const campoNascimento = encontrarColuna(chaves, ["data de nascimento", "nascimento"]);

                if (!campoNome) {
                    throw new Error("Não foi possível identificar a coluna de NOME!");
                }

                alunosGlobal = json.map(item => ({
                    nome: item[campoNome] || "",
                    escola: item[campoEscola] || "",
                    curso: item[campoCurso] || "",
                    serie: item[campoSerie] ? item[campoSerie].toString().trim() : "",
                    nascimento: formatarData(item[campoNascimento]) || ""
                }));

                aplicarFiltros(alunosGlobal);
                
            } catch (error) {
                console.error("Erro no processamento:", error);
                alert(`Erro: ${error.message}`);
            }
        };

        reader.onerror = function(error) {
            console.error("Erro na leitura do arquivo:", error);
            alert("Erro ao ler o arquivo. O arquivo pode estar corrompido.");
        };

        reader.readAsArrayBuffer(file);

    } catch (error) {
        console.error("Erro no processarArquivo:", error);
        alert(`Erro: ${error.message}`);
    }
}

function formatarData(data) {
    if (!data) return "";

    // Se já estiver no formato brasileiro (dd/mm/aaaa)
    if (typeof data === 'string' && data.match(/^\d{2}\/\d{2}\/\d{4}/)) {
        return data;
    }
    
    // Se for um número serial do Excel
    if (typeof data === 'number') {
        try {
            const date = new Date((data - (25567 + 2)) * 86400 * 1000);
            return date.toLocaleDateString('pt-BR');
        } catch (e) {
            return data.toString();
        }
    }
    
    // Tentar converter qualquer outro formato
    try {
        const date = new Date(data);
        if (isNaN(date.getTime())) return data.toString();
        return date.toLocaleDateString('pt-BR');
    } catch (e) {
        return data.toString();
    }
}

function aplicarFiltros(dados) {
    preencherDropdowns(dados);
    atualizarTabela();

    // Remove eventos antigos antes de adicionar novos
    ["filtroEscola", "filtroCurso", "filtroSerie", "filtroMes"].forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.replaceWith(element.cloneNode(true));
            document.getElementById(id).addEventListener("change", atualizarTabela);
        }
    });

    document.getElementById("filtros").classList.remove("d-none");
}

function preencherDropdowns(dados) {
    preencherSelectUnico("filtroEscola", dados.map(a => a.escola));
    preencherSelectUnico("filtroCurso", dados.map(a => a.curso));
    preencherSelectUnico("filtroSerie", dados.map(a => a.serie));

    const meses = dados.map(a => {
        try {
            const d = new Date(a.nascimento);
            return isNaN(d.getTime()) ? "" : d.toLocaleString("pt-BR", { month: "long" });
        } catch (e) {
            return "";
        }
    }).filter(mes => mes);

    preencherSelectUnico("filtroMes", meses);
}

function preencherSelectUnico(id, valores) {
    const select = document.getElementById(id);
    if (!select) return;
    
    const unicos = [...new Set(valores.filter(v => v))].sort();
    select.innerHTML = `<option value="">${id === 'filtroMes' ? 'Todos' : (id === 'filtroEscola' ? 'Todas' : (id === 'filtroCurso' ? 'Todos' : 'Todas'))}</option>` + 
        unicos.map(v => `<option value="${v}">${v}</option>`).join('');
}

function atualizarTabela() {
    try {
        const escola = document.getElementById("filtroEscola")?.value || "";
        const curso = document.getElementById("filtroCurso")?.value || "";
        const serie = document.getElementById("filtroSerie")?.value || "";
        const mes = document.getElementById("filtroMes")?.value || "";

        const filtrados = alunosGlobal.filter(a => {
            let mesAluno = "";
            try {
                const data = new Date(a.nascimento);
                mesAluno = isNaN(data.getTime()) ? "" : data.toLocaleString("pt-BR", { month: "long" });
            } catch (e) {
                mesAluno = "";
            }

            return (!escola || a.escola === escola)
                && (!curso || a.curso === curso)
                && (!serie || a.serie.toString() === serie)
                && (!mes || mesAluno === mes);
        });

        const tabelaBody = document.getElementById("tabelaAlunos");
        if (!tabelaBody) return;
        
        tabelaBody.innerHTML = filtrados.map(a => `
            <tr>
                <td>${a.nome}</td>
                <td>${a.escola}</td>
                <td>${a.curso}</td>
                <td>${a.serie}</td>
                <td>${a.nascimento}</td>
            </tr>
        `).join('');

        document.getElementById("totalAlunos").textContent = filtrados.length;
    } catch (error) {
        console.error("Erro ao atualizar tabela:", error);
    }
}

function resetarFiltros() {
    ["filtroEscola", "filtroCurso", "filtroSerie", "filtroMes"].forEach(id => {
        const element = document.getElementById(id);
        if (element) element.value = "";
    });
    atualizarTabela();
}