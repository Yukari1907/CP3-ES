# CP3-ES

### Aula 01 - Introdução à Engenharia de Software

#### 📐 Diagrama
<img width="1876" height="937" alt="protótipo visual  aula01-introdução a engenharia de software" src="https://github.com/user-attachments/assets/6793b71d-793e-4f47-92de-b050f3525d83" />

Este diagrama apresenta o protótipo de alta fidelidade do aplicativo Racha Rolê, focado na divisão inteligente de despesas compartilhadas entre amigos.

A modelagem prioriza a experiência do usuário (UX) através de decisões como:
- Divisão Proporcional e Granular: Permite selecionar itens específicos para consumidores específicos, evitando divisões injustas.
- Transparência Financeira: Inclui telas dedicadas a taxas, gorjetas e um resumo final com "Transferências Mínimas" para simplificar o acerto de contas.
- Interface Intuitiva: Utiliza elementos visuais modernos, como avatares e barras de progresso, para facilitar a gestão de contas ativas e históricos.

### Aula 02 - Levantamento de Requisitos: Técnicas de Elicitação

#### 💻 Código

'''

    def celsius_para_fahrenheit(celsius):
    """
    RF01: Converter Celsius para Fahrenheit
    Fórmula: F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32


    def fahrenheit_para_celsius(fahrenheit):
    """
    RF02: Converter Fahrenheit para Celsius
    Fórmula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9



    PROGRAMA PRINCIPAL


    print("="*40)
    print("  CONVERSOR DE TEMPERATURA")
    print("="*40)
    
    print("Escolha a conversão:")
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    
    opcao = input("Opção: ")

    try:
        if opcao == "1":
            temperatura = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(temperatura)
            print("="*40)
            print(f"{temperatura:.1f}°C = {resultado:.1f}°F")

        elif opcao == "2":
            temperatura = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(temperatura)
            print("="*40)
            print(f"{temperatura:.1f}°F = {resultado:.1f}°C")

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: Digite apenas números válidos para a temperatura.")

    print("="*40)

O código implementa uma aplicação prática de lógica de programação voltada à Engenharia de Software, utilizando funções estruturadas para converter escalas termométricas. O exercício reforça o aprendizado sobre a tradução de requisitos funcionais (RF01 e RF02) em algoritmos e a importância do tratamento de erros (try/except) para garantir a robustez do software.

#### 🖥️ Execução

<img width="567" height="288" alt="Aula2 - output" src="https://github.com/user-attachments/assets/bd845c68-2206-4583-8c7f-daed34199fa9" />

O output exibe uma interface textual (CLI) clara e organizada, que guia o usuário na escolha da conversão e apresenta o resultado formatado com precisão de uma casa decimal.

### Aula 03 - Requisitos Funcionais vs. Não-Funcionais

#### 💻 Código

'''

    import time

    print("🏋️ GymTrack — Validador de Treino")
    print("=" * 40)
  
    DADOS DO TREINO (mude os valores para testar!)
    exercicio = "Supino Reto"
    peso_kg  = 80
    repeticoes = 10


    RF01 — O sistema deve validar o nome do exercício
    (não pode ser vazio)
    
    if exercicio != "":
        print(f"✅ [RF01] Exercício válido: {exercicio}")
    else:
        print("❌ [RF01] Nome do exercício inválido!")


    RF02 — O peso deve estar entre 1 e 300 kg
    
    if 1 <= peso_kg <= 300:
        print(f"✅ [RF02] Peso válido: {peso_kg}kg")
    else:
        print("❌ [RF02] Peso inválido! Deve estar entre 1 e 300kg")


    RF03 — As repetições devem estar entre 1 e 50
    
    if 1 <= repeticoes <= 50:
        print(f"✅ [RF03] Repetições válidas: {repeticoes}")
    else:
        print("❌ [RF03] Número de repetições inválido! Deve estar entre 1 e 50")
    
    
    RNF01 — O registro deve ocorrer em menos de 200ms

    inicio = time.time()
    
    Simula o registro no banco de dados
    time.sleep(0.05)
    
    print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")
    
    fim = time.time()
    tempo_ms = (fim - inicio) * 1000
    
    if tempo_ms < 200:
        print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
    else:
        print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")

Este código Python implementa um **validador de lógica para registros de academia**, utilizando estruturas condicionais (`if/else`) para verificar Requisitos Funcionais (regras de negócio como limites de peso e repetições) e a biblioteca `time` para medir um Requisito Não Funcional (performance). Com ele, aprendi a transformar critérios técnicos em validações de código e a monitorar o tempo de execução para garantir a eficiência do sistema.

