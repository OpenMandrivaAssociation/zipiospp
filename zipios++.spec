#
# iThis file is based on openSUSE spec file for package 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define libname %mklibname zipios 0
%define develname %mklibname zipios -d

Name:           zipios++
Version:	0.1.5.9+cvs.2007.04.28
Release:	1
License:	GPLv2
Summary:	A java.util.zip-like C++ library for reading and writing Zip files
Url:		http://zipios.sourceforge.net/
Group:		Development/C++ 
Source0:	%{name}-%{version}.tar.bz2
Patch0:		zipios++-0.1.5.9-suse-support-arches.patch
Patch1:		zipios++-0.1.5.9-suse-fix-amd64.patch
Patch2:		zipios++-0.1.5.9-suse-fix-gcc43.patch
Patch3:		zipios++-0.1.5.9+cvs.2007.04.28-mdv-gcc46.patch
BuildRequires:	zlib-devel libcppunit-devel doxygen imagemagick

%description
Zipios++ is a java.util.zip-like C++ library for reading and writing Zip files.
Access to individual entries is provided through standard C++ iostreams.
A simple read-only virtual file system that mounts regular directories and zip
files is also provided

%package -n %{libname}
Summary:        A java.util.zip-like C++ library for reading and writing Zip files
Group:          System/Libraries

%description -n %{libname}
Zipios++ is a java.util.zip-like C++ library for reading and writing Zip files.
Access to individual entries is provided through standard C++ iostreams.
A simple read-only virtual file system that mounts regular directories and zip
files is also provided

%package -n %{develname}
Summary:	Zipios++ header files
Group:		Development/C++
Requires: 	%libname = %version
Requires:	zlib-devel
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
Header files and documentation for zipios++ development.

%prep
%setup -q -n %{name}-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

chmod -x AUTHORS NEWS README COPYING

%build
%configure2_5x --enable-static='no'

%make
%make doc

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_libdir}/libzipios.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%doc %dir doc/html/
%{_includedir}/zipios++
%{_libdir}/libzipios.so


%changelog
* Mon Jan 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.1.5.9+cvs.2007.04.28-1
+ Revision: 769742
- imported package zipios++

