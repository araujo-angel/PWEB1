
class DisciplinaService {
    constructor() {
        this.repositorio = new DisciplinaRepositorio();
        this.disciplina = new Disciplina();
    }

    cadastrar(nome, codigo) {
        const disciplinaPesquisada = this.listarDisciplinasPorCod(codigo);

        if(disciplinaPesquisada.length > 0) {
            throw new Error('Disciplina já existe!');
        }

        const disciplinaNova = new Disciplina(codigo, nome);
        this.repositorio.inserir(disciplinaNova);
        return disciplinaNova;
    }

    listar() {
        return this.repositorio.listar(); 
    }

    listarDisciplinasPorCod(codigo) {
        return this.repositorio.listar().filter(
            disciplina => disciplina.codigo === codigo);
    }

    remover(codigo) {
        this.repositorio.remover(codigo);
    }

    inserirAlunoNaDisciplina(codigo, aluno) {
        const disciplina = this.repositorio.listar().find(disciplina => disciplina.codigo === codigo);
        if (disciplina) {
            disciplina.inserirAluno(aluno);
        } else {
            throw new Error('Disciplina não encontrada!');
        }
    }
    
    listarAlunosDaDisciplina(codigo) {
        const disciplina = this.repositorio.listar().find(disciplina => disciplina.codigo === codigo);
        if (disciplina) {
            return disciplina.listarAlunos().map(aluno => ({
                nome: aluno.nome,
                idade: aluno.idade,
                matricula: aluno.matricula,
                disciplina: disciplina.nome
            }));
        }
        return [];
    }

}