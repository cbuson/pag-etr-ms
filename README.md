# PAG ETR · pacote científico reprodutível

**Prioridade por Analogia Geológica para Prospecção Geoquímica de Elementos Terras Raras · Mato Grosso do Sul, Brasil**

Este repositório foi extraído do ITA ARANDU MS para documentar, auditar e reproduzir o piloto espacial PAG ETR sem carregar a aplicação completa do Atlas.

## O que o método faz

PAG ETR é um sistema lógico e categórico de apoio à decisão para investigação geoquímica. A unidade final é uma **zona de investigação**, não um ponto de jazimento. O método não usa soma ponderada, pontuação de 0 a 100 ou probabilidade de depósito.

Estados do modelo

- N0 · Não avaliável
- N1 · Modelo aberto
- N2 · Justifica prospecção geoquímica
- N3 · Evidência local compatível
- N4 · Contradito localmente

## Resultado congelado do piloto espacial

| Escala | Células | N1 · Modelo aberto | M2 aberto | M4 aberto |
|---|---:|---:|---:|---:|
| 250 km² | 1554 | 49 | 3 | 46 |
| 500 km² | 793 | 37 | 3 | 34 |
| 1000 km² | 412 | 24 | 2 | 22 |

N2 e N3 não foram atribuídos automaticamente neste corte. Essa ausência é deliberada e conserva o caráter restritivo do piloto.

## Reproduzir o piloto

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python scripts/reproduce_pag_etr.py
python tests/validate_against_frozen.py
```

A reprodução parte das bases congeladas do mapa geológico e do mapa de recursos minerais e refaz as seleções de evidência M2 e M4. Em seguida, avalia as três malhas independentemente. A validação compara os **IDs exatos dos hexágonos** com o resultado congelado.

## Cadeia de rastreabilidade do piloto

```text
SGB / GeoSGB
    ↓
mapa_geologico_ms.geojson
mapa_recursos_minerais_ms.geojson
    ↓
M2 · Corpo Feixe dos Morros
M4 · Formação Bocaina + Formação Tamengo
Pontos com SUBSTANCIAS = Fósforo
    ↓
interseção espacial independente
    ↓
malha 250 km² · malha 500 km² · malha 1000 km²
    ↓
N0 / N1 no piloto espacial
    ↓
resultados congelados e validação por hex_id
```

## Organização

- `data/source` · fontes de base congeladas usadas para reconstruir as evidências atualmente espacializadas
- `data/evidence` · evidências derivadas e materializadas no ITA ARANDU
- `data/grids` · três malhas oficiais do piloto
- `data/context` · camadas úteis para interpretação e discussão, mas não usadas automaticamente como favorabilidade
- `results/frozen` · resultados originais extraídos do ITA ARANDU
- `results/reproduced` · resultados regenerados pelo script deste pacote
- `methodology` · metodologia original e especificação lógica
- `references` · bibliografia PAG ETR em APA 7
- `audit` · hashes, matrizes e logs de validação
- `figures` · figuras estáticas para o manuscrito
- `docs` · aplicação cartográfica pública para GitHub Pages com mapa inicial, método, reprodução, auditoria, figuras, manuscrito, referências e autoria
- `manuscript` · fonte de trabalho EarthArXiv, figuras do manuscrito e cópia preservada do template recebido

## Limite de reprodutibilidade

Este pacote reproduz integralmente o **piloto espacial materializado M2/M4** a partir das bases geológicas e minerais congeladas presentes no repositório. Ele não afirma reconstruir etapas históricas de aquisição remota anteriores aos snapshots nem modelos M1, M3 e M5–M11 que permaneceram sem critérios espacializados suficientes nesse corte. Isso é documentado como limite, não preenchido por inferência.

## Princípios de interpretação

- `SEM_DADO ≠ 0`
- um ponto não preenche um hexágono
- contexto acumulado não substitui requisito diagnóstico
- as malhas de 250, 500 e 1000 km² são avaliadas de forma independente
- resultado PAG ETR não equivale a autorização de campo
- resultado PAG ETR não demonstra depósito, recurso ou reserva

## Proveniência

A documentação original do ITA ARANDU MS, os metadados de camada e a bibliografia específica foram preservados neste pacote. O arquivo `audit/file_manifest.csv` registra SHA-256 e tamanho dos arquivos de dados congelados.

## Autoria e contribuição

**Carlos Busón Buesa** · Pesquisador de pós-doutorado voluntário na Universidade Federal de Mato Grosso do Sul, PPGTA / FAENG. ORCID 0000-0002-1446-2252. Contribuição no ITA ARANDU MS e PAG ETR · concepção do projeto, arquitetura científica e digital, integração territorial, desenho do sistema multiescalar, documentação e desenvolvimento metodológico.

**Supervisão acadêmica** · Sandra Garcia Gabas, orientadora do pós-doutorado. A condição de coautoria do preprint PAG ETR será definida na versão editorial final segundo a contribuição efetiva ao manuscrito.

## Como citar

A referência definitiva será adicionada somente depois do congelamento do repositório e da atribuição de DOI. Nenhum DOI foi inventado nesta versão.

## Especificação executável recuperada

A V2 incorpora a especificação M1–M11, o catálogo de testes documentados e um motor lógico executável transcrito fielmente da metodologia congelada de 13 de agosto de 2026. Esses arquivos tornam as regras testáveis, mas não são apresentados como scripts históricos recuperados. O piloto espacial M2/M4 continua sendo reproduzido separadamente a partir das fontes e resultados congelados.


## Integração EarthArXiv

A V2 integrada preserva o template EarthArXiv recebido em `manuscript/eartharxiv-template` e mantém uma fonte de trabalho em `manuscript/pag_etr_eartharxiv.tex`. Seções ainda não redigidas continuam marcadas como conteúdo em elaboração. O pacote não preenche resultados, DOI ou referências ausentes por inferência.
