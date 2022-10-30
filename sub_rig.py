import maya.cmds as cmds
import maya.mel as mel

# chair
cmds.setAttr( "IKSplineA3_R.stretchy", 0)
cmds.setAttr( "IKSplineA3_L.stretchy", 0)

# midlight
myNode = 'midlight_R_MUL'
cmds.createNode('multiplyDivide', n=myNode)
cmds.setAttr(myNode+'.input2Z', -1)

cmds.connectAttr('MidlightLook_R.ry', 'FKOffsetMidlight_R.rx', f=True)

cmds.connectAttr('MidlightLook_R.rz', myNode+'.input1Z', f=True)
cmds.connectAttr(myNode+'.outputZ', 'FKOffsetMidlight1_R.rz', f=True)

myNode = 'midlight_L_MUL'
cmds.createNode('multiplyDivide', n=myNode)
cmds.setAttr(myNode+'.input2Z', -1)

cmds.connectAttr('MidlightLook_L.ry', 'FKOffsetMidlight_L.rx', f=True)

cmds.connectAttr('MidlightLook_L.rz', myNode+'.input1Z', f=True)
cmds.connectAttr(myNode+'.outputZ', 'FKOffsetMidlight1_L.rz', f=True)

cmds.parentConstraint('FKBody_M','MidlightLook_R_nul', mo=True)
cmds.parentConstraint('FKBody_M','MidlightLook_L_nul', mo=True)
cmds.scaleConstraint('FKBody_M','MidlightLook_R_nul', mo=True)
cmds.scaleConstraint('FKBody_M','MidlightLook_L_nul', mo=True)

# hatch
myLook = 'HatchCoverClipLook_L'
cmds.aimConstraint(myLook, 'FKOffsetHatchCoverClipA_L', mo=True)
cmds.aimConstraint(myLook, 'FKOffsetHatchCoverClipB_L', mo=True)
cmds.aimConstraint(myLook, 'FKOffsetHatchCoverClipC_L', mo=True)

# pedal piston
mel.eval('cycleCheck -e off')
cmds.orientConstraint('PaddalA1_loc','FKOffsetPaddalA1_L')
cmds.orientConstraint('PaddalPistonA1_loc','FKOffsetPaddalPistonA1_L')
cmds.pointConstraint('FKPaddalA1_L','PaddalA1_loc')
cmds.pointConstraint('FKPaddalPistonA1_L','PaddalPistonA1_loc')

cmds.orientConstraint('PaddalA3_loc','FKOffsetPaddalA3_L')
cmds.orientConstraint('PaddalPistonA3_loc','FKOffsetPaddalPistonA3_L')
cmds.pointConstraint('FKPaddalA3_L','PaddalA3_loc')
cmds.pointConstraint('FKPaddalPistonA3_L','PaddalPistonA3_loc')

cmds.orientConstraint('PaddalB1_loc','FKOffsetPaddalB1_L')
cmds.orientConstraint('PaddalPistonB_loc','FKOffsetPaddalPistonB_L')
cmds.pointConstraint('FKPaddalB1_L','PaddalB1_loc')
cmds.pointConstraint('FKPaddalPistonB_L','PaddalPistonB_loc')

cmds.parentConstraint('FKPaddal_L','PaddalPistonA_up', mo=True)
cmds.parentConstraint('FKPaddal_L','PaddalPistonB_up', mo=True)

cmds.currentTime (1)
cmds.setKeyframe('FKPaddalA_L','FKPaddalB_L')
cmds.currentTime (10)
cmds.cutKey('FKPaddalA_L','FKPaddalB_L')
cmds.currentTime (1)

# monitorA
cmds.setAttr ("FKIKSplineB_M.FKIKBlend", 10)
cmds.setAttr ("IKSplineB3_M.stretchy", 0)
#cmds.hide('IKSplineB3_M','IKhybridSplineB2_M')

cmds.connectAttr('MonitorAIK_M.rz','FKExtraMonitorA_M.rz')
cmds.connectAttr('MonitorAIK1_M.rz','FKExtraMonitorA2_M.rz')

