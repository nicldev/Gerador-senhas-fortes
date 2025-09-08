#!/usr/bin/env python3
import unittest
from password_generator import (
    create_password_generator,
    encrypt_password,
    reverse_password,
    add_salt
)

class TesteBasicoGerador(unittest.TestCase):
    def test_senha_tamanho(self):
        """Verifica se a senha gerada tem o tamanho pedido"""
        gerador = create_password_generator(default_length=12)
        senha = gerador()
        self.assertEqual(len(senha), 12)

    def test_senha_com_numeros(self):
        """Verifica se pelo menos tem um número na senha"""
        gerador = create_password_generator(
            default_length=10,
            include_symbols=False,
            include_numbers=True,
            include_uppercase=False,
            include_lowercase=True
        )
        senha = gerador()
        self.assertTrue(any(c.isdigit() for c in senha))

    def test_criptografia(self):
        """Checa se a senha criptografada é diferente da original"""
        senha = "teste123"
        criptografada = encrypt_password(senha)
        self.assertNotEqual(senha, criptografada)

    def test_inverter(self):
        """Verifica se a função de inverter funciona"""
        senha = "abc123"
        self.assertEqual(reverse_password(senha), "321cba")

    def test_salt(self):
        """Confere se o salt é adicionado no formato certo"""
        senha = "meuTeste"
        com_salt = add_salt(senha)
        self.assertIn(":", com_salt)
        self.assertIn(senha, com_salt)


if __name__ == "__main__":

    print("Rodando testes")
    unittest.main(verbosity=2)

