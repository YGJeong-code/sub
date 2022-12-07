import maya.cmds as cmds
import maya.mel as mel
from piston.piston import makePiston

def beamSetup():
    # limit
    myConList = ['FKBeamB4_R','FKBeamB4_L','FKBeamA4_M']
    for i in myConList:
        cmds.transformLimits ( i, tz=(0, 15.5), etz=(True, True) )

    # controller position
    myConList = ['FKIKArm6_L']
    myList = ['tx','ty','tz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=False, keyable=True, channelBox=False )
        cmds.setAttr (myCon+'.tx', 8.196)
        cmds.setAttr (myCon+'.ty', 13.305)
        cmds.setAttr (myCon+'.tz', 8.656)
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    # follow
    cmds.setAttr ("IKArm5_M.follow", 10)
    cmds.setAttr ("PoleArm5_M.follow", 10)

    cmds.setAttr ("IKArm6_L.follow", 10)
    cmds.setAttr ("PoleArm6_L.follow", 10)

    cmds.setAttr ("IKArm6_R.follow", 10)
    cmds.setAttr ("PoleArm6_R.follow", 10)

    # channel
    myConList = ['IKArm5_M','IKArm6_L','IKArm6_R']
    myList = ['sx','sy','sz','stretchy','antiPop','Lenght1','Lenght2','Fatness1','Fatness2']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    # ik
    cmds.setAttr ("FKIKArm6_R.FKIKBlend", 10)
    cmds.setAttr ("FKIKArm6_L.FKIKBlend", 10)
    cmds.setAttr ("FKIKArm5_M.FKIKBlend", 10)

def handSetup():
    # shape
    cmds.select('FKHandRotate2_MShape.cv[0:7]', r=True)
    cmds.rotate(0, 90, 0, ocp=True, os=True, fo=True, r=True)
    cmds.select(cl=True)

    # add attribute & set driven
    cmds.addAttr('FKHandRotate2_M', ln="folding",  at='double', min=0, max=1 )
    cmds.setAttr('FKHandRotate2_M.folding', e=True, keyable=True)

    cmds.setDrivenKeyframe( 'FKExtraHand1_M.rx', cd='FKHandRotate2_M.folding' )
    cmds.setDrivenKeyframe( 'FKExtraHand2_M.rx', cd='FKHandRotate2_M.folding' )
    cmds.setDrivenKeyframe( 'FKExtraHand3_M.rx', cd='FKHandRotate2_M.folding' )

    cmds.setAttr ("FKHandRotate2_M.folding", 1)
    cmds.setAttr ("FKExtraHand1_M.rx", 90)
    cmds.setAttr ("FKExtraHand2_M.rx", -90)
    cmds.setAttr ("FKExtraHand3_M.rx", 90)
    cmds.setDrivenKeyframe( 'FKExtraHand1_M.rx', cd='FKHandRotate2_M.folding' )
    cmds.setDrivenKeyframe( 'FKExtraHand2_M.rx', cd='FKHandRotate2_M.folding' )
    cmds.setDrivenKeyframe( 'FKExtraHand3_M.rx', cd='FKHandRotate2_M.folding' )

    # channel lockAndHide
    myConList = ['FKHand_M']
    for i in myConList:
        cmds.transformLimits ( i, tz=(0, 7.648), etz=(True, True) )

    myConList = ['FKHandRotate1_M']
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHandRotate2_M','FKHand1_M','FKHand2_M','FKHand3_M']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHand_M','FKHand4_M']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHand5_M','FKFingerA_M','FKFingerB_L','FKFingerB_R']
    myList = ['tx','ty','tz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKFingerA1_M','FKFingerA2_M','FKFingerB1_L','FKFingerB2_L','FKFingerB1_R','FKFingerB2_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    # visibility
    cmds.setAttr ("FKIKParentConstraintArm7_M.v", 0)

def rubberSetup():
    # channel
    cmds.setAttr ("FKIKSpline_M.FKIKBlend", 10)
    cmds.setAttr ("IKSpline3_M.ikHybridVis", 0)

    # rename
    cmds.rename ( 'IKSpline3_M', 'CordPlug' )
    cmds.rename ( 'IKSpline2_M', 'Cord_Mid_Bow' )
    cmds.rename ( 'IKSpline1_M', 'Cord_Low_Bow' )

    # shape
    cmds.select ( 'Cord_Low_Bow', 'Cord_Mid_Bow', r=True )
    mel.eval('asSwapCurve;')

    # channel lockAndHide
    myConList = ['CordPlug']
    myList = ['ikCvVis','ikHybridVis']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def ikSetup():
    # arm
    cmds.setAttr ("FKIKArm_M.FKIKBlend", 10)
    cmds.setAttr ("IKArm_M.follow", 10)
    cmds.setAttr ("IKArm_M.stretchy", 10)

    cmds.setAttr ("PoleArm_M.translateY", 60)
    cmds.setAttr ("PoleArm_M.translateZ", -150)
    cmds.setAttr ("PoleArm_M.follow", 10)

    # suspention
    cmds.setAttr ("FKIKParentConstraintArm1_M.visibility", 0)

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

    myCon = 'FKBody_M'
    myList = ['tx','ty','tz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    # myConList = ['FKArm_M','FKArm1_M','FKArm2_M']
    myConList = ['FKArm_M','FKArm2_M']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKArm3_M'
    myList = ['tx','ty','tz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSuspension1_M','FKBeamACover_M', 'FKBeamBCover_L','FKBeamBCover_R','FKBeamA4_M','FKBeamB4_L','FKBeamB4_R']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKBeamA_M','FKBeamA1_M','FKBeamA2_M','FKBeamA3_M', 'FKBeamB_L','FKBeamB1_L','FKBeamB2_L','FKBeamB3_L', 'FKBeamB_R','FKBeamB1_R','FKBeamB2_R','FKBeamB3_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKBeamA5_M','FKBeamB5_L', 'FKBeamB5_R']
    myList = ['tx','ty','tz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'IKArm_M'
    myList = ['sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.hide('RootX_M')

beamSetup()
handSetup()
rubberSetup()
ikSetup()
lockAndHide()
