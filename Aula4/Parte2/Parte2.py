# ============================================================
# 🚀 SRS em Python — FIAP Marketplace
# Parte 1 + Parte 2 (com validação)
# ============================================================

from dataclasses import dataclass, field
from typing import List
from enum import Enum

# ============================================================
# ENUM DE PRIORIDADE
# ============================================================

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

# ============================================================
# CLASSES
# ============================================================

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str

@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)

    def relatorio(self):
        print(f"\n{'='*50}")
        print(f"SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f"{self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"[{rf.id}] {rf.nome} — {rf.prioridade.value}")
            print(f"Ator: {rf.ator}")
            print(f"Descrição: {rf.descricao}")
            print(f"Pré-condição: {rf.pre_condicao}")
            print(f"Pós-condição: {rf.pos_condicao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"[{rnf.id}] {rnf.categoria}")
            print(f"Descrição: {rnf.descricao}")
            print(f"Critério: {rnf.criterio_aceitacao}\n")

# ============================================================
# PARTE 2 — VALIDAÇÃO
# ============================================================

def validar_requisito(rf: RequisitoFuncional) -> dict:
    resultados = {}

    # ✔ Descrição > 20 caracteres
    resultados["descricao_valida"] = len(rf.descricao) > 20

    # ✔ Pré-condição não vazia
    resultados["pre_condicao_valida"] = rf.pre_condicao.strip() != ""

    # ✔ Possui número (critério mensurável)
    resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.descricao)

    return resultados

# ============================================================
# PARTE 1 — FIAP MARKETPLACE
# ============================================================

srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao="Marketplace interno para alunos venderem produtos artesanais entre si."
)

# 🔧 RF

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao="O sistema deve permitir cadastrar produtos com nome, descrição, preço e categoria em até 2 minutos.",
    prioridade=Prioridade.ALTA,
    ator="Aluno",
    pre_condicao="Usuário autenticado",
    pos_condicao="Produto disponível para venda"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao="O sistema deve permitir busca de produtos por categoria com retorno em até 3 segundos.",
    prioridade=Prioridade.MEDIA,
    ator="Aluno",
    pre_condicao="Produtos cadastrados",
    pos_condicao="Lista de produtos exibida"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Checkout",
    descricao="O sistema deve permitir finalizar compras com confirmação em até 5 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Aluno",
    pre_condicao="Itens no carrinho",
    pos_condicao="Pedido confirmado"
))

# ⚡ RNF

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao="Sistema com disponibilidade mínima de 99.9%",
    criterio_aceitacao="Uptime >= 99.9%"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Desempenho",
    descricao="Tempo de resposta da busca até 3 segundos",
    criterio_aceitacao="95% das requisições <= 3s"
))

# ============================================================
# RELATÓRIO
# ============================================================

srs.relatorio()

# ============================================================
# TESTE DA VALIDAÇÃO
# ============================================================

print("\n🔍 VALIDAÇÃO DOS REQUISITOS FUNCIONAIS\n")

for rf in srs.requisitos_funcionais:
    print(f"{rf.id} - {rf.nome}")
    print(validar_requisito(rf))
    print("-" * 50)