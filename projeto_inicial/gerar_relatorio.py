import os
from pathlib import Path

from pontuacao import calcular_pontuacao

TITULO = "Relatorio de pontuacao"


def gerar_relatorio():
    gabarito = [0, 1, 2]
    exemplos = [
        ("Nenhum acerto", [1, 2, 3]),
        ("Um acerto", [0, 2, 3]),
        ("Tres acertos", [0, 1, 2]),
    ]
    commit = os.environ.get("GITHUB_SHA", "execucao-local")
    linhas = [
        "---",
        "---",
        "",
        f"# {TITULO}",
        "",
        "Resultados calculados pelo programa Python durante o pipeline.",
        "",
        f"Commit publicado: `{commit}`",
        "",
        "| Exemplo | Pontuacao |",
        "| --- | ---: |",
    ]
    for nome, respostas in exemplos:
        pontos = calcular_pontuacao(respostas, gabarito)
        linhas.append(f"| {nome} | {pontos} |")

    pasta = Path("site")
    pasta.mkdir(exist_ok=True)
    destino = pasta / "index.md"
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"Relatorio gerado em {destino}")


if __name__ == "__main__":
    gerar_relatorio()
