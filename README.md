# Calculadora Básica (Calculadora-Python)

Este projeto contém uma calculadora gráfica simples desenvolvida em Python usando `tkinter`.

**Requisitos:**
- Python 3.8 ou superior instalado.
- `tkinter` (geralmente incluído por padrão no Windows e macOS). Em distribuições Linux, instale o pacote `python3-tk` se necessário.

**Arquivos principais:**
- `Calculadora-Basica.py`: aplicação principal (interface gráfica).

**Como executar (Windows):**
1. Abra o Prompt de Comando ou PowerShell na pasta do projeto.
2. Execute:

```
python Calculadora-Basica.py
```

ou, se você tiver o launcher do Python instalado:

```
py Calculadora-Basica.py
```

**Como executar (macOS / Linux):**

```
python3 Calculadora-Basica.py
```

Observações sobre dependências:
- O projeto não usa bibliotecas externas além da biblioteca padrão (`tkinter`).
- Se, ao executar, aparecer erro relacionado ao `tkinter`, instale o pacote correspondente para sua distribuição (por exemplo, `sudo apt install python3-tk`).

Criar um executável (opcional):
- Instale o PyInstaller: `pip install pyinstaller`.
- Gere o executável (janela sem console):

```
py -3 -m PyInstaller --onefile --windowed "Calculadora-Basica.py"
```

- O executável ficará localizado na pasta `dist` criada pelo PyInstaller.

Executáveis já gerados:
- Há uma pasta `build/` no repositório que pode conter saídas de um build anterior (gerado via PyInstaller).

Contribuições e suporte:
- Abra uma issue ou envie um pull request descrevendo a melhoria ou correção.

Licença:
- Este repositório não contém uma licença especificada. Se desejar, adicione um arquivo `LICENSE` com a licença escolhida.
