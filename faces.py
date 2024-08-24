import cv2
from tkinter import*
def checking():
    if box1.get()=="Admin" and box2.get()=='123':
        trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video=cv2.VideoCapture(0)
        while True:
            success,frame=video.read()
            if success==True:
                gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faces=trainedDataset.detectMultiScale(gray_img)
                for x,y,w,h in faces:
                    cv2.rectangle(frame, (x,y) , (x+w, y+h) , (0,0,255) , 2)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    org=(50,50)
                    thickness=2
                    color=(255,0,0)
                    fontScale=1
                    cv2.putText(frame,'person Founded',org,font,fontScale,color,thickness,cv2.LINE_AA)
                    cv2.imshow('video',frame)
                    key=cv2.waitKey(1)
                    if  key==83 or key==115:
                        break
                    else:
                        print('succes')
                        break
def close():
    t.destroy()
    


t=Tk()
t.title("Password Checking")
t.geometry("250x250")
t.config(bg='blue')
u1=Label(t,text="Username",fg='black',bg='blue',font=('Aerial',12))
u1.place(x=15,y=30)
box1=Entry(t,width=20)
box1.place(x=100,y=30)
u2=Label(t,text="Password",fg='black',bg='blue',font=('Aerial',12))
u2.place(x=15,y=70)
box2=Entry(t,width=20)
box2.place(x=100,y=70)
b1=Button(t,text="Login",command=checking,cursor="hand2")
b1.place(x=80,y=100)
b1=Button(t,text="Close",command=close,cursor="hand2")
b1.place(x=130,y=100)
t.mainloop()
