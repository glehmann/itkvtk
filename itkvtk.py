#!/usr/bin/env python
#coding: iso-8859-15
#
# refactor InsightToolkit module to be more structured
#
# Copyright (C) 2005  Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

import InsightToolkit, vtk, itkvtkPython

def initDict() :
	"""
	select attributes of InsightToolkit an split it in groups :
	+ typeDict : a dict. Key is class name without itk prefix. Values are dict with type as name and array of function name as value.
	"""
	import re
	classes = []	# stores classes with types. Types will be isolated later.
	
	# compile regexp which will be used to find itk classes with types.
	typeRegexp = re.compile(r'^itk([a-zA-Z0-9]+?[a-z])([A-Z]*[0-9][A-Z0-9]*)(_.*$|Ptr)')
	for f in dir(itkvtkPython) :
		if f.startswith('itk') :
			typeRes = typeRegexp.findall(f)
			if typeRes != [] :
				# type found
				classes.append(typeRes[0])
				
	# now, generate dict which contains classes with types
	typeDict = {}
	for c, t, func in classes :
		if not typeDict.has_key(c) :
			typeDict[c] = {}
		if not typeDict[c].has_key(t) :
			typeDict[c][t] = []
		typeDict[c][t].append(func)
	
	return typeDict

class ItkClassType :
	"""
	this class gives functions avaible for a given type of a given class
	"""
	def __init__(self, name, t, funcs) :
		self.__name__ = name
		self.__type__ = t
		self.__function__ = getattr(itkvtkPython, 'itk%s%s' % (name, t))		
		for func in funcs :
			# attribute name must not have _ prefix
			if func[0] == '_' :
				attrib = func[1:]
			else :
				attrib = func
				
			# get the function to add as attribute
			function = getattr(itkvtkPython, 'itk%s%s%s' % (name, t, func))
			
			if attrib == 'New' :
				# to make prototyping easier, allow to pass parameter(s) to New function
				# I can't understand why, but it don't work in pure functional style: I can't 
				# use function() in New defined below :-(
				self.__new__ = function
				def New(inputSrc=None) :
					# create a new New function to manage parameters
					ret = self.__new__()
					if inputSrc :
						ret.SetInput(inputSrc.GetOutput())
						
					return ret
				
				# finally, set our own New function as self.New
				setattr(self, attrib, New)
			    
			else :
			    # add method
			    setattr(self, attrib, function)
	
	def __call__(self, *args) :
		if hasattr(self, 'New') :
			return self.New(*args)
		return self.__function__(*args)
	
	def __repr__(self) :
		return '<itk.%s[%s]>' % (self.__name__, self.__type__)

		
class ItkClass :
	"""
	This class manage access to avaible types
	"""
	def __init__(self, name, types) :
		self.__name__ = name
		for t, funcs in types.iteritems() :
			attrib = self.__manageDigit__(t)
			setattr(self, attrib, ItkClassType(name, t, funcs))
			
	def __getitem__(self, key) :
		return getattr(self, self.__manageDigit__(self.__seq2str__(key)))

	# we don't use staticmethod to be able to mask the method
	def __seq2str__(self, seq) :
		if not isinstance(seq, str) and hasattr(seq, '__getitem__') :
			return "".join([self.__seq2str__(e) for e in seq])
		else :
			return str(seq) 
	
	def __manageDigit__(self, key) :
	    # to allow usage of numbers
	    key = str(key)
	    # number attributes must be avaible without _ prefix
	    if key.isdigit() :
		key = '_%s' % key
	    return key

	def __repr__(self) :
		return '<itk.%s>' % self.__name__

			
typeDict = initDict()

for name, types in typeDict.iteritems() :
	exec '%s = ItkClass(name, types)' % name


# remove vars used to create module attribute
del typeDict, name, types, initDict
# the same for classes and modules
del ItkClass, ItkClassType, InsightToolkit, vtk, itkvtkPython
