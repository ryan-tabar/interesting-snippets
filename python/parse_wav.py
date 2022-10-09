# parsing wav data and plotting it
import matplotlib.pyplot as plt

try:
    with open("one_small_step.wav", "rb") as f:
        file_size = 0
        data_size = 0
        bytes_per_second = 0

        # Total length of header should be 44 bytes
        print(f"File Format..........{f.read(4).decode('ascii')}")
        print(f"File Size............{(file_size := int.from_bytes(f.read(4), 'little', signed=False))}")
        print(f"File Type Header.....{f.read(4).decode('ascii')}")
        print(f"Format Chunk Marker..{f.read(4).decode('ascii')}")
        print(f"Length of Format.....{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"Type of Format.......{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Number of Channels...{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Sample Rate..........{int.from_bytes(f.read(4), 'little', signed=False)}")
        print(f"(SR * BPS * C) / 8...{(bytes_per_second := int.from_bytes(f.read(4), 'little', signed=False))}")
        print(f"(BPS * C / 8)........{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"Bits Per Sample......{int.from_bytes(f.read(2), 'little', signed=False)}")
        print(f"'data' chunk header..{f.read(4).decode('ascii')}")
        print(f"File Size (data).....{(data_size := int.from_bytes(f.read(4), 'little', signed=False))}")

        # sanity check
        if (file_size - data_size != 36):
            raise ValueError("Incorrect file or data size")

        # read 2 bytes at a time
        sample = int.from_bytes(f.read(2), 'little', signed=True)
        data = []
        while sample:
            data.append(sample)
            sample = int.from_bytes(f.read(2), 'little', signed=True)
        
        plt.plot(data)
        plt.ylabel("PCM data")
        plt.show()

except OSError as err:
    print(f"OS Error: {err}")

except ValueError as err:
    print(f"Value Error: {err}")