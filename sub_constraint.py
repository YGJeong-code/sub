import maya.cmds as cmds
import maya.mel as mel

# delete constraint
cmds.delete( cmds.listRelatives('sub_geo_Grp', c=True, ad=True, type='constraint') )

# skin delete
cmds.select ('sub_geo_Grp')
cmds.select (hi=True)
mySel = cmds.ls(sl=True)
cmds.delete(mySel, constructionHistory = True)

myPath = 'C:/woody/202210/rig/sub/skin/'

def allMeshScale():
    myMeshShape = cmds.listRelatives('sub_geo_Grp', c=True, ad=True, type='geometryShape')
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

def sub_body_Grp_const():
    myMeshShape = cmds.listRelatives('sub_body_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Root_M', i, mo=True)

def sub_interiol_monitorA_Grp_const():
    # cmds.parentConstraint ('MonitorABottom_M', 'sub_interiol_monitorA_b_metal_geo', mo=True)
    mySkin = cmds.skinCluster('Root_M','MonitorABottom_M', 'sub_interiol_monitorA_b_metal_geo', tsb=True)
    cmds.deformerWeights('MonitorABottom.xml', im=True, deformer=mySkin, path=myPath)

    cmds.parentConstraint ('MonitorA_M', 'sub_interiol_monitorA_a_b_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorA1_M', 'sub_interiol_monitorA_a_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorA1_M', 'sub_interiol_monitorA_a_b_c_plastic_geo', mo=True)

    cmds.parentConstraint ('MonitorA2_M', 'sub_interiol_monitorA_a_a_b_c_metal_geo', mo=True)

    cmds.parentConstraint ('MonitorA3_M', 'sub_interiol_monitorA_a_a_b_b_metal_geo', mo=True)
    myMeshShape = cmds.listRelatives('sub_interiol_monitorA_a_a_b_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('MonitorA3_M', i, mo=True)

    cmds.parentConstraint ('MonitorA4_M', 'sub_interiol_monitorA_a_a_a_c_metal_geo', mo=True)

    mySkin = cmds.skinCluster('MonitorA5_M','MonitorA6_M', 'sub_interiol_monitorA_a_a_a_b_metal_geo', tsb=True)
    cmds.deformerWeights('monitorA.xml', im=True, deformer=mySkin, path=myPath)

    cmds.parentConstraint ('MonitorA6_M', 'sub_interiol_monitorA_a_a_a_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('MonitorA6_M', 'sub_interiol_monitorA_a_a_a_a_emission_geo', mo=True)

def sub_interiol_centerjoystick_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_interiol_centerjoystick_d_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_interiol_centerjoystick_e_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_interiol_centerjoystick_f_metal_geo', mo=True)

    cmds.parentConstraint ('Root_M', 'sub_interiol_centerjoystick_a_a_a_a_a_metal_geo', mo=True)
    mySkin = cmds.skinCluster('CenterjoystickRubber_M','CenterjoystickRubber1_M','CenterjoystickRubber2_M','CenterjoystickRubber3_M','CenterjoystickRubber4_M','Centerjoystick_M', 'sub_interiol_centerjoystick_a_a_a_a_b_rubber_geo', tsb=True)
    cmds.deformerWeights('CenterjoystickRubber.xml', im=True, method='index', deformer=mySkin, path=myPath)
    cmds.skinCluster(mySkin, e=True, forceNormalizeWeights=True)

    cmds.parentConstraint ('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_a_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Centerjoystick5_M', 'sub_interiol_centerjoystick_a_a_b_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick3_M', 'sub_interiol_centerjoystick_a_a_b_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Centerjoystick17_M', 'sub_interiol_centerjoystick_a_a_c_a_plastic_geo', mo=True)
    mySkin = cmds.skinCluster('Centerjoystick17Rubber_M','Centerjoystick17Rubber1_M','Centerjoystick17Rubber2_M','Centerjoystick17Rubber3_M','Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_c_b_rubber_geo', tsb=True)
    cmds.deformerWeights('Centerjoystick17Rubber.xml', im=True, method='index', deformer=mySkin, path=myPath)
    cmds.skinCluster(mySkin, e=True, forceNormalizeWeights=True)

    cmds.parentConstraint ('Centerjoystick15_R', 'sub_interiol_centerjoystick_a_a_d_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_d_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Centerjoystick13_L', 'sub_interiol_centerjoystick_a_a_e_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_e_b_metal_geo', mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_a_a_f_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_centerjoystick_a_a_f_b_a_plastic_geo':
            cmds.parentConstraint ('Centerjoystick7_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_a_f_d_b_plastic_geo':
            cmds.parentConstraint ('Centerjoystick9_M', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_a_f_c_a_plastic_geo':
            cmds.parentConstraint ('Centerjoystick11_R', i, mo=True)
        else:
            cmds.parentConstraint ('Centerjoystick1_M', i, mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_a_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_centerjoystick_a_b_a_a_a_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonC_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_b_a_a_b_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonB_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_b_a_b_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonA_M', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_b_a_a_c_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonB_R', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_a_b_a_a_d_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonC_R', i, mo=True)
        else:
            cmds.parentConstraint ('Centerjoystick_M', i, mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_centerjoystick_b_a_a_a_metal_geo':
            cmds.parentConstraint ('CenterjoystickButtonF_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_a_b_a_metal_geo':
            cmds.parentConstraint ('CenterjoystickButtonE_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_a_c_a_metal_geo':
            cmds.parentConstraint ('CenterjoystickButtonD_M', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_a_d_a_metal_geo':
            cmds.parentConstraint ('CenterjoystickButtonE_R', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_a_e_a_metal_geo':
            cmds.parentConstraint ('CenterjoystickButtonF_R', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_a_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonJ_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_b_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonI_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_c_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonH_L', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_d_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonG_M', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_e_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonH_R', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_f_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonI_R', i, mo=True)
        elif i == 'sub_interiol_centerjoystick_b_b_g_a_plastic_geo':
            cmds.parentConstraint ('CenterjoystickButtonJ_R', i, mo=True)
        else:
            cmds.parentConstraint ('Centerjoystick_M', i, mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_c_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Centerjoystick_M', i, mo=True)

def sub_L_interiol_sidecontrolerA_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_L_interiol_sidecontrolerA_a_d_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonR_L', 'sub_L_interiol_sidecontrolerA_a_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonS_L', 'sub_L_interiol_sidecontrolerA_a_a_b_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonT_L', 'sub_L_interiol_sidecontrolerA_a_a_c_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonQ_L', 'sub_L_interiol_sidecontrolerA_a_a_d_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonP_L', 'sub_L_interiol_sidecontrolerA_a_a_e_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonO_L', 'sub_L_interiol_sidecontrolerA_a_a_f_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonN_L', 'sub_L_interiol_sidecontrolerA_a_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonM_L', 'sub_L_interiol_sidecontrolerA_a_b_b_metal_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonL_L', 'sub_L_interiol_sidecontrolerA_a_b_c_metal_geo', mo=True)

    cmds.parentConstraint ('Root_M', 'sub_L_interiol_sidecontrolerA_a_c_a_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_L_interiol_sidecontrolerA_a_c_c_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonK_L', 'sub_L_interiol_sidecontrolerA_a_c_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonK_L', 'sub_L_interiol_sidecontrolerA_a_c_b_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Root_M', 'sub_L_interiol_sidecontrolerA_b_d_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_L_interiol_sidecontrolerA_b_e_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonJ_L', 'sub_L_interiol_sidecontrolerA_b_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonI_L', 'sub_L_interiol_sidecontrolerA_b_a_b_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonH_L', 'sub_L_interiol_sidecontrolerA_b_a_c_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonG_L', 'sub_L_interiol_sidecontrolerA_b_a_d_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonF_L', 'sub_L_interiol_sidecontrolerA_b_a_e_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonE_L', 'sub_L_interiol_sidecontrolerA_b_a_f_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonD_L', 'sub_L_interiol_sidecontrolerA_b_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonB_L', 'sub_L_interiol_sidecontrolerA_b_b_b_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerAButtonC_L', 'sub_L_interiol_sidecontrolerA_b_c_a_glassD_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerAButtonA_L', 'sub_L_interiol_sidecontrolerA_b_c_b_glassD_geo', mo=True)

def sub_R_interiol_sidecontrolerB_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_R_interiol_sidecontrolerB_a_d_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonS_R', 'sub_R_interiol_sidecontrolerB_a_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonR_R', 'sub_R_interiol_sidecontrolerB_a_a_b_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonQ_R', 'sub_R_interiol_sidecontrolerB_a_a_c_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonN_R', 'sub_R_interiol_sidecontrolerB_a_a_d_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonO_R', 'sub_R_interiol_sidecontrolerB_a_a_e_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonP_R', 'sub_R_interiol_sidecontrolerB_a_a_f_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonM_R', 'sub_R_interiol_sidecontrolerB_a_a_g_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonL_R', 'sub_R_interiol_sidecontrolerB_a_a_h_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonK_R', 'sub_R_interiol_sidecontrolerB_a_a_i_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonT_R', 'sub_R_interiol_sidecontroler_B_a_b_a_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonU_R', 'sub_R_interiol_sidecontroler_B_a_b_b_plastic_geo', mo=True)

    myMeshShape = cmds.listRelatives('sub_R_interiol_sidecontrolerB_a_c_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Root_M', i, mo=True)

    cmds.parentConstraint ('Root_M', 'sub_R_interiol_sidecontrolerB_b_d_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_R_interiol_sidecontrolerB_b_e_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonD_R', 'sub_R_interiol_sidecontrolerB_b_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonF_R', 'sub_R_interiol_sidecontrolerB_b_a_b_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonE_R', 'sub_R_interiol_sidecontrolerB_b_a_c_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonA_R', 'sub_R_interiol_sidecontrolerB_b_a_d_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonC_R', 'sub_R_interiol_sidecontrolerB_b_a_e_plastic_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonB_R', 'sub_R_interiol_sidecontrolerB_b_a_f_plastic_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonJ_R', 'sub_R_interiol_sidecontrolerB_b_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonH_R', 'sub_R_interiol_sidecontrolerB_b_b_b_metal_geo', mo=True)

    cmds.parentConstraint ('SidecontrolerBButtonG_R', 'sub_R_interiol_sidecontrolerB_b_c_a_glassD_geo', mo=True)
    cmds.parentConstraint ('SidecontrolerBButtonI_R', 'sub_R_interiol_sidecontrolerB_b_c_b_glassD_geo', mo=True)

def sub_interiol_paddal_Grp_const():
    myMeshShape = cmds.listRelatives('sub_interiol_paddal_a_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('PaddalA_L', i, mo=True)

    cmds.parentConstraint ('PaddalA1_L', 'sub_interiol_paddal_a_b_a_a_a_metal_geo', mo=True)
    cmds.parentConstraint ('PaddalPistonA1_L', 'sub_interiol_paddal_a_b_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('PaddalPistonA1_L', 'sub_interiol_paddal_a_b_a_b_metal_geo', mo=True)

    cmds.parentConstraint ('PaddalA3_L', 'sub_interiol_paddal_a_b_b_a_a_metal_geo', mo=True)
    cmds.parentConstraint ('PaddalA3_L', 'sub_interiol_paddal_a_b_b_a_b_metal_geo', mo=True)

    cmds.parentConstraint ('PaddalPistonA3_L', 'sub_interiol_paddal_a_b_b_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('PaddalPistonA3_L', 'sub_interiol_paddal_a_b_b_b_b_metal_geo', mo=True)

    cmds.parentConstraint ('PaddalPistonA_L', 'sub_interiol_paddal_a_c_metal_geo', mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_paddal_b_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('PaddalB_L', i, mo=True)

    cmds.parentConstraint ('PaddalB1_L', 'sub_interiol_paddal_b_b_a_a_metal_geo', mo=True)
    cmds.parentConstraint ('PaddalB1_L', 'sub_interiol_paddal_b_b_a_b_metal_geo', mo=True)

    cmds.parentConstraint ('PaddalPistonB_L', 'sub_interiol_paddal_b_b_b_metal_geo', mo=True)

    myMeshShape = cmds.listRelatives('sub_interiol_paddal_c_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Paddal_L', i, mo=True)

def sub_hatch_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_hatch_bar_metal_geo', mo=True)

    myMeshShape = cmds.listRelatives('sub_hatch_body_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Root_M', i, mo=True)

    cmds.parentConstraint ('HatchCoverB_L', 'sub_hatch_cover_clip_a_a_metal_geo', mo=True)
    cmds.parentConstraint ('HatchCoverClipA_L', 'sub_hatch_cover_clip_a_b_metal_geo', mo=True)

    cmds.parentConstraint ('HatchCoverB_L', 'sub_hatch_cover_clip_b_a_metal_geo', mo=True)
    cmds.parentConstraint ('HatchCoverClipB_L', 'sub_hatch_cover_clip_b_b_metal_geo', mo=True)

    cmds.parentConstraint ('HatchCoverB_L', 'sub_hatch_cover_clip_c_a_metal_geo', mo=True)
    cmds.parentConstraint ('HatchCoverClipC_L', 'sub_hatch_cover_clip_c_b_metal_geo', mo=True)

    cmds.parentConstraint ('HatchCoverA_L', 'sub_hatch_cover_a_metal_geo', mo=True)

    mySkin = cmds.skinCluster('HatchCoverB_L','HatchCoverClipLook_L', 'sub_hatch_cover_b_metal_geo', tsb=True)
    cmds.deformerWeights('HatchCover.xml', im=True, deformer=mySkin, path=myPath)

    cmds.parentConstraint ('HatchCoverC_L', 'sub_hatch_cover_c_metal_geo', mo=True)

def sub_interiol_topmonitor_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_interiol_topmonitor_b_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_interiol_topmonitor_c_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_interiol_topmonitor_d_metal_geo', mo=True)

    cmds.parentConstraint ('Topmonitor_M', 'sub_interiol_topmonitor_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('Topmonitor1_M', 'sub_interiol_topmonitor_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('Topmonitor2_M', 'sub_interiol_topmonitor_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('Topmonitor3_M', 'sub_interiol_topmonitor_a_a_a_a_c_metal_geo', mo=True)

    cmds.parentConstraint ('Topmonitor4_L', 'sub_interiol_topmonitor_a_a_a_a_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Topmonitor4_L', 'sub_interiol_topmonitor_a_a_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('Topmonitor4_L', 'sub_interiol_topmonitor_a_a_a_a_a_c_emission_geo', mo=True)

    cmds.parentConstraint ('Topmonitor4_R', 'sub_interiol_topmonitor_a_a_a_a_b_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Topmonitor4_R', 'sub_interiol_topmonitor_a_a_a_a_b_b_metal_geo', mo=True)
    cmds.parentConstraint ('Topmonitor4_R', 'sub_interiol_topmonitor_a_a_a_a_b_c_emission_geo', mo=True)

def sub_C_midlight_Grp_const():
    cmds.parentConstraint ('Midlight1_R', 'sub_R_midlight_a_metal_geo', mo=True)
    cmds.parentConstraint ('Midlight_R', 'sub_R_midlight_b_metal_geo', mo=True)
    cmds.parentConstraint ('Midlight1_R', 'sub_R_midlight_c_emission_geo', mo=True)
    cmds.parentConstraint ('Midlight1_R', 'sub_R_midlight_d_glassD_geo', mo=True)

    cmds.parentConstraint ('Midlight1_L', 'sub_L_midlight_a_metal_geo', mo=True)
    cmds.parentConstraint ('Midlight_L', 'sub_L_midlight_b_metal_geo', mo=True)
    cmds.parentConstraint ('Midlight1_L', 'sub_L_midlight_emission_geo', mo=True)

def sub_interiol_body_Grp_const():
    myMeshShape = cmds.listRelatives('sub_interiol_body_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_body_j_a_plastic_geo':
            mySkin = cmds.skinCluster('Footstool1_L', i, tsb=True)
        elif i == 'sub_interiol_body_j_b_plastic_geo':
            cmds.parentConstraint ('Footstool_L', i, mo=True)
        else:
            cmds.parentConstraint ('Root_M', i, mo=True)

def sub_engine_Grp_const():
    # sub_engineA_Grp
    myMeshShape = cmds.listRelatives('sub_engineA_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Root_M', i, mo=True)

    # sub_engineB_Grp
    cmds.skinCluster('EngineB_L','EngineB_R', 'sub_engineB_a_metal_geo', tsb=True)
    cmds.skinCluster('EngineB_L','EngineB_R', 'sub_engineB_b_metal_geo', tsb=True)
    cmds.skinCluster('EngineB_L','EngineB_R', 'sub_engineB_c_metal_geo', tsb=True)

    # sub_engineC_Grp
    mySkin = cmds.skinCluster('Rubber9_M','Rubber10_M','Rubber11_M','Rubber12_M', 'sub_engineC_a_rubber_rubber_geo', tsb=True)
    cmds.deformerWeights('rubberA.xml', im=True, method='index', deformer=mySkin, path=myPath)
    cmds.skinCluster(mySkin, e=True, forceNormalizeWeights=True)

    mySkin = cmds.skinCluster('Rubber7_M','Rubber8_M','Rubber9_M','Rubber10_M','Rubber11_M', 'sub_engineC_b_rubber_rubber_geo', tsb=True)
    cmds.deformerWeights('rubberB.xml', im=True, method='index', deformer=mySkin, path=myPath)
    cmds.skinCluster(mySkin, e=True, forceNormalizeWeights=True)

    mySkin = cmds.skinCluster('Root_M','Rubber_M','Rubber1_M','Rubber2_M','Rubber3_M','Rubber4_M','Rubber5_M','Rubber6_M','Rubber7_M','Rubber8_M','Rubber9_M','Rubber10_M','Rubber11_M','Rubber12_M', 'sub_engineC_c_rubber_rubber_geo', tsb=True)
    cmds.deformerWeights('rubberC.xml', im=True, method='index', deformer=mySkin, path=myPath)
    cmds.skinCluster(mySkin, e=True, forceNormalizeWeights=True)

    # etc
    cmds.parentConstraint ('Root_M', 'sub_engineD_metal_geo', mo=True)
    cmds.parentConstraint ('Root_M', 'sub_engineE_metal_geo', mo=True)

    mySkin = cmds.skinCluster('EngineFA_R','EngineFB_R','EngineFC_R','EngineFA_L','EngineFB_L','EngineFC_L', 'sub_engineF_metal_geo', tsb=True)
    cmds.deformerWeights('engineF.xml', im=True, deformer=mySkin, path=myPath)

    cmds.parentConstraint ('Root_M', 'sub_engineG_metal_geo', mo=True)

    mySkin = cmds.skinCluster('Root_M','EngineH_L','EngineH1_L','EngineH_R','EngineH1_R', 'sub_engineH_metal_geo', tsb=True)
    cmds.deformerWeights('engineH.xml', im=True, deformer=mySkin, path=myPath)

    cmds.parentConstraint ('Root_M', 'sub_engineI_metal_geo', mo=True)

def sub_C_fan_Grp_const():
    # sub_L_fanA_Grp
    mySkin = cmds.skinCluster('FanA_L', 'sub_L_fanA_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanA1_L', 'sub_L_fanA_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_L_fanA_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanA_L', 'sub_L_fanA_d_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanA_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanA_L', 'sub_L_fanA_e_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanA_e.xml', im=True, deformer=mySkin, path=myPath)

    # sub_R_fanA_Grp
    mySkin = cmds.skinCluster('FanA_R', 'sub_R_fanA_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanA1_R', 'sub_R_fanA_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_R_fanA_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanA_R', 'sub_R_fanA_d_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanA_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanA_R', 'sub_R_fanA_e_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanA_e.xml', im=True, deformer=mySkin, path=myPath)

    # sub_L_fanB_Grp
    mySkin = cmds.skinCluster('FanB_L', 'sub_L_fanB_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanB1_L', 'sub_L_fanB_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_L_fanB_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanB_L', 'sub_L_fanB_d_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanB_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanB_L', 'sub_L_fanB_e_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanB_e.xml', im=True, deformer=mySkin, path=myPath)

    # sub_R_fanB_Grp
    mySkin = cmds.skinCluster('FanB_R', 'sub_R_fanB_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanB1_R', 'sub_R_fanB_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_R_fanB_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanB_R', 'sub_R_fanB_d_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanB_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanB_R', 'sub_R_fanB_e_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanB_e.xml', im=True, deformer=mySkin, path=myPath)

    # sub_L_fanC_Grp
    mySkin = cmds.skinCluster('FanC_L', 'sub_L_fanC_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanC1_L', 'sub_L_fanC_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_L_fanC_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanC_L', 'sub_L_fanC_d_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanC_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanC_L', 'sub_L_fanC_e_metal_geo', tsb=True)
    cmds.deformerWeights('L_fanC_e.xml', im=True, deformer=mySkin, path=myPath)

    # sub_R_fanC_Grp
    mySkin = cmds.skinCluster('FanC_R', 'sub_R_fanC_a_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('FanC1_R', 'sub_R_fanC_b_metal_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M', 'sub_R_fanC_c_rubber_geo', tsb=True)
    mySkin = cmds.skinCluster('Root_M','FanC_R', 'sub_R_fanC_d_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanC_d.xml', im=True, deformer=mySkin, path=myPath)
    mySkin = cmds.skinCluster('Root_M','FanC_R', 'sub_R_fanC_e_metal_geo', tsb=True)
    cmds.deformerWeights('R_fanC_e.xml', im=True, deformer=mySkin, path=myPath)

def sub_interiol_monitorC_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_interiol_monitorC_b_geo', mo=True)
    cmds.parentConstraint ('MonitorC_R', 'sub_interiol_monitorC_a_b_geo', mo=True)
    cmds.parentConstraint ('MonitorC1_R', 'sub_interiol_monitorC_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC1_R', 'sub_interiol_monitorC_a_a_c_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC2_R', 'sub_interiol_monitorC_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC2_R', 'sub_interiol_monitorC_a_a_a_c_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC3_R', 'sub_interiol_monitorC_a_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC4_R', 'sub_interiol_monitorC_a_a_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC5_R', 'sub_interiol_monitorC_a_a_a_a_a_a_b_metal_geo', mo=True)
    cmds.parentConstraint ('MonitorC5_R', 'sub_interiol_monitorC_a_a_a_a_a_a_a_plastic_geo', mo=True)
    cmds.parentConstraint ('MonitorC5_R', 'sub_interiol_monitorC_a_a_a_a_a_a_a_emission_geo', mo=True)

def sub_C_interiol_chair_Grp_const():
    mySkin = cmds.skinCluster('Chair_L','Chair1_L','Chair2_L', 'sub_L_interiol_chair_fabric_geo', tsb=True)
    cmds.deformerWeights('L_chair.xml', im=True, deformer=mySkin, path=myPath)

    mySkin = cmds.skinCluster('Chair_R','Chair1_R','Chair2_R', 'sub_R_interiol_chair_fabric_geo', tsb=True)
    cmds.deformerWeights('R_chair.xml', im=True, deformer=mySkin, path=myPath)

def etc():
    myMeshList = ['sub_interiol_backcontroler_Grp','sub_interiol_sidedetail_Grp','sub_interiol_screw_Grp','sub_mainglass_Grp']
    for mesh in myMeshList:
        myMeshShape = cmds.listRelatives(mesh, c=True, ad=True, type='geometryShape')
        myMesh = cmds.listRelatives(myMeshShape, p=True)
        for i in myMesh:
            cmds.parentConstraint ('Root_M', i, mo=True)

def deleteConst(mesh):
    myConstList = cmds.listRelatives(mesh, type='constraint')
    for const in myConstList:
        if 'scaleConstraint' in const:
            cmds.delete(const)

def copySkin(i, mesh):
    mySkinJntDict={}
    if bool( mel.eval('findRelatedSkinCluster '+i) ):
        skinFileName = mel.eval('findRelatedSkinCluster '+i)
        # make skin joint dict
        mySkinJntDict[i] = cmds.skinCluster(i, q=True, wi=True)
        mySkin = cmds.skinCluster(mySkinJntDict[i], mesh, tsb=True)
        # cmds.copySkinWeights( sourceSkin=skinFileName, destinationSkin=mySkin, noMirror=True )
        cmds.copySkinWeights( i, mesh, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation ='oneToOne' )

def proxy_const():
    myMeshShape = cmds.listRelatives('sub_PROXY', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for mesh in myMesh:
        i = mesh.replace('_PROXY','')

        if i == 'sub_interiol_monitorA_a_a_a_b_metal_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_interiol_monitorA_b_metal_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_hatch_cover_b_metal_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif 'sub_engineC_Grp' in cmds.listRelatives(i, f=True)[0]:
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_interiol_body_j_a_plastic_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif 'sub_engineB_Grp' in cmds.listRelatives(i, f=True)[0]:
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_engineF_metal_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_engineH_metal_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif 'sub_C_fan_Grp' in cmds.listRelatives(i, f=True)[0]:
            deleteConst(mesh)
            copySkin(i, mesh)
        elif 'sub_C_interiol_chair_Grp' in cmds.listRelatives(i, f=True)[0]:
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_interiol_centerjoystick_a_a_a_a_b_rubber_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        elif i == 'sub_interiol_centerjoystick_a_a_c_b_rubber_geo':
            deleteConst(mesh)
            copySkin(i, mesh)
        else:
            myConstList = cmds.listRelatives(i, type='constraint')
            for const in myConstList:
                if 'parentConstraint' in const:
                    targetCon = cmds.parentConstraint(const, q=True, tl=True)
                    cmds.parentConstraint(targetCon, mesh, mo=True)


allMeshScale()
sub_body_Grp_const()
sub_interiol_monitorA_Grp_const()
sub_interiol_centerjoystick_Grp_const()
sub_L_interiol_sidecontrolerA_Grp_const()
sub_R_interiol_sidecontrolerB_Grp_const()
sub_interiol_paddal_Grp_const()
sub_hatch_Grp_const()
sub_interiol_topmonitor_Grp_const()
sub_C_midlight_Grp_const()
sub_interiol_body_Grp_const()
sub_engine_Grp_const()
sub_C_fan_Grp_const()
sub_interiol_monitorC_Grp_const()
sub_C_interiol_chair_Grp_const()
etc()
proxy_const()
