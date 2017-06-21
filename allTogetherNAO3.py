from Tkinter import *
import sys
from naoqi import ALProxy
from naoqi import motion
import time
import almath

import threading
from threading import Thread



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


   try:
        tts = ALProxy("ALTextToSpeech", robotIP, PORT)
   except Exception,e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ",e
        sys.exit(1)
    


##________________________________MENU FUNCTIONS_______________________________________##

       
   menubar = Menu(root)     
   def donothing(): 
      print "dummy button"


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
       menuPlace = 559
       pitchSave = enHpitch.get()
       yawSave = enHyaw.get()
       name = ensaveAs1.get()

       f = open("allTogetherNAO.py", "r")
       contents = f.readlines()
       f.close() 

       contents.insert(menuPlace, "\n   headmenu.add_separator() \n   headmenu.add_command(label='" + name + "', command=lambda: moveHead2(" + pitchSave + ", " + yawSave + "))")
   
       f = open("allTogetherNAO.py", "w")
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
       menuPlace = 584
       shoulderPitchSave = enLSpitch.get()
       shoulderRollSave = enLSroll.get()
       elbowYawSave = enLEyaw.get()
       elbowRollSave = enLEroll.get()
       wristYawSave = enLWyaw.get()
       name = ensaveAs2.get()

       f = open("allTogetherNAO.py", "r")
       contents = f.readlines()
       f.close() 
       contents.insert(menuPlace, "\n   leftarmmenu.add_separator() \n   leftarmmenu.add_command(label='" + name + "', command=lambda: moveLeftArm2(" + shoulderPitchSave + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")
       
       f = open("allTogetherNAO.py", "w")
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
       motionProxy.setStiffnesses("RArm", 1.0)
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
       menuPlace = 609
       shoulderPitchSave = enRSpitch.get()
       shoulderRollSave = enRSroll.get()
       elbowYawSave = enREyaw.get()
       elbowRollSave = enREroll.get()
       wristYawSave = enRWyaw.get()
       name = ensaveAs3.get()


       f = open("allTogetherNAO.py", "r")
       contents = f.readlines()
       f.close() 

       contents.insert(menuPlace, "\n   rightarmmenu.add_separator() \n   rightarmmenu.add_command(label='" + name + "', command=lambda: moveRightArm2(" + shoulderPitchSave
                       + ", " + shoulderRollSave + ", " + elbowYawSave + ", "  + elbowRollSave + ", "  + wristYawSave + "))")

       f = open("allTogetherNAO.py", "w")
       contents = "".join(content)
       f.write(content)
       f.close()
       

   # SAVE AS (RIGHT ARM)
   saveAs3 = Label(content, text="Save as:")
   ensaveAs3 = Entry(content)
   bSave3 = Button(content, text="Save", width=10, command=saveAsRA)



   
   
##_________________________________FULL BODY STUFF______________________________________##

##   MULTITHREADING VERSION
##   def moveBody():
##      Thread(target = moveHead).start()
##      Thread(target = moveLeftArm).start()
##      Thread(target = moveRightArm).start()

   def moveBody():
       pitch = enHpitch.get()
       yaw = enHyaw.get()
        
       lshoulderPitch = enLSpitch.get()
       lshoulderRoll = enLSroll.get()
       lelbowYaw = enLEyaw.get()
       lelbowRoll = enLEroll.get()
       lwristYaw = enLWyaw.get()
       
       rshoulderPitch = enRSpitch.get()
       rshoulderRoll = enRSroll.get()
       relbowYaw = enREyaw.get()
       relbowRoll = enREroll.get()
       rwristYaw = enRWyaw.get()

       motionProxy.setStiffnesses("Body", 1.0)
       names  = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                 "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD,
                  float(lshoulderPitch)*almath.TO_RAD, float(lshoulderRoll)*almath.TO_RAD, float(lelbowYaw)*almath.TO_RAD, float(lelbowRoll)*almath.TO_RAD, float(lwristYaw)*almath.TO_RAD,
                  float(rshoulderPitch)*almath.TO_RAD, float(rshoulderRoll)*almath.TO_RAD, float(relbowYaw)*almath.TO_RAD, float(relbowRoll)*almath.TO_RAD, float(rwristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
        
   def moveBody2(yaw, pitch, lshoulderPitch, lshoulderRoll, lelbowYaw, lelbowRoll, lwristYaw,rshoulderPitch, rshoulderRoll, relbowYaw, relbowRoll, rwristYaw):
       motionProxy.setStiffnesses("Body", 1.0)
       names  = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                 "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
       angles  = [float(yaw)*almath.TO_RAD, float(pitch)*almath.TO_RAD,
                  float(lshoulderPitch)*almath.TO_RAD, float(lshoulderRoll)*almath.TO_RAD, float(lelbowYaw)*almath.TO_RAD, float(lelbowRoll)*almath.TO_RAD, float(lwristYaw)*almath.TO_RAD,
                  float(rshoulderPitch)*almath.TO_RAD, float(rshoulderRoll)*almath.TO_RAD, float(relbowYaw)*almath.TO_RAD, float(relbowRoll)*almath.TO_RAD, float(rwristYaw)*almath.TO_RAD]
       fractionMaxSpeed  = 0.2
       motionProxy.setAngles(names, angles, fractionMaxSpeed)
      

##
##
##   def saveAsAll():
##       menuPlace = 635
##
##       pitchSave = enHpitch.get()
##       yawSave = enHyaw.get()
##
##       lshoulderPitchSave = enLSpitch.get()
##       lshoulderRollSave = enLSroll.get()
##       lelbowYawSave = enLEyaw.get()
##       lelbowRollSave = enLEroll.get()
##       lwristYawSave = enLWyaw.get()
##       
##       rshoulderPitchSave = enRSpitch.get()
##       rshoulderRollSave = enRSroll.get()
##       relbowYawSave = enREyaw.get()
##       relbowRollSave = enREroll.get()
##       rwristYawSave = enRWyaw.get()
##       
##       name = ensaveAs4.get()
##
##
##       f = open("allTogetherNAO.py", "r")
##       contents = f.readlines()
##       f.close() 
##
##       #contents.insert(menuPlace, str(\n   bodymenu.add_separator() \n    bodymenu.add_command(label="name", command=lambda: moveBody2(pitchSave, yawSave, lshoulderPitchSave, lshoulderRollSave, lelbowYawSave, lelbowRollSave, lwristYawSave, rshoulderPitchSave, rshoulderRollSave, relbowYawSave, relbowRollSave, rwristYawSave))))       
##       #contents.insert(menuPlace, "\n   bodymenu.add_separator() \n    bodymenu.add_command(label='" + name + "', command=lambda: moveBody2(" + pitchSave + ", " + yawSave + ", " + lshoulderPitchSave + ", " + lshoulderRollSave + ", " + lelbowYawSave + ", "  + lelbowRollSave + ", " + lwristYawSave + ", " + rshoulderPitchSave + ", " + rshoulderRollSave + ", " + relbowYawSave + ", " + relbowRollSave + ", " + rwristYawSave + "))")
##       contents.insert(menuPlace, "\n   bodymenu.add_separator() \n   bodymenu.add_command(label='" + name + "', command=lambda: moveRightArm2(" + rshoulderPitchSave
##                       + ", " + rshoulderRollSave + ", " + relbowYawSave + ", "  + relbowRollSave + ", "  + rwristYawSave + "))")
##       
##       f = open("allTogetherNAO.py", "w")
##       contents = "".join(content)
##       f.write(content)
##       f.close()
##       
##
##   # SAVE AS (WHOLE BODY)
##   saveAs4 = Label(content, text="Save as:")
##   ensaveAs4 = Entry(content)
##   bSave4 = Button(content, text="Save all", width=10, command=saveAsAll)


      
   applyAll = Button(content, text="APPLY ALL", width=10, command=moveBody)

   def openRHand(): 
      motionProxy.openHand('RHand')
   def closeRHand(): 
      motionProxy.closeHand('RHand')
   def openLHand(): 
      motionProxy.openHand('LHand')
   def closeLHand(): 
      motionProxy.openHand('LHand')

##-------------------------------------------------------------------------------------

   def waveLeft():
      moveBody2(0.0, 0.0, -1.497, 27.332, -94.574, -86.835, 42.186, 80.072, -5.627, 47.899, 57.308, 3.337)
      openLHand()
      time.sleep(0.8)
      moveBody2(0.0, 0.0, -1.497, 27.332, -107.406, -74.618, 42.186, 80.072, -5.627, 47.899, 57.308, 3.337)
      time.sleep(0.8)
      moveBody2(0.0, 0.0, -1.497, 27.332, -94.574, -86.835, 42.186, 80.072, -5.627, 47.899, 57.308, 3.337)
      time.sleep(0.8)
      moveBody2(0.0, 0.0, -1.497, 27.332, -107.406, -74.618, 42.186, 80.072, -5.627, 47.899, 57.308, 3.337)
      time.sleep(0.8)
      moveBody2(0.0, 0.0, -1.497, 27.332, -94.574, -86.835, 42.186, 80.072, -5.627, 47.899, 57.308, 3.337)
      time.sleep(0.5)
      closeLHand()
      crouch()

   def waveRight():
      moveBody2(0.0, 0.0, 80.072, 9.666, -47.899, -57.308, 9.337, 1.497, -27.332, 94.574, 86.835, -42.186)
      openRHand()
      time.sleep(0.8)
      moveBody2(0.0, 0.0, 80.072, 9.666, -47.899, -57.308, 9.337, 1.497, -27.332, 107.406, 74.618, -42.186)
      time.sleep(0.8)
      moveBody2(0.0, 0.0,  80.072, 9.666, -47.899, -57.308, 9.337, 1.497, -27.332, 94.574, 86.835, -42.186)
      time.sleep(0.8)
      moveBody2(0.0, 0.0, 80.072, 9.666, -47.899, -57.308, 9.337, 1.497, -27.332, 107.406, 74.618, -42.186)
      time.sleep(0.8)
      moveBody2(0.0, 0.0, 80.072, 9.666, -47.899, -57.308, 9.337, 1.497, -27.332, 94.574, 86.835, -42.186)
      time.sleep(0.5)
      closeRHand()
      crouch()

##-------------------------------------------------------------------------------------

   def stopLeft():
      moveBody2(0.0, 0.0, 23.0, 0.0, -80.25, -61.308, 63.337, 79.497, -5.332, 51.574, 48.835, 10.186)
      openLHand()
      time.sleep(0.8)
      closeLHand()
      crouch()

   def stopRight():
      moveBody2(0.0, 0.0, 79.497, 5.332, -51.574, -60.835, 10.186, 33.0, 0.0, 80.25, 81.308, -63.337)
      openRHand()
      time.sleep(0.8)
      closeRHand()
      crouch()

##-------------------------------------------------------------------------------------

   def lookLeft():
      moveBody2(14.324, 22.918, 39.993, 30.149, -60.500, -2.0, 28.069, 80.594, -5.332, 51.574, 46.141, -6.798)
      openLHand()
      time.sleep(0.8)
      closeLHand()
      crouch()

   def lookRight():
      moveBody2(-14.324, 22.918, 80.594, 5.332, -51.574, -46.141, -29.798, 39.993, -30.149, 119.500, 2.0, -43.069)
      openRHand()
      time.sleep(0.8)
      closeRHand()
      crouch()

##-------------------------------------------------------------------------------------

   def cantHearLeft():
      moveBody2(-63.025, 5.730, 19.861, -2.385, -67.578, -88.500, 13.851, 79.984, -9.913, 47.272, 56.726, -2.621)
      openLHand()
      time.sleep(0.4)
      closeLHand()
      crouch()

   def cantHearRight():
      moveBody2(63.025, 5.730, 79.984, 9.913, -47.272, -56.726, 6.993, 11.149, -1.500, 64.0, 88.069, -5.364)
      openRHand()
      time.sleep(0.4)
      crouch()
      closeRHand()
      
##-------------------------------------------------------------------------------------

   def shakeNo():
      names  = ["HeadYaw","HeadPitch"]
      angleLists  = [[0.5, -0.5, 0.0], [0.0]]
      timeLists   = [[1.0, 2.0, 3.0], [1.0]]
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      tts.say("I do not agree")
      time.sleep(1.0)
      crouch()

   def startTeaching():
      names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
               "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
      angleLists  = [[0.0*almath.TO_RAD], [0.0*almath.TO_RAD],
                     [79.0*almath.TO_RAD],
                     [10.0*almath.TO_RAD],
                     [-47.0*almath.TO_RAD],
                     [-56.0*almath.TO_RAD],
                     [7.0*almath.TO_RAD],
                     [56.0*almath.TO_RAD, 79.9*almath.TO_RAD],
                     [7.0*almath.TO_RAD, -9.9*almath.TO_RAD],
                     [29.0*almath.TO_RAD, 47.2*almath.TO_RAD],
                     [88.0*almath.TO_RAD, 56.7*almath.TO_RAD],
                     [28.0*almath.TO_RAD, -2.6*almath.TO_RAD]]
      #*almath.TO_RAD
      timeLists   = [[1.0], [1.0],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5, 3.0],
                     [0.5, 3.0],
                     [0.5, 3.0],
                     [0.5, 3.0],
                     [0.5, 3.0]]
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      tts.say("So, I need to figure out where, and when, Lunara will be at different times in the race.")
      time.sleep(1.0)


   def teaching2():
      names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
               "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD, 5.0*almath.TO_RAD, 0.0*almath.TO_RAD, 5.0*almath.TO_RAD, 0.0*almath.TO_RAD],
                     [79.0*almath.TO_RAD],
                     [10.0*almath.TO_RAD],
                     [-47.0*almath.TO_RAD],
                     [-56.0*almath.TO_RAD],
                     [7.0*almath.TO_RAD],
                     [79.9*almath.TO_RAD],
                     [-9.9*almath.TO_RAD],
                     [47.2*almath.TO_RAD],
                     [56.7*almath.TO_RAD],
                     [-2.6*almath.TO_RAD]]
      #*almath.TO_RAD
      timeLists   = [[1.0],
                     [0.5, 0.7, 2.0, 4.0, 5.0],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5],
                     [0.5]]
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      tts.say("I know how long it took her too run 1 kilometer, and I know she runs consistantly,")
      time.sleep(1.0)

   def teaching3():
      names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
               "LWristYaw", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
      angleLists  = [[0.0*almath.TO_RAD],
                     [0.0*almath.TO_RAD],
                     
                     [52.0*almath.TO_RAD, 52.0*almath.TO_RAD, 52.0*almath.TO_RAD],
                     [3.0*almath.TO_RAD, -5.0*almath.TO_RAD, 3.0*almath.TO_RAD],
                     [-117.0*almath.TO_RAD, -119.0*almath.TO_RAD, -117.0*almath.TO_RAD],
                     [-75.0*almath.TO_RAD, -95.0*almath.TO_RAD, -75.0*almath.TO_RAD],
                     [-94.0*almath.TO_RAD, -94.0*almath.TO_RAD, -94.0*almath.TO_RAD],
                     
                     [52.9*almath.TO_RAD, 52.0*almath.TO_RAD, 52.9*almath.TO_RAD],
                     [-0.9*almath.TO_RAD, -5.0*almath.TO_RAD, -0.9*almath.TO_RAD],
                     [119.2*almath.TO_RAD, 119.0*almath.TO_RAD, 119.2*almath.TO_RAD],
                     [75.7*almath.TO_RAD, 96.0*almath.TO_RAD, 75.7*almath.TO_RAD],
                     [94.6*almath.TO_RAD, 94.0*almath.TO_RAD, 94.6*almath.TO_RAD]]
      #*almath.TO_RAD
      timeLists   = [[1.0],
                     [0.5],
                     
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5],
                     [0.5, 1.0, 2.5]]
      isAbsolute  = True
      # the post is so it happens at the same time as the speech
      motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
      tts.say("but I'm just not sure where to start to find out where she'll be after 3 kilometers.")
      time.sleep(1.0)


   def teachAll():
      tts.setVolume(1.0)
      startTeaching()
      teaching2()
      teaching3()


      
