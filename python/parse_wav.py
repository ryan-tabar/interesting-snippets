# parsing wav data
try:
    with open("coin_roll.wav", "rb") as f:
        print(f"File Format..........{f.read(4).decode('ascii')}")
        print(f"File Size............{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"File Type Header.....{f.read(4).decode('ascii')}")
        print(f"Format Chunk Marker..{f.read(4).decode('ascii')}")
        print(f"Length of Format.....{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"Type of Format.......{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Number of Channels...{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Sample Rate..........{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"(SR * BPS * C) / 8...{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"(BPS * C / 8)........{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Bits Per Sample......{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"'data' chunk header..{f.read(4).decode('ascii')}")
        print(f"File Size (data).....{int.from_bytes(f.read(4), 'little', signed=False)}")

except IOError:
    print("Error While Openning the file!")
