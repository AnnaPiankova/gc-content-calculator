# 🧬 GC Content Calculator

Python-скрипт для анализа GC-содержания в FASTA-последовательностях.  
Визуализирует распределение GC-контента и сохраняет гистограмму.

## 🚀 Установка

```bash
git clone https://github.com/AnnaPiankova/gc-content-calculator.git
cd gc-content-calculator
poetry install

## 🚀 Использование

1. Быстрый запуск

poetry run python src/gc_calculator/gc_calculator.py data/example.fasta

2. Указание путей вывода

poetry run python src/gc_calculator/gc_calculator.py \
  data/example.fasta \
  --plot plots/gc_histogram.png \
  --out output/gc_content.tsv

## 📊 Визуализация

Гистограмма GC-содержания сохраняется в plots/

