"""Gera faixas PNG sépia estilo cartaz de cinema para servir de cabeçalho de seção no README.

Estratégia: como o GitHub não permite background em HTML de README, usamos imagens
PNG largas (1200x110) com gradiente sépia e texto, inseridas antes de cada seção.
"""
from PIL import Image, ImageDraw, ImageFont

W = 1200
H = 110

INK = (46, 31, 16)        # #2E1F10
PAPER = (243, 229, 200)   # #F3E5C8
GOLD = (179, 154, 112)    # #B39A70
DEEP = (234, 220, 192)    # #EADCC0
BORDER = (26, 16, 8)      # #1a1008

def gradient_bg():
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        # gradiente vertical: DEEP no topo -> PAPER no meio -> DEEP embaixo
        r = int(DEEP[0] + (PAPER[0] - DEEP[0]) * abs(t - 0.5) * 2 * 0.55 + 0) if t < 0.5 else int(PAPER[0] - (PAPER[0] - DEEP[0]) * (t - 0.5) * 2 * 0.55)
        # simplificação: usar interpolação suave
    # refazer com interpolação clara
    stops = [(0, DEEP), (0.5, PAPER), (1, DEEP)]
    for y in range(H):
        t = y / H
        if t <= 0.5:
            a, b = stops[0][1], stops[1][1]
            k = t / 0.5
        else:
            a, b = stops[1][1], stops[2][1]
            k = (t - 0.5) / 0.5
        color = tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3))
        d.line([(0, y), (W, y)], fill=color)
    return img

def add_border(img, d):
    # moldura dupla estilo cartaz de cinema
    d.rectangle([2, 2, W - 3, H - 3], outline=BORDER, width=3)
    d.rectangle([7, 7, W - 8, H - 8], outline=GOLD, width=2)

def load_font(size):
    import subprocess, os
    for path in ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
                 '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf']:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def make_banner(text, emoji, out):
    img = gradient_bg()
    d = ImageDraw.Draw(img)
    add_border(img, d)
    # texto com ornamento tipográfico simples (a fonte não tem emojis coloridos)
    font = load_font(44)
    orn = '*'
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', 26)
    sep = '  ~  '
    full = f"{orn}{sep}{text}{sep}{orn}"
    bbox = d.textbbox((0, 0), full, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    d.text((x, (H - (bbox[3] - bbox[1])) // 2 - bbox[1]), full, font=font, fill=INK)
    img.save(out, optimize=True)
    print('ok', out)

sections = [
    ('Minhas estatísticas animadas', '📊', '/home/ubuntu/repo_jayv1i/banner-secao-stats.png'),
    ('Sobre mim', '🎞', '/home/ubuntu/repo_jayv1i/banner-secao-sobre.png'),
    ('Tecnologias que eu uso', '⚙', '/home/ubuntu/repo_jayv1i/banner-secao-stack.png'),
    ('Aprendendo agora', '📖', '/home/ubuntu/repo_jayv1i/banner-secao-aprendendo.png'),
    ('Meus projetos em destaque', '🚀', '/home/ubuntu/repo_jayv1i/banner-secao-projetos.png'),
    ('Filmstrip de contribuições', '🎬', '/home/ubuntu/repo_jayv1i/banner-secao-contribs.png'),
    ('Contato — vamos fazer algo juntos!', '✉', '/home/ubuntu/repo_jayv1i/banner-secao-contato.png'),
]

for text, emoji, out in sections:
    make_banner(text, emoji, out)
