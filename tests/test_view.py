import pytest
from unittest.mock import patch
from src.view import AgendamentoView


@pytest.fixture
def mock_agendamentos():
    return [
        {
            "data": "2024-12-01",
            "hora": "14:00",
            "aluno": "João Silva",
            "professor": "Maria Oliveira",
            "descricao": "Aula de reforço"
        },
        {
            "data": "2024-12-02",
            "hora": "10:00",
            "aluno": "Ana Souza",
            "professor": "Carlos Santos",
            "descricao": "Reunião com pais"
        }
    ]


def test_exibir_mensagem(capsys):
    mensagem = "Teste de exibição de mensagem"
    AgendamentoView.exibir_mensagem(mensagem)
    captured = capsys.readouterr()
    assert captured.out.strip() == mensagem


def test_exibir_agendamentos_vazio(capsys):
    AgendamentoView.exibir_agendamentos([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Não há agendamentos no sistema."


def test_exibir_agendamentos(mock_agendamentos, capsys):
    AgendamentoView.exibir_agendamentos(mock_agendamentos)
    captured = capsys.readouterr()
    esperado = (
        "2024-12-01 às 14:00 com professor Maria Oliveira "
        "- aluno João Silva - Aula de reforço\n"
        "2024-12-02 às 10:00 com professor Carlos Santos "
        "- aluno Ana Souza - Reunião com pais"
    )
    assert captured.out.strip() == esperado


@patch("builtins.input", side_effect=["João Silva",
                                      "Maria Oliveira",
                                      "2024-12-01",
                                      "14:00",
                                      "Aula de reforço"])
def test_obter_dados_agendamento(mock_input):
    esperado = ("2024-12-01", "14:00", "João Silva",
                "Maria Oliveira", "Aula de reforço")
    resultado = AgendamentoView.obter_dados_agendamento()
    assert resultado == esperado


@patch("builtins.input", side_effect=["João Silva",
                                      "Maria Oliveira",
                                      "2024-12-01",
                                      "14:00"])
def test_obter_dados_remocao(mock_input):
    esperado = ("2024-12-01", "14:00", "João Silva", "Maria Oliveira")
    resultado = AgendamentoView.obter_dados_remocao()
    assert resultado == esperado
