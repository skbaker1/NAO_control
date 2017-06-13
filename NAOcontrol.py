from Tkinter import *
import sys
from naoqi import ALProxy
from naoqi import motion
import time
import almath



root = Tk()

def main(robotIP):
   PORT = 9559
   
   try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
   except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)

        
   try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
   except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e


##_______________________________________________________________________##
        
   menubar = Menu(root)     
   def donothing(): 
      print "dummy button"

   def openHand(): 
      motionProxy.openHand('RHand')

   def stand():
      postureProxy.goToPosture("Stand", 0.5)
   def standInit():
      postureProxy.goToPosture("StandInit", 0.5)
   def standZero():
      postureProxy.goToPosture("StandZero", 0.5)
   def sitRelax():
      postureProxy.goToPosture("SitRelax", 0.5)
   def sit():
      postureProxy.goToPosture("Sit", 0.5) 
   def crouch():
      postureProxy.goToPosture("Crouch", 0.5) 
   def lyingBelly():
      postureProxy.goToPosture("LyingBelly", 0.5)
   def lyingBack():
      postureProxy.goToPosture("LyingBack", 0.5)
     
##_________________________________STIFFNESS______________________________________##
   
   def stiffnessOff():
      pNames = "Body"
      pStiffnessLists = 0.0
      pTimeLists = 1.0
      motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

   stiffnessOff = Button(root, text ="OFF", command = stiffnessOff)
   stiffnessOff.pack()

   def stiffnessOn():
      pNames = "Body"
      pStiffnessLists = 1.0
      pTimeLists = 1.0
      motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
      
   stiffnessOn = Button(root, text ="ON", command = stiffnessOn)
   stiffnessOn.pack()


   # Example that finds the difference between the command and sensed angles.
    names         = "Body"
    useSensors    = False
    commandAngles = motionProxy.getAngles(names, useSensors)
    print "Command angles:"
    print str(commandAngles)
    print ""

    useSensors  = True
    sensorAngles = motionProxy.getAngles(names, useSensors)
    print "Sensor angles:"
    print str(sensorAngles)
    print ""

    errors = []
    for i in range(0, len(commandAngles)):
        errors.append(commandAngles[i]-sensorAngles[i])
    print "Errors"
    print errors


##_________________________________FRAMES______________________________________##

   # frames for the buttons
   topframe = Frame(root)
   topframe.pack( side = TOP )

   frame = Frame(root)
   frame.pack( side = LEFT )

   bottomframe = Frame(root)
   bottomframe.pack( side = TOP )


##_________________________________HEAD STUFF______________________________________##

##   def moveHead():
##       pitch = enHpitch.get()
##       yaw = enHyaw.get()
##
##       motionProxy.setStiffnesses("Head", 1.0)
##       names  = ["HeadYaw", "HeadPitch"]
##       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
##       fractionMaxSpeed  = 0.2
##       motionProxy.setAngles(names, angles, fractionMaxSpeed)
##
##       time.sleep(3.0)
##       motionProxy.setStiffnesses("Head", 0.0)
##
##       print "HEAD PITCH: " + pitch + "      HEAD YAW: " + yaw
##
##   
##   def moveHead2(pitch, yaw):
##
##       motionProxy.setStiffnesses("Head", 1.0)
##       names  = ["HeadYaw", "HeadPitch"]
##       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
##       fractionMaxSpeed  = 0.2
##       motionProxy.setAngles(names, angles, fractionMaxSpeed)
##
##       time.sleep(3.0)
##       motionProxy.setStiffnesses("Head", 0.0)
##
##
##
##
##   # HEAD
##   Hpitch = Label(topframe, text="Head pitch:").pack( side = TOP )
##   enHpitch = Entry(topframe)
##   enHpitch.pack(side = TOP )
##
##   Hyaw = Label(topframe, text="Head yaw:")
##   Hyaw.pack( side = TOP )
##   enHyaw = Entry(topframe)
##   enHyaw.pack( side = TOP )
##
##   button1 = Button(topframe, text="APPLY", width=10, command=moveHead)
##   button1.pack( side = TOP )
##
##   # head diagram
##   headbutton = Button(topframe, text="HEAD")
##   headbutton.pack( side = TOP )
##   photo = PhotoImage(file="head.gif")
##   a = Label(headbutton, image=photo)
##   a.photo = photo
##   a.pack( side = TOP )
##
##
##   def saveAsH():
##       menuPlace = 306
##       pitchSave = enHpitch.get()
##       yawSave = enHyaw.get()
##       name = enb2.get()
##
##       f = open("NAOcontrol.py", "r")
##       contents = f.readlines()
##       f.close() 
##
##       contents.insert(menuPlace, "\n   headmenu.add_separator() \n   headmenu.add_command(label='" + name + "', command=lambda: moveHead2(" + pitchSave + ", " + yawSave + "))")
##       
##       f = open("NAOcontrol.py", "w")
##       contents = "".join(contents)
##       f.write(contents)
##       f.close()
##
##   
##       
##   # SAVE AS (HEAD)
##   b2 = Label(topframe, text="Save as:").pack( side = TOP)
##   enb2 = Entry(topframe)
##   enb2.pack(side = TOP)
##   button2 = Button(topframe, text="Save", width=10, command=saveAsH)
##   button2.pack( side = TOP )
##

