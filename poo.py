class Pet {
  String nome;
  int idade;
  String som;


  Pet(this.nome, this.idade, this.som);


  void exibirNome() {
    print('Nome: $nome');
  }


  void mostraIdade() {
    print('Idade: $idade');
  }
  
  void mostraSom() {
    print('Som: $som');
  }
}
  
  

void main() {
  // Um objeto é um classe em seu estado concreto
  // Fazendo uma simples comparação, uma Classe é um planta de uma casa
  // E o objeto é a Casa
  Pet luna = Pet('luna', 5, 'miau');
  luna.mostraIdade();
  luna.mostraSom();
  luna.exibirNome();


  // Podemos usar a mesma classe para criar n objetos
  Pet teddy = Pet('teddy', 2, 'auau');
  teddy.mostraIdade();
  teddy.exibirNome();
  teddy.mostraSom();
}
