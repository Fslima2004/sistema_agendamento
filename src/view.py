from typing import List, Tuple


class AgendamentoView:
    @staticmethod
    def exibir_mensagem(mensagem: str) -> None:
        print(mensagem)

    @staticmethod
    def exibir_agendamentos(agendamentos: List[dict]) -> None:
        if not agendamentos:
            print("Não há agendamentos no sistema.")
        else:
            print("\nAgendamentos ativos: \n")
            for agendamento in agendamentos:
                print(f"{agendamento['data']} às {agendamento['hora']} "
                      f"com professor {agendamento['professor']} "
                      f"- aluno {agendamento['aluno']}"
                      f" - {agendamento['descricao']}")

    @staticmethod
    def obter_dados_agendamento() -> Tuple[str, str, str, str, str]:
        aluno = input("Digite o nome do aluno: ")
        professor = input("Digite o nome do professor: ")
        data = input("Digite a data do agendamento (AAAA-MM-DD): ")
        hora = input("Digite a hora do agendamento (HH:MM): ")
        descricao = input("Digite a descrição do agendamento: ")
        return data, hora, aluno, professor, descricao

    @staticmethod
    def obter_dados_remocao() -> Tuple[str, str, str, str]:
        aluno = input("Digite o nome do aluno para "
                      "remover o agendamento: ")
        professor = input("Digite o nome do professor "
                          "para remover o agendamento: ")
        data = input("Digite a data do agendamento (AAAA-MM-DD): ")
        hora = input("Digite a hora do agendamento (HH:MM): ")
        return data, hora, aluno, professor
