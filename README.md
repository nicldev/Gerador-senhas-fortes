# Gerador de Senhas Seguras
Gerador de Senhas Seguras;

### Requisitos Funcionais

RF1: O sistema deve gerar senhas fortes de acordo com parâmetros do usuário.

Implementado em: generate_password() (arquivo password_generator.py).

RF2: O sistema deve permitir escolher o tamanho da senha.

Implementado em: parâmetro length da função generate_password().

RF3: O sistema deve incluir diferentes tipos de caracteres (maiúsculas, minúsculas, dígitos, símbolos).

Implementado em: variáveis letters, digits, symbols dentro de generate_password().

### Requisitos Não Funcionais

RNF1: O código deve ser legível e bem estruturado.

Evidência: uso de funções curtas, nomes descritivos.

RNF2: O código deve utilizar conceitos de programação funcional.

Evidência: lambda, list comprehension, closure, função de alta ordem

### Aplicação da programação funcional:

Lambda: para filtrar caracteres especiais.

List comprehension: gerar listas de caracteres.

Closure: criar uma função password_generator que guarda configurações padrão.

Função de alta ordem: função que recebe outra para transformar a senha (ex: criptografar).


Features

- **Geração segura**: Utiliza `secrets` module para criptografia segura
- **Configurável**: Permite escolher tamanho e tipos de caracteres
- **Programação funcional**: Implementa lambda, list comprehension, closure e funções de alta ordem
- **Transformações**: Suporte a criptografia, salt e outras transformações
- **Interface amigável**: Menu interativo para fácil uso


## Conceitos de Programação Funcional Implementados

### 1. **List Comprehension**
```python
# geração de conjuntos de caracteres
char_sets = [char_set for char_set in [LETTERS_LOWER, LETTERS_UPPER, NUMBERS, SYMBOLS]]

# filtragem de caracteres perigosos
safe_symbols = [char for char in SYMBOLS if filter_special_characters(char)]
```

### 2. **Lambda**
```python
# filtro de caracteres especiais perigosos
filter_special_characters = lambda char: char not in ['"', "'", '\\', '`', '~']

# transformação inline
upper_transformer = create_password_transformer(lambda x: x.upper())
```

### 3. **Closure**
```python
def create_password_generator(default_length=12, include_symbols=True, ...):
    def generate_password(length=None):
        # função interna para as configurações
        actual_length = length or default_length
        # lógica de geração
    return generate_password
```

### 4. **Função de Alta Ordem**
```python
def create_password_transformer(transform_func):
    def transform_password(password):
        return transform_func(password)
    return transform_password
```

## Como usar

### Interface Principal
```bash
python password_generator.py
```

### Opções disponíveis:
1. **gerar senha segura** (16 caracteres com símbolos)
2. **gerar senha simples** (8 caracteres, apenas letras e números)
3. **gerar senha customizada** (escolha tamanho e tipos de caracteres)
4. **aplicar transformações** (criptografia, salt, reversão)
5. **sair**

### Uso Programático
```python
from password_generator import create_password_generator, create_password_transformer

# criar gerador
generator = create_password_generator(
    default_length=16,
    include_symbols=True,
    include_numbers=True,
    include_uppercase=True,
    include_lowercase=True
)

# gerar senha
password = generator()
print(f"Senha: {password}")

# aplicar transformações
encryptor = create_password_transformer(lambda x: hashlib.sha256(x.encode()).hexdigest())
encrypted = encryptor(password)
```

## Testes

testes para verificar o funcionamento:

```bash
python test_password_generator.py
```

```bash
test_criptografia (__main__.TesteBasicoGerador.test_criptografia)
Checa se a senha criptografada é diferente da original ... ok
test_inverter (__main__.TesteBasicoGerador.test_inverter)
Verifica se a função de inverter funciona ... ok
test_salt (__main__.TesteBasicoGerador.test_salt)
Confere se o salt é adicionado no formato certo ... ok
test_senha_com_numeros (__main__.TesteBasicoGerador.test_senha_com_numeros)
Verifica se pelo menos tem um número na senha ... ok
test_senha_tamanho (__main__.TesteBasicoGerador.test_senha_tamanho)
Verifica se a senha gerada tem o tamanho pedido ... ok
```

## Segurança

- **Criptografia segura**: Usa `secrets` module em vez de `random`
- **Filtro de caracteres**: Remove caracteres perigosos que podem causar problemas
- **Garantia de complexidade**: Garante pelo menos um caractere de cada tipo
- **Embaralhamento**: Senhas são embaralhadas para evitar padrões

## Exemplos de Uso

### Senha Segura Padrão
```
Senha gerada: K9#mP2@vL7$nQ4!
```

### Senha Simples
```
Senha gerada: A7bC3dE9
```

### Senha Customizada (20 caracteres, sem símbolos)
```
Senha customizada: M8nP2qR5sT7vW9xY1zA3bC6
```

### Transformações
```
Senha original: K9#mP2@vL7$nQ4!
Senha criptografada: a1b2c3d4e5f6...
Senha com salt: 4f8a2b1c:K9#mP2@vL7$nQ4!
Senha invertida: !Q4n$L7v@P2m#9K
```
##Distribuição dos papéis da equipe
Mayara – Documentação dos requisitos e organização do relatório.

Nicolas – Implementação principal do código em Python.

Thiago – Testes e validação do funcionamento do sistema.

Cleberson – Apoio na implementação do código.

Rodrigo – Revisão de código e controle de versionamento (GitHub).

Flavio – Garantia de uso de programação funcional (lambda, closure, etc.) e integração final.

Um gerador de senhas seguras em python usando conceitos de programação funcional.

##Uso de IA no projeto:
Durante o desenvolvimento, a equipe utilizou inteligência artificial (ChatGPT) como apoio na organização dos requisitos e na revisão do código. A IA foi empregada para sugerir boas práticas, verificar a conformidade com os critérios da atividade e propor melhorias na documentação. Todas as decisões de implementação foram discutidas e ajustadas pelo grupo.
