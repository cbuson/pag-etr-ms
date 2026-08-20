# PAG ETR v1.0.1 · hotfix de identificação

Foi identificado um módulo JavaScript herdado do ITA ARANDU MS que permanecia carregado na interface pública.

`assets/js/ondas-sismicas-v38453.js`

Durante a inicialização, esse módulo executava uma instrução que substituía o conteúdo de `.ita-version-badge` por `V38.4.53`.

Correção aplicada

- removida a carga pública de `ondas-sismicas-v38453.js`
- removida a folha de estilo correspondente
- adicionada uma trava defensiva que mantém o badge público em `v1.0.1`
- nenhum dado, resultado científico, regra PAG ETR ou camada foi recalculado ou alterado
