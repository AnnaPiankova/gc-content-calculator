from Bio import SeqIO
import matplotlib.pyplot as plt

def compute_gc(seq: str) -> float:
    """Вычисляет GC-содержание в %"""
    g = seq.count("G")
    c = seq.count("C")
    if len(seq) == 0:
        return 0.0
    return 100 * (g + c) / len(seq)

def parse_fasta(filepath: str) -> dict:
    """Парсит FASTA и возвращает словарь {id: sequence}"""
    sequences = {}
    for record in SeqIO.parse(filepath, "fasta"):
        sequences[record.id] = str(record.seq).upper()
    return sequences

def plot_gc_distribution(gc_values: list[float], save_path="plots/gc_histogram.png"):
    """Рисует и сохраняет гистограмму GC-содержания"""
    plt.figure(figsize=(8, 5))
    plt.hist(gc_values, bins=10, color="skyblue", edgecolor="black")
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of sequences")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def main(fasta_path: str):
    sequences = parse_fasta(fasta_path)
    print(f"[DEBUG] Найдено {len(sequences)} последовательностей")
    gc_values = []

    for seq_id, seq in sequences.items():
        gc = compute_gc(seq)
        gc_values.append(gc)
        print(f"{seq_id}: GC-content = {gc:.2f}%")

    # Визуализация
    plot_gc_distribution(gc_values)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python src/gc_calculator.py <fasta_file>")
    else:
        main(sys.argv[1])