#### 🖥️ Execução

<img width="567" height="147" alt="Aula3 - Output" src="https://github.com/user-attachments/assets/9c74c540-013e-41b3-87a3-7594b0d4a004" />

O output apresenta o status de cada validação em tempo real, utilizando ícones visuais para confirmar que os dados inseridos e a performance do sistema atendem aos critérios estabelecidos. Ele demonstra uma execução bem-sucedida, onde o treino foi validado e registrado dentro do limite de tempo de 200ms.

### Aula 04 - Documento de Especificação de Requisitos de Software (SRS)

#### 💻 Código - Parte 1

'''

    from dataclasses import dataclass, field
    from typing import List
    from enum import Enum
    
    class Prioridade(Enum):
        ALTA = "Alta"
        MEDIA = "Média"
        BAIXA = "Baixa"
    
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
        categoria: str  # Desempenho, Segurança, Usabilidade...
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
            print(f"✅ RF '{req.id}' adicionado!")
    
        def adicionar_rnf(self, req: RequisitoNaoFuncional):
            self.requisitos_nao_funcionais.append(req)
            print(f"✅ RNF '{req.id}' adicionado!")
    
        def relatorio(self):
            print(f"\n{'='*50}")
            print(f"📋 SRS — {self.projeto} v{self.versao}")
            print(f"{'='*50}")
            print(f"📝 {self.descricao}\n")
    
            print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
            for rf in self.requisitos_funcionais:
                print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
                print(f"       Ator: {rf.ator}")
                print(f"       📌 {rf.descricao}\n")
    
            print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
            for rnf in self.requisitos_nao_funcionais:
                print(f"  [{rnf.id}] {rnf.categoria}")
                print(f"       📌 {rnf.descricao}")
                print(f"       ✔️  Critério: {rnf.criterio_aceitacao}\n")

    Criando o SRS do App de Delivery
    srs = SRS(
        projeto="App de Delivery — Módulo Rastreamento",
        versao="1.0",
        descricao="Sistema de rastreamento em tempo real de entregadores."
    )
    
    srs.adicionar_rf(RequisitoFuncional(
        id="RF-001",
        nome="Rastreamento em Tempo Real",
        descricao="Exibir posição do entregador no mapa atualizada a cada 3 segundos.",
        prioridade=Prioridade.ALTA,
        ator="Cliente",
        pre_condicao="Pedido com status 'Em rota'",
        pos_condicao="Cliente visualiza localização atual do entregador"
    ))
    
    srs.adicionar_rf(RequisitoFuncional(
        id="RF-002",
        nome="Notificação de Status",
        descricao="Enviar push notification ao cliente quando status do pedido mudar.",
        prioridade=Prioridade.ALTA,
        ator="Sistema",
        pre_condicao="Cliente com notificações habilitadas",
        pos_condicao="Cliente notificado sobre mudança de status"
    ))
    
    srs.adicionar_rnf(RequisitoNaoFuncional(
        id="RNF-001",
        categoria="Desempenho",
        descricao="O sistema deve suportar 50.000 usuários simultâneos.",
        criterio_aceitacao="Teste de carga com JMeter: 50k req/s com latência < 500ms"
    ))
    
    srs.adicionar_rnf(RequisitoNaoFuncional(
        id="RNF-002",
        categoria="Segurança",
        descricao="Dados de localização devem ser criptografados em trânsito.",
        criterio_aceitacao="Uso de TLS 1.3 validado por ferramenta de auditoria"
    ))
    
    srs.relatorio()

Este código implementa uma estrutura automatizada para a Especificação de Requisitos de Software (SRS) utilizando Programação Orientada a Objetos em Python. Ele organiza requisitos funcionais e não-funcionais em objetos estruturados, permitindo a validação de atributos essenciais como critérios de aceitação, prioridade e atores.

#### 🖥️ Execução - Parte 1

<img width="567" height="493" alt="Aula4 - Output1" src="https://github.com/user-attachments/assets/4416b247-dad0-4566-b345-446d2ca76320" />

O output exibe um **relatório consolidado e estruturado**, que organiza visualmente os detalhes técnicos de cada requisito (como atores, descrições e critérios de aceite), facilitando a leitura e a auditoria do escopo do projeto.

#### 💻 Código - Parte 2

'''

    from dataclasses import dataclass, field
    from typing import List
    from enum import Enum
    
    ENUM DE PRIORIDADE
    
    class Prioridade(Enum):
        ALTA = "Alta"
        MEDIA = "Média"
        BAIXA = "Baixa"
    
    CLASSES
    
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
    
    PARTE 2 — VALIDAÇÃO
    
    def validar_requisito(rf: RequisitoFuncional) -> dict:
        resultados = {}
    
        # ✔ Descrição > 20 caracteres
        resultados["descricao_valida"] = len(rf.descricao) > 20
    
        # ✔ Pré-condição não vazia
        resultados["pre_condicao_valida"] = rf.pre_condicao.strip() != ""
    
        # ✔ Possui número (critério mensurável)
        resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.descricao)
    
        return resultados
    
    PARTE 1 — FIAP MARKETPLACE
    
    srs = SRS(
        projeto="FIAP Marketplace",
        versao="1.0",
        descricao="Marketplace interno para alunos venderem produtos artesanais entre si."
    )
    
    🔧 RF
    
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
    
    ⚡ RNF
    
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
    
    RELATÓRIO
    
    srs.relatorio()
    
    TESTE DA VALIDAÇÃO
    
    print("\n🔍 VALIDAÇÃO DOS REQUISITOS FUNCIONAIS\n")
    
    for rf in srs.requisitos_funcionais:
        print(f"{rf.id} - {rf.nome}")
        print(validar_requisito(rf))
        print("-" * 50)

