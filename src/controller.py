from model import AgendamentoModel
from view import AgendamentoView


class AgendamentoController:
    def __init__(self, model: 'AgendamentoModel',
                 view: 'AgendamentoView') -> None:
        self.model = model
        self.view = view

    def adicionar_agendamento(self) -> None:
        data, hora, aluno, professor, descricao = \
            self.view.obter_dados_agendamento()
        self.model.adicionar_agendamento(
            data, hora, aluno, professor, descricao)
        self.view.exibir_mensagem(
            f"Agendamento de {aluno} para {data} às {hora} "
            f"com {professor} adicionado com sucesso!"
        )

    def listar_agendamentos(self) -> None:
        agendamentos = self.model.listar_agendamentos()
        self.view.exibir_agendamentos(agendamentos)

    def remover_agendamento(self) -> None:
        data, hora, aluno, professor = self.view.obter_dados_remocao()
        agendamento = self.model.remover_agendamento(
            data, hora, aluno, professor)
        if agendamento:
            self.view.exibir_mensagem(
                f"Agendamento de {aluno} para {data} às {hora} "
                f"com {professor} removido com sucesso!"
            )
        else:
            self.view.exibir_mensagem("Agendamento não encontrado.")

    def iniciar_menu(self) -> None:
        while True:
            print("\nSistema de Agendamento")
            print("1 - Adicionar agendamento")
            print("2 - Listar agendamentos")
            print("3 - Remover agendamento")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_agendamento()
            elif opcao == "2":
                self.listar_agendamentos()
            elif opcao == "3":
                self.remover_agendamento()
            elif opcao == "4":
                self.view.exibir_mensagem("Saindo do sistema...")
                break
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.")
