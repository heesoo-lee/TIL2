# tree.py — 안정 버전 (문자/색 분리 렌더링)
import sys, time, random

# ===== 설정 =====
WIDTH  = 70
HEIGHT = 32
FPS = 6
SNOW_CHANCE = 0.02  # 잔잔한 눈

# 트리(고정 폭)
TREE = [
"        *        ",
"       ***       ",
"      *****      ",
"     *******     ",
"    *********    ",
"   ***********   ",
"  *************  ",
" *************** ",
"*****************",
"       |||       ",
"       |||       "
]
ORN_POS     = {(2,9),(3,7),(3,11),(4,5),(4,13),(5,8),(6,6),(6,12),(7,9)}
ORN_COLORS  = ["91","92","93","95","96"]   # 빨/초/노/보/청

RUDOLPH = [
" (\\_/) ",
" ( •ᴥ•) ",
" / >🎄  "
]

# ===== 유틸 =====
ESC, RESET = "\033[", "\033[0m"
def cls(): sys.stdout.write("\033[2J\033[H")
def set_color(c): return f"{ESC}{c}m"

# 색/문자 분리 캔버스
def new_canvas():
    chars = [[" "] * WIDTH for _ in range(HEIGHT)]
    cols  = [[None] * WIDTH for _ in range(HEIGHT)]
    return chars, cols

def blit_text(chars, cols, x, y, text, color=None):
    """가시 좌표 기준으로 문자열을 캔버스에 올림 (문자 단위 배치)"""
    if y < 0 or y >= HEIGHT: return
    for i, ch in enumerate(text):
        px = x + i
        if 0 <= px < WIDTH:
            chars[y][px] = ch
            cols[y][px]  = color

# ===== 스노우 =====
snow = []
def drop_snow(chars, cols):
    global snow
    # 아래로 이동
    snow = [(y+1, x) for (y, x) in snow if y+1 < HEIGHT]
    # 새 눈 생성
    for _ in range(WIDTH // 3):
        if random.random() < SNOW_CHANCE:
            snow.append((0, random.randint(0, WIDTH-1)))
    # 그리기
    for y, x in snow:
        chars[y][x] = "*"
        cols[y][x]  = None  # 눈은 흰색(기본)

# ===== 트리 =====
def draw_tree(chars, cols, tick):
    start_y = 3
    for r, row in enumerate(TREE):
        y = start_y + r
        if not (0 <= y < HEIGHT): 
            continue
        sx = (WIDTH - len(row)) // 2
        for c, ch in enumerate(row):
            x = sx + c
            if not (0 <= x < WIDTH): 
                continue
            if (r, c) in ORN_POS and ch != " ":
                color = ORN_COLORS[(r + c + tick) // 8 % len(ORN_COLORS)]
                chars[y][x] = "o"
                cols[y][x]  = color
            elif ch == "*":
                chars[y][x] = "*"
                cols[y][x]  = "32"         # 녹색 잎
            elif ch == "|":
                chars[y][x] = "|"
                cols[y][x]  = "33"         # 노란 줄기
            else:
                chars[y][x] = ch
                # 공백은 색 없음
                cols[y][x]  = None if ch == " " else cols[y][x]

# ===== 루돌프 =====
def draw_rudolph(chars, cols, tick):
    x = (tick // 2) % (WIDTH + 12) - 12
    y = HEIGHT - 5
    for i, row in enumerate(RUDOLPH):
        blit_text(chars, cols, x, y + i, row, None)  # 루돌프는 기본색

# ===== 텍스트 =====
def draw_text(chars, cols):
    msg  = "MERRY CHRISTMAS"
    year = "2026"
    blit_text(chars, cols, (WIDTH - len(msg)) // 2,  HEIGHT - 6, msg,  "93")
    blit_text(chars, cols, (WIDTH - len(year)) // 2, HEIGHT - 4, year, "92")

# ===== 렌더러 (색 전환 최소화) =====
def render(chars, cols):
    cls()
    for y in range(HEIGHT):
        line_out = []
        cur = None
        for x in range(WIDTH):
            cchar = chars[y][x]
            ccol  = cols[y][x]
            if ccol != cur:
                if ccol is None:
                    line_out.append(RESET)
                else:
                    line_out.append(set_color(ccol))
                cur = ccol
            line_out.append(cchar)
        if cur is not None:
            line_out.append(RESET)
        print("".join(line_out))

# ===== 메인 루프 =====
def main():
    tick = 0
    try:
        while True:
            tick += 1
            chars, cols = new_canvas()
            drop_snow(chars, cols)
            draw_tree(chars, cols, tick)
            draw_rudolph(chars, cols, tick)
            draw_text(chars, cols)
            render(chars, cols)
            time.sleep(1 / FPS)
    except KeyboardInterrupt:
        cls()
        print("🎄 Merry Christmas & Happy 2026 ✨")

if __name__ == "__main__":
    main()
