# Bin Packing Problem - Módulo Python

Este diretório (`src`) contém o núcleo reutilizável do projeto Bin Packing Problem.

## Como reutilizar

1. Instale o pacote no modo editável (recomendado para desenvolvimento):

```bash
pip install -e .
```

2. Importe as principais interfaces no seu código Python:

```python
from src import main, Config

config = Config()
main(config)
```

## Estrutura
- `main.py`: Função principal de execução.
- `config.py`: Configurações do projeto.
- `algorithms/`, `models/`, `utils/`: Componentes reutilizáveis.

## Exemplo de uso
Veja acima como importar e executar o módulo principal.

## Observações
- Adicione `__init__.py` em subpastas para garantir que sejam módulos Python.
- Consulte a documentação de cada módulo para detalhes de uso avançado.
