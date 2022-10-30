import maya.cmds as cmds
import maya.mel as mel
# skin
# body
myMeshShape = cmds.listRelatives('sub_body_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i,tsb=True)

# pan
myList = ['A','B','C']
mySide = ['L','R']
for list in myList:
    for side in mySide:
        myMeshShape = cmds.listRelatives('sub_'+side+'_fan'+list+'_Grp', c=True, ad=True, type='geometryShape')
        myMesh = cmds.listRelatives(myMeshShape, p=True)
        for i in myMesh:
            if i == 'sub_'+side+'_fan'+list+'_a_metal_geo':
                cmds.skinCluster('Fan'+list+'_'+side, i,tsb=True)
            elif i == 'sub_'+side+'_fan'+list+'_b_metal_geo':
                cmds.skinCluster('Fan'+list+'1_'+side, i,tsb=True)
            elif i == 'sub_'+side+'_fan'+list+'_c_rubber_geo':
                cmds.skinCluster('Body_M', i,tsb=True)
            elif i == 'sub_'+side+'_fanA_d_metal_geo' or i == 'sub_'+side+'_fanC_d_metal_geo':
                mySkin = cmds.skinCluster('Body_M','Fan'+list+'_'+side, i,tsb=True)
                cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 0.0), ('Fan'+list+'_'+side, 1.0)])
                cmds.skinPercent( mySkin[0], i+'.vtx[0:3871]', transformValue=[('Body_M', 1.0), ('Fan'+list+'_'+side, 0.0)])
            elif i == 'sub_'+side+'_fanB_d_metal_geo':
                mySkin = cmds.skinCluster('Body_M','Fan'+list+'_'+side, i,tsb=True)
                cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 0.0), ('Fan'+list+'_'+side, 1.0)])
                cmds.skinPercent( mySkin[0], i+'.vtx[736:4607]', transformValue=[('Body_M', 1.0), ('Fan'+list+'_'+side, 0.0)])
            elif i == 'sub_'+side+'_fanA_e_metal_geo':
                mySkin = cmds.skinCluster('Body_M','Fan'+list+'_'+side, i,tsb=True)
                cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 0.0), ('Fan'+list+'_'+side, 1.0)])
                myList2 = ['.vtx[2087:2088]','.vtx[2095:2100]','.vtx[2107]','.vtx[2114:2119]','.vtx[2122:2123]','.vtx[2126:2127]','.vtx[2222:2223]','.vtx[2256:2315]','.vtx[2320:2323]','.vtx[2410]','.vtx[2437:2484]','.vtx[2489:2492]','.vtx[2507:2517]','.vtx[2529:2539]','.vtx[3077:3078]','.vtx[3111:3170]','.vtx[3175:3178]','.vtx[3265]','.vtx[3292:3339]','.vtx[3344:3347]','.vtx[3362:3372]','.vtx[3384:3502]','.vtx[4039:4040]','.vtx[4047:4052]','.vtx[4059]','.vtx[4066:4071]','.vtx[4074:4075]','.vtx[4078:4079]','.vtx[4174:4175]','.vtx[4208:4267]','.vtx[4272:4275]','.vtx[4362]','.vtx[4389:4436]','.vtx[4441:4444]','.vtx[4459:4469]','.vtx[4481:4491]','.vtx[5029:5030]','.vtx[5063:5122]','.vtx[5127:5130]','.vtx[5217]','.vtx[5244:5291]','.vtx[5296:5299]','.vtx[5314:5324]','.vtx[5336:5454]','.vtx[438:449]','.vtx[486:497]']
                for j in myList2:
                    cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 1.0), ('Fan'+list+'_'+side, 0.0)])
            elif i == 'sub_'+side+'_fanB_e_metal_geo':
                mySkin = cmds.skinCluster('Body_M','Fan'+list+'_'+side, i,tsb=True)
                cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 0.0), ('Fan'+list+'_'+side, 1.0)])
                myList2 = ['.vtx[464:465]','.vtx[472:477]','.vtx[484]','.vtx[491:496]','.vtx[499:500]','.vtx[503:504]','.vtx[599:600]','.vtx[633:692]','.vtx[697:700]','.vtx[787]','.vtx[814:861]','.vtx[866:869]','.vtx[884:894]','.vtx[906:916]','.vtx[1454:1455]','.vtx[1488:1547]','.vtx[1552:1555]','.vtx[1642]','.vtx[1669:1716]','.vtx[1721:1724]','.vtx[1739:1749]','.vtx[1761:1879]','.vtx[2416:2417]','.vtx[2424:2429]','.vtx[2436]','.vtx[2443:2448]','.vtx[2451:2452]','.vtx[2455:2456]','.vtx[2551:2552]','.vtx[2585:2644]','.vtx[2649:2652]','.vtx[2739]','.vtx[2766:2813]','.vtx[2818:2821]','.vtx[2836:2846]','.vtx[2858:2868]','.vtx[3406:3407]','.vtx[3440:3499]','.vtx[3504:3507]','.vtx[3594]','.vtx[3621:3668]','.vtx[3673:3676]','.vtx[3691:3701]','.vtx[3713:3831]','.vtx[5503:5514]','.vtx[5455:5466]']
                for j in myList2:
                    cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 1.0), ('Fan'+list+'_'+side, 0.0)])
            elif i == 'sub_'+side+'_fanC_e_metal_geo':
                mySkin = cmds.skinCluster('Body_M','Fan'+list+'_'+side, i,tsb=True)
                cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 0.0), ('Fan'+list+'_'+side, 1.0)])
                myList2 = ['.vtx[464:465]','.vtx[472:477]','.vtx[484]','.vtx[491:496]','.vtx[499:500]','.vtx[503:504]','.vtx[599:600]','.vtx[633:692]','.vtx[697:700]','.vtx[787]','.vtx[814:861]','.vtx[866:869]','.vtx[884:894]','.vtx[906:916]','.vtx[1454:1455]','.vtx[1488:1547]','.vtx[1552:1555]','.vtx[1642]','.vtx[1669:1716]','.vtx[1721:1724]','.vtx[1739:1749]','.vtx[1761:1879]','.vtx[2416:2417]','.vtx[2424:2429]','.vtx[2436]','.vtx[2443:2448]','.vtx[2451:2452]','.vtx[2455:2456]','.vtx[2551:2552]','.vtx[2585:2644]','.vtx[2649:2652]','.vtx[2739]','.vtx[2766:2813]','.vtx[2818:2821]','.vtx[2836:2846]','.vtx[2858:2868]','.vtx[3406:3407]','.vtx[3440:3499]','.vtx[3504:3507]','.vtx[3594]','.vtx[3621:3668]','.vtx[3673:3676]','.vtx[3691:3701]','.vtx[3713:3831]','.vtx[5503:5514]','.vtx[5431:5442]','.vtx[5455:5466]','.vtx[5479:5514]']
                for j in myList2:
                    cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 1.0), ('Fan'+list+'_'+side, 0.0)])

