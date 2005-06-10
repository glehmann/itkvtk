# This file demonstrates how to connect VTK and ITK pipelines together
# in scripted languages with the new ConnectVTKITK wrapping functionality.
# Data is loaded in with VTK, processed with ITK and written back to disc
# with VTK. 
#
# For this to work, you have to build InsightApplications/ConnectVTKITK
# as well.
#
# It also demonstrates the use of the python-specific itkPyCommand object.
#
# -- Charl P. Botha <cpbotha AT ieee.org>

import itk, vtk, ivtk

itk.auto_progress = True

# VTK will read the PNG image for us
reader = vtk.vtkPNGReader()
reader.SetFileName("/usr/share/itk-data/Input/cthead1.png")

# it has to be a single component, itk::VTKImageImport doesn't support more
lum = vtk.vtkImageLuminance()
lum.SetInput(reader.GetOutput())

# let's cast the output to float
imageCast = vtk.vtkImageCast()
imageCast.SetOutputScalarTypeToFloat()
imageCast.SetInput(lum.GetOutput())

vtk2itk = ivtk.VTKImageToImageFilter.F2.New(imageCast)

canny  = itk.CannyEdgeDetectionImageFilter.F2F2.New(vtk2itk)
rescaler = itk.RescaleIntensityImageFilter.F2US2.New(canny, OutputMinimum=0, OutputMaximum=65535)

itk2vtk = ivtk.ImageToVTKImageFilter.US2.New(rescaler)

# finally write the image to disk using VTK
writer = vtk.vtkPNGWriter()
writer.SetFileName('./testout.png')
writer.SetInput(itk2vtk.GetOutput())

# before we call Write() on the writer, it is prudent to give
# our ITK pipeline an Update() call... this is not necessary
# for normal error-less operation, but ensures that exceptions
# thrown by ITK get through to us in the case of an error;
# This is because the VTK wrapping system does not support
# C++ exceptions.
rescaler.Update()

# write the file to disk...
writer.Write()

print "\n\nWrote testout.png to current directory."
