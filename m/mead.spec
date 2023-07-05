Name:           mead
License:        GPL
Group:          Productivity/Scientific/Chemistry
Summary:        Macroscopic Electrostatics with Atomic Detail
URL:            https://www.stjuderesearch.org/site/lab/bashford
Version:        2.2.9
Release:        12.1
BuildRequires:  gcc-c++
Source0:        https://ftp.stjude.org/pub/software/%{name}-%{version}.tar.bz2
Patch1:         1-destdir.patch
Patch2:         2-c-warn.patch
Patch3:         3-prototype.patch

%description
MEAD is a set of software objects for the purpose of modeling the
electrostatics of molecules using a semi-macroscopic picture in
which the solvent and the molecular interior have different
dielectric constants, the boundary between the different
dielectric regions is dependent on the detailed atomic structure
of the molecule, and the electrostatic potential is determined by
the Poisson-Boltzmann equation. This version of MEAD includes
modeling of a membrane as a low dielectric slab, possibly with a
water-filled channel through a protein in the membrane.

MEAD is written in C++, which is a significant departure from most
molecular software, which is more commonly written in Fortran or
(recently) C.  My purpose in choosing C++ was to explore the
object-oriented programming style that C++ facilitates and to make
a software system that other people could borrow pieces from and
make extensions to in a convenient way.

Authors:
--------
        Donald Bashford
        don.bashford@stjude.org

        Hartwell Center
        Saint Jude Children's Research Hospital
        Memphis, TN

%package devel
Summary:        Macroscopic Electrostatics with Atomic Detail 
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Header files and libraries for the package mead.

%prep
%setup -q 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%build
%configure
sed -i 's|-O2|-O2 -fPIC|' Makefile */Makefile */Makefile.common
%{__make} %{?jobs:-j %jobs}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_bindir}/mulsidecomp
%{_bindir}/multiflex
%{_bindir}/pair_interactions
%{_bindir}/potential
%{_bindir}/potscan
%{_bindir}/redti
%{_bindir}/sav-driver
%{_bindir}/solinprot
%{_bindir}/solvate

%files devel
%{_includedir}/MEAD
%{_libdir}/lib%{name}.a
%{_libdir}/libMEADsolvate.a

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.9
- Rebuilt for Fedora
* Tue Mar 15 2011 aeszter@gwdg.de
- 2.2.9-2.0
- fix libMEADsolvate install paths
* Tue Mar 15 2011 aeszter@gwdg.de
- 2.2.9-1.0
- new upstream version
* Thu Jan 28 2010 Ansgar Esztermann <aeszter@gwdg.de>
- 2.2.8a-1.0
- initial package
