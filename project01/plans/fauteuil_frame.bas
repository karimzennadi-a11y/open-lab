Attribute VB_Name = "fauteuil_frame"
' ============================================================
' Fauteuil de transfert médical — Squelette 3D SolidWorks
' Macro VBA — à exécuter via Outils > Macro > Exécuter
' Open Lab — ENP Alger — v0.1
' ============================================================

Sub main()

    Dim swApp   As SldWorks.SldWorks
    Dim swDoc   As SldWorks.ModelDoc2
    Dim swSkMgr As SldWorks.SketchManager
    Dim bStatus As Boolean

    Set swApp = Application.SldWorks
    Set swDoc = swApp.ActiveDoc

    If swDoc Is Nothing Then
        MsgBox "Aucun document ouvert. Créez un nouveau Part d'abord.", vbExclamation
        Exit Sub
    End If

    ' ── Dimensions (en mètres — unité interne SolidWorks) ──
    Const W_EXT       As Double = 0.62
    Const HS          As Double = 0.5
    Const HH          As Double = 0.95
    Const LS          As Double = 0.42
    Const H_AXLE_REAR As Double = 0.1
    Const H_AXLE_FRT  As Double = 0.075
    Const H_FOOTREST  As Double = 0.08
    Const H_ARMREST   As Double = 0.73
    Const Y_HANDLE    As Double = -0.05
    Const Y_FOOTREST  As Double = 0.52
    Const Y_ARM_FRONT As Double = 0.37
    Const Y_ARM_REAR  As Double = 0.02

    Dim XL As Double: XL = -(W_EXT / 2)   ' -0.310 m
    Dim XR As Double: XR =  (W_EXT / 2)   ' +0.310 m
    Dim YR As Double: YR = 0.0             ' arrière
    Dim YF As Double: YF = LS              ' avant

    ' ── Ouverture sketch 3D ──
    bStatus = swDoc.Insert3DSketch2(False)
    Set swSkMgr = swDoc.SketchManager

    ' ── Cadre GAUCHE ──
    Call L(swSkMgr, XL, YR, 0,           XL, YR, HS)          ' pied arrière
    Call L(swSkMgr, XL, YR, HS,          XL, YF, HS)          ' rail siège
    Call L(swSkMgr, XL, YF, HS,          XL, YF, 0)           ' pied avant
    Call L(swSkMgr, XL, YR, HS,          XL, Y_HANDLE, HH)    ' dossier + poignée
    Call L(swSkMgr, XL, Y_ARM_REAR, H_ARMREST, XL, Y_ARM_FRONT, H_ARMREST) ' accoudoir
    Call L(swSkMgr, XL, Y_ARM_FRONT, HS, XL, Y_ARM_FRONT, H_ARMREST)       ' support acc av
    Call L(swSkMgr, XL, Y_ARM_REAR,  HS, XL, Y_ARM_REAR,  H_ARMREST)       ' support acc ar
    Call L(swSkMgr, XL, YF, H_AXLE_FRT, XL, Y_FOOTREST, H_FOOTREST)        ' support rf

    ' ── Cadre DROIT ──
    Call L(swSkMgr, XR, YR, 0,           XR, YR, HS)
    Call L(swSkMgr, XR, YR, HS,          XR, YF, HS)
    Call L(swSkMgr, XR, YF, HS,          XR, YF, 0)
    Call L(swSkMgr, XR, YR, HS,          XR, Y_HANDLE, HH)
    Call L(swSkMgr, XR, Y_ARM_REAR, H_ARMREST, XR, Y_ARM_FRONT, H_ARMREST)
    Call L(swSkMgr, XR, Y_ARM_FRONT, HS, XR, Y_ARM_FRONT, H_ARMREST)
    Call L(swSkMgr, XR, Y_ARM_REAR,  HS, XR, Y_ARM_REAR,  H_ARMREST)
    Call L(swSkMgr, XR, YF, H_AXLE_FRT, XR, Y_FOOTREST, H_FOOTREST)

    ' ── Traverses ──
    Call L(swSkMgr, XL, YR, H_AXLE_REAR,  XR, YR, H_AXLE_REAR)   ' T1 basse arr
    Call L(swSkMgr, XL, YF, H_AXLE_FRT,   XR, YF, H_AXLE_FRT)    ' T2 basse av
    Call L(swSkMgr, XL, YR, HS,           XR, YR, HS)              ' T3 siège arr
    Call L(swSkMgr, XL, YF, HS,           XR, YF, HS)              ' T4 siège av
    Call L(swSkMgr, XL, Y_HANDLE, HH,     XR, Y_HANDLE, HH)        ' T5 poignée
    Call L(swSkMgr, XL, Y_FOOTREST, H_FOOTREST, XR, Y_FOOTREST, H_FOOTREST) ' T6 rf
    Call L(swSkMgr, XL, Y_ARM_FRONT, H_ARMREST, XR, Y_ARM_FRONT, H_ARMREST) ' T7 acc

    ' ── Fermeture sketch ──
    swDoc.InsertSketch

    ' ── Reconstruction ──
    swDoc.EditRebuild3

    MsgBox "Squelette 3D créé avec succès !" & vbCrLf & _
           "Appliquer : Pièces soudées > Élément structurel" & vbCrLf & _
           "Standard: ISO | Type: Square Tube | 30x30x2", vbInformation, "Open Lab"

End Sub

' Raccourci pour CreateLine
Private Sub L(sk As SldWorks.SketchManager, _
              x1 As Double, y1 As Double, z1 As Double, _
              x2 As Double, y2 As Double, z2 As Double)
    Dim skLine As Object
    Set skLine = sk.CreateLine(x1, y1, z1, x2, y2, z2)
End Sub
