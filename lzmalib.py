import lzma
import shutil

def compress_file(path: str, output: str):
    compressor = lzma.LZMACompressor()
    with open(path, 'rb') as input:
        with open(output, 'wb') as output:
            while True:
                chunk = input.read(1024)
                if not chunk:
                    break
                output.write(compressor.compress(chunk))
            output.write(compressor.flush())

def decompress_file(path: str, output: str):
    with lzma.open(path, "rb") as fsrc:
        with open(output, "wb") as fdst:
            shutil.copyfileobj(fsrc, fdst)

    

if __name__ == "__main__":
    compress_file("TestProj/test.exe", "test.xz")
    print("Decompressing")
    decompress_file("test.xz", "test.file.exe")