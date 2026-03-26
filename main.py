# ============================================================
# SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAIS
# Disciplina: Algoritmos e Lógica de Programação
# ============================================================

# --- ESTRUTURAS DE DADOS ---
pecas = []
caixas = []
caixa_atual = []
CAPACIDADE_CAIXA = 10


# --- FUNÇÃO: AVALIAR QUALIDADE DA PEÇA ---
def avaliar_peca(peso, cor, comprimento):
    motivos = []  # Lista que vai guardar os motivos de reprovação

    # Verifica o peso
    if peso < 95 or peso > 105:
        motivos.append(f"Peso fora do padrão ({peso}g)")

    # Verifica a cor
    if cor.lower() not in ["azul", "verde"]:
        motivos.append(f"Cor inválida ({cor})")

    # Verifica o comprimento
    if comprimento < 10 or comprimento > 20:
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm)")

    # Se não há motivos de reprovação, a peça foi aprovada
    if len(motivos) == 0:
        return "aprovada", []
    else:
        return "reprovada", motivos


# --- FUNÇÃO: CADASTRAR NOVA PEÇA ---
def cadastrar_peca():
    print("\n" + "-"*45)
    print("        CADASTRO DE NOVA PEÇA")
    print("-"*45)

    # Coleta os dados da peça
    id_peca = input("  ID da peça: ").strip()

    # Garante que peso e comprimento sejam números
    try:
        peso = float(input("  Peso (g): "))
        comprimento = float(input("  Comprimento (cm): "))
    except ValueError:
        print("\n  ⚠️  Peso e comprimento devem ser números!")
        return

    cor = input("  Cor: ").strip()

    # Avalia a peça
    status, motivos = avaliar_peca(peso, cor, comprimento)

    # Monta o dicionário com os dados da peça
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    # Adiciona na lista geral de peças
    pecas.append(peca)

    # Se aprovada, adiciona na caixa atual
    if status == "aprovada":
        caixa_atual.append(peca)
        print(f"\n  ✅ Peça {id_peca} APROVADA!")
        print(f"  📦 Posição na caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")

        # Verifica se a caixa encheu
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas.append(list(caixa_atual))  # Fecha a caixa
            caixa_atual.clear()               # Abre uma nova caixa vazia
            print(f"\n  📦 Caixa {len(caixas)} fechada! Nova caixa iniciada.")
    else:
        print(f"\n  ❌ Peça {id_peca} REPROVADA!")
        for motivo in motivos:
            print(f"     → {motivo}")


# --- FUNÇÃO DO MENU ---
def exibir_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAIS")
    print("="*45)
    print("  1. Cadastrar nova peça")
    print("  2. Listar peças aprovadas/reprovadas")
    print("  3. Remover peça cadastrada")
    print("  4. Listar caixas fechadas")
    print("  5. Gerar relatório final")
    print("  0. Sair")
    print("="*45)


# --- LOOP PRINCIPAL DO PROGRAMA ---
def main():
    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            print("\n[Em breve] Listar peças...")
        elif opcao == "3":
            print("\n[Em breve] Remover peça...")
        elif opcao == "4":
            print("\n[Em breve] Listar caixas...")
        elif opcao == "5":
            print("\n[Em breve] Relatório final...")
        elif opcao == "0":
            print("\n  Encerrando o sistema. Até logo! 👋\n")
            break
        else:
            print("\n  ⚠️  Opção inválida! Tente novamente.")


# --- PONTO DE ENTRADA DO PROGRAMA ---
if __name__ == "__main__":
    main()