##_________________________________GET ANGLES______________________________________##
   
   # Example that finds the difference between the command and sensed angles.
   def getAngles():
      HeadYaw           = "HeadYaw"
      HeadPitch         = "HeadPitch"
      LShoulderPitch    = "LShoulderPitch"
      LShoulderRoll     = "LShoulderRoll"
      LElbowRoll        = "LElbowRoll"
      LElbowYaw         = "LElbowYaw"
      LWristYaw         = "LWristYaw"
      RShoulderPitch    = "RShoulderPitch"
      RShoulderRoll     = "RShoulderRoll"
      RElbowRoll        = "RElbowRoll"
      RElbowYaw         = "RElbowYaw"
      RWristYaw         = "RWristYaw"

      useSensors  = True
      HeadYawAngle = str(motionProxy.getAngles(HeadYaw, useSensors))[1:5]
      HeadPitchAngle = str(motionProxy.getAngles(HeadPitch, useSensors))[1:5]

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

      enHyaw.delete(0, END)
      enHyaw.insert(0, '%.3f'%(float(HeadYawAngle)*almath.TO_DEG))
      enHpitch.delete(0, END)
      enHpitch.insert(0, '%.3f'%(float(HeadPitchAngle)*almath.TO_DEG))

      enLSpitch.delete(0, END)
      enLSpitch.insert(0, '%.3f'%(float(LShoulderPitchAngle)*almath.TO_DEG))
      enLSroll.delete(0, END)
      enLSroll.insert(0, '%.3f'%(float(LShoulderRollAngle)*almath.TO_DEG))
      enLEroll.delete(0, END)
      enLEroll.insert(0, '%.3f'%(float(LElbowRollAngle)*almath.TO_DEG))
      enLEyaw.delete(0, END)
      enLEyaw.insert(0, '%.3f'%(float(LElbowYawAngle)*almath.TO_DEG))
      enLWyaw.delete(0, END)
      enLWyaw.insert(0, '%.3f'%(float(LWristYawAngle)*almath.TO_DEG))

      enRSpitch.delete(0, END)
      enRSpitch.insert(0, '%.3f'%(float(RShoulderPitchAngle)*almath.TO_DEG))
      enRSroll.delete(0, END)
      enRSroll.insert(0, '%.3f'%(float(RShoulderRollAngle)*almath.TO_DEG))
      enREroll.delete(0, END)
      enREroll.insert(0, '%.3f'%(float(RElbowRollAngle)*almath.TO_DEG))
      enREyaw.delete(0, END)
      enREyaw.insert(0, '%.3f'%(float(RElbowYawAngle)*almath.TO_DEG))
      enRWyaw.delete(0, END)
      enRWyaw.insert(0, '%.3f'%(float(RWristYawAngle)*almath.TO_DEG))
      

   getAngles = Button(content, text="Get Curent", width=10, command=getAngles)





