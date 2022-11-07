import maya.cmds as cmds
import maya.mel as mel
from piston.piston import makePiston

# IK
def ikSetup():
    # rubber
    myList = ['.fkVis','.ikVis','.fkIkVis','.aimVis','.aimFKVis','.aimLRVis','.fingerVis','.bendVis','.arrowVis','.drvSysVis','.jointVis']
    if bool( cmds.objExists('Main') ):
        cmds.parentConstraint ('Main','Add_Main', mo=True)
        cmds.scaleConstraint ('Main','Add_Main', mo=True)
        for i in myList:
            cmds.connectAttr ( 'Main'+i, 'Add_Main'+i, f=True)
    else:
        cmds.parentConstraint ('World','Add_Main', mo=True)
        cmds.scaleConstraint ('World','Add_Main', mo=True)
        for i in myList:
            cmds.connectAttr ( 'World'+i, 'Add_Main'+i, f=True)

    if bool( cmds.objExists('FKRoot_M') ):
        cmds.parentConstraint ('FKRoot_M','Add_FKRoot_M', mo=True)
        cmds.scaleConstraint ('FKRoot_M','Add_FKRoot_M', mo=True)
    else:
        cmds.parentConstraint ('FKExtraRoot_M|Root','Add_FKRoot_M', mo=True)
        cmds.scaleConstraint ('FKExtraRoot_M|Root','Add_FKRoot_M', mo=True)

    cmds.setAttr ("Add_IKSpline3_M.stretchy", 0)

    # arm
    cmds.setAttr ("FKIKArm_M.FKIKBlend", 10)
    cmds.setAttr ("IKArm_M.follow", 10)

    cmds.setAttr ("PoleArm_M.translateY", 50)
    cmds.setAttr ("PoleArm_M.translateZ", -240)
    cmds.setAttr ("PoleArm_M.follow", 10)

    # suspention
    cmds.setAttr ("FKIKParentConstraintArm1_M.visibility", 0)

    # hand
    cmds.setAttr ("FKIKParentConstraintArm7_M.visibility", 0)

    # beam
    cmds.setAttr ("IKArm5_M.follow", 10)
    cmds.setAttr ("PoleArm5_M.follow", 10)

    cmds.setAttr ("IKArm6_L.follow", 10)
    cmds.setAttr ("PoleArm6_L.follow", 10)

    cmds.setAttr ("IKArm6_R.follow", 10)
    cmds.setAttr ("PoleArm6_R.follow", 10)

    # hand
    cmds.setAttr ("IKArm2_M.follow", 10)
    cmds.setAttr ("PoleArm2_M.follow", 10)

    cmds.setAttr ("IKArm3_M.follow", 10)
    cmds.setAttr ("PoleArm3_M.follow", 10)

    cmds.setAttr ("IKArm4_L.follow", 10)
    cmds.setAttr ("PoleArm4_L.follow", 10)

    cmds.setAttr ("IKArm4_R.follow", 10)
    cmds.setAttr ("PoleArm4_R.follow", 10)

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

    # myCon = 'PoleArm_M'
    # myList = ['follow','lock']
    # for i in myList:
    #     cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKBody_M'
    myList = ['tx','ty','tz','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKArm_M','FKArm1_M','FKArm2_M']
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

    myConList = ['FKHand_M','FKHand1_M','FKHand2_M','FKHand3_M']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKHand4_M'
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz']
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

    myCon = 'IKArm_M'
    myList = ['sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['IKArm5_M','IKArm6_L','IKArm6_R','IKArm3_M','IKArm4_L','IKArm4_R']
    myList = ['tx','ry','rz','sx','sy','sz','stretchy','antiPop','Lenght1','Lenght2','Fatness1','Fatness2']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'IKArm2_M'
    myList = ['tx','ry','rz','sx','sy','sz','stretchy','antiPop','Lenght1','Lenght2','Lenght3','Fatness1','Fatness2','Fatness3']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.hide('RootX_M')
    # cmds.hide('FKFingerUpB_R','FKFingerUpA4_R','FKFingerDownB_R','FKFingerDownA4_R','FKFingerUpA2_R','FKFingerUpA2_R')
    # cmds.hide('FKFingerUpA2_R','FKFingerDownA2_R')
    # cmds.hide('FKIKParentConstraintArm_R')

ikSetup()
lockAndHide()
