import maya.cmds as cmds
import maya.mel as mel

myGrp = 'subOldHand_geo_Grp'
myPath = 'C:/woody/202210/rig/subOldHand/skin/'

# delete constraint
cmds.delete( cmds.listRelatives(myGrp, c=True, ad=True, type='constraint') )

# delete skin
cmds.delete( cmds.listRelatives(myGrp, c=True, ad=True, type='geometryShape'), constructionHistory=True )

# sampler
def skinSampler():
    cmds.skinCluster('Sampler_L', 'subOldHand_samplerB_metal_geo',tsb=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Sampler1_L', i,tsb=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_a_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Sampler2_L', i,tsb=True)

    myMeshShape = cmds.listRelatives('subOldHand_samplerA_a_b_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        if i == 'subOldHand_samplerA_a_b_a_a_a_a_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_a_b_a_a_b_glassD_geo':
            cmds.skinCluster('CapA_L', i,tsb=True)
        elif i == 'subOldHand_samplerA_a_b_a_a_a_c_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_a_b_a_b_b_glassD_geo':
            cmds.skinCluster('CapB_L', i,tsb=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_a_a_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_b_b_a_b_glassD_geo':
            cmds.skinCluster('CapC_L', i,tsb=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_a_c_glassD_geo' or i == 'subOldHand_samplerA_a_b_a_b_b_a_b_b_glassD_geo':
            cmds.skinCluster('CapD_L', i,tsb=True)
        elif i == 'subOldHand_samplerA_a_b_a_a_b_b_metal_geo':
            cmds.skinCluster('ValveA_L', i,tsb=True)
        elif i == 'subOldHand_samplerA_a_b_a_b_b_b_metal_geo':
            cmds.skinCluster('ValveB_L', i,tsb=True)
        else:
            cmds.skinCluster('Sampler3_L', i,tsb=True)

# oldHandA
def skinOldHandA():
    cmds.skinCluster('pistonA_R', 'subOldHand_oldarmA_b_a_metal_geo',tsb=True)
    cmds.skinCluster('Body1_R', 'subOldHand_oldarmA_b_b_metal_geo',tsb=True)

    # cmds.skinCluster('Attach1_M','HoseA_R','HoseA1_R','HoseB_R','HoseC_R','HoseC1_R', 'subOldHand_oldarmA_c_rubber_geo',tsb=True)
    # mel.eval('deformerWeights -import -method "index" -deformer "skinCluster32" -path "C:/Users/ygjeong/Desktop/ygjeong/202210/rig/subOldHand/" "hose_skin.xml"; skinCluster -e -forceNormalizeWeights "skinCluster32";')
    mySkin = cmds.skinCluster('Attach1_M','Hose1_R','Hose2_R','Hose3_R','Hose4_R','Hose5_R','Hose6_R','Hose7_R','Hose8_R','Hose9_R','Hose10_R','Hose11_R','Hose12_R','Hose13_R','Hose14_R','Hose15_R','Hose16_R','Hose17_R','Hose18_R','Hose19_R','Hose20_R', 'subOldHand_oldarmA_c_rubber_geo', tsb=True)
    # cmds.deformerWeights('hose.xml', im=True, deformer=mySkin, path=myPath)

    cmds.skinCluster('Body_M', 'subOldHand_oldarmA_a_b_metal_geo',tsb=True)
    cmds.skinCluster('Body_M', 'subOldHand_oldarmA_a_c_metal_geo',tsb=True)

    myMeshShape = cmds.listRelatives('subOldHand_oldarmA_a_a_a_Grp', c=True, ad=True, type='geometryShape')
    myMesh = cmds.listRelatives(myMeshShape, p=True)
    for i in myMesh:
        cmds.skinCluster('Attach1_M', i,tsb=True)

    cmds.skinCluster('BodyTop_M', 'subOldHand_oldarmA_a_a_b_metal_geo',tsb=True)
    cmds.skinCluster('BodyTop_M', 'subOldHand_oldarmA_a_a_c_metal_geo',tsb=True)
    cmds.skinCluster('Root_M', 'subOldHand_oldarmA_a_a_d_metal_geo',tsb=True)

# oldHandB
def skinOldHandB():
    # subOldHand_oldarmB_a_Grp
    cmds.skinCluster('pistonC_R', 'subOldHand_oldarmB_a_a_metal_geo',tsb=True)

    myMesh = 'subOldHand_oldarmB_a_b_metal_geo'
    mySkin = cmds.skinCluster('pistonB_R', 'pistonA_R', myMesh,tsb=True)
    cmds.skinPercent( mySkin[0], myMesh, transformValue=[('pistonB_R', 1.0), ('pistonA_R', 0.0)])
    cmds.skinPercent( mySkin[0], myMesh+'.vtx[399:406]', transformValue=[('pistonB_R', 0.0), ('pistonA_R', 1.0)])

    myMesh = 'subOldHand_oldarmB_a_c_metal_geo'
    mySkin = cmds.skinCluster('Arm_R', 'ArmPart1_R', 'ArmPart2_R', 'ArmPart3_R', 'add_Arm1_R', myMesh,tsb=True)
    myList = ['.vtx[273]','.vtx[276]','.vtx[279]','.vtx[297]','.vtx[300]','.vtx[303]','.vtx[319:325]','.vtx[343:348]','.vtx[400:402]','.vtx[412:429]','.vtx[481:483]','.vtx[493:504]','.vtx[510]','.vtx[513]','.vtx[516]','.vtx[534]','.vtx[537]','.vtx[540]','.vtx[556:562]','.vtx[580:585]','.vtx[637:639]','.vtx[649:666]','.vtx[718:720]','.vtx[730:741]','.vtx[876:1069]','.vtx[1688:1699]','.vtx[1757:1759]','.vtx[1763:1765]','.vtx[1778:1789]','.vtx[1898:1909]','.vtx[1970:1975]','.vtx[1988:1999]','.vtx[2464:2657]','.vtx[2744:2755]','.vtx[2813:2815]','.vtx[2819:2821]','.vtx[2834:2845]','.vtx[2954:2965]','.vtx[3026:3031]','.vtx[3044:3055]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('add_Arm1_R', 1.0)])

    # subOldHand_oldarmB_b_Grp
    myMesh = 'subOldHand_oldarmB_b_a_a_metal_geo'
    mySkin = cmds.skinCluster('pistonD_R', 'pistonC_R', myMesh,tsb=True)
    cmds.skinPercent( mySkin[0], myMesh, transformValue=[('pistonD_R', 1.0), ('pistonC_R', 0.0)])
    cmds.skinPercent( mySkin[0], myMesh+'.vtx[1:8]', transformValue=[('pistonD_R', 0.0), ('pistonC_R', 1.0)])

    myMesh = 'subOldHand_oldarmB_b_a_b_metal_geo'
    mySkin = cmds.skinCluster('Arm1_R', 'Arm1Part1_R', 'Arm1Part2_R', 'Arm1Part3_R', 'add_Arm2_R', myMesh,tsb=True)
    myList = ['.vtx[0:193]','.vtx[330:365]','.vtx[793:828]','.vtx[1122]','.vtx[1125]','.vtx[1128]','.vtx[1147]','.vtx[1160:1167]','.vtx[1210:1212]','.vtx[1222:1233]','.vtx[1252:1266]','.vtx[1285:1290]','.vtx[1330:1347]','.vtx[1502:1537]','.vtx[1965:2000]','.vtx[2565:2758]','.vtx[3626]','.vtx[3629]','.vtx[3632]','.vtx[3651]','.vtx[3664:3671]','.vtx[3714:3716]','.vtx[3726:3737]','.vtx[3756:3770]','.vtx[3789:3794]','.vtx[3834:3851]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('add_Arm2_R', 1.0)])

    cmds.skinCluster('pistonE_R', 'subOldHand_oldarmB_b_b_a_a_metal_geo',tsb=True)

    # cmds.skinCluster('pistonF_R', 'subOldHand_oldarmB_b_b_a_b_metal_geo',tsb=True)
    myMesh = 'subOldHand_oldarmB_b_b_a_b_metal_geo'
    mySkin = cmds.skinCluster('pistonF_R', 'pistonE_R', myMesh,tsb=True)
    cmds.skinPercent( mySkin[0], myMesh, transformValue=[('pistonF_R', 1.0), ('pistonE_R', 0.0)])
    cmds.skinPercent( mySkin[0], myMesh+'.vtx[1:8]', transformValue=[('pistonF_R', 0.0), ('pistonE_R', 1.0)])

    cmds.skinCluster('pistonRotate_R', 'subOldHand_oldarmB_b_b_b_metal_geo',tsb=True)
    cmds.skinCluster('pistonG_R', 'subOldHand_oldarmB_b_b_c_metal_geo',tsb=True)

# oldHandC
def skinOldHandC():
    # subOldHand_oldarmC_a_Grp
    myMesh = 'subOldHand_oldarmC_a_a_metal_geo'
    mySkin = cmds.skinCluster('Arm2_R','HandPart1_R', 'HandPart2_R', 'HandPart3_R','add_Hand1_R', myMesh,tsb=True)
    myList = ['.vtx[442:883]','.vtx[3536:3977]','.vtx[6680:6697]','.vtx[6701:6718]','.vtx[6725:6739]','.vtx[6807:6812]','.vtx[6942:6949]','.vtx[6953:6955]','.vtx[6969:6978]','.vtx[6982:6989]','.vtx[6993:7002]','.vtx[7006:7017]','.vtx[7094:7099]','.vtx[7108:7112]','.vtx[7121]','.vtx[7133]','.vtx[7135:7138]','.vtx[7147]','.vtx[7688:7705]','.vtx[7709:7726]','.vtx[7733:7747]','.vtx[7815:7820]','.vtx[7950:7957]','.vtx[7961:7963]','.vtx[7977:7986]','.vtx[7990:7997]','.vtx[8001:8010]','.vtx[8014:8025]','.vtx[8102:8107]','.vtx[8116:8120]','.vtx[8129]','.vtx[8141]','.vtx[8143:8146]','.vtx[8155]','.vtx[8221:8228]','.vtx[8506:8511]','.vtx[8520:8536]','.vtx[8545:8579]','.vtx[8674]','.vtx[8676:8678]','.vtx[8736:8788]','.vtx[8897:8901]','.vtx[9154:9170]','.vtx[9179:9207]','.vtx[9278]','.vtx[9280:9282]','.vtx[9330:9368]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('add_Hand1_R', 1.0)])
    myList = ['.vtx[884:1325]','.vtx[5746:6187]','.vtx[6220:6237]','.vtx[6241:6258]','.vtx[6265:6279]','.vtx[6302:6307]','.vtx[6326:6333]','.vtx[6337:6339]','.vtx[6353:6362]','.vtx[6366:6373]','.vtx[6377:6386]','.vtx[6390:6401]','.vtx[6425:6430]','.vtx[6434:6438]','.vtx[6442]','.vtx[6445]','.vtx[6447:6450]','.vtx[6454]','.vtx[7228:7245]','.vtx[7249:7266]','.vtx[7273:7287]','.vtx[7310:7315]','.vtx[7334:7341]','.vtx[7345:7347]','.vtx[7361:7370]','.vtx[7374:7381]','.vtx[7385:7394]','.vtx[7398:7409]','.vtx[7433:7438]','.vtx[7442:7446]','.vtx[7450]','.vtx[7453]','.vtx[7455:7458]','.vtx[7462]','.vtx[8229:8234]','.vtx[8347:8354]','.vtx[8358:8360]','.vtx[8367:8411]','.vtx[8661:8664]','.vtx[8725:8735]','.vtx[9005:9012]','.vtx[9016:9018]','.vtx[9025:9063]','.vtx[9265:9268]','.vtx[9321:9329]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('HandPart1_R', 1.0)])

    myMesh = 'subOldHand_oldarmC_a_b_metal_geo'
    mySkin = cmds.skinCluster('pistonH_R', 'pistonG_R', myMesh,tsb=True)
    cmds.skinPercent( mySkin[0], myMesh, transformValue=[('pistonH_R', 1.0), ('pistonG_R', 0.0)])
    cmds.skinPercent( mySkin[0], myMesh+'.vtx[1:8]', transformValue=[('pistonG_R', 1.0)])

    # subOldHand_oldarmC_b_Grp
    cmds.skinCluster('Hand1_R', 'subOldHand_oldarmC_b_b_metal_geo',tsb=True)

    cmds.skinCluster('FingerUpA1_R', 'subOldHand_oldarmC_b_a_a_a_metal_geo',tsb=True)

    myMesh = 'subOldHand_oldarmC_b_a_a_b_metal_geo'
    mySkin = cmds.skinCluster('FingerUpA_R','add_FingerUpA1_R', myMesh,tsb=True)
    myList = ['.vtx[0:136]','.vtx[138:144]','.vtx[160:161]','.vtx[172:192]','.vtx[244:396]','.vtx[398:399]','.vtx[406:426]','.vtx[478:493]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('add_FingerUpA1_R', 1.0)])

    cmds.skinCluster('FingerUpB_R', 'FingerUpA4_R', 'subOldHand_oldarmC_b_a_a_c_metal_geo',tsb=True)
    # cmds.skinCluster('FingerUpB_R', 'subOldHand_oldarmC_b_a_a_c_metal_geo',tsb=True)

    cmds.skinCluster('FingerDownA1_R', 'subOldHand_oldarmC_b_a_b_a_metal_geo',tsb=True)

    myMesh = 'subOldHand_oldarmC_b_a_b_b_metal_geo'
    mySkin = cmds.skinCluster('FingerDownA_R','add_FingerDownA1_R', myMesh,tsb=True)
    myList = ['.vtx[0:136]','.vtx[138:144]','.vtx[160:161]','.vtx[172:192]','.vtx[244:396]','.vtx[398:399]','.vtx[406:426]','.vtx[478:493]']
    for i in myList:
        cmds.skinPercent( mySkin[0], myMesh+i, transformValue=[('add_FingerDownA1_R', 1.0)])

    cmds.skinCluster('FingerDownB_R', 'FingerDownA4_R', 'subOldHand_oldarmC_b_a_b_c_metal_geo',tsb=True)
    # cmds.skinCluster('FingerDownB_R', 'subOldHand_oldarmC_b_a_b_c_metal_geo',tsb=True)

# make skin add joint
def skinAddJnt():
    myJntList = ['Arm1_R','Arm2_R','Hand1_R','FingerUpA1_R','FingerDownA1_R']
    for myJnt in myJntList:
        cmds.select(cl=True)
        myBaseJnt = cmds.joint()
        mySkinJnt = 'add_'+myJnt

        if bool( cmds.ls(mySkinJnt) ):
            cmds.delete( myBaseJnt )
        else:
            cmds.rename(myBaseJnt, mySkinJnt)
            cmds.matchTransform(mySkinJnt, myJnt)

            cmds.pointConstraint(myJnt, mySkinJnt)
            cmds.scaleConstraint(myJnt, mySkinJnt)

            myParent = cmds.listRelatives(myJnt, p=True)
            cmds.parent(mySkinJnt, myParent)

skinAddJnt()
skinSampler()
skinOldHandA()
skinOldHandB()
skinOldHandC()
