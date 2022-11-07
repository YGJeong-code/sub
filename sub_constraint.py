import maya.cmds as cmds
import maya.mel as mel

# delete constraint
cmds.delete( cmds.listRelatives('sub_geo_Grp', c=True, ad=True, type='constraint') )

# skin delete
cmds.select ('sub_geo_Grp')
cmds.select (hi=True)
mySel = cmds.ls(sl=True)
cmds.delete(mySel, constructionHistory = True)

myPath = 'C:/woody/202210/rig/sub/'

def allMeshScale():
    myMeshShape = cmds.listRelatives('sub_geo_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_interiol_monitorA_a_a_a_b_metal_geo' or i == 'sub_hatch_cover_b_metal_geo':
            pass
        else:
            cmds.scaleConstraint ('Main', i)

def sub_body_Grp_const():
    myMeshShape = cmds.listRelatives('sub_body_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.parentConstraint ('Root_M', i, mo=True)

def sub_interiol_monitorA_Grp_const():
    cmds.parentConstraint ('Root_M', 'sub_interiol_monitorA_b_metal_geo', mo=True)

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
    cmds.parentConstraint ('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_a_a_b_rubber_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_a_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Centerjoystick5_M', 'sub_interiol_centerjoystick_a_a_b_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick3_M', 'sub_interiol_centerjoystick_a_a_b_b_plastic_geo', mo=True)

    cmds.parentConstraint ('Centerjoystick17_M', 'sub_interiol_centerjoystick_a_a_c_a_plastic_geo', mo=True)
    cmds.parentConstraint ('Centerjoystick17_M', 'sub_interiol_centerjoystick_a_a_c_b_rubber_geo', mo=True)

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

allMeshScale()
sub_body_Grp_const()
sub_interiol_monitorA_Grp_const()
sub_interiol_centerjoystick_Grp_const()
sub_L_interiol_sidecontrolerA_Grp_const()
sub_R_interiol_sidecontrolerB_Grp_const()
sub_interiol_paddal_Grp_const()
sub_hatch_Grp_const()
