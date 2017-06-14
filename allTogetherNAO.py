from Tkinter import *
import sys
from naoqi import ALProxy
from naoqi import motion
import time
import almath


root = Tk()
content = Frame(root)
frame = Frame(content, borderwidth=5, width=200, height=100)


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


##________________________________MENU FUNCTIONS_______________________________________##

       
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
   stiffnessOff = Button(content, text ="OFF", command = stiffnessOff)

   
   def stiffnessOn():
      pNames = "Body"
      pStiffnessLists = 1.0
      pTimeLists = 1.0
      motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
   stiffnessOn = Button(content, text ="ON", command = stiffnessOn)

   
   

##_________________________________HEAD STUFF______________________________________##

   def moveHead():
       pitch = enHpitch.get()
       yaw = enHyaw.get()
       motionProxy.setStiffnesses("Head", 1.0)
       names  = ["HeadYaw", "HeadPitch"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
       time.sleep(3.0)
       motionProxy.setStiffnesses("Head", 0.0)


   def moveHead2(pitch, yaw):
       motionProxy.setStiffnesses("Head", 1.0)
       names  = ["HeadYaw", "HeadPitch"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
       time.sleep(3.0)
       motionProxy.setStiffnesses("Head", 0.0)


   # HEAD
   Hpitch = Label(content, text="Head pitch:")
   enHpitch = Entry(content)

   Hyaw = Label(content, text="Head yaw:")
   enHyaw = Entry(content)

   apply1 = Button(content, text="APPLY", width=10, command=moveHead)


   # head diagram
   def saveAsH():
       menuPlace = 306
       pitchSave = enHpitch.get()
       yawSave = enHyaw.get()
       name = enb2.get()

       f = open("NAOcontrol.py", "r")
       contents = f.readlines()
       f.close() 

       contents.insert(menuPlace, "\n   headmenu.add_separator() \n   headmenu.add_command(label='" + name + "', command=lambda: moveHead2(" + pitchSave + ", " + yawSave + "))")
   
       f = open("NAOcontrol.py", "w")
       contents = "".join(contents)
       f.write(contents)
       f.close()


	   
   # SAVE AS (HEAD)
   saveAs1 = Label(content, text="Save as:")
   ensaveAs1 = Entry(content)
   bSave1 = Button(content, text="Save", width=10, command=saveAsH)



##_________________________________LEFT ARM STUFF______________________________________##

   def moveLeftArm():
       shoulderPitch = enLSpitch.get()
       shoulderRoll = enLSroll.get()
       elbowYaw = enLEyaw.get()
       elbowRoll = enLEroll.get()
       wristYaw = enLWyaw.get()
	   
       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

	   
   
   def moveLeftArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):

       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)


   # LEFT ARM
   LSpitch = Label(content, text="Left Shoulder pitch: ")
   enLSpitch = Entry(content)
   
   LSroll = Label(content, text="Left Shoulder roll: ")
   enLSroll = Entry(content)
   
   LEyaw = Label(content, text="Left Elbow yaw: ")
   enLEyaw = Entry(content)
  
   LEroll = Label(content, text="Left Elbow roll: ")
   enLEroll = Entry(content)
   
   LWyaw = Label(content, text="Left Wrist yaw: ")
   enLWyaw = Entry(content)


   apply2 = Button(content, text="APPLY", width=10, command=moveLeftArm)



   def saveAsLA():
       menuPlace = 321
       shoulderPitchSave = enLSpitch.get()
       shoulderRollSave = enLSroll.get()
       elbowYawSave = enLEyaw.get()
       elbowRollSave = enLEroll.get()
       wristYawSave = enLWyaw.get()
       name = enb4.get()

       f = open("NAOcontrol.py", "r")
       contents = f.readlines()
       f.close() 
       contents.insert(menuPlace, "\n   leftarmmenu.add_separator() \n   leftarmmenu.add_command(label='" + name + "', command=lambda: moveLeftArm2(" + shoulderPitchSave + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
       
       f = open("NAOcontrol.py", "w")
       contents = "".join(contents)
       f.write(contents)
       f.close()


       
   # SAVE AS (RIGHT ARM)
   saveAs2 = Label(content, text="Save as:")
   ensaveAs2 = Entry(content)
   bSave2 = Button(content, text="Save", width=10, command=saveAsLA)


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
       

   def moveRightArm2(shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw):
       motionProxy.setStiffnesses("LArm", 1.0)
       names  = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(shoulderPitch)*almath.TO_RAD, float(shoulderRoll)*almath.TO_RAD, float(elbowYaw)*almath.TO_RAD, float(elbowRoll)*almath.TO_RAD, float(wristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)

       #time.sleep(3.0)
       #motionProxy.setStiffnesses("LArm", 0.0)


   # RIGHT ARM

   RSpitch = Label(content, text="Right Shoulder pitch: ")
   enRSpitch = Entry(content)
  
   RSroll = Label(content, text="Right Shoulder roll: ")
   enRSroll = Entry(content)

   REyaw = Label(content, text="Right Elbow yaw: ")
   enREyaw = Entry(content)

   REroll = Label(content, text="Right Elbow roll: ")
   enREroll = Entry(content)

   RWyaw = Label(content, text="Right Wrist yaw: ")
   enRWyaw = Entry(content)

   apply3 = Button(content, text="APPLY", width=10, command=moveRightArm)




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
       contents = "".join(content)
       f.write(content)
       f.close()
       

   # SAVE AS (RIGHT ARM)
   saveAs3 = Label(content, text="Save as:")
   ensaveAs3 = Entry(content)
   bSave3 = Button(content, text="Save", width=10, command=saveAsRA)

   
   
   
   
##_________________________________GET ANGLES______________________________________##
   
   # Example that finds the difference between the command and sensed angles.
   def getAngles():
	   HeadPitch         	= "HeadPitch"
	   HeadYaw         		= "HeadYaw"
	   
	   LShoulderPitch 		= "LShoulderPitch"
	   LShoulderRoll 		= "LShoulderRoll"
	   LElbowRoll         	= "LElbowRoll"
	   LElbowYaw 			= "LElbowYaw"
	   LWristYaw         	= "LWristYaw"
	   
	   RShoulderPitch 		= "RShoulderPitch"
	   RShoulderRoll 		= "RShoulderRoll"
	   RElbowRoll 			= "RElbowRoll"
	   RElbowYaw 			= "RElbowYaw"
	   RWristYaw 			= "RWristYaw"
	   
	   useSensors  = True
	   HeadPitchAngle = str(motionProxy.getAngles(HeadPitch, useSensors))[1:5]
	   HeadYawAngle = str(motionProxy.getAngles(HeadYaw, useSensors))[1:5]
	   
	   LShoulderPitchAngle = str(motionProxy.getAngles(LShoulderPitch, useSensors))[1:10]
	   LShoulderRollAngle = str(motionProxy.getAngles(LShoulderRoll, useSensors))[1:10]
	   LElbowRollAngle = str(motionProxy.getAngles(LElbowRoll, useSensors))[1:10]
	   LElbowYawAngle = str(motionProxy.getAngles(LElbowYaw, useSensors))[1:10]
	   LWristYawAngle = str(motionProxy.getAngles(LWristYaw, useSensors))[1:10]
	   
	   RShoulderPitchAngle = str(motionProxy.getAngles(RShoulderPitch, useSensors))[1:10]
	   RShoulderRollAngle = str(motionProxy.getAngles(RShoulderRoll, useSensors))[1:10]
	   RElbowRollAngle = str(motionProxy.getAngles(RElbowRoll, useSensors))[1:10]
	   RElbowYawAngle = str(motionProxy.getAngles(RElbowYaw, useSensors))[1:10]
	   RWristYawAngle = str(motionProxy.getAngles(RWristYaw, useSensors))[1:10]
	   
	   enHpitch.delete(0, END)
	   enHpitch.insert(0, float(HeadPitchAngle)*almath.TO_DEG)

   getAngles = Button(content, text="Get Curent", width=10, command=getAngles)





##_________________________________GRID STUFF______________________________________##
   
   content.grid(column=0, row=0)
   frame.grid(column=0, row=0, columnspan=3, rowspan=2)
   
   stiffnessOff.grid(column=0, row=0)
   stiffnessOn.grid(column=1, row=0)


   Hpitch.grid(column=2, row=2)
   enHpitch.grid(column=2, row=3)
   Hyaw.grid(column=2, row=4)
   enHyaw.grid(column=2, row=5)
   apply1.grid(column=2, row=6)
   saveAs1.grid(column=2, row=7)
   ensaveAs1.grid(column=2, row=8)
   bSave1.grid(column=2, row=9)


   LSpitch.grid(column=3, row=2)
   enLSpitch.grid(column=3, row=3)
   LSroll.grid(column=3, row=4)
   enLSroll.grid(column=3, row=5)
   LEyaw.grid(column=3, row=6)
   enLEyaw.grid(column=3, row=7)
   LEroll.grid(column=3, row=8)
   enLEroll.grid(column=3, row=9)
   LWyaw.grid(column=3, row=10)
   enLWyaw.grid(column=3, row=11)
   apply2.grid(column=3, row=12)
   saveAs2.grid(column=3, row=13)
   ensaveAs2.grid(column=3, row=14)
   bSave2.grid(column=3, row=15)


   RSpitch.grid(column=4, row=2)
   enRSpitch.grid(column=4, row=3)
   RSroll.grid(column=4, row=4)
   enRSroll.grid(column=4, row=5)
   REyaw.grid(column=4, row=6)
   enREyaw.grid(column=4, row=7)
   REroll.grid(column=4, row=8)
   enREroll.grid(column=4, row=9)
   RWyaw.grid(column=4, row=10)
   enRWyaw.grid(column=4, row=11)
   apply3.grid(column=4, row=12)
   saveAs3.grid(column=4, row=13)
   ensaveAs3.grid(column=4, row=14)
   bSave3.grid(column=4, row=15)
   getAngles.grid(column=4, row=16)

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
