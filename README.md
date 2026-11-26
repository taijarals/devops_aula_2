# UNIJORGE — AV2 de DevOps

Professor Me. Taijara Loiola Oliveira de Santana

Avaliação prática em grupos de até cinco integrantes. Cada grupo deve construir o fluxo no próprio repositório e entregar uma única prova com os nomes de todos os integrantes.

Objetivo: versionar um programa Python, executar testes no GitHub Actions, publicar seu relatório no GitHub Pages e explicar o processo com evidências.

Valor total: 10,0 pontos. São cinco questões abertas de 2,0 pontos cada.

Use os códigos fornecidos e siga as etapas na ordem. As pastas deste repositório são material de consulta; os destinos no repositório do grupo estão indicados em cada etapa. Todos devem participar da execução e da discussão das respostas.

Responda nos espaços da prova. Registre links completos em RESPOSTAS.md no repositório do grupo; na folha, identifique os commits pelos sete primeiros caracteres. Ao terminar, deixe o código corrigido e entregue o endereço do repositório.

Em caso de problema no computador ou na internet, comunique ao professor. Use os códigos do anexo para explicar o comportamento previsto, identifique a resposta como análise sem execução e descreva quais evidências buscaria. Não apresente previsões como resultados observados. A correção considerará a justificativa técnica equivalente.

## Material de referência

| Arquivo fornecido | Destino no repositório do grupo |
| --- | --- |
| [projeto_inicial/pontuacao.py](projeto_inicial/pontuacao.py) | `pontuacao.py` |
| [projeto_inicial/gerar_relatorio.py](projeto_inicial/gerar_relatorio.py) | `gerar_relatorio.py` |
| [testes/test_pontuacao.py](testes/test_pontuacao.py) | `tests/test_pontuacao.py` |
| [modelos/01_ci_testes.yml](modelos/01_ci_testes.yml) | `.github/workflows/ci-cd.yml na etapa 2` |
| [modelos/02_ci_cd_pages.yml](modelos/02_ci_cd_pages.yml) | `substitui o mesmo .github/workflows/ci-cd.yml na etapa 4` |

Abra o arquivo e use a opção de copiar conteúdo ou Raw. Copie somente o código, sem marcadores de bloco Markdown. Python e YAML dependem da indentação por espaços. Os códigos completos também acompanham o anexo da prova impressa.

## Como os testes automatizados funcionam

### unittest e TestCase

unittest é o módulo de testes da biblioteca padrão do Python. Ele organiza e executa verificações e apresenta seus resultados, sem instalação adicional neste projeto.

A classe TestPontuacao herda de unittest.TestCase e recebe métodos de verificação, como assertEqual. Cada método iniciado por test_ representa um caso. self identifica a instância do teste em execução.

### Como ler assertEqual

```python
self.assertEqual(resultado_obtido, resultado_esperado)
```

assertEqual compara os dois valores. Se forem iguais, a verificação passa; se forem diferentes, registra uma falha com os valores comparados. Ao falhar, o método de teste termina; os demais casos continuam por padrão.

Exemplo independente para leitura da sintaxe:

```python
self.assertEqual(2 + 2, 4)
```

O primeiro argumento produz 4; o segundo informa o esperado. A verificação passa. No projeto, o primeiro argumento chama calcular_pontuacao e o segundo informa a pontuação esperada.

### Execução e importância para DevOps

```bash
python -m unittest discover -s tests -v
```

Na raiz do projeto, discover busca arquivos test*.py em tests e executa seus casos; -v mostra os nomes. Ran N tests informa a quantidade. OK indica sucesso; FAILED informa falhas ou erros.

O assert simples também verifica condições, mas sozinho não organiza a execução nem gera esse resumo. TestCase e assertEqual ajudam a repetir verificações e localizar regressões após mudanças.

No Actions, o comando sinaliza falha ao processo quando há teste reprovado. Nos modelos fornecidos, isso reprova o job; needs: testes condiciona a publicação ao sucesso dele. A proteção depende também da configuração do workflow.

Referência: https://docs.python.org/3/library/unittest.html


## Etapa 1 — Versionamento e rastreabilidade

1. Crie um repositório público para o grupo, com README.md e branch main. Utilize um único repositório por grupo.
2. No repositório de referência, abra projeto_inicial. Copie pontuacao.py e gerar_relatorio.py para a raiz do repositório do grupo. Use Add file → Create new file ou Upload files e faça um commit.
3. Edite gerar_relatorio.py pelo ícone de lápis. Altere TITULO para identificar o grupo e faça outro commit.
4. Consulte o histórico de commits e compare as duas versões.

