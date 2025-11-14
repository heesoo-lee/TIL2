import os, time, random
from colorama import init, Fore, Style
init()

rainbow = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]

art = [
"           ❄️    *     ❄️     ",
"        ✨      *   ❄️       ✨ ",
"            ⛄  ho ho~ ⛄     ",
"          ⠀⠀  (•‿•)          ",
"           ⠀⠀ (︶︶)           ",
"          ⠀⠀ /(   )\\        ",
"        ❄️  /__⛄__\\   ❄️   ",
"",
"             🎄 Merry 🎄",
"        ✨  Christmas  ✨",
"",
"        🎁      🧸      🎁",
"      (•ᴥ•)   (｡◕‿◕｡)   (•ᴥ•)",
"      /🎅 \\  /✨\\    /🎅 \\",
"     /____\\   /___\\   /____\\",
"",
"     ⭐️  ⭐️  ⭐️  ⭐️  ⭐️  ⭐️",
]

width = 50
snow_rows = 8
flakes = ["*", ".", "❄", "•", "✦"]
snow_positions = [random.randint(0, width-1) for _ in range(snow_rows)]

def clear(): os.system("cls" if os.name == "nt" else "clear")

def cute_color(t):
    out = ""
    for ch in t:
        if ch.strip():
            out += random.choice(rainbow) + ch
        else:
            out += ch
    return out

try:
    while True:
        clear()
        for i in range(snow_rows):
            row = [" "] * width
            snow_positions[i] = (snow_positions[i] + random.choice([-1,0,1])) % width
            row[snow_positions[i]] = random.choice(flakes)
            print(random.choice(rainbow) + "".join(row))
        for ln in art:
            print(cute_color(ln))
        time.sleep(0.12)

except KeyboardInterrupt:
    print(Style.RESET_ALL + "\n🎅✨ Ho Ho Ho! Merry Cute-mas!! 🎄❄️")
