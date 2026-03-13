 Padrões de Projeto Estruturais em Python

Este repositório apresenta exemplos de implementação de padrões de projeto estruturais utilizando a linguagem Python.

O objetivo deste trabalho é compreender quais problemas esses padrões resolvem e como eles ajudam a organizar melhor a estrutura de sistemas de software.

 Padrões implementados

Neste repositório foram implementados dois padrões estruturais:

 1. Decorator

O padrão Decorator permite adicionar novas funcionalidades a um objeto de forma dinâmica, sem alterar a classe original.

Ele funciona envolvendo o objeto original com outros objetos chamados decoradores, que adicionam novos comportamentos.

No exemplo implementado:

- Café simples
- Café com leite
- Café com caramelo
- Café com leite e caramelo

Cada ingrediente adicional funciona como um decorador que modifica a descrição e o preço do café.

Arquivo:

```
decorator.py
```


 2. Facade

O padrão Facade fornece uma interface simples para um sistema complexo.

Ele cria uma classe intermediária que reúne várias funcionalidades de diferentes classes, facilitando o uso do sistema pelo usuário.

No exemplo implementado foi criado um sistema de Home Theater, que possui subsistemas como:

- Luzes
- Som
- Projetor

A classe `HomeTheaterFacade` simplifica o processo de assistir um filme executando todas as ações necessárias com apenas um método.

Arquivo:

```
facade.py
```


 Como executar os códigos

1. Instale o Python em seu computador.

2. Execute os arquivos pelo terminal:

```
python decorator.py
```

ou

```
python facade.py
```


 Estrutura do repositório

```
Padroes-de-Projeto-Estruturais
│
├── decorator.py
├── facade.py
└── README.md
```


 Referência

Material de apoio utilizado para estudo:

Refactoring Guru
https://refactoring.guru/pt-br/design-patterns/structural-patterns


 Autora

Leticia Gabriella
