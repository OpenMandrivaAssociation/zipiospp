%define oname	Zipios

%define major	2

%define libname %mklibname zipios++ %{major}
%define develname %mklibname zipios++ -d
%bcond_with docs

Name:           zipios++
Version:	2.2.6
Release:	1
License:        LGPLv2+
Summary:        C++ library for reading and writing Zip files
Group:          Development/C++
URL:            http://zipios.sourceforge.net/
# Upstream is dead. Using updated Debian source as they are fixing FTBFS issues.
Source0:	https://github.com/Zipios/Zipios/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  graphviz
BuildRequires:  pkgconfig(zlib)
%if %{with docs}
BuildRequires:	doxygen
%endif


%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%package -n %{libname}
Summary:        A java.util.zip-like C++ library for reading and writing Zip files
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
Zipios++ is a java.util.zip-like C++ library for reading and writing Zip files.
Access to individual entries is provided through standard C++ iostreams.
A simple read-only virtual file system that mounts regular directories and zip
files is also provided

%package -n %{develname}
Summary:        Header files for zipios++
Group:          Development/C++
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       zlib-devel

%description -n %{develname}
The header files are only needed for development of programs using the
zipios++.

%prep
%setup -q -n %{oname}-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build
rm -rf %{buildroot}/%{_datadir}/doc/zipios/

%files
%{_bindir}/appendzip
%{_bindir}/dosdatetime
%{_bindir}/zipios
%if %{with docs}
%{_mandir}/man3/zipios*
%endif
%{_datadir}/metainfo/zipios.metainfo.xml

%files -n %{libname}
%{_libdir}/libzipios.so.%{major}
%{_libdir}/libzipios.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/zipios
%{_datadir}/cmake/ZipIos/ZipIosConfig.cmake
