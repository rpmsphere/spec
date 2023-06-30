Name:          libELFIO
Version:       1.0.3
Release:       13.1
Summary:       A C++ library for reading and generating files in the ELF binary format
Group:         System/Libraries
URL:           https://elfio.sourceforge.net/
Source:        https://mesh.dl.sourceforge.net/sourceforge/elfio/ELFIO-%{version}.tar.gz
License:       LGPL
BuildRequires: gcc-c++

%description
ELFIO is a C++ library for reading and generating files in the ELF binary format.
This library is unique and not based on any other product. It is also platform
independent. The library uses standard ANSI C++ constructions and runs on a wide
variety of architectures. 

While the library's implementation does make your work easier: a basic knowledge
of the ELF binary format is required. Information about ELF is included in the TIS
(Tool Interface Standards) documentation you received with the library's source code.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
AutoReqProv: off

%description devel
ELFIO is a C++ library for reading and generating files in the ELF binary format.
This library is unique and not based on any other product. It is also platform
independent. The library uses standard ANSI C++ constructions and runs on a wide
variety of architectures. 

While the library's implementation does make your work easier: a basic knowledge
of the ELF binary format is required. Information about ELF is included in the TIS
(Tool Interface Standards) documentation you received with the library's source code.

This package contains static libraries and header files need for development.

%prep
%setup -q -n ELFIO-%{version}

%build
export CXXFLAGS='-g -O2 -fPIC'
%configure
make

# build shared library
cd ELFIO
g++ $CXXFLAGS -shared *.o -o libELFIO.so.1

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -Dm755 ELFIO/libELFIO.so.1 $RPM_BUILD_ROOT%{_libdir}/libELFIO.so.1
ln -s libELFIO.so.1 $RPM_BUILD_ROOT%{_libdir}/libELFIO.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libELFIO.so.1
%doc AUTHORS COPYING ChangeLog README

%files devel
%{_bindir}/ELFDump
%{_libdir}/libELFIO.a
%{_libdir}/libELFIO.so
%{_includedir}/*.h

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
* Wed Sep 26 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.3-1mamba
- package created by autospec