### Questão 1 — 2,0 pontos

Compare o commit que adicionou os arquivos Python com o commit que alterou o título. Informe seus identificadores e explique como o histórico permite descobrir o que mudou e recuperar a versão utilizada em uma execução do pipeline.

Evidências a registrar: Identificadores dos dois commits e descrição da alteração.

## Etapa 2 — Integração contínua e execução do workflow

1. Abra testes/test_pontuacao.py no material de referência. No seu repositório, use Add file → Create new file e crie tests/test_pontuacao.py com esse conteúdo. Faça o commit. Atenção: o destino usa tests, não testes.
2. Crie .github/workflows/ci-cd.yml e copie o conteúdo completo de modelos/01_ci_testes.yml. Preserve os espaços de indentação e faça o commit na main.
3. Abra Actions → CI Python. Selecione a execução desse commit, abra Testar Python e examine os passos e os logs de Executar testes.
4. Confira o número de testes executados e seus resultados. Se a execução ainda estiver na fila, aguarde sua conclusão.

### Questão 2 — 2,0 pontos

Na execução observada, qual evento iniciou o workflow? Explique o papel de runs-on, uses e run, relacionando cada elemento a um trecho do seu YAML. Apresente o link da execução e a evidência de quantos testes foram executados.

Evidências a registrar: Link da execução e trecho do resumo dos testes.

## Etapa 3 — Falha controlada e diagnóstico

1. Em pontuacao.py, prepare a alteração de pontos += 1 para pontos += 2. Antes do commit, registre quais testes você prevê que falharão e por quê.
2. Faça o commit, acompanhe a execução no Actions e compare sua previsão com os resultados. Copie o valor esperado e o obtido em pelo menos um teste reprovado.
3. Restaure pontos += 1 e faça um novo commit. Confirme o resultado dos testes na nova execução.

### Questão 3 — 2,0 pontos

Quais testes o grupo previu que falhariam e quais realmente falharam? Explique a relação entre a alteração no código e os valores apresentados no log de um teste reprovado. Por que executar novamente o workflow do commit defeituoso não substitui criar e testar o commit de correção? Inclua os links das execuções com falha e após a correção.

Evidências a registrar: Previsão, comparação entre esperado e obtido e links das duas execuções.

## Etapa 4 — Publicação e ambientes de execução

1. Abra Settings → Pages. Em Build and deployment → Source, selecione GitHub Actions.
2. Edite o arquivo existente .github/workflows/ci-cd.yml. Substitua todo o conteúdo pelo modelo modelos/02_ci_cd_pages.yml. Mantenha um único arquivo de workflow ativo e faça o commit.
3. Em Actions → CI/CD Python, acompanhe Testar Python e Publicar relatorio. Examine os passos de geração, conversão do Markdown, empacotamento e publicação.
4. Após a conclusão, abra o endereço indicado no ambiente github-pages ou em Settings → Pages. Confira o título, a tabela e o commit mostrado na página.

### Questão 4 — 2,0 pontos

Explique o caminho entre o commit e o relatório publicado: onde os testes executam, onde o programa Python executa e o que o GitHub Pages disponibiliza ao visitante. Qual é a função de needs: testes nesse caminho? Apresente o endereço da página e compare o commit exibido nela com o da execução que realizou a publicação.

Evidências a registrar: Endereço da página, link da execução e comparação entre os commits.

## Etapa 5 — Bloqueio de publicação e recuperação

1. Com uma versão publicada corretamente, anote o commit mostrado na página.
2. Introduza novamente pontos += 2 em pontuacao.py e faça o commit. Observe os estados dos jobs de testes e publicação.
3. Reabra a página e compare o commit exibido com o commit defeituoso. Registre as evidências antes de corrigir.
4. Restaure pontos += 1, faça outro commit e acompanhe a recuperação. Confira o relatório após a nova publicação.

### Questão 5 — 2,0 pontos

Após a nova falha nos testes, o que aconteceu com o job de publicação e com a página que já estava no ar? Use os estados dos jobs e os identificadores dos commits como evidências. Se needs: testes fosse removido, a falha nos testes ainda garantiria o bloqueio da publicação? Justifique.

Evidências a registrar: Estados dos jobs, comparação entre commits e link da execução de recuperação.

## Entrega

Preencha a prova impressa e o arquivo [RESPOSTAS.md](RESPOSTAS.md) no repositório do grupo. Identifique até cinco integrantes. Entregue o link do repositório e o endereço do Pages, se a publicação tiver sido concluída.
