/* This is an itk-specific typemap used by CableSwig.  Also see comments
 * and "throws" code in CableSwig.cxx.
 *   -- Charl P. Botha <cpbotha AT ieee.org>
 */

#ifdef SWIGPYTHON

/* ------------------------------------------------------------
 * PyObject *  - Just pass straight through unmodified
 * This is default behaviour for python.swg, but Cable passes
 * a PyObject * through as a "p._object", so we redo the typemap
 * ------------------------------------------------------------ */
  
%typemap(in)   p._object "$1 = $input;";
%typemap(out)  p._object "$result = $1;";

#endif

%include exception.i

/* A "throws" attribute with the "std::exception" type is added synthetically
 * to each method node by CableSwig.cxx.  When gcc_xml starts passing through
 * correct throws types, this typemap could be optionally extended to
 * account for more different types.  For now this is sufficient though.
 */
 
%typemap(throws) std::exception {
   SWIG_exception(SWIG_RuntimeError, const_cast<char*>(_e.what()));
}

%include std_string.i

/* disable this c linkage warning on windows */
%{
#ifdef _WIN32
#pragma warning ( disable : 4190 )
#pragma warning ( disable : 4049 )
#endif
%}

%{
#include "vtkImageImport.h"
#include "vtkImageExport.h"
#include "itkImageToImageFilter.h"
#include "itkVTKImageExport.h"
#include "itkVTKImageImport.h"
#include "vtkImageData.h"
%}

#ifdef SWIGTCL
%{
#include "vtkTclUtil.h"
%}

%typemap(in) vtkImageExport* {
  int cerror=0;
  $1 = NULL;
  $1 = (vtkImageExport*) vtkTclGetPointerFromObject(Tcl_GetString($input),
                                                    "vtkImageExport", interp,
                                                    cerror );
  if ( cerror ) { SWIG_fail; }
}

%typemap(in) vtkImageImport* {
  int cerror=0;
  $1 = NULL;
  $1 = (vtkImageImport*) vtkTclGetPointerFromObject(Tcl_GetString($input),
                                                    "vtkImageImport", interp,
                                                    cerror );
  if ( cerror ) { SWIG_fail; }
}

#endif

#ifdef SWIGPYTHON
%{
#include "vtkPythonUtil.h"
%}

%typemap(out) vtkImageExport* {
  $result = vtkPythonGetObjectFromPointer ( (vtkImageExport*)$1 );
}

%typemap(out) vtkImageImport* {
  $result = vtkPythonGetObjectFromPointer ( (vtkImageImport*)$1 );
}

%typemap(out) vtkImageData* {
  $result = vtkPythonGetObjectFromPointer ( (vtkImageData*)$1 );
}

%typemap(in) vtkImageData* {
  $1 = NULL;
  $1 = (vtkImageData*) vtkPythonGetPointerFromObject ( $input, "vtkImageData" );
  if ( $1 == NULL ) { SWIG_fail; }
}

#endif
