from src.controller import AgendamentoController
from src.model import AgendamentoModel
from src.view import AgendamentoView


if __name__ == "__main__":
    model = AgendamentoModel()
    view = AgendamentoView()
    controller = AgendamentoController(model, view)
    controller.iniciar_menu()