# Midlight
mySide = ['L','R']
for side in mySide:
    myMeshShape = cmds.listRelatives('sub_'+side+'_midlight_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'sub_'+side+'_midlight_b_metal_geo':
            cmds.skinCluster('Midlight_'+side, i,tsb=True)
        else:
            cmds.skinCluster('Midlight1_'+side, i,tsb=True)

# hatch
myMeshShape = cmds.listRelatives('sub_hatch_body_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)
cmds.skinCluster('Body_M', 'sub_hatch_bar_metal_geo' ,tsb=True)

# hatch cover
myList = ['a','b','c']
for list in myList:
    cmds.skinCluster('HatchCoverB_L', 'sub_hatch_cover_clip_'+list+'_a_metal_geo',tsb=True)
for list in myList:
    cmds.skinCluster('HatchCoverClip'+list.upper()+'_L', 'sub_hatch_cover_clip_'+list+'_b_metal_geo',tsb=True)
myList2 = ['.vtx[2770:3525]' ,'.vtx[3701:4114]' ,'.vtx[4855:4935]']
for list in myList:
    if list == 'b':
        mySkin = cmds.skinCluster('HatchCoverB_L', 'HatchCoverClipLook_L', 'sub_hatch_cover_b_metal_geo',tsb=True)
        cmds.skinPercent( mySkin[0], 'sub_hatch_cover_b_metal_geo', transformValue=[('HatchCoverB_L', 1.0), ('HatchCoverClipLook_L', 0.0)])
        for i in myList2:
            cmds.skinPercent( mySkin[0], 'sub_hatch_cover_b_metal_geo'+i, transformValue=[('HatchCoverB_L', 0.0), ('HatchCoverClipLook_L', 1.0)])
    else:
        cmds.skinCluster('HatchCover'+list.upper()+'_L', 'sub_hatch_cover_'+list+'_metal_geo',tsb=True)

# engine
myList = ['A','B','C']
for list in myList:
    myMeshShape = cmds.listRelatives('sub_engine'+list+'_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if list == 'C':
            cmds.skinCluster('EngineFA_R', 'EngineFB_R', 'EngineFC_R', 'EngineFA_L', 'EngineFB_L', 'EngineFC_L', i, tsb=True)
        else:
            cmds.skinCluster('Body_M', i, tsb=True)

myList = ['D','E','F','G','H','I']
for list in myList:
    myMeshShape = cmds.listRelatives('sub_engine'+list+'_metal_geo', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if list == 'F':
            cmds.skinCluster('Body_M', 'rubber_M', 'rubber1_M', 'rubber2_M', 'rubber3_M', 'rubber4_M', i, tsb=True)
        elif list == 'H':
            mySkin = cmds.skinCluster('Body_M', 'EngineH_R', 'EngineH1_R', 'EngineH_L', 'EngineH1_L', i, tsb=True)
            cmds.skinPercent( mySkin[0], i, transformValue=[('Body_M', 1.0), ('EngineH_R', 0.0), ('EngineH1_R', 0.0), ('EngineH_L', 0.0), ('EngineH1_L', 0.0)])
            myList2 = ['.vtx[12550:12953]','.vtx[14974:16993]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 0.0), ('EngineH_R', 0.0), ('EngineH1_R', 1.0), ('EngineH_L', 0.0), ('EngineH1_L', 0.0)])
            myList2 = ['.vtx[690:6072]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 0.0), ('EngineH_R', 1.0), ('EngineH1_R', 0.0), ('EngineH_L', 0.0), ('EngineH1_L', 0.0)])
            myList2 = ['.vtx[12146:12549]','.vtx[12954:14973]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 0.0), ('EngineH_R', 0.0), ('EngineH1_R', 0.0), ('EngineH_L', 0.0), ('EngineH1_L', 1.0)])
            myList2 = ['.vtx[6763:12145]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 0.0), ('EngineH_R', 0.0), ('EngineH1_R', 0.0), ('EngineH_L', 1.0), ('EngineH1_L', 0.0)])
            myList2 = ['.vtx[690]','.vtx[900]','.vtx[2067:2072]','.vtx[2086]','.vtx[2099]','.vtx[2106]','.vtx[2115]','.vtx[2605:2658]','.vtx[2713:2730]','.vtx[2771:2952]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 1.0), ('EngineH_R', 0.0), ('EngineH1_R', 0.0), ('EngineH_L', 0.0), ('EngineH1_L', 0.0)])
            myList2 = ['.vtx[6763]','.vtx[6973]','.vtx[8140:8145]','.vtx[8159]','.vtx[8172]','.vtx[8179]','.vtx[8188]','.vtx[8678:8731]','.vtx[8786:8803]','.vtx[8844:9025]']
            for j in myList2:
                cmds.skinPercent( mySkin[0], i+j, transformValue=[('Body_M', 1.0), ('EngineH_R', 0.0), ('EngineH1_R', 0.0), ('EngineH_L', 0.0), ('EngineH1_L', 0.0)])
        else:
            cmds.skinCluster('Body_M', i, tsb=True)

# mainglass
myMeshShape = cmds.listRelatives('sub_mainglass_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_interiol_body_Grp
myMeshShape = cmds.listRelatives('sub_interiol_body_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_C_interiol_chair_Grp
mySide = ['R','L']
for side in mySide:
    mySkin = cmds.skinCluster('Chair_'+side, 'Chair1_'+side, 'Chair2_'+side, 'sub_'+side+'_interiol_chair_fabric_geo', tsb=True)
    myList = ['.vtx[2038:3291]', '.vtx[5148:5831]']
    for i in myList:
        cmds.skinPercent( mySkin[0], 'sub_'+side+'_interiol_chair_fabric_geo'+i, transformValue=[('Chair_'+side, 1.0), ('Chair1_'+side, 0.0), ('Chair2_'+side, 0.0)])

    myList = ['.vtx[0:417]','.vtx[780:2037]','.vtx[3292:5147]']
    for i in myList:
        cmds.skinPercent( mySkin[0], 'sub_'+side+'_interiol_chair_fabric_geo'+i, transformValue=[('Chair_'+side, 0.0), ('Chair1_'+side, 1.0), ('Chair2_'+side, 0.0)])

    cmds.skinPercent( mySkin[0], 'sub_'+side+'_interiol_chair_fabric_geo.vtx[418:779]', transformValue=[('Chair_'+side, 0.0), ('Chair1_'+side, 0.0), ('Chair2_'+side, 1.0)])


# cmds.skinCluster('Chair_L', 'Chair1_L', 'Chair2_L', 'Chair3_L', 'sub_L_interiol_chair_fabric_geo', tsb=True)

# sub_interiol_monitorA_Grp
cmds.skinCluster('Body_M', 'sub_interiol_monitorA_b_metal_geo', tsb=True)
cmds.skinCluster('MonitorA1_M', 'sub_interiol_monitorA_a_b_a_metal_geo', tsb=True)
cmds.skinCluster('MonitorA_M', 'sub_interiol_monitorA_a_b_b_metal_geo', tsb=True)
cmds.skinCluster('MonitorA1_M', 'sub_interiol_monitorA_a_b_c_plastic_geo', tsb=True)

cmds.skinCluster('MonitorA3_M', 'sub_interiol_monitorA_a_a_b_b_metal_geo', tsb=True)
cmds.skinCluster('MonitorA2_M', 'sub_interiol_monitorA_a_a_b_c_metal_geo', tsb=True)
myMeshShape = cmds.listRelatives('sub_interiol_monitorA_a_a_b_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('MonitorA3_M', i, tsb=True)

cmds.skinCluster('MonitorA5_M', 'sub_interiol_monitorA_a_a_a_b_metal_geo', tsb=True)
cmds.skinCluster('MonitorA4_M', 'sub_interiol_monitorA_a_a_a_c_metal_geo', tsb=True)
myMeshShape = cmds.listRelatives('sub_interiol_monitorA_a_a_a_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('MonitorA5_M', i, tsb=True)

# sub_interiol_monitorC_Grp
cmds.skinCluster('Body_M', 'sub_interiol_monitorC_b_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_monitorC_a_b_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('MonitorC_R', i, tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_monitorC_a_a_b_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('MonitorC1_R', i, tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_monitorC_a_a_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('MonitorC2_R', i, tsb=True)

# sub_interiol_centerjoystick_Grp
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_d_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_e_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_f_metal_geo', tsb=True)

cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_a_a_a_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_a_a_b_rubber_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_a_b_plastic_geo', tsb=True)

# mid button
cmds.skinCluster('Centerjoystick5_M', 'sub_interiol_centerjoystick_a_a_b_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick3_M', 'sub_interiol_centerjoystick_a_a_b_b_plastic_geo', tsb=True)

# top button
cmds.skinCluster('Centerjoystick17_M', 'sub_interiol_centerjoystick_a_a_c_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'Centerjoystick17_M', 'sub_interiol_centerjoystick_a_a_c_b_rubber_geo', tsb=True)

cmds.skinCluster('Centerjoystick15_R', 'sub_interiol_centerjoystick_a_a_d_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_d_b_plastic_geo', tsb=True)

cmds.skinCluster('Centerjoystick13_L', 'sub_interiol_centerjoystick_a_a_e_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_e_b_metal_geo', tsb=True)

# sub_interiol_centerjoystick_a_a_f_Grp
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_a_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_a_glassS_geo', tsb=True)

cmds.skinCluster('Centerjoystick7_L', 'sub_interiol_centerjoystick_a_a_f_b_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_b_b_plastic_geo', tsb=True)

cmds.skinCluster('Centerjoystick11_R', 'sub_interiol_centerjoystick_a_a_f_c_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_c_b_plastic_geo', tsb=True)

cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_d_a_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick9_M', 'sub_interiol_centerjoystick_a_a_f_d_b_plastic_geo', tsb=True)

cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_e_metal_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_f_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_g_plastic_geo', tsb=True)
cmds.skinCluster('Centerjoystick1_M', 'sub_interiol_centerjoystick_a_a_f_h_plastic_geo', tsb=True)

# sub_interiol_centerjoystick_a_b_Grp
cmds.skinCluster('CenterjoystickButtonC_L', 'sub_interiol_centerjoystick_a_b_a_a_a_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_a_a_a_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonB_L', 'sub_interiol_centerjoystick_a_b_a_a_b_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_a_a_b_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonB_R', 'sub_interiol_centerjoystick_a_b_a_a_c_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_a_a_c_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonC_R', 'sub_interiol_centerjoystick_a_b_a_a_d_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_a_a_d_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonA_M', 'sub_interiol_centerjoystick_a_b_a_b_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_b_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_a_b_c_metal_geo', tsb=True)

# sub_interiol_centerjoystick_b_a_Grp
cmds.skinCluster('CenterjoystickButtonF_L', 'sub_interiol_centerjoystick_b_a_a_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_a_a_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonE_L', 'sub_interiol_centerjoystick_b_a_b_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_a_b_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonD_M', 'sub_interiol_centerjoystick_b_a_c_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_a_c_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonE_R', 'sub_interiol_centerjoystick_b_a_d_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_a_d_b_plastic_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonF_R', 'sub_interiol_centerjoystick_b_a_e_a_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_a_e_b_plastic_geo', tsb=True)

# sub_interiol_centerjoystick_b_b_Grp
cmds.skinCluster('CenterjoystickButtonJ_L', 'sub_interiol_centerjoystick_b_b_a_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_a_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonI_L', 'sub_interiol_centerjoystick_b_b_b_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_b_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonH_L', 'sub_interiol_centerjoystick_b_b_c_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_c_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonG_M', 'sub_interiol_centerjoystick_b_b_d_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_d_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonH_R', 'sub_interiol_centerjoystick_b_b_e_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_e_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonI_R', 'sub_interiol_centerjoystick_b_b_f_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_f_b_metal_geo', tsb=True)

cmds.skinCluster('CenterjoystickButtonJ_R', 'sub_interiol_centerjoystick_b_b_g_a_plastic_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_b_g_b_metal_geo', tsb=True)

# sub_interiol_centerjoystick_b_c_Grp
myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_b_c_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

cmds.skinCluster('Body_M', 'sub_interiol_centerjoystick_b_d_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_centerjoystick_c_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_interiol_paddal_Grp
myMeshShape = cmds.listRelatives('sub_interiol_paddal_a_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('PaddalA_L', i, tsb=True)

cmds.skinCluster('PaddalA1_L', 'sub_interiol_paddal_a_b_a_a_a_metal_geo', tsb=True)
cmds.skinCluster('PaddalPistonA1_L', 'sub_interiol_paddal_a_b_a_a_b_metal_geo', tsb=True)
cmds.skinCluster('PaddalPistonA1_L', 'sub_interiol_paddal_a_b_a_b_metal_geo', tsb=True)

cmds.skinCluster('PaddalA3_L', 'sub_interiol_paddal_a_b_b_a_a_metal_geo', tsb=True)
cmds.skinCluster('PaddalA3_L', 'sub_interiol_paddal_a_b_b_a_b_metal_geo', tsb=True)

cmds.skinCluster('PaddalPistonA3_L', 'sub_interiol_paddal_a_b_b_b_a_metal_geo', tsb=True)
cmds.skinCluster('PaddalPistonA3_L', 'sub_interiol_paddal_a_b_b_b_b_metal_geo', tsb=True)

cmds.skinCluster('PaddalPistonA_L', 'sub_interiol_paddal_a_c_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_paddal_b_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('PaddalB_L', i, tsb=True)

cmds.skinCluster('PaddalB1_L', 'sub_interiol_paddal_b_b_a_a_metal_geo', tsb=True)
cmds.skinCluster('PaddalB1_L', 'sub_interiol_paddal_b_b_a_b_metal_geo', tsb=True)

cmds.skinCluster('PaddalPistonB_L', 'sub_interiol_paddal_b_b_b_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_paddal_c_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Paddal_L', i, tsb=True)

# sub_interiol_sidedetail_Grp
myMeshShape = cmds.listRelatives('sub_interiol_sidedetail_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_L_interiol_sidecontrolerA_a_a_Grp
cmds.skinCluster('SidecontrolerAButtonR_L', 'sub_L_interiol_sidecontrolerA_a_a_a_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonS_L', 'sub_L_interiol_sidecontrolerA_a_a_b_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonT_L', 'sub_L_interiol_sidecontrolerA_a_a_c_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonQ_L', 'sub_L_interiol_sidecontrolerA_a_a_d_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonP_L', 'sub_L_interiol_sidecontrolerA_a_a_e_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonO_L', 'sub_L_interiol_sidecontrolerA_a_a_f_plastic_geo', tsb=True)

# sub_L_interiol_sidecontrolerA_a_b_Grp
cmds.skinCluster('SidecontrolerAButtonN_L', 'sub_L_interiol_sidecontrolerA_a_b_a_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonM_L', 'sub_L_interiol_sidecontrolerA_a_b_b_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonL_L', 'sub_L_interiol_sidecontrolerA_a_b_c_metal_geo', tsb=True)

# sub_L_interiol_sidecontrolerA_a_c_b_geo
cmds.skinCluster('Body_M', 'sub_L_interiol_sidecontrolerA_a_c_a_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonK_L', 'sub_L_interiol_sidecontrolerA_a_c_b_a_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonK_L', 'sub_L_interiol_sidecontrolerA_a_c_b_b_plastic_geo', tsb=True)

cmds.skinCluster('Body_M', 'sub_L_interiol_sidecontrolerA_a_c_c_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_L_interiol_sidecontrolerA_a_d_metal_geo', tsb=True)

# sub_L_interiol_sidecontrolerA_b_a_Grp
cmds.skinCluster('SidecontrolerAButtonJ_L', 'sub_L_interiol_sidecontrolerA_b_a_a_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonI_L', 'sub_L_interiol_sidecontrolerA_b_a_b_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonH_L', 'sub_L_interiol_sidecontrolerA_b_a_c_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonG_L', 'sub_L_interiol_sidecontrolerA_b_a_d_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonF_L', 'sub_L_interiol_sidecontrolerA_b_a_e_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonE_L', 'sub_L_interiol_sidecontrolerA_b_a_f_plastic_geo', tsb=True)

# sub_L_interiol_sidecontrolerA_b_b_Grp
cmds.skinCluster('SidecontrolerAButtonD_L', 'sub_L_interiol_sidecontrolerA_b_b_a_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonB_L', 'sub_L_interiol_sidecontrolerA_b_b_b_metal_geo', tsb=True)

# sub_L_interiol_sidecontrolerA_b_c_Grp
cmds.skinCluster('SidecontrolerAButtonC_L', 'sub_L_interiol_sidecontrolerA_b_c_a_glassD_geo', tsb=True)
cmds.skinCluster('SidecontrolerAButtonA_L', 'sub_L_interiol_sidecontrolerA_b_c_b_glassD_geo', tsb=True)

cmds.skinCluster('Body_M', 'sub_L_interiol_sidecontrolerA_b_d_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_L_interiol_sidecontrolerA_b_e_metal_geo', tsb=True)

# sub_R_interiol_sidecontrolerB_a_a_Grp
cmds.skinCluster('SidecontrolerBButtonS_R', 'sub_R_interiol_sidecontrolerB_a_a_a_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonR_R', 'sub_R_interiol_sidecontrolerB_a_a_b_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonQ_R', 'sub_R_interiol_sidecontrolerB_a_a_c_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonN_R', 'sub_R_interiol_sidecontrolerB_a_a_d_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonO_R', 'sub_R_interiol_sidecontrolerB_a_a_e_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonP_R', 'sub_R_interiol_sidecontrolerB_a_a_f_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonM_R', 'sub_R_interiol_sidecontrolerB_a_a_g_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonL_R', 'sub_R_interiol_sidecontrolerB_a_a_h_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonK_R', 'sub_R_interiol_sidecontrolerB_a_a_i_plastic_geo', tsb=True)

# sub_R_interiol_sidecontrolerB_a_b_Grp
cmds.skinCluster('SidecontrolerBButtonT_R', 'sub_R_interiol_sidecontroler_B_a_b_a_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonU_R', 'sub_R_interiol_sidecontroler_B_a_b_b_plastic_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_R_interiol_sidecontrolerB_a_c_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

cmds.skinCluster('Body_M', 'sub_R_interiol_sidecontrolerB_a_d_metal_geo', tsb=True)

# sub_R_interiol_sidecontrolerB_b_a_Grp
cmds.skinCluster('SidecontrolerBButtonD_R', 'sub_R_interiol_sidecontrolerB_b_a_a_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonF_R', 'sub_R_interiol_sidecontrolerB_b_a_b_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonE_R', 'sub_R_interiol_sidecontrolerB_b_a_c_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonA_R', 'sub_R_interiol_sidecontrolerB_b_a_d_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonC_R', 'sub_R_interiol_sidecontrolerB_b_a_e_plastic_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonB_R', 'sub_R_interiol_sidecontrolerB_b_a_f_plastic_geo', tsb=True)

# sub_R_interiol_sidecontrolerB_b_b_Grp
cmds.skinCluster('SidecontrolerBButtonJ_R', 'sub_R_interiol_sidecontrolerB_b_b_a_metal_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonH_R', 'sub_R_interiol_sidecontrolerB_b_b_b_metal_geo', tsb=True)

# sub_R_interiol_sidecontrolerB_b_c_Grp
cmds.skinCluster('SidecontrolerBButtonG_R', 'sub_R_interiol_sidecontrolerB_b_c_a_glassD_geo', tsb=True)
cmds.skinCluster('SidecontrolerBButtonI_R', 'sub_R_interiol_sidecontrolerB_b_c_b_glassD_geo', tsb=True)

cmds.skinCluster('Body_M', 'sub_R_interiol_sidecontrolerB_b_d_metal_geo', tsb=True)
cmds.skinCluster('Body_M', 'sub_R_interiol_sidecontrolerB_b_e_metal_geo', tsb=True)

# sub_interiol_backcontroler_Grp
myMeshShape = cmds.listRelatives('sub_interiol_backcontroler_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_interiol_topmonitor_Grp
myMeshShape = cmds.listRelatives('sub_L_interiol_topmonitor_a_a_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Topmonitor1_L', i, tsb=True)

cmds.skinCluster('Topmonitor_M', 'sub_L_interiol_topmonitor_a_a_b_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_R_interiol_topmonitor_a_b_a_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Topmonitor1_L', i, tsb=True)

cmds.skinCluster('Topmonitor_M', 'sub_R_interiol_topmonitor_a_b_b_metal_geo', tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_topmonitor_b_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

myMeshShape = cmds.listRelatives('sub_interiol_topmonitor_c_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)

# sub_interiol_screw_Grp
myMeshShape = cmds.listRelatives('sub_interiol_screw_Grp', c=True, ad=True, type='geometryShape')
myMesh = cmds.listRelatives(myMeshShape, p=True)
for i in myMesh:
    cmds.skinCluster('Body_M', i, tsb=True)
