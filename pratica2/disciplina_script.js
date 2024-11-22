
const disciplinaServico = new DisciplinaService();
const controlador = new DisciplinaControlador(disciplinaServico); 
window.controlador = controlador; 
console.log("Controlador inicializado com sucesso:", controlador);