Através da função de validação, aprendi a aplicar regras de qualidade sobre as definições de software, garantindo que os requisitos sejam detalhados, mensuráveis e possuam pré-condições claras antes de seguirem para o desenvolvimento.

#### 🖥️ Execução - Parte 2

<img width="567" height="177" alt="Aula4 - Output2" src="https://github.com/user-attachments/assets/1483fa9a-e629-42ae-bc3b-800051d90572" />

O output demonstra que todos os requisitos do **FIAP Marketplace** foram aprovados nos critérios de qualidade, apresentando descrições detalhadas e métricas de tempo (ex: 3s, 5s) que os tornam tecnicamente testáveis. Ele fornece um relatório limpo e estruturado, ideal para uma revisão rápida entre a equipe de produto e os desenvolvedores.

### Aula 05 - Introdução à UML e Diagramas de Casos de Uso

####  📐 Diagrama

 <img width="1536" height="1024" alt="Aula05 - Diagrama" src="https://github.com/user-attachments/assets/ca616077-798d-4529-945d-8870d5171742" />

 Este diagrama de Casos de Uso ilustra as interações entre os atores (**Leitor**, **Bibliotecário** e **Sistema de Pagamento**) e as funcionalidades centrais de um **Sistema de Biblioteca Digital**. A modelagem destaca que o empréstimo obrigatoriamente inclui a verificação de disponibilidade, enquanto a aplicação de multas é tratada como uma extensão condicional (opcional) nos processos de devolução e renovação.

 #### 💻 Código

 '''

    catalogo = [
        {"titulo": "Clean Code", "autor": "Robert C. Martin", "disponivel": True},
        {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas", "disponivel": True},
        {"titulo": "Design Patterns", "autor": "Gang of Four", "disponivel": True},
    ]
    
    emprestimos = []
    
    UC-01: LISTAR CATÁLOGO
    
    print("📚 Catálogo disponível:")
    for livro in catalogo:
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} {livro['titulo']} — {livro['autor']}")
    
    UC-02: BUSCAR LIVRO
    
    print("\n🔍 Buscando livro...")
    busca = "clean"
    
    encontrados = False
    for livro in catalogo:
        if busca.lower() in livro["titulo"].lower():
            print(f"📘 {livro['titulo']} — {livro['autor']}")
            encontrados = True
    
    if not encontrados:
        print("❌ Nenhum livro encontrado.")
    
    UC-03: EMPRESTAR LIVRO
    
    print("\n📌 Empréstimo:")
    leitor = "Ana Silva"
    titulo = "Clean Code"
    
    livro_encontrado = None
    for livro in catalogo:
        if livro["titulo"] == titulo:
            livro_encontrado = livro
            break
    
    if livro_encontrado is None:
        print("❌ Livro não encontrado no catálogo.")
    elif livro_encontrado["disponivel"] == False:
        print(f"⚠️  '{titulo}' já está emprestado!")
    else:
        livro_encontrado["disponivel"] = False
        emprestimos.append({"leitor": leitor, "livro": titulo})
        print(f"✅ '{titulo}' emprestado para {leitor}!")
    
    UC-04: DEVOLVER LIVRO
    
    print("\n🔄 Devolução:")
    leitor_devolvendo = "Ana Silva"
    titulo_devolvendo = "Clean Code"
    
    registro_encontrado = None
    
    for registro in emprestimos:
        if registro["leitor"] == leitor_devolvendo and registro["livro"] == titulo_devolvendo:
            registro_encontrado = registro
            break
    
    if registro_encontrado:
        # marcar como disponível
        for livro in catalogo:
            if livro["titulo"] == titulo_devolvendo:
                livro["disponivel"] = True
                break
    
        # remover empréstimo
        emprestimos.remove(registro_encontrado)
    
        print(f"✅ '{titulo_devolvendo}' devolvido com sucesso!")
    
        # <> aplicar multa
        atraso = input("Houve atraso? (s/n): ").lower()
        if atraso == "s":
            print("📋 Multa aplicada!")
    else:
        print("❌ Empréstimo não encontrado.")
    
    ESTADO FINAL
    
    print("\n📖 Catálogo após operações:")
    for livro in catalogo:
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} {livro['titulo']}")
    
    print(f"\n📋 Empréstimos ativos: {emprestimos}")

O código implementa um sistema básico de gerenciamento de biblioteca em Python, cobrindo o ciclo de vida de um livro: listagem, busca por palavra-chave, controle de disponibilidade e registro de empréstimos/devoluções.

#### 🖥️ Execução

<img width="567" height="316" alt="Aula5 - Output" src="https://github.com/user-attachments/assets/979dd33e-90fe-44d4-9dad-0ac5b0807a4c" />

O output demonstra a execução fluida dos casos de uso, confirmando que a alteração de estado do livro (**disponível vs. ocupado**) reflete corretamente no inventário após as operações de empréstimo e devolução. Ele valida visualmente a integridade dos dados, garantindo que a lógica de busca e as mensagens de confirmação ao usuário estejam funcionando conforme o esperado.

### Aula 06 - Diagramas de Atividades para Processos de Negócio

#### 📐 Diagrama

<img width="1536" height="1024" alt="Aula6 - Diagrama" src="https://github.com/user-attachments/assets/9dd82cc0-028d-40b3-bc24-3e81cd824156" />

Este diagrama de atividades ilustra o fluxo de **cadastro e aprovação de novos usuários**, separando claramente as responsabilidades entre o cliente e o sistema através de *swimlanes*. A modelagem prioriza a **segurança e integridade dos dados** ao incluir verificações críticas de validação de e-mail e duplicidade de conta, condicionando a liberação do acesso à confirmação obrigatória via e-mail.

#### 💻 Código

'''
    
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
    
    Testes (não apague!)
    print(cadastro_usuario("joao@email.com", "senha123", False, True))
    print(cadastro_usuario("email-invalido", "senha123", False, True))
    print(cadastro_usuario("joao@email.com", "senha123", True, True))

