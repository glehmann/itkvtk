/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkVTKImageToImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/04/02 22:43:59 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkVTKImageToImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

//=================================
//THIS FILE GENERATED WITH MakeConsistentWrappedClasses.sh
//=================================
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkVTKImageToImageFilter);
  namespace wrappers
  {
    //===========2D Wrapped Filters==============
    ITK_WRAP_OBJECT1(VTKImageToImageFilter, image::F2 , itkVTKImageToImageFilterF2  );
    ITK_WRAP_OBJECT1(VTKImageToImageFilter, image::US2, itkVTKImageToImageFilterUS2);

    //===========3D Wrapped Filters==============
    ITK_WRAP_OBJECT1(VTKImageToImageFilter, image::F3 , itkVTKImageToImageFilterF3  );
    ITK_WRAP_OBJECT1(VTKImageToImageFilter, image::US3, itkVTKImageToImageFilterUS3);
  }
}
#endif
