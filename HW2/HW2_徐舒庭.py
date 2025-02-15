from psychopy import core,visual,event
import socket,pickle

code='utf-8'
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('hpc.psy.ntu.edu.tw', 1234))
c.sendall('b11705018'.encode(code)) # Change your ID here!
print(c.recv(9).decode(code)) # Should show your ID!

w=visual.Window(size=[800,400],units='norm')
for t in range(8):
    sz=int(c.recv(2).decode(code)) # size
    word=pickle.loads(c.recv(sz))
    print(word)
    # Make your changes here (4 points for graphical displaying):
    text = word['text']
    color = word['color']

    text_stim = visual.TextStim(w, text=text, color=color, height=0.1)
    text_stim.draw()
    w.flip()
    
    r=event.waitKeys(keyList=['r','g','b','y'],timeStamped=core.Clock())
    c.sendall(pickle.dumps(r[0]))

print(c.recv(5).decode(code)) # 4 points for passing
