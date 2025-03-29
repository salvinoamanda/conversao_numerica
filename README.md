# Conversão Numérica

Este projeto realiza a conversão de números entre diferentes bases numéricas, suportando bases de **2 a 40**.

## 📜 Funcionalidades

- Permite a entrada de qualquer caractere díponível na lista, incluíndo números inteiros, letras e símbolos. <br>Lista: `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$']`<br>
Os valores após o número '9' são a continuação da contagem, ex. `A = 10, B = 11, C = 12...` e assim por diante até 40 ($).
- Verifica se o número informado é válido.
- Converte um número de uma base para outra.
- Suporta caracteres especiais (!, @, #, \$) para bases acima de 36.

## 🛠️ Como Usar

1. Execute o script em um terminal:
   ```sh
   python conversao.py
   ```
2. Insira um valor numérico **inteiro positivo e maior que zero**.
3. Informe a **base original** do número (2 a 40).
4. Informe a **base para conversão** (2 a 40).
5. O programa retorna o valor convertido.

## 📌 Exemplo de Uso

```sh
Digite um valor positivo maior que zero (0): 1A
Digite a base do número informado (2 a 40): 16
Digite a base que deseja converter (2 a 40): 10

O número convertido é:
26
```

## 📋 Requisitos

- Python 3+
- Biblioteca `string` (padrão do Python)

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.
