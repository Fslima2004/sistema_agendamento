import pytest
from src.model import AgendamentoModel


@pytest.fixture
def model():
    return AgendamentoModel()


def test_adicionar_agendamento(model):
    model.adicionar_agendamento("2024-12-01", "10:00", "João",
                                "Prof. Silva", "Reunião")
    assert len(model.agendamentos) == 1
    assert model.agendamentos[0]["aluno"] == "João"


def test_listar_agendamentos_vazio(model):
    assert model.listar_agendamentos() == []


def test_remover_agendamento(model):
    model.adicionar_agendamento("2024-12-01", "10:00", "João",
                                "Prof. Silva",
                                "Reunião")
    removido = model.remover_agendamento("2024-12-01",
                                         "10:00",
                                         "João",
                                         "Prof. Silva")
    assert removido is not None
    assert len(model.agendamentos) == 0