cmds.connectAttr('MonitorAIK_M.ry','FKExtraMonitorA1_M.ry')
cmds.connectAttr('MonitorAIK1_M.ry','FKExtraMonitorA3_M.ry')

# pan
myCon = 'FKBody_M'
myAttr_speed = 'panSpeed'

cmds.addAttr(myCon, ln=myAttr_speed, at='long', dv=1000)
cmds.setAttr(myCon+'.'+myAttr_speed, e=True, keyable=True)

cmds.expression( s = 'FKExtraFanA1_R.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraFanA1_L.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraFanB1_R.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraFanB1_L.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraFanC1_R.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraFanC1_L.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraEngineH1_R.rx = -time*'+myCon+'.'+myAttr_speed )
cmds.expression( s = 'FKExtraEngineH1_L.rx = -time*'+myCon+'.'+myAttr_speed )

myCon = 'FKBody_M'
myAttr_noiseSpeed = 'panNoiseSpeed'
myAttr_offset = 'panNoiseOffset'

myNoiseSpeed = myCon+'.'+myAttr_noiseSpeed
myNoiseOffset = myCon+'.'+myAttr_offset

cmds.addAttr(myCon, ln=myAttr_noiseSpeed, at='double', dv=10)
cmds.setAttr(myNoiseSpeed, e=True, keyable=True)
cmds.addAttr(myCon, ln=myAttr_offset, at='double', dv=0.03)
cmds.setAttr(myNoiseOffset, e=True, keyable=True)

# cmds.expression( s = 'FKExtraFanA1_R.tx = (noise(time * %s) * %s)/2'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraFanA1_L.tx = (noise(time * %s) * %s)/2+0.1'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraFanB1_R.tx = (noise(time * %s) * %s)/2'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraFanB1_L.tx = (noise(time * %s) * %s)/2'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraFanC1_R.tx = (noise(time * %s) * %s)/2'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraFanC1_L.tx = (noise(time * %s) * %s)/2'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraEngineH1_R.tx = (noise(time * %s) * %s)/2+0.1'%(myNoiseSpeed,myNoiseOffset) )
# cmds.expression( s = 'FKExtraEngineH1_L.tx = (noise(time * %s) * %s)/2-0.1'%(myNoiseSpeed,myNoiseOffset) )

# cmds.expression( s = 'FKExtraFanA_R.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraFanA_L.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraFanB_R.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraFanB_L.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraFanC_R.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraFanC_L.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraEngineH_R.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )
# cmds.expression( s = 'FKExtraEngineH_L.tz = (noise(time*'+myNoiseSpeed+')*'+myNoiseOffset+')/2' )

