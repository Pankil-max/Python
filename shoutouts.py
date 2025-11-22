from  win32com.client import Dispatch

l=["Rahul","Prabesh","Ramrari padera gu khanu"]


def speak(str):
    speak=Dispatch(("SAPI.SPVOICE"))
    speak.speak(str)

if __name__=="__main__":
    for name in l:
        speak(name)