##_________________________________LEFT ARM STUFF______________________________________##

##   def moveLeftArm():
##
##       shoulderPitch = enLSpitch.get()
##       shoulderRoll = enLSroll.get()
##       elbowYaw = enLEyaw.get()
##       elbowRoll = enLEroll.get()
##       wristYaw = enLWyaw.get()
##       
##
##       motionProxy.setStiffnesses("LArm", 1.0)
##       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
##       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
##       fractionMaxSpeed  = 0.2
##       motionProxy.setAngles(names, angles, fractionMaxSpeed)
##
##       #time.sleep(3.0)
##       #motionProxy.setStiffnesses("LArm", 0.0)
##
##       print "SHOULDER PITCH: " + shoulderPitch + "   SHOULDER ROLL: " + shoulderRoll + "   ELBOW YAW: " + elbowYaw + "   ELBOW ROLL: " + elbowRoll + "   WRIST YAW: " + wristYaw
##
##   
##   def moveLeftArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):
##
##       motionProxy.setStiffnesses("LArm", 1.0)
##       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
##       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
##       fractionMaxSpeed  = 0.2
##       motionProxy.setAngles(names, angles, fractionMaxSpeed)
##
##       #time.sleep(3.0)
##       #motionProxy.setStiffnesses("LArm", 0.0)
##
##
##
##   # LEFT ARM
##   LSpitch = Label(frame, text="Left Shoulder pitch: ")
##   LSpitch.pack( side = TOP )
##   enLSpitch = Entry(frame)
##   enLSpitch.pack( side = TOP )
##   
##   LSroll = Label(frame, text="Left Shoulder roll: ")
##   LSroll.pack( side = TOP )
##   enLSroll = Entry(frame)
##   enLSroll.pack( side = TOP )
##   
##   LEyaw = Label(frame, text="Left Elbow yaw: ")
##   LEyaw.pack( side = TOP )
##   enLEyaw = Entry(frame)
##   enLEyaw.pack( side = TOP )
##   
##   LEroll = Label(frame, text="Left Elbow roll: ")
##   LEroll.pack( side = TOP )
##   enLEroll = Entry(frame)
##   enLEroll.pack( side = TOP )
##   
##   LWyaw = Label(frame, text="Left Wrist yaw: ")
##   LWyaw.pack( side = TOP )
##   enLWyaw = Entry(frame)
##   enLWyaw.pack( side = TOP )
##   
##   
##   button3 = Button(frame, text="APPLY", width=10, command=moveLeftArm)
##   button3.pack( side = TOP )
##
##   # left arm diagram
##   leftarmbutton = Button(topframe, text="LEFT ARM")
##   leftarmbutton.pack( side = TOP )
##   photo = PhotoImage(file="leftarm.gif")
##   a = Label(leftarmbutton, image=photo)
##   a.photo = photo
##   a.pack( side = TOP )
##
##
##   def saveAsLA():
##       menuPlace = 321
##       shoulderPitchSave = enLSpitch.get()
##       shoulderRollSave = enLSroll.get()
##       elbowYawSave = enLEyaw.get()
##       elbowRollSave = enLEroll.get()
##       wristYawSave = enLWyaw.get()
##       name = enb4.get()
##
##       f = open("NAOcontrol.py", "r")
##       contents = f.readlines()
##       f.close() 
##
##       contents.insert(menuPlace, "\n   leftarmmenu.add_separator() \n   leftarmmenu.add_command(label='" + name + "', command=lambda: moveLeftArm2(" + shoulderPitchSave + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
##       
##       f = open("NAOcontrol.py", "w")
##       contents = "".join(contents)
##       f.write(contents)
##       f.close()
##
##   
##       
##   # SAVE AS (LEFT ARM)
##   b4 = Label(frame, text="Save as:").pack( side = LEFT)
##   enb4 = Entry(frame)
##   enb4.pack(side = LEFT)
##   button4 = Button(frame, text="Save", width=10, command=saveAsLA)
##   button4.pack( side = LEFT )
##

   ##_________________________________RIGHT ARM STUFF______________________________________##

   def moveRightArm():

       shoulderPitch = enRSpitch.get()
       shoulderRoll = enRSroll.get()
       elbowYaw = enREyaw.get()
       elbowRoll = enREroll.get()
       wristYaw = enRWyaw.get()
       

       motionProxy.setStiffnesses("RArm", 1.0)
       names  = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

       #time.sleep(3.0)
       #motionProxy.setStiffnesses("LArm", 0.0)

       print "SHOULDER PITCH: " + shoulderPitch + "   SHOULDER ROLL: " + shoulderRoll + "   ELBOW YAW: " + elbowYaw + "   ELBOW ROLL: " + elbowRoll + "   WRIST YAW: " + wristYaw

   
   def moveRightArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):

       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

       #time.sleep(3.0)
       #motionProxy.setStiffnesses("LArm", 0.0)



   # RIGHT ARM
   RSpitch = Label(frame, text="Right Shoulder pitch: ")
   RSpitch.pack( side = TOP )
   enRSpitch = Entry(frame)
   enRSpitch.pack( side = TOP )
   
   RSroll = Label(frame, text="Right Shoulder roll: ")
   RSroll.pack( side = TOP )
   enRSroll = Entry(frame)
   enRSroll.pack( side = TOP )
   
   REyaw = Label(frame, text="Right Elbow yaw: ")
   REyaw.pack( side = TOP )
   enREyaw = Entry(frame)
   enREyaw.pack( side = TOP )
   
   REroll = Label(frame, text="Right Elbow roll: ")
   REroll.pack( side = TOP )
   enREroll = Entry(frame)
   enREroll.pack( side = TOP )
   
   RWyaw = Label(frame, text="Right Wrist yaw: ")
   RWyaw.pack( side = TOP )
   enRWyaw = Entry(frame)
   enRWyaw.pack( side = TOP )
   
   
   button5 = Button(frame, text="APPLY", width=10, command=moveRightArm)
   button5.pack( side = TOP )

   # left arm diagram
   rightarmbutton = Button(topframe, text="RIGHT ARM")
   rightarmbutton.pack( side = TOP )
   photo = PhotoImage(file="rightarm.gif")
   a = Label(rightarmbutton, image=photo)
   a.photo = photo
   a.pack( side = TOP )


   def saveAsRA():
       menuPlace = 441
       shoulderPitchSave = enRSpitch.get()
       shoulderRollSave = enRSroll.get()
       elbowYawSave = enREyaw.get()
       elbowRollSave = enREroll.get()
       wristYawSave = enRWyaw.get()
       name = enb6.get()

       f = open("NAOcontrol.py", "r")
       contents = f.readlines()
       f.close() 

       contents.insert(menuPlace, "\n   rightarmmenu.add_separator() \n   rightarmmenu.add_command(label='" + name + "', command=lambda: moveRightArm2(" + shoulderPitchSave + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
       
       f = open("NAOcontrol.py", "w")
       contents = "".join(contents)
       f.write(contents)
       f.close()

   
       
   # SAVE AS (LEFT ARM)
   b6 = Label(frame, text="Save as:").pack( side = LEFT)
   enb6 = Entry(frame)
   enb6.pack(side = LEFT)
   button6 = Button(frame, text="Save", width=10, command=saveAsRA)
   button6.pack( side = LEFT )


##__________________________________MENUS_____________________________________##
   

   menubar = Menu(root)
   # POSTURE MENU
   posturemenu = Menu(menubar, tearoff=0)
   posturemenu.add_command(label="Stand", command=stand)
   posturemenu.add_separator()
   posturemenu.add_command(label="StandInit", command=standInit)
   posturemenu.add_separator()
   posturemenu.add_command(label="StandZero", command=standZero)
   posturemenu.add_separator()
   posturemenu.add_command(label="SitRelax", command=sitRelax)
   posturemenu.add_separator()
   posturemenu.add_command(label="Sit", command=sit)
   posturemenu.add_separator()
   posturemenu.add_command(label="Crouch", command=crouch)
   posturemenu.add_separator()
   posturemenu.add_command(label="LyingBelly", command=lyingBelly)
   posturemenu.add_separator()
   posturemenu.add_command(label="LyingBack", command=lyingBack)

   menubar.add_cascade(label="Posture", menu=posturemenu)

   # HEAD MENU

   headmenu = Menu(menubar, tearoff=0)










   menubar.add_cascade(label="Head", menu=headmenu)


   leftarmmenu = Menu(menubar, tearoff=0)










   menubar.add_cascade(label="Left Arm", menu=leftarmmenu)
   

   rightarmmenu = Menu(menubar, tearoff=0)










   menubar.add_cascade(label="Right Arm", menu=rightarmmenu)
   
   root.config(menu=menubar)
   root.mainloop()


##_________________________________MAIN______________________________________##
   

if __name__ == "__main__":
    robotIp = "10.218.107.156"


    if len(sys.argv) <= 1:
        print "Usage python almotion_openhand.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
