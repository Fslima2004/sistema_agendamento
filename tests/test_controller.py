import pytest
from unittest.mock import MagicMock, patch
from src.controller import AgendamentoController


@pytest.fixture
def mock_model():
    """Fixture para o modelo simulado."""
    model = MagicMock()
    model.listar_agendamentos.return_value = [
        {
            "data": "2024-12-01",
            "hora": "14:00",
            "aluno": "João Silva",
            "professor": "Maria Oliveira",
            "descricao": "Aula de reforço"
        }
    ]
    model.remover_agendamento.return_value = True
    return model


@pytest.fixture
def mock_view():
    """Fixture para a view simulada."""
    view = MagicMock()
    return view


@pytest.fixture
def controller(mock_model, mock_view):
    """Fixture para instanciar o controlador com os mocks."""
    return AgendamentoController(mock_model, mock_view)


def test_adicionar_agendamento(controller, mock_model, mock_view):
    """Testa o método adicionar_agendamento."""
    mock_view.obter_dados_agendamento.return_value = (
        "2024-12-01", "14:00", "João Silva",
        "Maria Oliveira", "Aula de reforço"
    )

    controller.adicionar_agendamento()

    mock_model.adicionar_agendamento.assert_called_once_with(
        "2024-12-01", "14:00", "João Silva",
        "Maria Oliveira", "Aula de reforço"
    )
    mock_view.exibir_mensagem.assert_called_once_with(
        "Agendamento de João Silva para 2024-12-01 às 14:00 "
        "com Maria Oliveira adicionado com sucesso!"
    )


def test_listar_agendamentos(controller, mock_model, mock_view):
    """Testa o método listar_agendamentos."""
    controller.listar_agendamentos()

    mock_model.listar_agendamentos.assert_called_once()
    mock_view.exibir_agendamentos.assert_called_once_with(
        mock_model.listar_agendamentos.return_value
    )


def test_remover_agendamento_sucesso(controller, mock_model, mock_view):
    """Testa o método remover_agendamento com sucesso."""
    mock_view.obter_dados_remocao.return_value = (
        "2024-12-01", "14:00", "João Silva", "Maria Oliveira"
    )

    controller.remover_agendamento()

    mock_model.remover_agendamento.assert_called_once_with(
        "2024-12-01", "14:00", "João Silva", "Maria Oliveira"
    )
    mock_view.exibir_mensagem.assert_called_once_with(
        "Agendamento de João Silva para 2024-12-01 às 14:00 "
        "com Maria Oliveira removido com sucesso!"
    )


def test_remover_agendamento_falha(controller, mock_model, mock_view):
    """Testa o método remover_agendamento
    quando o agendamento não é encontrado."""
    mock_model.remover_agendamento.return_value = False
    mock_view.obter_dados_remocao.return_value = (
        "2024-12-01", "14:00", "João Silva", "Maria Oliveira"
    )

    controller.remover_agendamento()

    mock_model.remover_agendamento.assert_called_once_with(
        "2024-12-01", "14:00", "João Silva", "Maria Oliveira"
    )
    mock_view.exibir_mensagem.assert_called_once_with(
        "Agendamento não encontrado.")


@patch("builtins.input", side_effect=["4"])
def test_iniciar_menu_sair(mock_input, controller, mock_view):
    """Testa o método iniciar_menu para a opção de saída."""
    controller.iniciar_menu()
    mock_view.exibir_mensagem.assert_called_once_with("Saindo do sistema...")
