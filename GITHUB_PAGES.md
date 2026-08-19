# Publicação no GitHub Pages

O mini site científico está em `docs/`.

1. Crie um repositório GitHub novo para PAG ETR.
2. Copie todo o conteúdo deste pacote para a raiz do repositório.
3. Faça commit e push na branch `main`.
4. Em **Settings → Pages**, selecione **GitHub Actions** como fonte.
5. O workflow `.github/workflows/pages.yml` publicará automaticamente `docs/`.

O visor utiliza Leaflet e cartografia base online. Os GeoJSON científicos do PAG ETR permanecem armazenados no próprio repositório.
