import maya.cmds as cmds
from piston.piston import makePiston

# Arm
def armSetup():
    # cmds.setAttr ("FKIKArm_R.FKIKBlend", 10)
    cmds.setAttr ("FKIKArm1_R.FKIKBlend", 10)
    cmds.setAttr ("FKIKArm2_R.FKIKBlend", 10)
    cmds.setAttr ("FKIKArm3_R.FKIKBlend", 10)

    cmds.setAttr ("PoleArm_R.follow", 10)
    cmds.setAttr ("PoleArm1_R.follow", 10)
    cmds.setAttr ("PoleArm2_R.follow", 10)
    cmds.setAttr ("PoleArm3_R.follow", 10)

    cmds.setAttr ("IKArm_R.follow", 10)
    cmds.setAttr ("IKArm1_R.follow", 10)
    cmds.setAttr ("IKArm2_R.follow", 10)
    cmds.setAttr ("IKArm3_R.follow", 10)

    cmds.setAttr ("HandPart1_R.twistAmount", 0)
    cmds.setAttr ("HandPart2_R.twistAmount", 0)
    cmds.setAttr ("HandPart3_R.twistAmount", 0)

def hoseSetup():
    cmds.setAttr ("FKIKSpline_R.FKIKBlend", 10)
    cmds.setAttr ("IKSpline4_R.ikHybridVis", 0)

    myCon = 'IKSpline4_R'
    myList = ['ikCvVis','ikHybridVis']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.parentConstraint ( 'FKBody1_R', 'IKExtraSpline4_R', mo=True )
    cmds.parentConstraint ( 'FKAttach1_M', 'IKExtraSpline1_R', mo=True )

# lock & hide
def lockAndHide():
    cmds.rename('Main','World')
    cmds.connectAttr('World.sx', 'World.sy', f=True)
    cmds.connectAttr('World.sx', 'World.sz', f=True)
    cmds.setAttr('World.jointVis',0)

    cmds.rename('FKRoot_M','Root')
    cmds.select('RootShape.cv[0:7]', r=True)
    cmds.rotate(-90, 0, 0, ocp=True, os=True, fo=True, r=True)
    cmds.select(cl=True)

    myCon = 'World'
    myList = ['sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKExtraRoot_M|Root'
    myList = ['sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['IKArm1_R','IKArm2_R']
    myList = ['sx','sy','sz','stretchy']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'IKArm_R'
    myList = ['sx','sy','sz','Fatness1']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKHand1_R'
    myList = ['tx','ty','rx','ry','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'IKArm3_R'
    myList = ['sx','sy','sz','Fatness1','Fatness2']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKBody_M'
    myList = ['tx','ty','tz','rx','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKBody1_R'
    myList = ['tx','ty','tz','rx','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKAttach1_M'
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKpistonRotate_R'
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKSampler_L'
    myList = ['sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKSampler1_L'
    myList = ['tx','ty','tz','rx','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKSampler2_L'
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSampler3_L','FKCapA_L','FKCapB_L','FKCapC_L','FKCapD_L','FKValveA_L','FKValveB_L']
    myList = ['tx','ty','tz','rx','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKArm_R','FKArm1_R','FKArm2_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKFingerUpA_R','FKFingerUpA1_R','FKFingerDownA_R','FKFingerDownA1_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKBodyTop_M']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.hide('FKpistonA_R','FKpistonB_R','FKpistonC_R','FKpistonD_R','FKpistonE_R','FKpistonF_R','FKpistonG_R','FKpistonH_R','RootX_M')
    cmds.hide('FKFingerUpB_R','FKFingerUpA4_R','FKFingerDownB_R','FKFingerDownA4_R','FKFingerUpA2_R','FKFingerUpA2_R')
    cmds.hide('FKFingerUpA2_R','FKFingerDownA2_R')
    cmds.hide('FKIKParentConstraintArm_R')

# attribute
def addAttribute():
    cmds.addAttr('FKExtraRoot_M|Root', ln="sampler",  at='enum', en='off:on:')
    cmds.setAttr('FKExtraRoot_M|Root.sampler', e=True, keyable=True)
    cmds.connectAttr('FKExtraRoot_M|Root.sampler', 'FKSampler_L.v', f=True)
    cmds.connectAttr('FKExtraRoot_M|Root.sampler', 'subOldHand_sampler_Grp.v', f=True)

# piston
def pistonSetup():
    makePiston('Z', 'Y', 'FKFingerUpA4_R', 'FKFingerUpB_R')
    makePiston('Z', 'Y', 'FKFingerDownA4_R', 'FKFingerDownB_R')
    makePiston('Z', 'Y', 'FKpistonH_R', 'FKpistonG_R')
    makePiston('Z', 'Y', 'FKpistonF_R', 'FKpistonE_R')
    makePiston('Z', 'Y', 'FKpistonD_R', 'FKpistonC_R')
    makePiston('Z', 'Y', 'FKpistonB_R', 'FKpistonA_R')

armSetup()
hoseSetup()
lockAndHide()
addAttribute()
pistonSetup()
