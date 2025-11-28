import multiprocessing
import requests

url="https://picsum.photos/200/300"

def downloadFile(url,name):
    response=requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    print(f"Finished downloading file{name}")

if __name__ == '__main__':
    pros=[]
    for i in range(7):
            p = multiprocessing.Process(target=downloadFile, args=[url, i])
            p.start()
            pros.append(p)

    for p in pros:
            p.join() # main program waits until this download finishes


