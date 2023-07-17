# agentes-busca
📕 Algoritmos desenvolvidos na cadeira de Inteligência Artificial (2023.1)

**O que são agentes racionais?** São entidades compostas por sensores e atuadores que têm como objetivo alcançar resultados otimizados em um ambiente, tendo como base seus objetivos e a capacidade de atingi-los.

Para ser considerado racional, um agente deve:
- Ser autônomo, ou seja, aprender com base nas suas percepções e nos efeitos de cada ação realizada.
- Escolher ações que vão aumentar o seu desempenho, levando em consideração a sequência de percepções e conhecimentos internos.

A percepção do ambiente é feita através dos sensores, enquanto os atuadores são utilizados para agir no ambiente. Se formos trazer esse conceito para o dia a dia, em um agente humano, os sensores poderiam ser os olhos e ouvidos, e os atuadores poderiam ser mãos e pernas.

### Mapeamento de percepções em ações

É um processo onde um agente, ao receber uma sequência de percepções do ambiente, seleciona e executa ações apropriadas. Esse mapeamento é representado por uma função que relaciona percepções a ações, denotada como: [f: P* A] .

### Modelo PEAS

É uma representação que ajuda a definir o ambiente de tarefa para um agente inteligente. Esse modelo é importante para definir um modelo de inteligência artificial e entender o funcionamento dos agentes e o ambiente que eles atuam. 

**P**erformance (Desempenho): quantifica o quão bem ele está alcançando seus objetivos. 
**E**nvironment (Ambiente): é o contexto no qual o agente opera e interage.
**A**ctuators (Atuadores): São os dispositivos que permitem ao agente agir no ambiente. 
**S**ensors (Sensores): Permitem ao agente perceber o ambiente e coletar informações.

## Agentes

Os agentes inteligentes podem ser categorizados em quatro tipos principais: reativo simples, baseado em modelos, baseado em objetivos e baseado na utilidade. Cada um deles possui características e abordagens diferentes para interagir e responder ao ambiente.

- **Agente reativo simples**: Este tipo de agente escolhe ações com base no estado atual, ignorando o histórico de estados anteriores. Ele opera com uma série de regras condicionais (se-então), onde a condição é baseada no estado atual do ambiente. No entanto, esse agente não tem capacidade de rastrear o mundo além do que pode ver atualmente. Isso os torna limitados na capacidade de lidar com situações onde a informação do passado pode ser útil.

- **Agente baseado em modelos**: Este agente mantém algum tipo de modelo interno do mundo, que ele usa para rastrear aspectos do mundo que não pode ver atualmente. Ele leva em consideração o histórico de estados do ambiente para tomar suas decisões. Isso permite que ele lide com situações onde a visibilidade é parcial.

- **Agente baseado em objetivos**: Este agente, além de ter um modelo do mundo, possui informações sobre o objetivo que precisa ser alcançado. Ele toma decisões com base em seu modelo do mundo e em como suas ações o moverão em direção a seus objetivos.

- **Agente baseado na utilidade**: Este agente, além de ter um modelo do mundo e objetivos, possui uma função de utilidade. Essa função é usada para avaliar as opções e determinar qual ação levará ao estado mais útil. Em outras palavras, não apenas busca alcançar seus objetivos, mas também busca fazê-lo da maneira mais eficiente e eficaz possível

