%global debug_package %{nil}

Name:          libtrio
Version:       1.14
Release:       5.1
Summary:       Portable and extendable printf and string functions
Group:         System/Libraries
URL:           http://daniel.haxx.se/projects/trio/
Source:        http://switch.dl.sourceforge.net/sourceforge/ctrio/trio-%{version}.tar.gz
License:       MIT

%description
Trio is a fully matured and stable set of printf and string functions designed
be used by applications with focus on portability or with the need for
additional features that are not supported by standard stdio implementation. 

There are several cases where you may want to consider using trio:
* Portability across heterogeneous platforms. 
* Embedded systems without stdio support. 
* Extendability of unsupported features. 
* Your native version doesn't do everything you need.

Trio fully implements the C99 (ISO/IEC 9899:1999) and UNIX98) standards, as
well as many features from other implemenations, e.g. the GNU libc and BSD4.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}

%description devel
Trio is a fully matured and stable set of printf and string functions designed
be used by applications with focus on portability or with the need for
additional features that are not supported by standard stdio implementation.

There are several cases where you may want to consider using trio:                      
* Portability across heterogeneous platforms.
* Embedded systems without stdio support.
* Extendability of unsupported features.
* Your native version doesn't do everything you need.

Trio fully implements the C99 (ISO/IEC 9899:1999) and UNIX98) standards, as
well as many features from other implemenations, e.g. the GNU libc and BSD4.

This package contains static libraries and header files need for development.

%prep
%setup -q -n trio-%{version}

%build
%configure
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files devel
%{_includedir}/*.h
%{_libdir}/libtrio.a
%doc CHANGES README

%changelog
* Tue Jun 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14
- Rebuild for Fedora
* Tue May 11 2010 Automatic Build System <autodist@mambasoft.it> 1.14-1mamba
- automatic update by autodist
* Thu Jan 29 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.13-1mamba
- automatic update by autodist
* Mon Jun 23 2008 Tiziana Ferro <tiziana.ferro@email.it> 1.12-1mamba
- update to 1.12
* Tue Oct 17 2006 Davide Madrisan <davide.madrisan@qilinux.it> 1.11-1qilnx
- package created by autospec
