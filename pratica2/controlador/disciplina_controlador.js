class DisciplinaControlador{
    constructor(){
        this.disciplina_servico = new DisciplinaService();
    }

    cadastrar(){
        const nomeElemento = document.querySelector("#nome");
        const codigoElemento = document.querySelector("#codigo");
        const disciplinaInserida = this.disciplina_servico.cadastrar(nomeElemento.value, Number(codigoElemento.value));
        const listaDisciplinasElemento = document.querySelector("#listaDisciplinas");
        if (disciplinaInserida) {
            this.inserirDisciplinaNoHtml(disciplinaInserida, listaDisciplinasElemento);
        }
    }

    listar() {
        const listaDisciplinasElemento = document.querySelector('#listaDisciplinas');
        const listaDisciplinas = this.disciplina_servico.listarAlunos();
        listaDisciplinas.forEach(disciplina => this.inserirDisciplinaNoHtml(disciplina, listaDisciplinasElemento));

        const listaAlunosElemento = document.querySelector('#listaAlunos');
        listaAlunosElemento.innerHTML = '';
        listaDisciplinas.forEach(disciplina => {
        const alunos = this.disciplina_servico.listarAlunosDaDisciplina(disciplina.codigo);
        alunos.forEach(aluno => {
            this.inserirAlunoNoHtml(aluno, listaAlunosElemento);
        });
    });
    }

    inserirDisciplinaNoHtml(disciplina, elementoDestino) {
        const disciplinaElemento = document.createElement("li");
        disciplinaElemento.textContent = `Nome: ${disciplina.nome} - Codigo: ${disciplina.codigo}`;
        elementoDestino.appendChild(disciplinaElemento);
    }

    inserirAlunoNaDisciplina(){
        const nomeElemento = document.querySelector("#nomeAluno");
        const idadeElemento = document.querySelector("#idade");
        const matriculoElemento = document.querySelector("#matricula");
        const codigoDisciplinaElemento = document.querySelector("#codigoDisciplinaAluno");
        const aluno = {nome: nomeElemento.value, idade: idadeElemento.value, matricula: matriculoElemento.value}
        const codigoDisciplina = Number(codigoDisciplinaElemento.value);
        this.disciplina_servico.inserirAlunoNaDisciplina(codigoDisciplina, aluno);
        console.log(this.disciplina_servico.listarAlunosDaDisciplina(codigoDisciplina));
        console.log(this.listarAlunosDaDisciplina(codigoDisciplina));
        //this.listar();
    }

    listarAlunosDaDisciplina(codigoDisciplina) {
        const listaAlunosElemento = document.querySelector('#listaAlunos');

        const alunos = this.disciplina_servico.listarAlunosDaDisciplina(codigoDisciplina);
        alunos.forEach(aluno => this.inserirAlunoNoHtml(aluno, listaAlunosElemento));
    }
    
    inserirAlunoNoHtml(aluno, elementoDestino) {
        const alunoElemento = document.createElement("li");
        alunoElemento.textContent = `Nome: ${aluno.nome} - Idade: ${aluno.idade} - Matrícula: ${aluno.matricula} - Disciplina: ${aluno.disciplina}`;
        elementoDestino.appendChild(alunoElemento);
    }
   
}