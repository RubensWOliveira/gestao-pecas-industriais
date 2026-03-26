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
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append(f"Peso fora do padrão ({peso}g)")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append(f"Cor inválida ({cor})")

    if comprimento < 10 or comprimento > 20:
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm)")

    if len(motivos) == 0:
        return "aprovada", []
    else:
        return "reprovada", motivos


# --- FUNÇÃO: CADASTRAR NOVA PEÇA ---
def cadastrar_peca():
    print("\n" + "-"*45)
    print("        CADASTRO DE NOVA PEÇA")
    print("-"*45)

    id_peca = input("  ID da peça: ").strip()

    try:
        peso = float(input("  Peso (g): "))
        comprimento = float(input("  Comprimento (cm): "))
    except ValueError:
        print("\n  ⚠️  Peso e comprimento devem ser números!")
        return

    cor = input("  Cor: ").strip()

    status, motivos = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    pecas.append(peca)

    if status == "aprovada":
        caixa_atual.append(peca)
        print(f"\n  ✅ Peça {id_peca} APROVADA!")
        print(f"  📦 Posição na caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")

        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas.append(list(caixa_atual))
            caixa_atual.clear()
            print(f"\n  📦 Caixa {len(caixas)} fechada! Nova caixa iniciada.")
    else:
        print(f"\n  ❌ Peça {id_peca} REPROVADA!")
        for motivo in motivos:
            print(f"     → {motivo}")


# --- FUNÇÃO: LISTAR PEÇAS ---
def listar_pecas():
    print("\n" + "-"*45)
    print("         LISTA DE PEÇAS CADASTRADAS")
    print("-"*45)

    # Verifica se há peças cadastradas
    if len(pecas) == 0:
        print("  Nenhuma peça cadastrada ainda.")
        return

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    # Mostra peças aprovadas
    print(f"\n  ✅ APROVADAS ({len(aprovadas)}):")
    if len(aprovadas) == 0:
        print("     Nenhuma peça aprovada.")
    else:
        for p in aprovadas:
            print(f"     → ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")

    # Mostra peças reprovadas
    print(f"\n  ❌ REPROVADAS ({len(reprovadas)}):")
    if len(reprovadas) == 0:
        print("     Nenhuma peça reprovada.")
    else:
        for p in reprovadas:
            print(f"     → ID: {p['id']} | Motivo(s): {', '.join(p['motivos'])}")


# --- FUNÇÃO: REMOVER PEÇA ---
def remover_peca():
    print("\n" + "-"*45)
    print("         REMOVER PEÇA CADASTRADA")
    print("-"*45)

    if len(pecas) == 0:
        print("  Nenhuma peça cadastrada para remover.")
        return

    id_remover = input("  Digite o ID da peça a remover: ").strip()

    # Procura a peça na lista
    peca_encontrada = None
    for p in pecas:
        if p["id"] == id_remover:
            peca_encontrada = p
            break

    if peca_encontrada is None:
        print(f"\n  ⚠️  Peça com ID '{id_remover}' não encontrada.")
        return

    # Remove da lista de peças
    pecas.remove(peca_encontrada)

    # Se era aprovada, remove da caixa atual também
    if peca_encontrada in caixa_atual:
        caixa_atual.remove(peca_encontrada)

    print(f"\n  🗑️  Peça {id_remover} removida com sucesso!")


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
            listar_pecas()
        elif opcao == "3":
            remover_peca()
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