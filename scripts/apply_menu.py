import subprocess

def aplicar_traducoes():
    print("\nAplicando traduções...")

    resultado = subprocess.run(
        ["python3", "scripts/apply_translation.py"],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)

    if resultado.returncode == 0:
        print("Traduções aplicadas com sucesso!")
    else:
        print("Erro ao aplicar traduções:")
        print(resultado.stderr)
