import maya.cmds as cmds
import maya.mel as mel
import importlib

def openUI():
    if cmds.window('myWin', ex=True):
        cmds.deleteUI('myWin')

    win = cmds.window('myWin', title="sub", iconName='Short Name', width=200 )
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='subScale', c=subScale_exec )
    cmds.separator()
    cmds.button( label='sub_skin', c=sub_skin_exec )
    cmds.button( label='sub_con', c=sub_con_exec )
    cmds.button( label='sub_constraint', c=sub_constraint_exec )
    cmds.button( label='sub_rig', c=sub_rig_exec )
    cmds.separator()
    cmds.button( label='subOldHand_skin', c=subOldHand_skin_exec )
    cmds.button( label='subOldHand_rig', c=subOldHand_rig_exec )
    cmds.separator()
    cmds.button( label='subNewHand_skin', c=subNewHand_skin_exec )
    cmds.button( label='subNewHand_rig', c=subNewHand_rig_exec )
    cmds.setParent( '..' )
    cmds.showWindow( win )

def subScale_exec(*args):
    mel.eval('source "C:/Users/ygjeong/Documents/maya/scripts/sub/subScale.mel";')

def sub_skin_exec(*args):
    cmds.select ('sub_geo_Grp')
    cmds.select (hi=True)
    mySel = cmds.ls(sl=True)
    cmds.delete(mySel, constructionHistory = True)

    import sub.sub_skin
    importlib.reload(sub.sub_skin)

def sub_con_exec(*args):
    mel.eval('source "C:/Users/ygjeong/Documents/maya/scripts/sub/sub_control.mel";')

def sub_constraint_exec(*args):
    import sub.sub_constraint
    importlib.reload(sub.sub_constraint)

def sub_rig_exec(*args):
    import sub.sub_rig
    importlib.reload(sub.sub_rig)

def subOldHand_skin_exec(*args):
    import sub.subOldHand_skin
    importlib.reload(sub.subOldHand_skin)

def subOldHand_rig_exec(*args):
    import sub.subOldHand_rig
    importlib.reload(sub.subOldHand_rig)

def subNewHand_skin_exec(*args):
    import sub.subNewHand_skin
    importlib.reload(sub.subNewHand_skin)

def subNewHand_rig_exec(*args):
    import sub.subNewHand_rig
    importlib.reload(sub.subNewHand_rig)
