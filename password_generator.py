#!/usr/bin/env python3

import random
import string
import hashlib
import secrets
from typing import List, Callable, Optional


# constantes para caracteres
LETTERS_LOWER = string.ascii_lowercase
LETTERS_UPPER = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def generate_character_sets() -> List[str]:
    """
    List comprehension para gerar listas de caracteres
    """
    return [
        char_set for char_set in [
            LETTERS_LOWER,
            LETTERS_UPPER, 
            NUMBERS,
            SYMBOLS
        ]
    ]


def filter_special_characters(char: str) -> bool:
    """
    Lambda para filtrar caracteres especiais perigosos
    """
    dangerous_chars = ['"', "'", '\\', '`', '~']
    return char not in dangerous_chars


def create_password_generator(
    default_length: int = 12,
    include_symbols: bool = True,
    include_numbers: bool = True,
    include_uppercase: bool = True,
    include_lowercase: bool = True
):
    """
    Closure: Função que retorna uma função geradora de senhas
    com configurações padrão armazenadas
    """
    def generate_password(length: Optional[int] = None) -> str:
        """
        Função interna que gera a senha usando as configurações do closure
        """
        actual_length = length or default_length
        
        # pool de caracteres
        char_pools = []
        if include_lowercase:
            char_pools.extend([char for char in LETTERS_LOWER])
        if include_uppercase:
            char_pools.extend([char for char in LETTERS_UPPER])
        if include_numbers:
            char_pools.extend([char for char in NUMBERS])
        if include_symbols:
            # lambda
            char_pools.extend([char for char in SYMBOLS if filter_special_characters(char)])
        
        if not char_pools:
            raise ValueError("Pelo menos um tipo de caractere deve ser habilitado")
        
        # pelo menos um caractere de cada tipo
        password = []
        if include_lowercase and LETTERS_LOWER:
            password.append(secrets.choice(LETTERS_LOWER))
        if include_uppercase and LETTERS_UPPER:
            password.append(secrets.choice(LETTERS_UPPER))
        if include_numbers and NUMBERS:
            password.append(secrets.choice(NUMBERS))
        if include_symbols:
            safe_symbols = [char for char in SYMBOLS if filter_special_characters(char)]
            if safe_symbols:
                password.append(secrets.choice(safe_symbols))
        
        # preencher o resto da senha aleatoriamente
        while len(password) < actual_length:
            password.append(secrets.choice(char_pools))
        
        # embaralhar a senha para evitar padrões
        random.shuffle(password)
        return ''.join(password)
    
    return generate_password


def create_password_transformer(transform_func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Função de alta ordem: recebe uma função de transformação
    """
    def transform_password(password: str) -> str:
        return transform_func(password)
    
    return transform_password



def encrypt_password(password: str) -> str:
    """Criptografa a senha usando SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def add_salt(password: str) -> str:
    """Adiciona um salt aleatório à senha"""
    salt = secrets.token_hex(8)
    return f"{salt}:{password}"


def reverse_password(password: str) -> str:
    """Inverte a senha"""
    return password[::-1]


def create_secure_password_generator():
    """
    gerador de senhas fortes com configurações de segurança
    """
    return create_password_generator(
        default_length=16,
        include_symbols=True,
        include_numbers=True,
        include_uppercase=True,
        include_lowercase=True
    )


def create_simple_password_generator():
    """
     gerador de senhas simples (apenas letras e números)
    """
    return create_password_generator(
        default_length=8,
        include_symbols=False,
        include_numbers=True,
        include_uppercase=True,
        include_lowercase=True
    )


def main():
    """
    Interface principal do gerador de senhas
    """
    print(" GERADOR DE SENHAS SEGURAS ")
    
    secure_generator = create_secure_password_generator()
    simple_generator = create_simple_password_generator()
    
    
    encryptor = create_password_transformer(encrypt_password)
    salter = create_password_transformer(add_salt)
    reverser = create_password_transformer(reverse_password)
    
    while True:
        print("\nOpções:")
        print("1. Gerar senha forte! (16 caracteres)")
        print("2. Gerar senha simples (8 caracteres)")
        print("3. Gerar senha customizada")
        print("4. Aplicar transformações")
        print("5. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            password = secure_generator()
            print(f"Senha gerada: {password}")
            
        elif choice == "2":
            password = simple_generator()
            print(f"Senha gerada: {password}")
            
        elif choice == "3":
            try:
                length = int(input("Digite o tamanho da senha: "))
                include_sym = input("Incluir símbolos? (s/n): ").lower() == 's'
                include_num = input("Incluir números? (s/n): ").lower() == 's'
                include_upper = input("Incluir maiúsculas? (s/n): ").lower() == 's'
                include_lower = input("Incluir minúsculas? (s/n): ").lower() == 's'
                
                custom_generator = create_password_generator(
                    default_length=length,
                    include_symbols=include_sym,
                    include_numbers=include_num,
                    include_uppercase=include_upper,
                    include_lowercase=include_lower
                )
                
                password = custom_generator()
                print(f"Senha customizada: {password}")
                
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif choice == "4":
            password = secure_generator()
            print(f"Senha original: {password}")
            print(f"Senha criptografada: {encryptor(password)}")
            print(f"Senha com salt: {salter(password)}")
            print(f"Senha invertida: {reverser(password)}")
            
        elif choice == "5":
            print("Obrigado por usar o gerador de senhas!")
            break
            
        else:
            print("Opção inválida!")


def demonstrate_functional_concepts():
    """
    Demonstra os conceitos de programação funcional implementados
    """
    print("\nDEMONSTRAÇÃO DOS CONCEITOS FUNCIONAIS\n")
    
    #List Comprehension
    print("1. LIST COMPREHENSION:")
    char_sets = generate_character_sets()
    print(f"Conjuntos de caracteres: {char_sets}")
    
    #Lambda
    print("\n2. LAMBDA (filtro de caracteres especiais):")
    test_chars = ['a', '!', '"', 'b', '\\', 'c']
    filtered = [char for char in test_chars if filter_special_characters(char)]
    print(f"Caracteres originais: {test_chars}")
    print(f"Caracteres filtrados: {filtered}")
    
    #Closure
    print("\n3. CLOSURE (gerador com configurações):")
    generator = create_password_generator(default_length=10, include_symbols=False)
    password1 = generator()
    password2 = generator(15)
    print(f"Senha com tamanho padrão (10): {password1}")
    print(f"Senha com tamanho customizado (15): {password2}")
    
    #Função de Alta Ordem
    print("\n4. FUNÇÃO DE ALTA ORDEM (transformadores):")
    transformer = create_password_transformer(lambda x: x.upper())
    test_password = "teste123"
    transformed = transformer(test_password)
    print(f"Senha original: {test_password}")
    print(f"Senha transformada: {transformed}")


if __name__ == "__main__":
    
    demonstrate_functional_concepts()
    
    
    main()