mySide = ['R','L']
myList = ['A','B','C']
for i in mySide:
    for j in myList:
        myNode = cmds.createNode('multiplyDivide')
        cmds.connectAttr ('Fan'+j+'_'+i+'.scale', 'Fan'+j+'1_'+i+'.scale', f=True)
        cmds.connectAttr ('FKExtraFan'+j+'_'+i+'.scale', myNode+'.input1', f=True)
        cmds.connectAttr ('FKFan'+j+'_'+i+'.scale', myNode+'.input2', f=True)
        cmds.connectAttr (myNode+'.outputX', 'Fan'+j+'_'+i+'.scaleX', f=True)
        cmds.connectAttr (myNode+'.outputY', 'Fan'+j+'_'+i+'.scaleY', f=True)
        cmds.connectAttr (myNode+'.outputZ', 'Fan'+j+'_'+i+'.scaleZ', f=True)
        cmds.setAttr ( 'FKExtraFan'+j+'_'+i+'.sx', lock=False, keyable=True, channelBox=True)
        cmds.setAttr ( 'FKExtraFan'+j+'_'+i+'.sy', lock=False, keyable=True, channelBox=True)
        cmds.setAttr ( 'FKExtraFan'+j+'_'+i+'.sz', lock=False, keyable=True, channelBox=True)
        cmds.expression( s = 'FKExtraFan'+j+'_'+i+'.sx = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )
        cmds.expression( s = 'FKExtraFan'+j+'_'+i+'.sy = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )
        cmds.expression( s = 'FKExtraFan'+j+'_'+i+'.sz = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )

mySide = ['R','L']
for i in mySide:
    myNode = cmds.createNode('multiplyDivide')
    cmds.connectAttr ('EngineH_'+i+'.scale', 'EngineH1_'+i+'.scale', f=True)
    cmds.connectAttr ('FKExtraEngineH_'+i+'.scale', myNode+'.input1', f=True)
    cmds.connectAttr ('FKEngineH_'+i+'.scale', myNode+'.input2', f=True)
    cmds.connectAttr (myNode+'.outputX', 'EngineH_'+i+'.scaleX', f=True)
    cmds.connectAttr (myNode+'.outputY', 'EngineH_'+i+'.scaleY', f=True)
    cmds.connectAttr (myNode+'.outputZ', 'EngineH_'+i+'.scaleZ', f=True)
    cmds.setAttr ( 'FKExtraEngineH_'+i+'.sx', lock=False, keyable=True, channelBox=True)
    cmds.setAttr ( 'FKExtraEngineH_'+i+'.sy', lock=False, keyable=True, channelBox=True)
    cmds.setAttr ( 'FKExtraEngineH_'+i+'.sz', lock=False, keyable=True, channelBox=True)
    cmds.expression( s = 'FKExtraEngineH_'+i+'.sx = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )
    cmds.expression( s = 'FKExtraEngineH_'+i+'.sy = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )
    cmds.expression( s = 'FKExtraEngineH_'+i+'.sz = ((noise(time * %s) +1) * %s) + 1'%(myNoiseSpeed,myNoiseOffset) )


# center button
myCon = 'FKCenterjoystick_M'
cmds.setAttr( myCon+".tx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ty", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".tz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ry", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sy", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".v", lock=True, keyable=False, channelBox=False)

myList = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','C6','C7']
for i in myList:
    if i == 'A3':
        cmds.addAttr(myCon, ln=i, at='double', min=-90.0, max=90.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'B1' or i == 'B2' or i == 'B3' or i == 'B4' or i == 'B5':
        cmds.addAttr(myCon, ln=i, at='double', min=-25.0, max=25.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    else:
        cmds.addAttr(myCon, ln=i, at='double', min=-0.2, max=0.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

cmds.connectAttr(myCon+'.A1', 'FKExtraCenterjoystickButtonC_L.tx', f=True)
cmds.connectAttr(myCon+'.A2', 'FKExtraCenterjoystickButtonB_L.tx', f=True)
cmds.connectAttr(myCon+'.A3', 'FKExtraCenterjoystickButtonA_M.rx', f=True)
cmds.connectAttr(myCon+'.A4', 'FKExtraCenterjoystickButtonB_R.tx', f=True)
cmds.connectAttr(myCon+'.A5', 'FKExtraCenterjoystickButtonC_R.tx', f=True)
cmds.connectAttr(myCon+'.B1', 'FKExtraCenterjoystickButtonF_L.rz', f=True)
cmds.connectAttr(myCon+'.B2', 'FKExtraCenterjoystickButtonE_L.rz', f=True)
cmds.connectAttr(myCon+'.B3', 'FKExtraCenterjoystickButtonD_M.rz', f=True)
cmds.connectAttr(myCon+'.B4', 'FKExtraCenterjoystickButtonE_R.rz', f=True)
cmds.connectAttr(myCon+'.B5', 'FKExtraCenterjoystickButtonF_R.rz', f=True)
cmds.connectAttr(myCon+'.C1', 'FKExtraCenterjoystickButtonJ_L.tx', f=True)
cmds.connectAttr(myCon+'.C2', 'FKExtraCenterjoystickButtonI_L.tx', f=True)
cmds.connectAttr(myCon+'.C3', 'FKExtraCenterjoystickButtonH_L.tx', f=True)
cmds.connectAttr(myCon+'.C4', 'FKExtraCenterjoystickButtonG_M.tx', f=True)
cmds.connectAttr(myCon+'.C5', 'FKExtraCenterjoystickButtonH_R.tx', f=True)
cmds.connectAttr(myCon+'.C6', 'FKExtraCenterjoystickButtonI_R.tx', f=True)
cmds.connectAttr(myCon+'.C7', 'FKExtraCenterjoystickButtonJ_R.tx', f=True)

# right button
myCon = 'FKSidecontrolerB_R'
cmds.setAttr( myCon+".tx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ty", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".tz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ry", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sy", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".v", lock=True, keyable=False, channelBox=False)

myList = ['A1','A2','A3','A4','A5','A6','BA1','BA2','BB1','BB2','C1','C2','C3','C4','C5','C6','C7','C8','C9','D1','D2']
for i in myList:
    if i == 'A1' or i == 'A2' or i == 'A3' or i == 'A4' or i == 'A5' or i == 'A6':
        cmds.addAttr(myCon, ln=i, at='double', min=-0.2, max=0.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'BA1' or i == 'BA2':
        cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=70.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'BB1' or i == 'BB2':
        cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=50.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    else:
        cmds.addAttr(myCon, ln=i, at='double', min=-90.0, max=90.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

cmds.connectAttr(myCon+'.A1', 'FKExtraSidecontrolerBButtonA_R.tx', f=True)
cmds.connectAttr(myCon+'.A2', 'FKExtraSidecontrolerBButtonB_R.tx', f=True)
cmds.connectAttr(myCon+'.A3', 'FKExtraSidecontrolerBButtonC_R.tx', f=True)
cmds.connectAttr(myCon+'.A4', 'FKExtraSidecontrolerBButtonD_R.tx', f=True)
cmds.connectAttr(myCon+'.A5', 'FKExtraSidecontrolerBButtonE_R.tx', f=True)
cmds.connectAttr(myCon+'.A6', 'FKExtraSidecontrolerBButtonF_R.tx', f=True)
cmds.connectAttr(myCon+'.BA1', 'FKExtraSidecontrolerBButtonG_R.rz', f=True)
cmds.connectAttr(myCon+'.BA2', 'FKExtraSidecontrolerBButtonI_R.rz', f=True)
cmds.connectAttr(myCon+'.BB1', 'FKExtraSidecontrolerBButtonH_R.rz', f=True)
cmds.connectAttr(myCon+'.BB2', 'FKExtraSidecontrolerBButtonJ_R.rz', f=True)
cmds.connectAttr(myCon+'.C1', 'FKExtraSidecontrolerBButtonK_R.rx', f=True)
cmds.connectAttr(myCon+'.C2', 'FKExtraSidecontrolerBButtonL_R.rx', f=True)
cmds.connectAttr(myCon+'.C3', 'FKExtraSidecontrolerBButtonM_R.rx', f=True)
cmds.connectAttr(myCon+'.C4', 'FKExtraSidecontrolerBButtonN_R.rx', f=True)
cmds.connectAttr(myCon+'.C5', 'FKExtraSidecontrolerBButtonO_R.rx', f=True)
cmds.connectAttr(myCon+'.C6', 'FKExtraSidecontrolerBButtonP_R.rx', f=True)
cmds.connectAttr(myCon+'.C7', 'FKExtraSidecontrolerBButtonQ_R.rx', f=True)
cmds.connectAttr(myCon+'.C8', 'FKExtraSidecontrolerBButtonR_R.rx', f=True)
cmds.connectAttr(myCon+'.C9', 'FKExtraSidecontrolerBButtonS_R.rx', f=True)
cmds.connectAttr(myCon+'.D1', 'FKExtraSidecontrolerBButtonT_R.rx', f=True)
cmds.connectAttr(myCon+'.D2', 'FKExtraSidecontrolerBButtonU_R.rx', f=True)

# left button
myCon = 'FKSidecontrolerA_L'
cmds.setAttr( myCon+".tx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ty", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".tz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ry", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sy", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".v", lock=True, keyable=False, channelBox=False)

myList = ['AA1','AA2','AB1','AB2','B1','B2','B3','B4','B5','B6','C1','D1','D2','D3','E1','E2','E3','E4','E5','E6']
for i in myList:
    if i == 'AA1' or i == 'AA2':
        cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=70.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'AB1' or i == 'AB2':
        cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=50.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'B1' or i == 'B2' or i == 'B3' or i == 'B4' or i == 'B5' or i == 'B6':
        cmds.addAttr(myCon, ln=i, at='double', min=-0.2, max=0.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'C1':
        cmds.addAttr(myCon, ln=i, at='double', min=-60.0, max=60.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'D1' or i == 'D2':
        cmds.addAttr(myCon, ln=i, at='double', min=-25.0, max=25.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    elif i == 'D3':
        cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=50.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
    else:
        cmds.addAttr(myCon, ln=i, at='double', min=-90.0, max=90.0, dv=0.0)
        cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

cmds.connectAttr(myCon+'.AA1', 'FKExtraSidecontrolerAButtonA_L.rz', f=True)
cmds.connectAttr(myCon+'.AA2', 'FKExtraSidecontrolerAButtonC_L.rz', f=True)
cmds.connectAttr(myCon+'.AB1', 'FKExtraSidecontrolerAButtonB_L.rz', f=True)
cmds.connectAttr(myCon+'.AB2', 'FKExtraSidecontrolerAButtonD_L.rz', f=True)
cmds.connectAttr(myCon+'.B1', 'FKExtraSidecontrolerAButtonE_L.tx', f=True)
cmds.connectAttr(myCon+'.B2', 'FKExtraSidecontrolerAButtonF_L.tx', f=True)
cmds.connectAttr(myCon+'.B3', 'FKExtraSidecontrolerAButtonG_L.tx', f=True)
cmds.connectAttr(myCon+'.B4', 'FKExtraSidecontrolerAButtonH_L.tx', f=True)
cmds.connectAttr(myCon+'.B5', 'FKExtraSidecontrolerAButtonI_L.tx', f=True)
cmds.connectAttr(myCon+'.B6', 'FKExtraSidecontrolerAButtonJ_L.tx', f=True)
cmds.connectAttr(myCon+'.C1', 'FKExtraSidecontrolerAButtonK_L.rz', f=True)
cmds.connectAttr(myCon+'.D1', 'FKExtraSidecontrolerAButtonL_L.rz', f=True)
cmds.connectAttr(myCon+'.D2', 'FKExtraSidecontrolerAButtonM_L.rz', f=True)
cmds.connectAttr(myCon+'.D3', 'FKExtraSidecontrolerAButtonN_L.rz', f=True)
cmds.connectAttr(myCon+'.E1', 'FKExtraSidecontrolerAButtonO_L.rx', f=True)
cmds.connectAttr(myCon+'.E2', 'FKExtraSidecontrolerAButtonP_L.rx', f=True)
cmds.connectAttr(myCon+'.E3', 'FKExtraSidecontrolerAButtonQ_L.rx', f=True)
cmds.connectAttr(myCon+'.E4', 'FKExtraSidecontrolerAButtonR_L.rx', f=True)
cmds.connectAttr(myCon+'.E5', 'FKExtraSidecontrolerAButtonS_L.rx', f=True)
cmds.connectAttr(myCon+'.E6', 'FKExtraSidecontrolerAButtonT_L.rx', f=True)

# Engine
myCon = 'FKEngineI_M'
cmds.setAttr( myCon+".tx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ty", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".tz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".ry", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".rz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sx", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sy", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".sz", lock=True, keyable=False, channelBox=False)
cmds.setAttr( myCon+".v", lock=True, keyable=False, channelBox=False)
