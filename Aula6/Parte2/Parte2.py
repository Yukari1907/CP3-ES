import re

def validar_email(email: str) -> bool:
    """Valida formato básico de e-mail"""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    """
    Fluxo:
    1. Validar e-mail
    2. Verificar duplicidade
    3. Criar conta
    4. Enviar confirmação
    5. Aguardar confirmação
    6. Liberar acesso ou expirar
    """

    # 1. Validar e-mail
    if not validar_email(email):
        return "Erro: E-mail inválido"

    # 2. Verificar duplicidade
    if email_ja_existe:
        return "Erro: E-mail já cadastrado"

    # 3. Criar conta
    print("Conta criada com sucesso")

    # 4. Enviar e-mail
    print("E-mail de confirmação enviado")

    # 5. Verificar confirmação
    if not confirmou_email:
        return "Cadastro expirado: e-mail não confirmado"

    # 6. Liberar acesso
    return "Acesso liberado com sucesso"


# Testes (não apague!)
print(cadastro_usuario("joao@email.com", "senha123", False, True))
print(cadastro_usuario("email-invalido", "senha123", False, True))
print(cadastro_usuario("joao@email.com", "senha123", True, True))