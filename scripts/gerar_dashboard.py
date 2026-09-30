import json
from pathlib import Path

def gerar_html():
    results_file = Path("results/results.json")
    if not results_file.exists():
        print("⚠️ Ficheiro results/results.json não encontrado. Corre o runner primeiro!")
        return

    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    html_content = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Benchmark NF-e</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f9; color: #333; }
        h1 { color: #0066cc; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        th, td { padding: 12px 15px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #0066cc; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .ok { color: green; font-weight: bold; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>📊 Dashboard de Benchmark de Parsers NF-e</h1>
    <p>Resultados comparativos de desempenho e precisão dos parsers.</p>
    <table>
        <tr>
            <th>Parser</th>
            <th>Amostra</th>
            <th>Status</th>
            <th>Acurácia</th>
            <th>Tempo (ms)</th>
            <th>Erros</th>
        </tr>
"""

    for r in data:
        status_class = "ok" if r["ok"] else "error"
        status_text = "✅ OK" if r["ok"] else "❌ Erro"
        acc = f"{r['accuracy'] * 100:.1f}%"
        tempo = f"{r['elapsed_ms']:.2f} ms"
        erro = r["error"] if r["error"] else "-"
        
        html_content += f"""        <tr>
            <td>{r['parser']}</td>
            <td>{r['sample']}</td>
            <td class="{status_class}">{status_text}</td>
            <td>{acc}</td>
            <td>{tempo}</td>
            <td>{erro}</td>
        </tr>\n"""

    html_content += """    </table>
</body>
</html>"""

    output_html = Path("dashboard.html")
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Dashboard gerado com sucesso em {output_html}")

if __name__ == "__main__":
    gerar_html()
