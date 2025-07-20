import pytest
from gc_calculator.gc_calculator import compute_gc, parse_fasta


def test_compute_gc_basic():
    assert compute_gc("GCGCGC") == 100.0
    assert compute_gc("ATATAT") == 0.0
    assert compute_gc("ATGC") == 50.0
    assert compute_gc("") == 0.0

def test_parse_fasta(tmp_path):
    # создаём временный fasta-файл
    fasta_content = ">seq1\nATGC\n>seq2\nGGCC"
    test_file = tmp_path / "test.fasta"
    test_file.write_text(fasta_content)

    result = parse_fasta(str(test_file))
    assert result == {
        "seq1": "ATGC",
        "seq2": "GGCC"
    }

