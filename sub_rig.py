import maya.cmds as cmds
import maya.mel as mel
from piston.piston import makePiston
from piston.piston import makeLookAt_makeLookAtPos

def conName():
    cmds.rename('Main','World')

    cmds.connectAttr('World.sx', 'World.sy', f=True)
    cmds.connectAttr('World.sx', 'World.sz', f=True)
    # cmds.setAttr('World.jointVis',0)

    cmds.rename('RootX_M','Base')
    cmds.rename('FKRoot_M','Root')

    myCon = 'World'
    myList = ['sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKExtraRoot_M|Root'
    myList = ['sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def monitorA():
    # monitorA
    cmds.connectAttr('MonitorA_a_con.rx','FKExtraMonitorA_M.rx', f=True)
    cmds.connectAttr('MonitorA_a_con.ry','FKExtraMonitorA1_M.ry', f=True)

    cmds.connectAttr('MonitorA_b_con.rx','FKExtraMonitorA2_M.rx', f=True)
    cmds.connectAttr('MonitorA_b_con.ry','FKExtraMonitorA3_M.ry', f=True)

    cmds.connectAttr('MonitorA_c_con.rx','FKExtraMonitorA4_M.rx', f=True)
    cmds.connectAttr('MonitorA_c_con.ry','FKExtraMonitorA5_M.ry', f=True)

    cmds.connectAttr('MonitorA_d_con.rz','FKExtraMonitorA6_M.rz', f=True)

    cmds.parentConstraint('Root_M', 'MonitorA_a_nul', mo=True)
    cmds.parentConstraint('MonitorA1_M', 'MonitorA_b_nul', mo=True)
    cmds.parentConstraint('MonitorA3_M', 'MonitorA_c_nul', mo=True)
    cmds.parentConstraint('MonitorA5_M', 'MonitorA_d_nul', mo=True)

    cmds.scaleConstraint('Root_M', 'MonitorA_a_nul', mo=True)
    cmds.scaleConstraint('Root_M', 'MonitorA_b_nul', mo=True)
    cmds.scaleConstraint('Root_M', 'MonitorA_c_nul', mo=True)
    cmds.scaleConstraint('Root_M', 'MonitorA_d_nul', mo=True)

    myCon = 'FKMonitorA6_M'
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.hide('FKMonitorA_M')

def createConnect(driver, driven, value):
    myNode = cmds.createNode('multiplyDivide', n=driver+'_mult')
    cmds.connectAttr (driver, myNode+'.input1.input1X', f=True)
    cmds.setAttr(myNode+'.input2.input2X', value)
    cmds.connectAttr (myNode+'.outputX', driven, f=True)

def center_button():
    # center button
    myCon = 'FKCenterjoystick_M'
    myList = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myList = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','C6','C7']
    for i in myList:
        if i == 'A3':
            cmds.addAttr(myCon, ln=i, at='double', dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'B1' or i == 'B2' or i == 'B3' or i == 'B4' or i == 'B5':
            cmds.addAttr(myCon, ln=i, at='double', min=-12.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        else:
            cmds.addAttr(myCon, ln=i, at='double', min=-2.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

    createConnect(myCon+'.A1', 'FKExtraCenterjoystickButtonC_L.tz', -0.02)
    createConnect(myCon+'.A2', 'FKExtraCenterjoystickButtonB_L.tz', -0.02)
    createConnect(myCon+'.A3', 'FKExtraCenterjoystickButtonA_M.rz', -1)
    createConnect(myCon+'.A4', 'FKExtraCenterjoystickButtonB_R.tz', -0.02)
    createConnect(myCon+'.A5', 'FKExtraCenterjoystickButtonC_R.tz', -0.02)
    createConnect(myCon+'.B1', 'FKExtraCenterjoystickButtonF_L.rx', -3)
    createConnect(myCon+'.B2', 'FKExtraCenterjoystickButtonE_L.rx', -3)
    createConnect(myCon+'.B3', 'FKExtraCenterjoystickButtonD_M.rx', -3)
    createConnect(myCon+'.B4', 'FKExtraCenterjoystickButtonE_R.rx', -3)
    createConnect(myCon+'.B5', 'FKExtraCenterjoystickButtonF_R.rx', -3)
    createConnect(myCon+'.C1', 'FKExtraCenterjoystickButtonJ_L.tz', -0.02)
    createConnect(myCon+'.C2', 'FKExtraCenterjoystickButtonI_L.tz', -0.02)
    createConnect(myCon+'.C3', 'FKExtraCenterjoystickButtonH_L.tz', -0.02)
    createConnect(myCon+'.C4', 'FKExtraCenterjoystickButtonG_M.tz', -0.02)
    createConnect(myCon+'.C5', 'FKExtraCenterjoystickButtonH_R.tz', -0.02)
    createConnect(myCon+'.C6', 'FKExtraCenterjoystickButtonI_R.tz', -0.02)
    createConnect(myCon+'.C7', 'FKExtraCenterjoystickButtonJ_R.tz', -0.02)

    myCon = 'FKCenterjoystick1_M'
    myList = ['tx','ty','tz','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKCenterjoystick17_M','FKCenterjoystick13_L','FKCenterjoystick11_R']
    myList = ['tx','ty','tz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKCenterjoystick3_M','FKCenterjoystick7_L','FKCenterjoystick9_M','FKCenterjoystick15_R','FKCenterjoystickButtonC_L','FKCenterjoystickButtonB_L','FKCenterjoystickButtonB_R','FKCenterjoystickButtonC_R','FKCenterjoystickButtonJ_L','FKCenterjoystickButtonI_L','FKCenterjoystickButtonH_L','FKCenterjoystickButtonG_M','FKCenterjoystickButtonH_R','FKCenterjoystickButtonI_R','FKCenterjoystickButtonJ_R']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKCenterjoystick5_M'
    myList = ['tx','ty','ry','rz','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myCon = 'FKCenterjoystickButtonA_M'
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKCenterjoystickButtonF_L','FKCenterjoystickButtonE_L','FKCenterjoystickButtonD_M','FKCenterjoystickButtonE_R','FKCenterjoystickButtonF_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def left_button():
    # left button
    myCon = 'FKSidecontrolerA_L'
    myList = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myList = ['AA1','AA2','AB1','AB2','B1','B2','B3','B4','B5','B6','C1','D1','D2','D3','E1','E2','E3','E4','E5','E6']
    for i in myList:
        if i == 'AA1' or i == 'AA2':
            cmds.addAttr(myCon, ln=i, at='double', min=-2.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'AB1' or i == 'AB2':
            cmds.addAttr(myCon, ln=i, at='double', min=-12.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'B1' or i == 'B2' or i == 'B3' or i == 'B4' or i == 'B5' or i == 'B6':
            cmds.addAttr(myCon, ln=i, at='double', min=-2.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'C1':
            cmds.addAttr(myCon, ln=i, at='double', min=-12.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'D1' or i == 'D2' or i == 'D3':
            cmds.addAttr(myCon, ln=i, at='double', min=-12.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        # elif i == 'D3':
        #     cmds.addAttr(myCon, ln=i, at='double', min=0.0, max=50.0, dv=0.0)
        #     cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        else:
            cmds.addAttr(myCon, ln=i, at='double', dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

    createConnect(myCon+'.AA1', 'FKExtraSidecontrolerAButtonA_L.rx', -7)
    createConnect(myCon+'.AA2', 'FKExtraSidecontrolerAButtonC_L.rx', -7)
    createConnect(myCon+'.AB1', 'FKExtraSidecontrolerAButtonB_L.rx', -3)
    createConnect(myCon+'.AB2', 'FKExtraSidecontrolerAButtonD_L.rx', -3)
    createConnect(myCon+'.B1', 'FKExtraSidecontrolerAButtonE_L.tz', -0.02)
    createConnect(myCon+'.B2', 'FKExtraSidecontrolerAButtonF_L.tz', -0.02)
    createConnect(myCon+'.B3', 'FKExtraSidecontrolerAButtonG_L.tz', -0.02)
    createConnect(myCon+'.B4', 'FKExtraSidecontrolerAButtonH_L.tz', -0.02)
    createConnect(myCon+'.B5', 'FKExtraSidecontrolerAButtonI_L.tz', -0.02)
    createConnect(myCon+'.B6', 'FKExtraSidecontrolerAButtonJ_L.tz', -0.02)
    createConnect(myCon+'.C1', 'FKExtraSidecontrolerAButtonK_L.rx', -7)
    createConnect(myCon+'.D1', 'FKExtraSidecontrolerAButtonL_L.rx', -3)
    createConnect(myCon+'.D2', 'FKExtraSidecontrolerAButtonM_L.rx', -3)
    createConnect(myCon+'.D3', 'FKExtraSidecontrolerAButtonN_L.rx', -3)
    createConnect(myCon+'.E1', 'FKExtraSidecontrolerAButtonO_L.rz', -1)
    createConnect(myCon+'.E2', 'FKExtraSidecontrolerAButtonP_L.rz', -1)
    createConnect(myCon+'.E3', 'FKExtraSidecontrolerAButtonQ_L.rz', -1)
    createConnect(myCon+'.E4', 'FKExtraSidecontrolerAButtonR_L.rz', -1)
    createConnect(myCon+'.E5', 'FKExtraSidecontrolerAButtonS_L.rz', -1)
    createConnect(myCon+'.E6', 'FKExtraSidecontrolerAButtonT_L.rz', -1)

    myConList = ['FKSidecontrolerAButtonA_L','FKSidecontrolerAButtonC_L','FKSidecontrolerAButtonB_L','FKSidecontrolerAButtonD_L','FKSidecontrolerAButtonK_L','FKSidecontrolerAButtonL_L','FKSidecontrolerAButtonM_L','FKSidecontrolerAButtonN_L']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSidecontrolerAButtonE_L','FKSidecontrolerAButtonF_L','FKSidecontrolerAButtonG_L','FKSidecontrolerAButtonH_L','FKSidecontrolerAButtonI_L','FKSidecontrolerAButtonJ_L']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSidecontrolerAButtonO_L','FKSidecontrolerAButtonP_L','FKSidecontrolerAButtonQ_L','FKSidecontrolerAButtonR_L','FKSidecontrolerAButtonS_L','FKSidecontrolerAButtonT_L']
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def right_button():
    # right button
    myCon = 'FKSidecontrolerB_R'
    myList = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for i in myList:
        cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myList = ['A1','A2','A3','A4','A5','A6','BA1','BA2','BB1','BB2','C1','C2','C3','C4','C5','C6','C7','C8','C9','D1','D2']
    for i in myList:
        if i == 'A1' or i == 'A2' or i == 'A3' or i == 'A4' or i == 'A5' or i == 'A6':
            cmds.addAttr(myCon, ln=i, at='double', min=-2.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'BA1' or i == 'BA2':
            cmds.addAttr(myCon, ln=i, at='double', min=-2.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        elif i == 'BB1' or i == 'BB2':
            cmds.addAttr(myCon, ln=i, at='double', min=-12.0, max=12.0, dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)
        else:
            cmds.addAttr(myCon, ln=i, at='double',dv=0.0)
            cmds.setAttr(myCon+'.'+i, e=True, keyable=True)

    createConnect(myCon+'.A1', 'FKExtraSidecontrolerBButtonA_R.tz', -0.02)
    createConnect(myCon+'.A2', 'FKExtraSidecontrolerBButtonB_R.tz', -0.02)
    createConnect(myCon+'.A3', 'FKExtraSidecontrolerBButtonC_R.tz', -0.02)
    createConnect(myCon+'.A4', 'FKExtraSidecontrolerBButtonD_R.tz', -0.02)
    createConnect(myCon+'.A5', 'FKExtraSidecontrolerBButtonE_R.tz', -0.02)
    createConnect(myCon+'.A6', 'FKExtraSidecontrolerBButtonF_R.tz', -0.02)
    createConnect(myCon+'.BA1', 'FKExtraSidecontrolerBButtonG_R.rx', -7)
    createConnect(myCon+'.BA2', 'FKExtraSidecontrolerBButtonI_R.rx', -7)
    createConnect(myCon+'.BB1', 'FKExtraSidecontrolerBButtonH_R.rx', -3)
    createConnect(myCon+'.BB2', 'FKExtraSidecontrolerBButtonJ_R.rx', -3)
    createConnect(myCon+'.C1', 'FKExtraSidecontrolerBButtonK_R.rz', -1)
    createConnect(myCon+'.C2', 'FKExtraSidecontrolerBButtonL_R.rz', -1)
    createConnect(myCon+'.C3', 'FKExtraSidecontrolerBButtonM_R.rz', -1)
    createConnect(myCon+'.C4', 'FKExtraSidecontrolerBButtonN_R.rz', -1)
    createConnect(myCon+'.C5', 'FKExtraSidecontrolerBButtonO_R.rz', -1)
    createConnect(myCon+'.C6', 'FKExtraSidecontrolerBButtonP_R.rz', -1)
    createConnect(myCon+'.C7', 'FKExtraSidecontrolerBButtonQ_R.rz', -1)
    createConnect(myCon+'.C8', 'FKExtraSidecontrolerBButtonR_R.rz', -1)
    createConnect(myCon+'.C9', 'FKExtraSidecontrolerBButtonS_R.rz', -1)
    createConnect(myCon+'.D1', 'FKExtraSidecontrolerBButtonT_R.rz', -1)
    createConnect(myCon+'.D2', 'FKExtraSidecontrolerBButtonU_R.rz', -1)

    myConList = ['FKSidecontrolerBButtonA_R','FKSidecontrolerBButtonB_R','FKSidecontrolerBButtonC_R','FKSidecontrolerBButtonD_R','FKSidecontrolerBButtonE_R','FKSidecontrolerBButtonF_R']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSidecontrolerBButtonG_R','FKSidecontrolerBButtonI_R','FKSidecontrolerBButtonH_R','FKSidecontrolerBButtonJ_R']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKSidecontrolerBButtonK_R','FKSidecontrolerBButtonL_R','FKSidecontrolerBButtonM_R','FKSidecontrolerBButtonN_R','FKSidecontrolerBButtonO_R','FKSidecontrolerBButtonP_R','FKSidecontrolerBButtonQ_R','FKSidecontrolerBButtonR_R','FKSidecontrolerBButtonS_R','FKSidecontrolerBButtonT_R','FKSidecontrolerBButtonU_R']
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def pedal():
    # pedal piston
    makePiston('Z', 'Y', 'FKPaddalPistonA1_L', 'FKPaddalA1_L')
    makePiston('Z', 'Y', 'FKPaddalPistonA3_L', 'FKPaddalA3_L')
    makePiston('Z', 'Y', 'FKPaddalPistonB_L', 'FKPaddalB1_L')

    cmds.hide('FKPaddalPistonA_L','FKPaddalA1_L','FKPaddalA3_L','FKPaddalPistonB_L','FKPaddalB1_L')

    myConList = ['FKPaddal_L']
    myList = ['sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKPaddalA_L','FKPaddalB_L']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

def hatch():
    # hatch
    makeLookAt_makeLookAtPos('Z', 'Y', 'HatchCoverClipLook_L', 'FKHatchCoverClipA_L','HatchCoverClipA1_L')
    makeLookAt_makeLookAtPos('Z', 'Y', 'HatchCoverClipLook_L', 'FKHatchCoverClipB_L','HatchCoverClipB1_L')
    makeLookAt_makeLookAtPos('Z', 'Y', 'HatchCoverClipLook_L', 'FKHatchCoverClipC_L','HatchCoverClipC1_L')

    createConnect('FKHatchCoverA_L.tz', 'FKExtraHatchCoverClipLook_L.tz', 0.7)

    myConList = ['FKHatchCoverB_L']
    myList = ['tx','ty','tz','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHatchCoverC_L']
    myList = ['tx','ty','tz','rx','ry','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHatchCoverA_L']
    myList = ['tx','ty','rx','ry','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    myConList = ['FKHatchCoverClipLook_L']
    myList = ['tx','ty','rx','ry','rz','sx','sy','sz','v']
    for myCon in myConList:
        for i in myList:
            cmds.setAttr (myCon+'.'+i, lock=True, keyable=False, channelBox=False )

    cmds.hide('FKHatchCoverClipA_L','FKHatchCoverClipB_L','FKHatchCoverClipC_L')

def pan():
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

def chair():
    # chair
    cmds.setAttr( "IKSplineA3_R.stretchy", 0)
    cmds.setAttr( "IKSplineA3_L.stretchy", 0)

def midlight():
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

    cmds.parentConstraint('Root_M','MidlightLook_R_nul', mo=True)
    cmds.parentConstraint('Root_M','MidlightLook_L_nul', mo=True)
    cmds.scaleConstraint('Root_M','MidlightLook_R_nul', mo=True)
    cmds.scaleConstraint('Root_M','MidlightLook_L_nul', mo=True)

def engine():
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

conName()
monitorA()
center_button()
left_button()
right_button()
pedal()
hatch()
