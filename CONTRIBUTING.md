# 🤝 Contribuir para o NF-e Bench

Obrigado pelo teu interesse em contribuir para o **nf-e-bench**! Este projeto é um benchmark aberto para comparar o desempenho, a velocidade e a precisão de diferentes parsers de Notas Fiscais Eletrónicas (NF-e/NFC-e/CT-e) em Python.

## 🚀 Como adicionar um novo Parser

Se quiseres adicionar um novo parser ao benchmark (por exemplo, `pynfe`, `nfelib`, etc.), segue estes passos:

1. Cria um novo ficheiro adapter dentro da pasta `nfe_bench/` (ex: `nfe_bench/meu_parser.py`).
2. Herda a classe base `NFeParser` definida em `nfe_bench/base.py`.
3. Implementa o método `parse(self, xml_path: Path) -> dict` retornando o dicionário padronizado com os campos exigidos.
4. Regista o teu parser no ficheiro `nfe_bench/runner.py` dentro da função `get_parsers()`.
5. Executa os testes localmente e submete um Pull Request com as tuas alterações!

## 📋 Padrões de Código
- Mantém o código limpo e documentado.
- Segue as boas práticas da comunidade Python.
