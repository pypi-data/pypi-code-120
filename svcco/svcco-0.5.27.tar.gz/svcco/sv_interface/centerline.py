centerline ="""if not terminating:
    outlets = []
    for i,face in enumerate(mesher.get_model_face_ids()):
        if face == walls[0]:
            continue
        elif face == inlet:
            continue
        else:
            outlets.append(face)
    centerline = vmtk.centerlines(mesher.get_model_polydata(),[inlet],outlets,use_face_ids=True)
    centerline_model = modeling.PolyData()
    centerline_model.set_surface(centerline)
    centerline_model.write('{}'+os.sep+'centerlines','vtp')
"""
