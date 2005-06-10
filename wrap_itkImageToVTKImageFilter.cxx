/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkImageToVTKImageFilter.cxx,v $
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
#include "itkImageToVTKImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

//=================================
//THIS FILE GENERATED WITH MakeConsistentWrappedClasses.sh
//=================================
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkImageToVTKImageFilter);
  namespace wrappers
  {
    //===========2D Wrapped Filters==============
    ITK_WRAP_OBJECT1(ImageToVTKImageFilter, image::F2 , itkImageToVTKImageFilterF2  );
    ITK_WRAP_OBJECT1(ImageToVTKImageFilter, image::US2, itkImageToVTKImageFilterUS2);

    //===========3D Wrapped Filters==============
    ITK_WRAP_OBJECT1(ImageToVTKImageFilter, image::F3 , itkImageToVTKImageFilterF3  );
    ITK_WRAP_OBJECT1(ImageToVTKImageFilter, image::US3, itkImageToVTKImageFilterUS3);
  }
}
#endif
