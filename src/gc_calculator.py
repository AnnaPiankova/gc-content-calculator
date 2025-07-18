import argparse
import csv
import os
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

def plot_gc_distribution(gc_values: list[float], save_path="plots/gc_histogram.png", show=True):
    """Рисует и сохраняет гистограмму GC-содержания"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.hist(gc_values, bins=10, color="skyblue", edgecolor="black")
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of Sequences")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    if show:
        plt.show()

def save_csv(results: dict, out_path: str):
    """Сохраняет GC-результаты в CSV"""
    with open(out_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(["Sequence ID", "GC Content (%)"])
        for seq_id, gc in results.items():
            writer.writerow([seq_id, f"{gc:.2f}"]) 

def main(fasta_path: str):
    parser = argparse.ArgumentParser(description="GC Content Calculator for FASTA sequences")
    parser.add_argument("fasta_path", help="Path to the input FASTA file")
    parser.add_argument("--csv", help="Path to save TSV with GC content")
    parser.add_argument("--no-show", action="store_true", help="Do not display histogram")
    parser.add_argument("--plot", default="plots/gc_histogram.png", help="Path to save the histogram plot")

    args = parser.parse_args()

    sequences = parse_fasta(args.fasta_path)
    results = {}
    gc_values = []

    for seq_id, seq in sequences.items():
        gc = compute_gc(seq)
        results[seq_id] = gc
        gc_values.append(gc)
        print(f"{seq_id}: GC-content = {gc:.2f}%")

    if args.csv:
        save_csv(results, args.csv)
        print(f"✅ GC values saved to: {args.csv}")

    # Визуализация
    plot_gc_distribution(gc_values, save_path=args.plot, show=not args.no_show)

if __name__ == "__main__":
    main()

