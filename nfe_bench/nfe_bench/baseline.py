import xml.etree.ElementTree as ET
from pathlib import Path
from .base import NFeParser

class BaselineParser(NFeParser):
    name = "manual-xml (baseline)"
    install_hint = "built-in (ElementTree)"

    def parse(self, xml_path: Path) -> dict:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Remove namespace se houver para facilitar a busca
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]

        inf_nfe = root.find(".//infNFe")
        ide = root.find(".//ide")
        emit = root.find(".//emit")
        dest = root.find(".//dest")
        tot = root.find(".//ICMSTot")

        det_list = root.findall(".//det")

        def get_text(el, path):
            found = el.find(path) if el is not None else None
            return found.text if found is not None else None

        return {
            "chave_acesso": inf_nfe.attrib.get("Id", "").replace("NFe", "") if inf_nfe is not None else None,
            "numero_nfe": get_text(ide, "nNF"),
            "serie": get_text(ide, "serie"),
            "data_emissao": get_text(ide, "dhEmi") or get_text(ide, "dEmi"),
            "cnpj_emitente": get_text(emit, "CNPJ"),
            "nome_emitente": get_text(emit, "xNome"),
            "cpf_destinatario": get_text(dest, "CPF"),
            "cnpj_destinatario": get_text(dest, "CNPJ"),
            "nome_destinatario": get_text(dest, "xNome"),
            "quantidade_itens": len(det_list) if det_list else 0,
            "valor_produtos": float(get_text(tot, "vProd")) if get_text(tot, "vProd") else 0.0,
            "valor_total": float(get_text(tot, "vNF")) if get_text(tot, "vNF") else 0.0,
        }
