# 🏭 Sistema de Gestão de Peças Industriais

> Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação** — UniFECAF

---

## 📋 Sobre o Projeto

Este sistema simula uma solução de automação digital para o controle de qualidade
de peças fabricadas em uma linha de montagem industrial.

O programa avalia automaticamente cada peça cadastrada com base em critérios de
qualidade pré-definidos, armazena as peças aprovadas em caixas e gera relatórios
consolidados da produção.

---

## ✅ Critérios de Qualidade

| Critério | Valor aceito |
|---|---|
| ⚖️ Peso | Entre 95g e 105g |
| 🎨 Cor | Azul ou Verde |
| 📏 Comprimento | Entre 10cm e 20cm |

---

## 🖥️ Funcionalidades

- **1. Cadastrar nova peça** — registra os dados e avalia automaticamente
- **2. Listar peças** — exibe aprovadas e reprovadas com motivos
- **3. Remover peça** — remove uma peça pelo ID
- **4. Listar caixas fechadas** — mostra caixas completas (10 peças cada)
- **5. Gerar relatório final** — exibe totais, motivos e taxa de aprovação

---

## 🚀 Como Rodar o Programa

### Pré-requisitos
- Python 3.x instalado → [python.org](https://www.python.org/downloads/)
- Git instalado → [git-scm.com](https://git-scm.com/)

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/RubensWOliveira/gestao-pecas-industriais.git
```

**2. Entre na pasta do projeto:**
```bash
cd gestao-pecas-industriais
```

**3. Execute o programa:**
```bash
python main.py
```

---

## 💡 Exemplos de Uso

### Cadastrando uma peça APROVADA ✅
```
Escolha uma opção: 1

CADASTRO DE NOVA PEÇA
ID da peça: P001
Peso (g): 100
Comprimento (cm): 15
Cor: azul

✅ Peça P001 APROVADA!
📦 Posição na caixa atual: 1/10
```

### Cadastrando uma peça REPROVADA ❌
```
Escolha uma opção: 1

CADASTRO DE NOVA PEÇA
ID da peça: P002
Peso (g): 200
Comprimento (cm): 5
Cor: vermelha

❌ Peça P002 REPROVADA!
   → Peso fora do padrão (200g)
   → Cor inválida (vermelha)
   → Comprimento fora do padrão (5cm)
```

### Relatório Final 📊
```
RELATÓRIO FINAL
📊 Total de peças cadastradas : 12
✅ Total de peças aprovadas   : 10
❌ Total de peças reprovadas  : 2
📦 Total de caixas utilizadas : 1
📈 Taxa de aprovação: 83.3%
```

---

## 🧠 Lógica do Sistema
```
Programa inicia
      ↓
Exibe menu interativo
      ↓
Usuário escolhe uma opção
      ↓
   [Opção 1] → Coleta dados → Avalia critérios → Aprovada ou Reprovada
                                                        ↓
                                              Aprovada → Adiciona na caixa
                                                        ↓
                                              Caixa cheia? → Fecha e abre nova
      ↓
Volta ao menu (até o usuário sair)
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **Git** — controle de versão
- **GitHub** — hospedagem do repositório

---

## 👨‍💻 Autor

**Rubens W. Oliveira**  
Curso: Análise e Desenvolvimento de Sistemas  
Instituição: UniFECAF  
Disciplina: Algoritmos e Lógica de Programação