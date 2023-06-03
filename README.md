# Portuguese/Português

Essa atividade faz parte do curso de Ciência dos Dados na Universidade Federal de Mato Grosso do Sul (UFMS). O código fornecido é uma representação prática de conceitos e técnicas abordados durante o curso, visando desenvolver as habilidades dos alunos em programação, estruturas de dados e lógica de programação.

O código fornecido implementa uma fila comum e uma fila prioritária. Ele permite adicionar pessoas a uma das filas e removê-las de acordo com algumas regras.

Na primeira parte do código, temos uma versão simples usando funções. As filas são representadas como listas de strings. As funções implementadas são as seguintes:

- `andarFila()`: Esta função verifica o tamanho da fila prioritária e remove duas pessoas dessa fila, se houver pelo menos duas pessoas. Se a fila normal tiver pessoas, também remove uma pessoa dessa fila. A função imprime uma mensagem indicando quantas pessoas foram removidas das filas.
- `adicionarEmFilaPrioritaria()`: Esta função solicita o nome da pessoa ao usuário e adiciona o nome à fila prioritária.
- `adicionarEmFilaNormal()`: Esta função solicita o nome da pessoa ao usuário e adiciona o nome à fila normal.
- `iniciar()`: Esta função solicita ao usuário que escolha entre adicionar ou remover pessoas. Se a opção for remover, chama a função `andarFila()`. Caso contrário, solicita a idade da pessoa e, com base nessa idade, chama a função `adicionarEmFilaPrioritaria()` ou `adicionarEmFilaNormal()`.

A segunda parte do código apresenta uma versão em forma de classe chamada `Fila`. A classe possui os mesmos métodos que as funções da versão anterior, mas agora eles são métodos de instância da classe. Além disso, as variáveis `filaNormal` e `filaPrioritaria` são atributos de instância inicializados no construtor (`__init__()`).

Ao criar uma instância da classe `Fila` e chamar o método `iniciar()`, o programa permite interagir com a fila, adicionando e removendo pessoas de acordo com as regras definidas.

A versão em classe é mais estruturada e encapsula os dados e a lógica relacionada em uma única entidade. Isso torna o código mais modular e organizado, facilitando sua manutenção e reutilização.

# English/Inglês
This activity is part of the Data Science course at the Federal University of Mato Grosso do Sul (UFMS). The provided code is a practical representation of concepts and techniques covered in the course, aimed at developing students' skills in programming, data structures, and programming logic.

The provided code implements a regular queue and a priority queue. It allows adding people to one of the queues and removing them according to certain rules.

In the first part of the code, we have a simple version using functions. The queues are represented as lists of strings. The implemented functions are as follows:

- `andarFila()`: This function checks the size of the priority queue and removes two people from that queue if there are at least two people. If the regular queue has people, it also removes one person from that queue. The function prints a message indicating how many people were removed from the queues.
- `adicionarEmFilaPrioritaria()`: This function prompts the user for the person's name and adds the name to the priority queue.
- `adicionarEmFilaNormal()`: This function prompts the user for the person's name and adds the name to the regular queue.
- `iniciar()`: This function prompts the user to choose between adding or removing people. If the option is to remove, it calls the `andarFila()` function. Otherwise, it asks for the person's age and based on that age, it calls either the `adicionarEmFilaPrioritaria()` or `adicionarEmFilaNormal()` function.

The second part of the code presents a class-based version called `Fila`. The class has the same methods as the functions in the previous version, but now they are instance methods of the class. Additionally, the `filaNormal` and `filaPrioritaria` variables are instance attributes initialized in the constructor (`__init__()`).

By creating an instance of the `Fila` class and calling the `iniciar()` method, the program allows interacting with the queue, adding and removing people according to the defined rules.

The class version is more structured and encapsulates the related data and logic into a single entity. This makes the code more modular and organized, facilitating its maintenance and reusability.