##_________________________________GRID STUFF______________________________________##
   
   content.grid(column=0, row=0)
   #frame.grid(column=0, row=0, columnspan=3, rowspan=1)
   
   stiffnessOff.grid(column=5, row=0)
   stiffnessOn.grid(column=6, row=0)


   Hyaw.grid(column=2, row=1, padx=10)
   enHyaw.grid(column=2, row=2, padx=10)
   Hpitch.grid(column=2, row=3, padx=10)
   enHpitch.grid(column=2, row=4, padx=10)
   apply1.grid(column=2, row=5, padx=10)
   saveAs1.grid(column=2, row=16, padx=10)
   ensaveAs1.grid(column=2, row=17, padx=10)
   bSave1.grid(column=2, row=18, padx=10)


   LSpitch.grid(column=3, row=1, padx=15)
   enLSpitch.grid(column=3, row=2, padx=15)
   LSroll.grid(column=3, row=3, padx=15)
   enLSroll.grid(column=3, row=4, padx=15)
   LEyaw.grid(column=3, row=5, padx=15)
   enLEyaw.grid(column=3, row=6, padx=15)
   LEroll.grid(column=3, row=7, padx=15)
   enLEroll.grid(column=3, row=8, padx=15)
   LWyaw.grid(column=3, row=9, padx=15)
   enLWyaw.grid(column=3, row=10, padx=15)
   apply2.grid(column=3, row=13, padx=15)
   saveAs2.grid(column=3, row=16, padx=15)
   ensaveAs2.grid(column=3, row=17, padx=15)
   bSave2.grid(column=3, row=18, padx=15)
   
   getAngles.grid(column=5, row=14, padx=15)


   RSpitch.grid(column=4, row=1, padx=15)
   enRSpitch.grid(column=4, row=2, padx=15)
   RSroll.grid(column=4, row=3, padx=15)
   enRSroll.grid(column=4, row=4, padx=15)
   REyaw.grid(column=4, row=5, padx=15)
   enREyaw.grid(column=4, row=6, padx=15)
   REroll.grid(column=4, row=7, padx=15)
   enREroll.grid(column=4, row=8, padx=15)
   RWyaw.grid(column=4, row=9, padx=15)
   enRWyaw.grid(column=4, row=10, padx=15)
   apply3.grid(column=4, row=13, padx=15)
   saveAs3.grid(column=4, row=16, padx=15)
   ensaveAs3.grid(column=4, row=17, padx=15)
   bSave3.grid(column=4, row=18, padx=15)


