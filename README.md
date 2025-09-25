# Gerador de Senhas Seguras
Este projeto implementa um sistema de geração e transformação de senhas com foco em segurança e boas práticas de programação funcional.
---

## Requisitos Funcionais (RF)

### RF1 – O sistema deve gerar senhas fortes de acordo com parâmetros do usuário.

* **Implementação:**

  * Função `create_password_generator()` → gera senhas parametrizadas.
  * Usado em `create_secure_password_generator()`, `create_simple_password_generator()` e também no menu da `main()`.
  * Uso do módulo `secrets` para aleatoriedade criptográfica e inclusão obrigatória de pelo menos um caractere de cada tipo.

---

### RF2 – O sistema deve permitir escolher o tamanho da senha.

* **Implementação:**

  * Parâmetro `default_length` em `create_password_generator()`.
  * Entrada do usuário na opção 3 do `main()` (`length = int(input(...))`).
  * Parâmetro `length` aceito dentro de `generate_password()` (closure interna).

---

### RF3 – O sistema deve incluir diferentes tipos de caracteres (maiúsculas, minúsculas, dígitos, símbolos).

* **Implementação:**

  * Constantes `LETTERS_LOWER`, `LETTERS_UPPER`, `NUMBERS`, `SYMBOLS`.
  * Inclusão controlada pelos parâmetros `include_lowercase`, `include_uppercase`, `include_numbers`, `include_symbols` em `create_password_generator()`.
  * Evidência: blocos que adicionam cada conjunto ao `char_pools`.

---

### RF4 – O sistema deve permitir aplicar transformações sobre senhas.

* **Implementação:**

  * Função de alta ordem `create_password_transformer()`.
  * Exemplos:

    * `encrypt_password()` (hash SHA-256).
    * `add_salt()` (concatenação de salt aleatório).
    * `reverse_password()` (inversão da string).
  * Chamados na `main()` opção 4.

---

## Requisitos Não Funcionais (RNF)

### RNF1 – O código deve ser legível e bem estruturado.

* **Evidência:**

  * Funções curtas e coesas (`generate_character_sets`, `encrypt_password`, `add_salt`, etc.).
  * Nomes descritivos (`create_secure_password_generator`, `filter_special_characters`).
  * Docstrings explicando cada função.
  * Separação clara de responsabilidades (geração, transformação, interface).

---

### RNF2 – O código deve utilizar conceitos de programação funcional.

* **Evidência:**

  * **List comprehension:** usado em `generate_character_sets()` e na construção de `char_pools`.
  * **Lambda:** em `filter_special_characters` (retorno usado em compreensões de lista).
  * **Closure:** `create_password_generator()` retorna `generate_password()`.
  * **Função de alta ordem:** `create_password_transformer()` recebe outra função como argumento e retorna nova função.
  * **Demonstração explícita:** função `demonstrate_functional_concepts()` imprime exemplos desses conceitos.

---
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
### Distribuição dos papéis da equipe
- **Mayara** – Documentação dos requisitos e organização do relatório.  
- **Nicolas** – Implementação principal do código em Python.  
- **Thiago** – Testes e validação do funcionamento do sistema.  
- **Cleberson** – Apoio na implementação e refatoração do código.  
- **Rodrigo** – Revisão de código e controle de versionamento (GitHub).  
- **Flavio** – Garantia de uso de programação funcional (lambda, closure, etc.)

### Uso de IA no projeto:
Durante o desenvolvimento, a equipe utilizou inteligência artificial (ChatGPT) como apoio na organização dos requisitos e na revisão do código. A IA foi empregada para sugerir boas práticas, verificar a conformidade com os critérios da atividade e propor melhorias na documentação. Todas as decisões de implementação foram discutidas e ajustadas pelo grupo.

### Exemplos:
**pergunta**: 
faça uma analise desse arquivo leia todo o codigo dele e baseado no texto que ja tenho de requisitos funcionais e nao funcionais , verifique te atendo totalmente esse criterio: Criar documento com os requisitos (diferenciando os requisitos funcionais e não funcionais) e realizar a identificação de como os requisitos estão codificados. o Exemplo, o requisito “o sistema deverá garantir segurança para as credenciais” está na função encrypt_password e store_password.

**resposta:**
Li todo a o arquivo password_generator.py que você enviou e cruzei com os requisitos funcionais e não funcionais que você já tinha listado
Conclusão da Análise

👉 Todos os requisitos funcionais e não funcionais listados estão plenamente atendidos e possuem evidências no código.(como RF4: transformações de senha e criptografia).
Quer que eu já te entregue isso em formato README.md (documentação formal pronta para GitHub) ou em formato relatório técnico (docx/pdf)?

-----
-----
**pergunta:**
oq significa uso programatico

**resposta:**
Uso programático" significa: usar algo por meio de código, dentro de um programa.

📌 Em outras palavras:

Uso normal → quando você usa uma ferramenta “na mão”, por exemplo abrir um aplicativo e clicar em botões para gerar a senha.

Uso programático → quando você chama funções dessa ferramenta dentro do seu próprio código, automatizando o processo.

-----
-----
**pergunta:**
''extension pylance wants to make refactoring changes with this file move'' oq isso quer dize

**resposta:**
Essa mensagem do VS Code aparece quando você está tentando mover ou renomear um arquivo Python e a extensão Pylance (que faz análise de código, autocompletar e refatoração) detecta que isso pode afetar referências dentro do seu projeto.

Basicamente, ela quer dizer:

“A extensão Pylance quer atualizar automaticamente o código que importa ou referencia este arquivo para refletir o novo nome ou local.”

Explicando melhor:

Se o seu arquivo é independente, que você só roda sozinho (python password_generator.py), você pode ignorar a mensagem e confirmar a mudança.

Se o arquivo é usado por outros arquivos (com import password_generator), Pylance sugere atualizar automaticamente essas importações para o novo nome, evitando erros de importação.

Conclusão

Arquivo isolado → pode renomear sem problemas.

Arquivo usado em outros módulos → deixar Pylance atualizar é seguro e recomendado.

Se quiser, posso te mostrar como renomear o arquivo sem quebrar nada e ainda manter a análise do Pylance funcionando. Quer que eu faça isso?

----
----
**pergunta:**
uso o comando python password_generator.py abre uma janela escolho abrir pelo vscode e abre uma aba no vscode ''python'' mas sem nada nela estou tendo a saida das 2 senhas

**resposta:**
que está acontecendo é só um detalhe do Windows + VS Code:

Quando você roda python password_generator.py, o Windows pergunta com qual aplicativo abrir arquivos .py (aquela janela de “Selecionar aplicativo”).

Mas, na prática, o Python já está rodando no terminal do VS Code → por isso você já vê as senhas sendo geradas lá embaixo no painel do terminal.

Ou seja: ✅ o código está funcionando corretamente, você já tem a saída esperada com as senhas.

🔧 Como corrigir essa janela chata

Para evitar que o Windows fique perguntando sempre:

Clique em Iniciar > Configurações > Aplicativos > Aplicativos padrão.

Procure por Python na lista.

Configure para que arquivos .py abram com Python (não com VS Code).

Assim, não aparece mais a tela de escolha quando você roda o comando.
