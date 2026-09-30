from abc import ABC, abstractmethod
from pathlib import Path

class NFeParser(ABC):
    """Interface base que todo parser de NF-e/NFC-e/CT-e deve implementar."""
    
    name: str = "base"
    install_hint: str = ""

    @abstractmethod
    def parse(self, xml_path: Path) -> dict:
        """
        Lê o arquivo XML e retorna um dicionário padronizado com os campos:
        - chave_acesso
        - numero_nfe
        - serie
        - data_emissao
        - cnpj_emitente
        - nome_emitente
        - cpf_destinatario
        - cnpj_destinatario
        - nome_destinatario
        - quantidade_itens
        - valor_produtos
        - valor_total
        """
        pass
