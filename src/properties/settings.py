import ctypes


def get_resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height


lev_txt = open('levels/res/level_text.txt')
level_map = lev_txt.read().split('\n')
lev_txt.close()

# размер экрана и плитки
screen_width, screen_height = get_resolution()
tile_size = (
    screen_height // len(level_map)
    if (screen_height // len(level_map)) % 2 == 0
    else (screen_height // len(level_map)) + 1
)
