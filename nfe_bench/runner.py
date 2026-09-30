import json
import time
from pathlib import Path
from .baseline import BaselineParser

def get_parsers():
    return [
        BaselineParser(),
        # Adicione novos parsers aqui conforme for criando os adapters
    ]

def run_benchmark():
    samples_dir = Path("data/samples")
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    xml_files = sorted(list(samples_dir.glob("*.xml")))
    if not xml_files:
        print("⚠️ Nenhuma amostra XML encontrada em data/samples/")
        return

    parsers = get_parsers()
    all_results = []

    for xml_path in xml_files:
        print(f"📄 Testando amostra: {xml_path.name}")
        
        # Carrega ground truth se existir
        gt_path = xml_path.with_suffix(".json")
        ground_truth = {}
        if gt_path.exists():
            with open(gt_path, "r", encoding="utf-8") as f:
                ground_truth = json.load(f)

        for parser in parsers:
            print(f"  ⚡ Rodando parser: {parser.name}")
            
            # Medição de tempo (média de repetições)
            times = []
            parsed_data = None
            error_msg = None
            ok = True

            for _ in range(5):
                start = time.perf_counter()
                try:
                    parsed_data = parser.parse(xml_path)
                except Exception as e:
                    ok = False
                    error_msg = str(e)
                    parsed_data = {}
                end = time.perf_counter()
                times.append((end - start) * 1000) # em milissegundos

            elapsed_ms = sorted(times)[len(times) // 2] # mediana

            # Cálculo de acurácia básica baseada no ground truth
            missing_fields = []
            wrong_fields = []
            accuracy = 1.0

            if ok and ground_truth:
                matches = 0
                total = len(ground_truth)
                for key, expected in ground_truth.items():
                    val = parsed_data.get(key)
                    if val is None:
                        missing_fields.append(key)
                    elif val != expected:
                        wrong_fields.append(key)
                    else:
                        matches += 1
                accuracy = matches / total if total > 0 else 1.0

            all_results.append({
                "parser": parser.name,
                "sample": xml_path.name,
                "ok": ok,
                "error": error_msg,
                "accuracy": accuracy,
                "elapsed_ms": elapsed_ms,
                "missing_fields": missing_fields,
                "wrong_fields": wrong_fields
            })

    output_file = results_dir / "results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Benchmark concluído! Resultados salvos em {output_file}")

if __name__ == "__main__":
    run_benchmark()
