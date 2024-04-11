import ctypes

def get_resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return (width, height)

# level_map = [
#     '                                           ',
#     '                                           ',
#     '   P                                       ',
#     ' GGG      GGG        GGGGG                 ',
#     ' XXXTT          H                          ',
#     ' XXXGG         GGG        GG               ',
#     ' XX             XXG       XXG              ',
#     ' X       GGGGG   XXGGG    XXX     GGGG     ',
#     '        GXXXXX   XXXXX    XXXGG      XX    ',
#     '     GGGXXXXXX   XXXXX    XXXXXG           ',
#     'GGGGGXXXXXXXXX   XXXXX    XXXXXXGG    GGGG ',
#     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ',
# ]

lev_txt = open('levels/res/level_text.txt')
level_map = lev_txt.read().split('\n')

# размер плитки
screen_width, screen_height = get_resolution()
tile_size = screen_height // len(level_map) if (screen_height // len(level_map)) % 2 == 0 else (screen_height // len(level_map)) + 1