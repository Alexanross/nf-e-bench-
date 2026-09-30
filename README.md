[README.md](https://github.com/user-attachments/files/32837962/README.md)
# 📊 nfe-bench

> Benchmark open source de parsers de documentos fiscais brasileiros (NF-e, NFC-e, CT-e).

![CI](https://github.com/Alexanross/nf-e-bench-/actions/workflows/benchmark.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Licença](https://img.shields.io/badge/licença-MIT-green)

![Preview do dashboard](docs/dashboard-preview.png)

## Por que existe?

Quem integra NF-e no Brasil escolhe parser **no escuro**. Não existe comparação
pública de precisão e velocidade entre as ferramentas disponíveis. Este repositório
mede isso de forma **reprodutível, automatizada e contínua**.

## Como funciona?

1. **Dataset**: XMLs de NF-e (exemplos públicos e sintéticos) em `data/samples/`
2. **Ground truth**: para cada XML, um `.json` com os valores corretos
3. **Runners**: cada parser implementa a mesma interface (`parse(xml) -> dict`)
4. **Métricas**: acurácia campo a campo + tempo de execução (mediana de N repetições)
5. **CI**: GitHub Actions re-executa o benchmark toda semana e publica os resultados

## 🚀 Quickstart

```bash
git clone https://github.com/Alexanross/nf-e-bench-.git
cd nfe-bench
pip install -e .

# roda o benchmark
python -m nfe_bench.runner

# gera o relatório em Markdown
python scripts/generate_report.py
```

Resultados em `results/results.json` e `results/report.md`.

## 🧩 Como adicionar um parser

1. Instale a lib: `pip install python-nfe` (ou a que for)
2. Crie `nfe_bench/parsers/python_nfe.py`:

```python
from pathlib import Path
from .base import NFeParser

class PythonNFeParser(NFeParser):
    name = "python-nfe"
    install_hint = "pip install python-nfe"

    def parse(self, xml_path: Path) -> dict:
        # extraia e retorne o mesmo conjunto de campos dos demais parsers
        ...
```

3. Registre em `nfe_bench/runner.py` em `available_parsers()`

Campos-padrão extraídos: `chave_acesso`, `numero_nfe`, `serie`, `data_emissao`,
`cnpj_emitente`, `nome_emitente`, `cpf_destinatario`, `cnpj_destinatario`,
`nome_destinatario`, `quantidade_itens`, `valor_produtos`, `valor_total`.

## 🎯 Parsers que queremos incluir

- [ ] [python-nfe](https://github.com/TadaSoftware/PyNFe)
- [ ] [nfelib](https://github.com/erpbrasil/nfelib)
- [ ] [erpbrasil.edoc](https://github.com/erpbrasil/erpbrasil.edoc)
- [ ] Parsers em JS/TS (já pensando no benchmark multilinguagem)
- [ ] O seu! 🙌

## 🗺️ Roadmap

- [x] Estrutura base + parser baseline (ElementTree puro)
- [x] Métricas de acurácia e tempo
- [x] CI semanal no GitHub Actions
- [ ] Adapters para as libs mais usadas
- [ ] Dataset maior (milhares de XMLs, todos os layouts 2.00 → 4.00)
- [ ] Suporte a CT-e e NFC-e
- [ ] Site estático com gráficos e histórico

## ⚖️ Aviso legal

Use apenas XMLs públicos ou sintéticos. **Nunca** commite documentos fiscais
reais contendo dados de terceiros.

## 🤝 Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md). Toda contribuição é bem-vinda —
de novos parsers a novos casos de teste!

## Licença

[MIT](LICENSE)
