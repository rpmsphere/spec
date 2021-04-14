Summary: Tools for chemical kinetics, thermodynamics, and/or transport problems
Name:          cantera
Version:       2.4.0
Release:       1
License:       New BSD
Group:         Productivity/Scientific/Other
URL:           http://cantera.github.io/docs/sphinx/html/index.html
Source0:       http://cantera.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: python2-scons
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: graphviz
BuildRequires: atlas-devel
BuildRequires: sundials-devel
BuildRequires: python2-devel
BuildRequires: numpy
BuildRequires: netpbm
BuildRequires: ghostscript-core
#BuildRequires: Cython

%description
Cantera is a suite of object-oriented software tools for problems involving
chemical kinetics, thermodynamics, and/or transport processes.

With Cantera's object technology, you assemble your architectural masterpiece
(i.e application program) from a set of very special bricks you pick up at the
Cantera quarry! Each "brick" (or object) represents some well-defined small
component of the global structure.

Some of the types (or classes) of objects Cantera provides represent:
* phases of matter
* interfaces between these phases
* reaction managers
* time-dependent or steady reactor networks
  - IC engine models
  - CSTR reactor network 
* One-dimensional flows
  - Burner-stabilized flat flames
  - Air plasma formed behind the bow shock on a re-entry vehicle during re-entry
    into the Earth's atmosphere
  - Adiabatic propagating flat flames

%package devel
Summary: Tools for chemical kinetics, thermodynamics, and/or transport problems
Group:       Development/Libraries/Other
Requires:    %{name} = %{version}-%{release}

%description devel
The packages contains development files for Cantera.

%prep
%setup -q
#sed -i 's|math\.h|cmath|' SConstruct
#sed -i 's|SUNDIALS_PACKAGE_VERSION|31|' SConstruct
sed -i "s|'3.0','3.1'|'3.0','3.1','3.2'|" SConstruct
sed -i 's|-pthread|-pthread -Wl,--allow-multiple-definition|' SConstruct

%build
scons build prefix=/usr boost_inc_dir=/usr/include/boost

%install
scons install stage_dir=%{buildroot}
sed -i 's|%{buildroot}/||' %{buildroot}%{_bindir}/setup_cantera*

%clean
rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/man/man1/*.1.*
%{_libdir}/lib*.so.*
%exclude %{_libdir}/lib*.a

%files devel
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Wed Dec 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.0
- Rebuilt for Fedora
* Tue Nov 15 2011 - Armin Wehrfritz
- fix install directories for /lib or /lib64
- put 'man' and 'doc' to 'share'
* Fri Nov 11 2011 - Armin Wehrfritz
- fix script to set PYTHONPATH environment variable
- Remove 'cmake' from 'BuildRequires', since not used
* Thu Nov 10 2011 - Armin Wehrfritz
- Initial package 
- SVN snapshot of version 1.8
- Heavy modifications to install with ${DESTDIR} and build rpm-package
