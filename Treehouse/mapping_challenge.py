TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == '||':
        line_end = "\n"
        print(end = line_end)
    else:
        line_end = ""
        print(tile, end = line_end)