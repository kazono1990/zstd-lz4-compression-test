import warnings
import zlib
import zstd
import lz4.frame
import time

warnings.simplefilter('ignore')


DATA_DIR = './data'
TYPES = ['ascii', 'random']
LIBRARIES = ['zlib', 'zstd', 'lz4']
SIZES = [
        # 0,
        4,
        16,
        256,
        1024,
        4096
        ]


def calc_comp_ration(compressed_data, byte_data):
    return len(byte_data) / len(compressed_data)


def decompression(compressed_data, compression_type):
    start = time.time()
    if(compression_type == 'zstd'):
        s = zstd.decompress(compressed_data)
    elif (compression_type == 'zlib'):
        s = zlib.decompress(compressed_data)
    else:
        s = lz4.frame.decompress(compressed_data)
    decomp_time = time.time() - start

    return decomp_time


def compression(byte_data, data_type, data_length, compression_type):
    start = time.time()
    if (compression_type == 'zstd'):
        compressed_data = zstd.compress(byte_data, 1)
    elif (compression_type == "zlib"):
        compressed_data = zlib.compress(byte_data)
    else:
        compressed_data = lz4.frame.compress(byte_data)
    comp_time = time.time() - start

    return (comp_time, compressed_data)


def main():
    for compression_type in LIBRARIES:
        print('# [COMPRESSION TYPE]: %s' % (compression_type))
        for data_type in TYPES:
            print('# [DATA TYPE] %s' % (data_type))
            print('DATA SIZE\t COMP TIME\t DECOMP TIME\t COMP RAITON')
            for data_length in SIZES:
                filename = '{0}/data_{1}_{2}KB.bin'.format(DATA_DIR, data_type, data_length)
                with open(filename, 'rb') as f:
                    byte_data = f.read()
                    comp_time, compressed_data = compression(byte_data, data_type, data_length, compression_type)
                    decomp_time = decompression(compressed_data, compression_type)
                    comp_ration = calc_comp_ration(compressed_data, byte_data)

                    print('%9d\t %.6f\t %.6f\t %.6f\t' % (data_length, comp_time * 1000, decomp_time * 1000, comp_ration))
                    f.close()
        print('####################')


if __name__ == '__main__':
    main()