Este código implementa uma lógica de **fluxo de cadastro de usuários**, integrando validação de formato de e-mail, verificação de duplicidade no banco de dados e controle de confirmação de conta. Através dele, pratiquei o uso de **condicionais aninhadas** para gerenciar diferentes estados do sistema e a importância de validar entradas antes de processar regras de negócio.

#### 🖥️ Execução

<img width="567" height="91" alt="Aula6 - Output" src="https://github.com/user-attachments/assets/52d9834c-3030-4cf5-a858-67e87698e7d9" />

O output demonstra o tratamento de diferentes cenários: primeiro o **sucesso** completo do fluxo, seguido pela interrupção por **erro de formato** (regex) e, por fim, o bloqueio por **e-mail duplicado**. Isso confirma que as validações estão funcionando como barreiras de segurança sequenciais antes da liberação do acesso.

### Aula 07 - Diagramas de Sequência: Interação entre Objetos

#### 📐 Diagrama

<img width="1536" height="1024" alt="Aula7 - Diagrama" src="https://github.com/user-attachments/assets/86e80983-3324-4ab0-b1a3-da9ad48491c8" />

Este diagrama de sequência detalha o fluxo de uma transferência bancária no ecossistema do Nubank, destacando a interação entre o usuário, o aplicativo e o backend. A modelagem utiliza um fragmento **"alt"** para tratar de forma lógica as ramificações do processo (sucesso ou falha por saldo insuficiente) e separa claramente as responsabilidades de validação lógica no servidor e persistência de dados no banco.

