# coding: utf-8

import io, os
import sys
import urllib.request as request

BUFF_SIZE = 1024
path = os.path.join("Livro Estudo Python", "saida.zip")

def download_length(response, output, length):
    times = length // BUFF_SIZE

    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE ))
        print("Downloaded %d" % (((time * BUFF_SIZE )/length)*100))

def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE )
        total_download += len(data)
        if not data:
            break
        output.write(data)
        # print("Downloaded {bites}".format(bytes=total_download))
        print(f"Downloaded {total_download}")


def main():
    response = request.urlopen(sys.argv[1])
    # response = request.urlopen("http://livropython.com.br/dados.zip")
    # out_file = io.FileIO("Livro Estudo Python\saida.zip",mode="w")
    out_file = io.FileIO(path,mode="wb")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response,out_file,length)
    else:
        download(response,out_file)
    
    response.close()
    #out_file()
    out_file.close() 
    print("Finished")

if __name__ == "__main__":
    main()