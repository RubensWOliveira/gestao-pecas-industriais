# ============================================================
# SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAIS
# Disciplina: Algoritmos e Lógica de Programação
# ============================================================

# --- ESTRUTURAS DE DADOS ---
# Lista que guarda todas as peças cadastradas
pecas = []

# Lista que guarda as caixas fechadas
caixas = []

# Caixa atual que está sendo preenchida
caixa_atual = []

# Capacidade máxima de peças por caixa
CAPACIDADE_CAIXA = 10


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
            print("\n[Em breve] Cadastrar peça...")
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