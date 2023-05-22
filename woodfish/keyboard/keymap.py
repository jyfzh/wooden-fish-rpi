import logging


# Map modifier keys to array element in the bit array
modkeys = {
    "LEFTALT": 5,
    "LEFTCTRL": 7,
    "LEFTMETA": 4,
    "LEFTSHIFT": 6,
    "RIGHTALT": 1,
    "RIGHTCTRL": 3,
    "RIGHTMETA": 0,
    "RIGHTSHIFT": 2,
}


# Convert key to a HID code
keytable = {
    "0": (39, None),
    ")": (39, modkeys["LEFTSHIFT"]),
    "1": (30, None),
    "!": (30, modkeys["LEFTSHIFT"]),
    "2": (31, None),
    "@": (31, modkeys["LEFTSHIFT"]),
    "3": (32, None),
    "#": (32, modkeys["LEFTSHIFT"]),
    "4": (33, None),
    "$": (33, modkeys["LEFTSHIFT"]),
    "5": (34, None),
    "%": (34, modkeys["LEFTSHIFT"]),
    "6": (35, None),
    "^": (35, modkeys["LEFTSHIFT"]),
    "7": (36, None),
    "&": (36, modkeys["LEFTSHIFT"]),
    "8": (37, None),
    "*": (37, modkeys["LEFTSHIFT"]),
    "9": (38, None),
    "(": (38, modkeys["LEFTSHIFT"]),
    "102ND": (100, None),
    "AGAIN": (121, None),
    "'": (52, None),
    '"': (52, modkeys["LEFTSHIFT"]),
    "a": (4, None),
    "A": (4, modkeys["LEFTSHIFT"]),
    "\\": (50, None),
    "BACKSPACE": (42, None),
    "BACK": (241, None),
    "b": (5, None),
    "B": (5, modkeys["LEFTSHIFT"]),
    "CALC": (251, None),
    "CAPSLOCK": (57, None),
    "COFFEE": (249, None),
    ",": (54, None),
    "<": (54, modkeys["LEFTSHIFT"]),
    "COMPOSE": (101, None),
    "COPY": (124, None),
    "CUT": (123, None),
    "c": (6, None),
    "C": (6, modkeys["LEFTSHIFT"]),
    "DELETE": (76, None),
    ".": (55, None),
    ">": (55, modkeys["LEFTSHIFT"]),
    "DOWN": (81, None),
    "d": (7, None),
    "D": (7, modkeys["LEFTSHIFT"]),
    "EDIT": (247, None),
    "EJECTCD": (236, None),
    "END": (77, None),
    "\n": (40, None),
    "=": (46, None),
    "+": (46, modkeys["LEFTSHIFT"]),
    "ESC": (41, None),
    "e": (8, None),
    "E": (8, modkeys["LEFTSHIFT"]),
    "F1": (58, None),
    "F2": (59, None),
    "F3": (60, None),
    "F4": (61, None),
    "F5": (62, None),
    "F6": (63, None),
    "F7": (64, None),
    "F8": (65, None),
    "F9": (66, None),
    "F10": (67, None),
    "F11": (68, None),
    "F12": (69, None),
    "F13": (104, None),
    "F14": (105, None),
    "F15": (106, None),
    "F16": (107, None),
    "F17": (108, None),
    "F18": (109, None),
    "F19": (110, None),
    "F20": (111, None),
    "F21": (112, None),
    "F22": (113, None),
    "F23": (114, None),
    "F24": (115, None),
    "FIND": (244, None),
    "FORWARD": (242, None),
    "FRONT": (119, None),
    "f": (9, None),
    "F": (9, modkeys["LEFTSHIFT"]),
    "`": (53, None),
    "~": (53, modkeys["LEFTSHIFT"]),
    "g": (10, None),
    "G": (10, modkeys["LEFTSHIFT"]),
    "HANGEUL": (144, None),
    "HANJA": (145, None),
    "HELP": (117, None),
    "HENKAN": (138, None),
    "HIRAGANA": (147, None),
    "HOME": (74, None),
    "h": (11, None),
    "H": (11, modkeys["LEFTSHIFT"]),
    "INSERT": (73, None),
    "i": (12, None),
    "I": (12, modkeys["LEFTSHIFT"]),
    "j": (13, None),
    "J": (13, modkeys["LEFTSHIFT"]),
    "KATAKANAHIRAGANA": (136, None),
    "KATAKANA": (146, None),
    "KP0": (98, None),
    "KP1": (89, None),
    "KP2": (90, None),
    "KP3": (91, None),
    "KP4": (92, None),
    "KP5": (93, None),
    "KP6": (94, None),
    "KP7": (95, None),
    "KP8": (96, None),
    "KP9": (97, None),
    "KPASTERISK": (85, None),
    "KPCOMMA": (133, None),
    "KPDOT": (99, None),
    "KPENTER": (88, None),
    "KPEQUAL": (103, None),
    "KPJPCOMMA": (140, None),
    "KPMINUS": (86, None),
    "KPPLUS": (87, None),
    "KPSLASH": (84, None),
    "k": (14, None),
    "K": (14, modkeys["LEFTSHIFT"]),
    "LEFTALT": (226, None),
    "[": (47, None),
    "{": (47, modkeys["LEFTSHIFT"]),
    "LEFTCTRL": (224, None),
    "LEFTMETA": (227, None),
    "LEFTSHIFT": (225, None),
    "LEFT": (80, None),
    "l": (15, None),
    "L": (15, modkeys["LEFTSHIFT"]),
    "-": (45, None),
    "_": (45, modkeys["LEFTSHIFT"]),
    "MUHENKAN": (139, None),
    "MUTE": (239, None),
    "m": (16, None),
    "M": (16, modkeys["LEFTSHIFT"]),
    "NEXTSONG": (235, None),
    "NUMLOCK": (83, None),
    "n": (17, None),
    "N": (17, modkeys["LEFTSHIFT"]),
    "OPEN": (116, None),
    "o": (18, None),
    "O": (18, modkeys["LEFTSHIFT"]),
    "PAGEDOWN": (78, None),
    "PAGEUP": (75, None),
    "PASTE": (125, None),
    "PAUSE": (72, None),
    "PLAYPAUSE": (232, None),
    "POWER": (102, None),
    "PREVIOUSSONG": (234, None),
    "PROPS": (118, None),
    "p": (19, None),
    "P": (19, modkeys["LEFTSHIFT"]),
    "q": (20, None),
    "Q": (20, modkeys["LEFTSHIFT"]),
    "REFRESH": (250, None),
    "RESERVED": (0, None),
    "RIGHTALT": (230, None),
    "]": (48, None),
    "}": (48, modkeys["LEFTSHIFT"]),
    "RIGHTCTRL": (228, None),
    "RIGHTMETA": (231, None),
    "RIGHTSHIFT": (229, None),
    "RIGHT": (79, None),
    "RO": (135, None),
    "r": (21, None),
    "R": (21, modkeys["LEFTSHIFT"]),
    "SCROLLDOWN": (246, None),
    "SCROLLLOCK": (71, None),
    "SCROLLUP": (245, None),
    ";": (51, None),
    ":": (51, modkeys["LEFTSHIFT"]),
    "/": (56, None),
    "?": (56, modkeys["LEFTSHIFT"]),
    "SLEEP": (248, None),
    " ": (44, None),
    "STOPCD": (233, None),
    "STOP": (243, None),
    "SYSRQ": (70, None),
    "s": (22, None),
    "S": (22, modkeys["LEFTSHIFT"]),
    "TAB": (43, None),
    "t": (23, None),
    "T": (23, modkeys["LEFTSHIFT"]),
    "UNDO": (122, None),
    "UP": (82, None),
    "u": (24, None),
    "U": (24, modkeys["LEFTSHIFT"]),
    "VOLUMEDOWN": (238, None),
    "VOLUMEUP": (237, None),
    "v": (25, None),
    "V": (25, modkeys["LEFTSHIFT"]),
    "WWW": (240, None),
    "w": (26, None),
    "W": (26, modkeys["LEFTSHIFT"]),
    "x": (27, None),
    "X": (27, modkeys["LEFTSHIFT"]),
    "YEN": (137, None),
    "y": (28, None),
    "Y": (28, modkeys["LEFTSHIFT"]),
    "ZENKAKUHANKAKU": (148, None),
    "z": (29, None),
    "Z": (29, modkeys["LEFTSHIFT"]),
}


def convert_char_to_hid(char):
    kc = 0
    mk = 0
    if char in keytable:
        hid_code = keytable[char]
        kc = hid_code[0]
        mk = 0 if hid_code[1] is None else hid_code[1]
    else:
        logging.warn("Unknown char: %s", char)
    return [0xA1, 1, mk, 0, kc, 0, 0, 0, 0, 0]