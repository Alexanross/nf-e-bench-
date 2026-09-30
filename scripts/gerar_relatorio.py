import json
from pathlib import Path

def gerar_markdown():
    results_file = Path("results/results.json")
    if not results_file.exists():
        print("⚠️ Ficheiro results/results.json não encontrado. Corre o runner primeiro!")
        return

    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    md_content = "# 📊 Relatório de Benchmark - Parsers NF-e\n\n"
    md_content += "| Parser | Amostra | Status | Acurácia | Tempo (ms) | Erros |\n"
    md_content += "|---|---|---|---|---|---|\n"

    for r in data:
        status = "✅ OK" if r["ok"] else "❌ Erro"
        acc = f"{r['accuracy'] * 100:.1f}%"
        tempo = f"{r['elapsed_ms']:.2f} ms"
        erro = r["error"] if r["error"] else "-"
        md_content += f"| {r['parser']} | {r['sample']} | {status} | {acc} | {tempo} | {erro} |\n"

    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    output_md = docs_dir / "relatorio.md"
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"✅ Relatório Markdown gerado com sucesso em {output_md}")

if __name__ == "__main__":
    gerar_markdown()
