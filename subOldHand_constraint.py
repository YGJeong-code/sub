import maya.cmds as cmds
import maya.mel as mel

myGrp = 'subOldHand_geo_Grp'
myPath = 'C:/woody/202210/rig/subOldHand/skin/'

# delete constraint
cmds.delete( cmds.listRelatives(myGrp, c=True, ad=True, type='constraint') )

# delete skin
cmds.delete( cmds.listRelatives(myGrp, c=True, ad=True, type='geometryShape'), constructionHistory=True )

def allMeshScale():
    myMeshShape = cmds.listRelatives(myGrp, c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_monitorA_a_a_a_b_metal_geo':
            pass
        elif i == 'sub_interiol_monitorA_b_metal_geo':
            pass
        elif i == 'sub_hatch_cover_b_metal_geo':
            pass
        elif i == 'sub_engineC_Grp' in cmds.listRelatives(i, f=True)[0]:
            pass
        elif i == 'sub_interiol_body_j_a_plastic_geo':
            pass
        elif i == 'sub_engineB_Grp' in cmds.listRelatives(i, f=True)[0]:
            pass
        elif i == 'sub_engineF_metal_geo':
            pass
        elif i == 'sub_engineH_metal_geo':
            pass
        elif 'sub_C_fan_Grp' in cmds.listRelatives(i, f=True)[0]:
            pass
        elif 'sub_C_interiol_chair_Grp' in cmds.listRelatives(i, f=True)[0]:
            pass
        elif i == 'sub_interiol_centerjoystick_a_a_a_a_b_rubber_geo':
            pass
        elif i == 'sub_interiol_centerjoystick_a_a_c_b_rubber_geo':
            pass
        else:
            cmds.scaleConstraint ('Main', i)

# sampler
def subOldHand_sampler_Grp_const():
    cmds.parentConstraint ('Sampler_L', 'subOldHand_samplerB_metal_geo', mo=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Sampler1_L', i, mo=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_a_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Sampler2_L', i, mo=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_a_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'subOldHand_samplerA_a_b_a_a_a_a_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_a_b_a_a_b_glassD_geo':
            cmds.parentConstraint ('CapA_L', i, mo=True)
        elif i == 'subOldHand_samplerA_a_b_a_a_a_c_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_a_b_a_b_b_glassD_geo':
            cmds.parentConstraint ('CapB_L', i, mo=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_a_a_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_b_b_a_b_glassD_geo':
            cmds.parentConstraint ('CapC_L', i, mo=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_a_c_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_b_b_a_b_b_glassD_geo':
            cmds.parentConstraint ('CapD_L', i, mo=True)
        elif i == 'subOldHand_samplerA_a_b_a_a_b_b_metal_geo':
            cmds.parentConstraint ('ValveA_L', i, mo=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_b_b_metal_geo':
            cmds.parentConstraint ('ValveB_L', i, mo=True)
        else:
            cmds.parentConstraint ('Sampler3_L', i, mo=True)

# oldHandA
def subOldHand_oldarmA_Grp_const():
    cmds.skinCluster('pistonA_R', 'subOldHand_oldarmA_b_a_metal_geo',tsb=True)
    cmds.skinCluster('Body1_R', 'subOldHand_oldarmA_b_b_metal_geo',tsb=True)

    cmds.skinCluster('Attach1_M','HoseA_R','HoseA1_R','HoseB_R','HoseC_R','HoseC1_R', 'subOldHand_oldarmA_c_rubber_geo',tsb=True)
    mel.eval('deformerWeights -import -method "index" -deformer "skinCluster32" -path "C:/Users/ygjeong/Desktop/ygjeong/202210/rig/subOldHand/" "hose_skin.xml"; skinCluster -e -forceNormalizeWeights "skinCluster32";')

    cmds.skinCluster('Body_M', 'subOldHand_oldarmA_a_b_metal_geo',tsb=True)
    cmds.skinCluster('Body_M', 'subOldHand_oldarmA_a_c_metal_geo',tsb=True)

    myMeshShape = cmds.listRelatives('subOldHand_oldarmA_a_a_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Attach1_M', i,tsb=True)

    cmds.skinCluster('Root_M', 'subOldHand_oldarmA_a_a_b_metal_geo',tsb=True)
    cmds.skinCluster('Root_M', 'subOldHand_oldarmA_a_a_c_metal_geo',tsb=True)
    cmds.skinCluster('Root_M', 'subOldHand_oldarmA_a_a_d_metal_geo',tsb=True)

allMeshScale()
subOldHand_sampler_Grp_const()
subOldHand_oldarmA_Grp_const()
