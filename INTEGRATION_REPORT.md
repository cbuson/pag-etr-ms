# PAG ETR · integração EarthArXiv e navegação pública

## Estado

A integração preserva o pacote científico reprodutível e adiciona uma camada pública de navegação em `docs` e uma área editorial em `manuscript`.

## Navegação pública

A aplicação abre no mapa. As seções disponíveis são mapa, método, reprodução, auditoria, figuras, manuscrito, referências e autoria. A navegação aceita fragmentos de URL como `#map`, `#method`, `#audit` e `#manuscript`.

Em dispositivos móveis, o mapa permanece como área principal. A navegação inferior dá acesso a camadas, mapa, método, auditoria e às demais áreas.

## Mapas

A malha de 250 km² é carregada inicialmente. As malhas de 500 e 1000 km² podem ser ativadas no painel. As evidências M2, M4, os registros de fósforo, a geologia de base e a cobertura de mapeamento podem ser ativadas de forma independente.

Os contadores são calculados a partir dos GeoJSON carregados pela interface.

## EarthArXiv

O template recebido foi preservado em `manuscript/eartharxiv-template`. A fonte de trabalho está em `manuscript/pag_etr_eartharxiv.tex` e foi testada com `pdflatex` no ambiente de integração.

O resumo e as seções sem texto científico consolidado permanecem explicitamente marcados como conteúdo em elaboração.

## Validação

A reprodução M2 e M4 continua retornando os mesmos resultados congelados nas três escalas.

- 250 km² · 1554 células · 49 N1 · M2 3 · M4 46
- 500 km² · 793 células · 37 N1 · M2 3 · M4 34
- 1000 km² · 412 células · 24 N1 · M2 2 · M4 22

Os testes `validate_against_frozen.py` permanecem em PASS nas três escalas.