##   saveAs4.grid(column=5, row=14, padx=10)
##   ensaveAs4.grid(column=5, row=15, padx=10)
##   bSave4.grid(column=5, row=16, padx=10)
   applyAll.grid(column=5, row=15, padx=15)

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






   leftarmmenu.add_separator() 
   leftarmmenu.add_command(label='thing', command=lambda: moveLeftArm2(80.594, 9.226, -45.354, -60.467, 7.468))















   menubar.add_cascade(label="Left Arm", menu=leftarmmenu)
   

   rightarmmenu = Menu(menubar, tearoff=0)





















   menubar.add_cascade(label="Right Arm", menu=rightarmmenu)


   bodymenu = Menu(menubar, tearoff=0)

   bodymenu.add_command(label="Hello (left)", command=waveLeft)
   bodymenu.add_separator()
   bodymenu.add_command(label="Hello (right)", command=waveRight)
   bodymenu.add_separator()
   bodymenu.add_command(label="Stop (left)", command=stopLeft)
   bodymenu.add_separator()
   bodymenu.add_command(label="Stop (right)", command=stopRight)
   bodymenu.add_separator()
   bodymenu.add_command(label="Look (left)", command=lookLeft)
   bodymenu.add_separator()
   bodymenu.add_command(label="Look (right)", command=lookRight)
   bodymenu.add_separator()
   bodymenu.add_command(label="I can't hear you (left)", command=cantHearLeft)
   bodymenu.add_separator()
   bodymenu.add_command(label="I can't hear you (right)", command=cantHearRight)
   bodymenu.add_separator()
   bodymenu.add_command(label="Shake NO", command=shakeNo)












   menubar.add_cascade(label="Full Body", menu=bodymenu)

   # TEACHING MENU
   teachmenu = Menu(menubar, tearoff=0)

   teachmenu.add_separator()
   teachmenu.add_command(label="teach1", command=startTeaching)
   teachmenu.add_separator()
   teachmenu.add_command(label="teach2", command=teaching2)
   teachmenu.add_separator()
   teachmenu.add_command(label="teach3", command=teaching3)
   teachmenu.add_separator()
   teachmenu.add_command(label="teach All", command=teachAll)

















   menubar.add_cascade(label="Teaching", menu=teachmenu)

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
