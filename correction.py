from colorsys import rgb_to_hls, hls_to_rgb

def get_color_types(hex):
    rgb = [int(hex[i:i+2], 16) for i in range(1, len(hex), 2)]
    tsl = list(rgb_to_hls(*[x/255 for x in rgb]))
    tsl.insert(-1, tsl.pop())
    hls = (f"{round(tsl[0]*360)}°", *[f"{el:.0%}" for el in tsl[1:3]])
    return { 'hex': hex, 'rvb': rgb, 'tls_norm': hls, 'tsl':tuple(tsl) }

def get_complenentary(color):
    t, s, l = get_color_types(color)["tsl"]
    hex = f'#{"".join([f"{int(x*255):02x}" for x in hls_to_rgb(t + .5 % 1, l, s)])}'
    return f"{color} => {hex}"