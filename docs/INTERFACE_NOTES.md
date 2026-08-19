# Interface PAG ETR

A página inicia sempre no mapa quando não há fragmento de navegação na URL.

A interface pública separa mapa, método, reprodução, auditoria, figuras, manuscrito, referências e autoria. Em telas móveis, o mapa permanece como área principal e a navegação inferior oferece acesso direto às funções essenciais.

Os dados científicos do mapa são carregados de `docs/data`. Os resumos de auditoria publicados em `docs/public` são cópias de arquivos existentes no pacote ou estruturas derivadas diretamente desses registros.

Nenhum estado científico novo é calculado pela interface. Os contadores do mapa são lidos dos GeoJSON carregados.
