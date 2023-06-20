%define oname	Zipios

%define major	2

%define libname %mklibname zipios++
%define oldlibname %mklibname zipios++ %{major}
%define develname %mklibname zipios++ -d

Name:           zipios++
Version:	2.2.6
Release:	2
License:        LGPLv2+
Summary:        C++ library for reading and writing Zip files
Group:          Development/C++
URL:            http://zipios.sourceforge.net/
# Upstream is dead. Using updated Debian source as they are fixing FTBFS issues.
Source0:	https://github.com/Zipios/Zipios/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:	cmake ninja
BuildRequires:  graphviz
BuildRequires:  pkgconfig(zlib)
BuildRequires:	recode locales-extra-charsets
BuildRequires:	doxygen graphviz

%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%package -n %{libname}
Summary:        A java.util.zip-like C++ library for reading and writing Zip files
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
%rename %{oldlibname}

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
%autosetup -p1 -n %{oname}-%{version}

# The XML file is marked UTF-8, but contains an
# ISO-8859-1 encoded umlaut
recode iso8859-1 contrib/zipios.metainfo.xml.in

%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
rm -rf %{buildroot}/%{_datadir}/doc/zipios/

%files
%{_bindir}/appendzip
%{_bindir}/dosdatetime
%{_bindir}/zipios
%{_mandir}/man3/zipios*
%{_datadir}/metainfo/zipios.metainfo.xml

%files -n %{libname}
%{_libdir}/libzipios.so.%{major}
%{_libdir}/libzipios.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/zipios
%{_datadir}/cmake/ZipIos/ZipIosConfig.cmake
