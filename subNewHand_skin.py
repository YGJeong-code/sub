import maya.cmds as cmds
import maya.mel as mel

# skin delete
myGrp = cmds.ls('robotHand_geo_Grp')
cmds.delete( cmds.listRelatives(myGrp, c=True, ad=True, type='geometryShape'), constructionHistory=True )

myPath = 'C:/woody/202210/rig/robotHand/skin/'

# robotHand_A_Grp
def skinAgrp():
    myMeshShape = cmds.listRelatives('robotHand_A_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Root_M', i,tsb=True)

    myMeshShape = cmds.listRelatives('robotHand_A_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Root_M', i,tsb=True)

    myMesh = 'robotHand_A_c_a_rubber_geo'
    mySkin = cmds.skinCluster('Rubber8_M','Rubber9_M', myMesh,tsb=True)
    cmds.deformerWeights('rubberA.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_A_c_b_rubber_geo'
    mySkin = cmds.skinCluster('Rubber5_M','Rubber6_M','Rubber7_M','Rubber8_M','Rubber9_M', myMesh,tsb=True)
    cmds.deformerWeights('rubberB.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_A_c_c_rubber_geo'
    mySkin = cmds.skinCluster('Root_M','Rubber1_M','Rubber2_M','Rubber3_M','Rubber4_M','Rubber5_M','Rubber6_M','Rubber7_M','Rubber8_M', myMesh,tsb=True)
    cmds.deformerWeights('rubberC.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_A_c_d_metal_geo'
    mySkin = cmds.skinCluster('Rubber9_M', myMesh,tsb=True)

# robotHand_B_Grp
def skinBgrp():
    myMesh = 'robotHand_B_a_a_metal_geo'
    mySkin = cmds.skinCluster('Body_M','add_Arm_M', myMesh,tsb=True)
    cmds.deformerWeights('arm00.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_B_a_b_metal_geo'
    mySkin = cmds.skinCluster('Arm_M','add_Arm2_M', myMesh,tsb=True)
    cmds.deformerWeights('arm01.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_B_b_a_metal_geo'
    mySkin = cmds.skinCluster('Arm2_M','add_Arm3_M', myMesh,tsb=True)
    cmds.deformerWeights('arm02.xml', im=True, deformer=mySkin, path=myPath)

    myMesh = 'robotHand_B_b_b_metal_geo'
    mySkin = cmds.skinCluster('Arm3_M','add_Arm5_M', myMesh,tsb=True)
    cmds.deformerWeights('arm03.xml', im=True, deformer=mySkin, path=myPath)

    cmds.skinCluster('add_Arm5_M', 'robotHand_B_b_c_metal_geo', tsb=True)

# robotHand_C_Grp
def skinCgrp():
    mySkin = cmds.skinCluster('Arm5_M','Suspension1_M', 'robotHand_C_a_b_metal_geo', tsb=True)
    cmds.deformerWeights('suspension.xml', im=True, deformer=mySkin, path=myPath)

    # cmds.skinCluster('Suspension1_M', 'robotHand_C_a_c_metal_geo', tsb=True)
    cmds.skinCluster('Suspension1_M', 'robotHand_C_a_c_a_metal_geo', tsb=True)
    cmds.skinCluster('HandRotate1_M', 'robotHand_C_a_c_b_metal_geo', tsb=True)

    cmds.skinCluster('Hand_M', 'robotHand_C_a_d_metal_geo', tsb=True)
    cmds.skinCluster('Hand1_M', 'robotHand_C_a_e_metal_geo', tsb=True)
    cmds.skinCluster('Hand2_M', 'robotHand_C_a_f_metal_geo', tsb=True)

    cmds.skinCluster('Hand3_M', 'robotHand_C_a_a_a_a_metal_geo', tsb=True)
    cmds.skinCluster('Hand3_M', 'robotHand_C_a_a_a_b_metal_geo', tsb=True)

    mySkin = cmds.skinCluster('Hand3_M','Hand4_M', 'robotHand_C_a_a_a_c_metal_geo', tsb=True)
    cmds.deformerWeights('hand.xml', im=True, deformer=mySkin, path=myPath)

    cmds.skinCluster('Hand4_M', 'robotHand_C_a_a_a_d_metal_geo', tsb=True)
    cmds.skinCluster('Hand5_M', 'robotHand_C_a_a_a_e_metal_geo', tsb=True)

    cmds.skinCluster('FingerB_L', 'robotHand_C_a_a_b_a_a_metal_geo', tsb=True)
    cmds.skinCluster('FingerB_L', 'robotHand_C_a_a_b_a_b_metal_geo', tsb=True)
    cmds.skinCluster('FingerB1_L', 'robotHand_C_a_a_b_a_c_metal_geo', tsb=True)
    cmds.skinCluster('FingerB2_L', 'robotHand_C_a_a_b_a_d_metal_geo', tsb=True)

    cmds.skinCluster('FingerA_M', 'robotHand_C_a_a_b_b_a_metal_geo', tsb=True)
    cmds.skinCluster('FingerA_M', 'robotHand_C_a_a_b_b_b_metal_geo', tsb=True)
    cmds.skinCluster('FingerA1_M', 'robotHand_C_a_a_b_b_c_metal_geo', tsb=True)
    cmds.skinCluster('FingerA2_M', 'robotHand_C_a_a_b_b_d_metal_geo', tsb=True)

    cmds.skinCluster('FingerB_R', 'robotHand_C_a_a_b_c_a_metal_geo', tsb=True)
    cmds.skinCluster('FingerB_R', 'robotHand_C_a_a_b_c_b_metal_geo', tsb=True)
    cmds.skinCluster('FingerB1_R', 'robotHand_C_a_a_b_c_c_metal_geo', tsb=True)
    cmds.skinCluster('FingerB2_R', 'robotHand_C_a_a_b_c_d_metal_geo', tsb=True)

    cmds.skinCluster('BeamA_M', 'robotHand_C_b_a_a_metal_geo', tsb=True)
    cmds.skinCluster('BeamA1_M', 'robotHand_C_b_a_b_metal_geo', tsb=True)
    cmds.skinCluster('BeamACover_M', 'robotHand_C_b_a_c_metal_geo', tsb=True)
    cmds.skinCluster('BeamA1_M', 'robotHand_C_b_a_d_metal_geo', tsb=True)
    cmds.skinCluster('BeamA2_M', 'robotHand_C_b_a_e_metal_geo', tsb=True)
    cmds.skinCluster('BeamA3_M', 'robotHand_C_b_a_f_metal_geo', tsb=True)
    cmds.skinCluster('BeamA4_M', 'robotHand_C_b_a_g_metal_geo', tsb=True)
    cmds.skinCluster('BeamA5_M', 'robotHand_C_b_a_h_metal_geo', tsb=True)

    cmds.skinCluster('BeamB_R', 'robotHand_C_b_b_a_metal_geo', tsb=True)
    cmds.skinCluster('BeamB1_R', 'robotHand_C_b_b_b_metal_geo', tsb=True)
    cmds.skinCluster('BeamBCover_R', 'robotHand_C_b_b_c_metal_geo', tsb=True)
    cmds.skinCluster('BeamB1_R', 'robotHand_C_b_b_d_metal_geo', tsb=True)
    cmds.skinCluster('BeamB2_R', 'robotHand_C_b_b_e_metal_geo', tsb=True)
    cmds.skinCluster('BeamB3_R', 'robotHand_C_b_b_f_metal_geo', tsb=True)
    cmds.skinCluster('BeamB4_R', 'robotHand_C_b_b_g_metal_geo', tsb=True)
    cmds.skinCluster('BeamB5_R', 'robotHand_C_b_b_h_metal_geo', tsb=True)

    cmds.skinCluster('BeamB_L', 'robotHand_C_b_c_a_metal_geo', tsb=True)
    cmds.skinCluster('BeamB1_L', 'robotHand_C_b_c_b_metal_geo', tsb=True)
    cmds.skinCluster('BeamBCover_L', 'robotHand_C_b_c_c_metal_geo', tsb=True)
    cmds.skinCluster('BeamB1_L', 'robotHand_C_b_c_d_metal_geo', tsb=True)
    cmds.skinCluster('BeamB2_L', 'robotHand_C_b_c_e_metal_geo', tsb=True)
    cmds.skinCluster('BeamB3_L', 'robotHand_C_b_c_f_metal_geo', tsb=True)
    cmds.skinCluster('BeamB4_L', 'robotHand_C_b_c_g_metal_geo', tsb=True)
    cmds.skinCluster('BeamB5_L', 'robotHand_C_b_c_h_metal_geo', tsb=True)

# make skin add joint
def skinAddJnt():
    myJntList = ['Arm_M','Arm2_M','Arm3_M','Arm5_M']
    for myJnt in myJntList:
        cmds.select(cl=True)
        myBaseJnt = cmds.joint()
        mySkinJnt = 'add_'+myJnt

        if bool(cmds.objExists(mySkinJnt)):
            cmds.delete(myBaseJnt)
        else:
            cmds.rename(myBaseJnt, mySkinJnt)
            cmds.matchTransform(mySkinJnt,myJnt)

            cmds.pointConstraint(myJnt, mySkinJnt)
            cmds.scaleConstraint(myJnt, mySkinJnt)

            myParent = cmds.listRelatives(myJnt, p=True)
            cmds.parent(mySkinJnt, myParent)

def skinMethod():
    for i in cmds.listRelatives(myGrp, c=True, ad=True, type='geometryShape'):
        if bool( mel.eval('findRelatedSkinCluster '+i) ):
            mySkin = mel.eval('findRelatedSkinCluster '+i)
            cmds.setAttr ( mySkin + '.skinningMethod', 1 )

skinAddJnt()
skinAgrp()
skinBgrp()
skinCgrp()
skinMethod()
