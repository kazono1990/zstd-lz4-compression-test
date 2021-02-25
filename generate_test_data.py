import os
import string
import random

DATA_DIR = 'data'
TYPES = ['ascii', 'random']
SIZES = [
        4,
        16,
        256,
        1024,
        4096
        ]


def create_data_dir():
    if not os.path.isdir(DATA_DIR):
        print('There is no data directory.')
        os.mkdir(DATA_DIR)
        print('Created directory [%s]' % DATA_DIR)


def generate_binary_data(data_type, data_size):
    file_name = "{0}/data_{1}_{2}KB.bin".format(DATA_DIR, data_type, data_size)
    with open (file_name, 'wb') as f:
        byte_array = bytearray([])
        if data_type == 'ascii':
            byte_array.extend([ord(random.choice(string.ascii_letters)) for i in range(data_size * 1024)])
        else:
            byte_array.extend([random.randint(0, 255) for i in range(data_size * 1024)])
        f.write(byte_array)
    print('Generate data(Data type:[%s], Data size:[%dKB])' % (data_type, data_size))


def main():
    create_data_dir()
    for data_type in TYPES:
        for data_size in SIZES:
            generate_binary_data(data_type, data_size)

if __name__ == '__main__':
    main()
