# Comparação de Desempenho: Pandas vs Polars

## Objetivo

Este repositório foi criado com o objetivo de comparar o desempenho das bibliotecas de manipulação de dados **Pandas** e **Polars**. Diversos métodos de ambas as bibliotecas foram testados com dataframes de diferentes tamanhos, a fim de avaliar a eficiência e o desempenho em várias tarefas comuns de manipulação de dados.

## Como Utilizar

Para explorar e executar os testes de desempenho, siga os passos abaixo:

### 1. Configuração do Ambiente Virtual

Antes de começar, é recomendável configurar e ativar um ambiente virtual para manter as dependências do projeto isoladas. Você pode fazer isso da seguinte forma:

```bash
# Acesse a pasta do projeto
cd <path-to-repository>

# Crie um ambiente virtual chamado 'venv'
python -m venv venv

# Ative o ambiente virtual
source venv/Scripts/activate   # Linux/Mac
venv\Scripts\activate          # Windows
```

### 2. Geração de Dados
Para gerar os datasets utilizados nos testes, navegue até a pasta mock_data e execute o script mock_data.py.

```bash
Copy code
# Navegue até a pasta 'mock_data'
cd mock_data
```

Este script irá criar os datasets necessários para a execução dos testes de desempenho.

### 3. Execução dos Testes
Após a geração dos dados, retorne à pasta principal e execute o script principal main.ipynb para realizar os testes de desempenho.

Os resultados dos testes serão exibidos nas células do Jupyter Notebook e os gráficos comparativos serão gerados.
