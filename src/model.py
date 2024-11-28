from typing import List, Dict, Optional


class AgendamentoModel:
    def __init__(self):
        self.agendamentos: List[Dict[str, str]] = []

    def adicionar_agendamento(self, data: str,
                              hora: str, aluno: str,
                              professor: str,
                              descricao: str) \
            -> Dict[str, str]:
        agendamento = {
            "data": data,
            "hora": hora,
            "aluno": aluno,
            "professor": professor,
            "descricao": descricao
        }
        self.agendamentos.append(agendamento)
        return agendamento

    def listar_agendamentos(self) -> List[Dict[str, str]]:
        return self.agendamentos

    def remover_agendamento(self, data: str, hora: str,
                            aluno: str = "",
                            professor: str = "")\
            -> Optional[Dict[str, str]]:
        for agendamento in self.agendamentos[:]:
            if (
                agendamento["aluno"].upper() == aluno.upper() and
                agendamento["professor"].upper() == professor.upper() and
                agendamento["data"].upper() == data.upper() and
                agendamento["hora"].upper() == hora.upper()
            ):
                self.agendamentos.remove(agendamento)
                return agendamento
        return None
