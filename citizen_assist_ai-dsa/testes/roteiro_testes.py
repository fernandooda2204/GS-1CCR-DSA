"""Registra evidências reproduzíveis em testes/evidencias/saida_roteiro.txt."""
from contextlib import redirect_stdout
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from main import roteiro_automatico


def main():
    destino = Path(__file__).resolve().parent / 'evidencias' / 'saida_roteiro.txt'
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open('w', encoding='utf-8') as arquivo, redirect_stdout(arquivo):
        roteiro_automatico()
    print(f'Evidência gerada: {destino}')


if __name__ == '__main__':
    main()
