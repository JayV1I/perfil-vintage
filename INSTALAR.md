# 🎬 Como instalar seu perfil vintage em 5 minutos

Este pacote contém tudo o que você precisa para transformar seu GitHub em um
perfil interativo estilo cinema dos anos 30, com site próprio no GitHub Pages.

## 📦 O que tem aqui

| Pasta | O que contém | Como personalizar |
|---|---|---|
| `banner/` | SVG animado base do banner | Abra `banner-base.svg` em qualquer editor de texto e edite: seu nome (`<tspan>`), as frases do balão de fala (`<animate attributeName="values">`), a moldura e as cores |
| `personagens/` | PNGs dos personagens em várias poses | Troque pelos seus (ou use os meus como base) — mantenha o fundo transparente |
| `faixas/` | PNGs das faixas de seção + script gerador | Rode `python3 gerar-faixas.py` e edite os títulos no script |
| `site/` | Template completo do site (GitHub Pages) | Edite `index.html` (conteúdo) e `style.css` (cores e fontes) |

## 🚀 Passo a passo

### 1. Crie seu repositório de perfil

1. Crie um repositório com o **mesmo nome do seu usuário** (ex.: `seuusuario/seuusuario`)
2. Envie o `banner-base.svg` e as faixas para a **raiz** do repositório
3. Crie um `README.md` colando a estrutura de exemplo abaixo

### 2. Exemplo mínimo de README.md

```markdown
<img src="./banner-base.svg" alt="Banner do perfil" width="100%" />

<p align="center">
  <a href="https://jayv1i.github.io/JayV1I/"><img src="https://img.shields.io/badge/🎬_ENTRE_NO_MEU_ESTÚDIO-Abrir_site-2E1F10?style=for-the-badge" alt="Site" /></a>
</p>

<img src="./banner-secao-sobre.png" width="100%" alt="Sobre mim" />

### Sobre mim
Escreva sobre você aqui...

<img src="./banner-secao-stack.png" width="100%" alt="Stack" />

### Stack
![Python](https://img.shields.io/badge/-Python-2E1F10?style=for-the-badge)
```

### 3. Publique seu site

1. No repositório de perfil, crie a pasta `docs/` e coloque o conteúdo de `site/`
2. Vá em **Settings → Pages → Source: Deploy from a branch → main → /docs → Save**
3. Em instantes seu site estará em `seuusuario.github.io/seuusuario/`

### 4. Personalize as cores

A paleta vintage padrão usa estas variáveis (edite no SVG e no CSS):

```css
:root {
  --ink: #3B2415;      /* tinta (texto, molduras) */
  --papel: #F3E5C8;    /* papel (fundo claro) */
  --gry: #B39A70;      /* cinza vintage (destaques) */
  --escuro: #2E1F10;   /* marrom escuro (cabeçalhos) */
}
```

## 💡 Dicas

- O banner SVG é animado **nativamente** (SMIL) — funciona direto no GitHub, sem JavaScript
- As faixas de seção são geradas por script: é só trocar o texto em `gerar-faixas.py`
- Mantenha seus personagens com fundo transparente (use o script `remove-bg.py` do repositório de exemplo, ou ferramentas como remove.bg)