#### 💻 Código

'''

    Célula 1 — BancoDeDados
    class BancoDeDados:
        def __init__(self):
            # Criando o dicionário de saldos
            self.saldos = {
                "user_123": 500.0
            }
    
        def verificar_saldo(self, user_id: str) -> float:
            return self.saldos.get(user_id, 0.0)
    
        def debitar(self, user_id: str, valor: float) -> bool:
            saldo_atual = self.verificar_saldo(user_id)
    
            if saldo_atual >= valor:
                self.saldos[user_id] -= valor
                return True
            else:
                return False
    
    
    Célula 2 — ServidorNubank
    class ServidorNubank:
        def __init__(self):
            self.banco = BancoDeDados()
    
        def processar_transferencia(self, user_id: str, valor: float) -> dict:
            saldo = self.banco.verificar_saldo(user_id)
    
            if saldo >= valor:
                self.banco.debitar(user_id, valor)
                saldo_restante = self.banco.verificar_saldo(user_id)
    
                return {
                    "status": "aprovado",
                    "saldo_restante": saldo_restante
                }
            else:
                return {
                    "status": "recusado",
                    "motivo": "saldo insuficiente"
                }
    
    
    Célula 3 — AppNubank
    class AppNubank:
        def __init__(self):
            self.servidor = ServidorNubank()
    
        def transferir(self, user_id: str, valor: float):
            print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")
    
            resultado = self.servidor.processar_transferencia(user_id, valor)
    
            if resultado["status"] == "aprovado":
                print(f"[APP] ✅ Transferência aprovada! Saldo: R$ {resultado['saldo_restante']:.2f}")
            else:
                print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")
    
    
    Célula 4 — Testes
    app = AppNubank()
    
    print("=== Teste 1: Transferência dentro do saldo ===")
    app.transferir("user_123", 200.0)
    
    print("\n=== Teste 2: Transferência acima do saldo ===")
    app.transferir("user_123", 500.0)
    
    print("\n=== Teste 3: Múltiplas transferências ===")
    app.transferir("user_123", 100.0)
    app.transferir("user_123", 250.0)

O código acima implementa um sistema de transferência bancária simplificado utilizando o paradigma de Programação Orientada a Objetos (POO). Ele simula a interação real entre diferentes camadas de um software: a interface (App), a lógica de negócio (Servidor) e o armazenamento de dados (Banco de Dados).

#### 🖥️ Execução

<img width="567" height="198" alt="Aula7 - Output" src="https://github.com/user-attachments/assets/ae8f958d-51c9-4036-a54e-ec33a63157c1" />

O output demonstra o controle de fluxo do sistema, exibindo o sucesso das transferências quando há fundos e o bloqueio automático ("recusado") quando o saldo se torna insuficiente. Ele valida a persistência do estado do objeto `BancoDeDados`, que mantém o saldo atualizado após cada operação bem-sucedida.

### Aula 08 - Diagramas de Classes: Estrutura, Relacionamentos, Atributos, Métodos e Conexões

#### 📐 Diagrama

<img width="1536" height="1024" alt="Aula8 - Diagrama" src="https://github.com/user-attachments/assets/a7a73adf-2d64-49ba-b25b-2860ed0719bb" />

Este diagrama de classes representa a estrutura de um **Sistema de Streaming**, organizando a hierarquia entre plataformas, catálogos e filmes. As decisões de modelagem destacam o uso de **composição** para indicar dependência existencial (como avaliações que pertencem exclusivamente a um usuário) e **agregação** para relações independentes, onde filmes podem existir independentemente de estarem em um catálogo específico.

#### 💻 Código

'''

    class Filme:
        def __init__(self, titulo, duracao, genero):
            self.titulo = titulo
            self.duracao = duracao
            self.genero = genero
    
        def __str__(self):
            return f"{self.titulo} ({self.genero}) - {self.duracao} min"
    
    
    class Avaliacao:
        def __init__(self, nota, comentario):
            self.nota = nota
            self.comentario = comentario
            self.filme = None
    
        def associar_filme(self, filme):
            self.filme = filme
    
    
    class Usuario:
        def __init__(self, nome, email, plano):
            self.nome = nome
            self.email = email
            self.plano = plano
            self.avaliacoes = []
    
        def avaliar(self, filme, avaliacao):
            avaliacao.associar_filme(filme)
            self.avaliacoes.append(avaliacao)
    
        def ver_avaliacoes(self):
            print(f"\nAvaliações de {self.nome}:")
            for av in self.avaliacoes:
                print(f"- {av.filme.titulo}: Nota {av.nota} | {av.comentario}")
    
    
    class Catalogo:
        def __init__(self, titulo, qtdFilmes):
            self.titulo = titulo
            self.qtdFilmes = qtdFilmes
            self.filmes = []
    
        def add_filme(self, filme):
            self.filmes.append(filme)
            self.qtdFilmes += 1
    
        def listar_filmes(self):
            print(f"\nCatálogo: {self.titulo}")
            for filme in self.filmes:
                print(f"- {filme}")
    
    
    class Plataforma:
        def __init__(self, nome, pais):
            self.nome = nome
            self.pais = pais
            self.catalogos = []
    
        def add_catalogo(self, catalogo):
            self.catalogos.append(catalogo)
    
    
    TESTE 
    
    netflix = Plataforma("Netflix", "EUA")
    
    catalogo = Catalogo("Filmes em Destaque", 0)
    
    filme1 = Filme("Oppenheimer", 180, "Drama")
    filme2 = Filme("Barbie", 114, "Comédia")
    
    catalogo.add_filme(filme1)
    catalogo.add_filme(filme2)
    
    netflix.add_catalogo(catalogo)
    
    usuario = Usuario("Ana", "ana@email.com", "Premium")
    
    avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")
    
    usuario.avaliar(filme1, avaliacao)
    
    catalogo.listar_filmes()
    usuario.ver_avaliacoes()

