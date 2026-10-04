from pynput import keyboard
import time

Tks=0
Bks=0
keyfreq={}

def my_press_function(key):
    f=open("keystrokes.log", mode="a")

    global Tks
    Tks+=1

    if hasattr(key, 'char')==True:
        f.write(key.char)
        if key.char in keyfreq:
            keyfreq[key.char]+=1
        else:
            keyfreq[key.char]=1
    else:
        L=str(key)
        M=L[4:]
        L=f"[{M.upper()}]"
        f.write(L)
        if L in keyfreq:
            keyfreq[L]+=1
        else:
            keyfreq[L]=1

    M=time.localtime()
    L=f"[{M[3]}:{M[4]}:{M[5]}-{M[2]}/{M[1]}/{M[0]}]"
    f.write(L)
    if key==keyboard.Key.backspace:
        global Bks
        Bks+=1

    f.close()

def exc():
    listener.stop()
    hotkeys.stop()
    
hotkeys = keyboard.GlobalHotKeys({'<ctrl>+<alt>+r': exc})
    
listener=keyboard.Listener(on_press=my_press_function)
start=time.perf_counter()
listener.start()
hotkeys.start()

listener.join()
stop=time.perf_counter()

Ar=stop-start
E=f"{Ar:.2f}"
A=int(Ar)
B=(Tks*60)/(A*5)
C=(Tks-(Bks*2))*(60)/(A*5)
D=(Bks*100)/Tks

print("Total Keystrokes=",Tks,"\n")
print(f"Active runtime= {E} seconds \n")
print(f"Gross WPM={B:.0f} \n")
print(f"Net WPM={C:.0f} \n")
print(f"Backspace Error Rates={D:.2f} \n")

Max= None
MaxC=0
print("Top 5 keys used: \n")
for I in range(5):
    Max= None
    MaxC=0
    for k in keyfreq:
        if keyfreq[k]>MaxC:
            Max=k
            MaxC=keyfreq[k]
    print(I+1,".",Max,":",MaxC)
    keyfreq.pop(Max)
    
    
