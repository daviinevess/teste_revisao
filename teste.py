#Aqui vou desenvolver meu cógigo de teste para a revisão.

# cadastro_motores.py
# Protótipo monolítico para cadastro de motores em memória (apenas para teste)

motores = []
proximo_id = 1


def cadastrar_motor(codigo: str, modelo: str, fabricante: str, potencia_cv: float, tensao_v: int, rpm: int) -> dict:
    """Cadastra um novo motor na lista em memória e retorna o registro criado."""
    global proximo_id

    for motor in motores:
        if motor["codigo"].lower() == codigo.strip().lower():
            raise ValueError(f"Já existe um motor cadastrado com o código '{codigo}'.")

    if potencia_cv <= 0 or tensao_v <= 0 or rpm <= 0:
        raise ValueError("Potência, tensão e RPM devem ser maiores que zero.")

    novo_motor = {
        "id": proximo_id,
        "codigo": codigo.strip(),
        "modelo": modelo.strip(),
        "fabricante": fabricante.strip(),
        "potencia_cv": float(potencia_cv),
        "tensao_v": int(tensao_v),
        "rpm": int(rpm),
        "status": "ativo",
    }

    motores.append(novo_motor)
    proximo_id += 1
    return novo_motor


def listar_motores() -> list[dict]:
    """Retorna todos os motores cadastrados."""
    return motores


def buscar_motor(termo: str) -> list[dict]:
    """Busca motores por ID, código, modelo ou fabricante."""
    termo_limpo = termo.strip().lower()
    resultados = []

    for motor in motores:
        if (
            str(motor["id"]) == termo_limpo
            or termo_limpo in motor["codigo"].lower()
            or termo_limpo in motor["modelo"].lower()
            or termo_limpo in motor["fabricante"].lower()
        ):
            resultados.append(motor)

    return resultados


def atualizar_status_motor(motor_id: int, novo_status: str) -> dict | None:
    """Atualiza o status de um motor (ex.: 'ativo', 'manutencao', 'inativo')."""
    status_validos = {"ativo", "manutencao", "inativo"}
    status_formatado = novo_status.strip().lower()

    if status_formatado not in status_validos:
        raise ValueError(f"Status inválido. Use um de: {', '.join(sorted(status_validos))}.")

    for motor in motores:
        if motor["id"] == motor_id:
            motor["status"] = status_formatado
            return motor

    return None


def remover_motor(motor_id: int) -> bool:
    """Remove um motor pelo ID. Retorna True se removido ou False se não encontrado."""
    for i, motor in enumerate(motores):
        if motor["id"] == motor_id:
            motores.pop(i)
            return True
    return False


def exibir_motores(lista: list[dict]) -> None:
    """Imprime os motores de forma legível no terminal."""
    if not lista:
        print("Nenhum motor encontrado.")
        return

    for m in lista:
        print(
            f"[ID {m['id']}] Código: {m['codigo']} | Modelo: {m['modelo']} | "
            f"Fabricante: {m['fabricante']} | {m['potencia_cv']} CV | "
            f"{m['tensao_v']}V | {m['rpm']} RPM | Status: {m['status']}"
        )


def menu_interativo() -> None:
    """Loop simples via terminal para testar o cadastro."""
    while True:
        print("\n=== CADASTRO DE MOTORES (TESTE) ===")
        print("1 - Cadastrar motor")
        print("2 - Listar motores")
        print("3 - Buscar motor")
        print("4 - Alterar status")
        print("5 - Remover motor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                codigo = input("Código: ")
                modelo = input("Modelo: ")
                fabricante = input("Fabricante: ")
                potencia_cv = float(input("Potência (CV): "))
                tensao_v = int(input("Tensão (V): "))
                rpm = int(input("RPM: "))

                criado = cadastrar_motor(codigo, modelo, fabricante, potencia_cv, tensao_v, rpm)
                print(f"Motor cadastrado com sucesso! ID: {criado['id']}")

            elif opcao == "2":
                exibir_motores(listar_motores())

            elif opcao == "3":
                termo = input("Digite ID, código, modelo ou fabricante: ")
                exibir_motores(buscar_motor(termo))

            elif opcao == "4":
                motor_id = int(input("ID do motor: "))
                novo_status = input("Novo status (ativo / manutencao / inativo): ")
                atualizado = atualizar_status_motor(motor_id, novo_status)
                if atualizado:
                    print("Status atualizado com sucesso.")
                else:
                    print("Motor não encontrado.")

            elif opcao == "5":
                motor_id = int(input("ID do motor para remover: "))
                if remover_motor(motor_id):
                    print("Motor removido.")
                else:
                    print("Motor não encontrado.")

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")

        except ValueError as erro:
            print(f"Erro de validação: {erro}")


if __name__ == "__main__":
    # Dados iniciais de exemplo para facilitar os testes
    cadastrar_motor("MOT-001", "W22 IR3", "WEG", 15.0, 380, 1760)
    cadastrar_motor("MOT-002", "1LE1", "Siemens", 7.5, 220, 1450)
    menu_interativo()