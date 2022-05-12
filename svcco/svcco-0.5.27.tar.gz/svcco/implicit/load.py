import numpy as np
import vtk
from vtk.util import numpy_support
import pyvista as pv

def load3d(filename,subdivisions=0):
    vtk_reader = {'stl':vtk.vtkSTLReader,
                  'obj':vtk.vtkOBJReader,
                  'ply':vtk.vtkPLYReader,
                  'vtu':vtk.vtkXMLUnstructuredGridReader,
                  'vtp':vtk.vtkXMLPolyDataReader,
                  '3ds':vtk.vtk3DSImporter}

    ext = filename.rsplit('.')[1].lower()
    if ext not in vtk_reader.keys():
        print('Not a supported 3D file format')
        print('Supported Formats:\n{}'.format([supported_ext + '\n' for supported_ext in vtk_reader.keys() ]))
        return
    reader = vtk_reader[ext]()
    reader.SetFileName(filename)
    if ext == '3ds':
        reader.ComputeNormalsOn()
        reader.Update()
    elif ext == 'vtu':
        pass
    else:
        reader.Update()
        data = reader.GetOutput()
        points = data.GetPoints()
        points = points.GetData()
        points = numpy_support.vtk_to_numpy(points)
        data_normals = data.GetPointData()
        normals = data_normals.GetNormals()
        if subdivisions > 0:
            linearSubdivision = vtk.vtkLinearSubdivisionFilter()
            linearSubdivision.SetNumberOfSubdivisions(subdivisions)
            linearSubdivision.SetInputData(data)
            linearSubdivision.Update()
            data = linearSubdivision.GetOutput()
            points = data.GetPoints()
            points = points.GetData()
            points = numpy_support.vtk_to_numpy(points)
            normals_gen = vtk.vtkPolyDataNormals()
            normals_gen.SplittingOn()
            normals_gen.ComputeCellNormalsOff()
            normals_gen.ComputePointNormalsOn()
            normals_gen.SetInputData(data)
            normals_gen.Update()
            normal_polydata = normals_gen.GetOutput()
            normal_point_data = normal_polydata.GetPointData()
            normals = normal_point_data.GetNormals()
            normals = numpy_support.vtk_to_numpy(normals)
        else:
            #normals = numpy_support.vtk_to_numpy(normals)
            if normals is None:
                """
                normals_gen = vtk.vtkPolyDataNormals()
                normals_gen.SplittingOn()
                normals_gen.ComputeCellNormalsOff()
                normals_gen.ComputePointNormalsOn()
                normals_gen.SetInputData(data)
                normals_gen.Update()
                normal_polydata = normals_gen.GetOutput()
                normal_point_data = normal_polydata.GetPointData()
                normals = normal_point_data.GetNormals()
                normals = numpy_support.vtk_to_numpy(normals).tolist()
                points = []
                norms = []
                for idx in range(normal_polydata.GetNumberOfCells()):
                    tri = normal_polydata.GetCell(idx)
                    tri_points = numpy_support.vtk_to_numpy(tri.GetPoints().GetData()).tolist()
                    points.extend(tri_points)
                    for jdx in range(len(tri_points)):
                        norms.append(normals[idx])
                """
                obj = pv.PolyData(var_inp=data)
                obj = obj.compute_normals()
                #points = np.array(points)
                #normals = np.array(norms)
                points = obj.points
                normals = obj['Normals']
            else:
                normals = numpy_support.vtk_to_numpy(normals)
        upt,uid = np.unique(points,axis=0,return_index=True)
        points = points[uid]
        normals = normals[uid]
        #normals = numpy_support.vtk_to_numpy(normals)
        #Check and clean duplicate points
        #points,idx = np.unique(points,axis=0,return_index=True)
        #normals    = normals[idx]
        # later duplicate points will be allowed to accomodate C1
        # surfaces which will require splitting during VTK NORMAL
        # calculation. This will also have to make the splitting
        # and PU angle thresholds the same to allow for non-singluar
        # matricies.
        return points,normals,data