Este código implementa um sistema básico de gerenciamento de streaming, estruturando a interação entre **Plataforma**, **Catálogo**, **Filme** e **Usuário** através de Programação Orientada a Objetos.

O que o código implementa: O script simula o fluxo real de uma plataforma: organiza filmes dentro de catálogos temáticos e permite que usuários registrem avaliações (notas e comentários) vinculadas a títulos específicos, mantendo um histórico pessoal de interações.

O que foi aprendido:
* **Associação entre Classes:** Demonstra como objetos de classes diferentes (como `Avaliacao` e `Filme`) se relacionam para compor um sistema mais complexo.
* **Gerenciamento de Coleções:** O uso de listas para armazenar dinamicamente objetos dentro de outros objetos (catálogos e listas de avaliações).
* **Métodos Especiais:** A utilização do método `__str__` para personalizar a representação textual dos objetos, facilitando a exibição de dados para o usuário final.

#### 🖥️ Execução

<img width="567" height="119" alt="Aula8 - Output" src="https://github.com/user-attachments/assets/c2808924-607b-43c6-8938-06ca17f3b7fb" />

O output exibe a lista detalhada dos filmes presentes no catálogo e, em seguida, as avaliações personalizadas do usuário, comprovando que os objetos foram vinculados corretamente entre si. Ele demonstra a execução bem-sucedida da lógica de armazenamento e recuperação de dados formatados do sistema.

### Aula 09 - Arquitetura de Software: Introdução a Camadas e MVC

#### 📐 Diagrama

<img width="1135" height="613" alt="Aula9 - Diagrama1" src="https://github.com/user-attachments/assets/7c54ccc4-e5cc-4705-a595-b7709711a489" />

O diagrama ilustra a arquitetura em camadas de um sistema de lista de tarefas, utilizando o padrão **MVC** dentro da camada de apresentação para gerenciar a interface. A modelagem destaca a separação de responsabilidades, onde o fluxo percorre desde a interação do usuário na **View** até a persistência na **Camada de Dados**, garantindo que a lógica de negócio esteja isolada e o estado seja sincronizado via notificações do **Model**.

#### Figma

<img width="1901" height="846" alt="Aula9 - Figma" src="https://github.com/user-attachments/assets/76c63de9-9b90-4715-8441-a4b5ca6a12b4" />

O diagrama apresenta o **fluxo de navegação** de um aplicativo de lista de tarefas, conectando a visualização principal à tela de criação. As decisões de modelagem focam na **simplicidade da experiência do usuário**, utilizando um botão de ação flutuante (FAB) para adição e um fluxo de retorno direto após o salvamento, garantindo uma interação cíclica e intuitiva.


