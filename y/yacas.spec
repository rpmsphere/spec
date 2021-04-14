%undefine _debugsource_packages
Name:           yacas
Version:        1.9.1
Release:        1
License:        LGPL-2.0+
Summary:        An easy to use, general purpose Computer Algebra System
URL:            http://yacas.sourceforge.net/
Group:          Productivity/Scientific/Math
BuildRequires:  dejagnu
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gnuplot
BuildRequires:  gperf
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRequires:  gzip 
BuildRequires:  desktop-file-utils
# lynx is defined as help browser in /usr/share/yacas/yacasinit.ys
Requires:       lynx
BuildRequires:  gcc-gfortran
BuildRequires:  texlive-latex
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-dvips
BuildRequires:  texlive
BuildRequires:  bzip2-libs 
BuildRequires:  ncurses-devel 
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  cmake
BuildRequires:  google-benchmark-devel
BuildRequires:  zmqpp-devel
BuildRequires:  jsoncpp-devel
Source0:        %{name}-%{version}.tar.gz

%description
YACAS is an easy to use, general purpose Computer Algebra System, a
program for symbolic manipulation of mathematical expressions.

It uses its own programming language designed for symbolic as well as
arbitrary-precision numerical computations.

The system has a library of scripts that implement many of the symbolic
algebra operations; new algorithms can be easily added to the library.

YACAS comes with extensive documentation (320+ pages) covering the
scripting language, the functionality that is already implemented in
the system, and the algorithms we used.

%package devel
Summary:        Development package for YACAS based software
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       mesa-libGL-devel
Requires:       glibc-devel
Requires:       gsl-devel
Requires:       libICE-devel 
Requires:       libSM-devel  
Requires:       libX11-devel 
Requires:       libXau-devel 
Requires:       libXext-devel
Requires:       libXmu-devel
Requires:       libXt-devel
Requires:       libxcb-devel

%description devel
This package contains the header files and libraries needed to develop
programs that use YACAS.

%prep
%setup -q
cp README.rst README
#sed -i 's|jsoncpp/json/|json/|' cyacas/yacas-kernel/include/yacas_kernel.hpp cyacas/yacas-kernel/src/*.cpp

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install



%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README* TODO
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/pixmaps/%{name}-gui.png
%{_datadir}/icons/hicolor/*/apps/%{name}-gui.png

%files devel
%{_includedir}/%{name}
%{_libdir}/libyacas.so
%{_libdir}/libyacas_mp.so

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.1
- Rebuilt for Fedora
* Sat Dec 27 2014 lars@linux-schulserver.de
- update to 1.3.6:
  + Quite a few improvements and assorted bugfixes
- removed yacas-disable_wester_test.patch
- disable the build of static libraries
- run ldconfig during (un)install
- libraries are now in _libdir
- include files are now below _includedir
* Tue Apr  1 2014 avvissu@yandex.ru
- Clean up spec file for current version of the source
- Fix package-with-huge-docs:
  + move all documentation files from the package (yacas) to
  the subpackage (yacas-doc)
- Remove INSTALL file
- Fix incorrect-fsf-address
- Fix files-duplicate
- Fix unresolvable dependencies for Fedora:
  + add RPM conditional test {?fedora} and list the packages that
  requires to build
- Fix compilation error on Fedora: permission denied:
  + add $DESTDIR to make install
* Fri Feb 14 2014 lars@linux-schulserver.de
- update to 1.3.4:
  + Minor improvements and assorted bugfixes
- refreshed patches:
  * yacas-disable_wester_test.patch
* Fri Oct  5 2012 lars@linux-schulserver.de
- update to 1.3.3
* Sun Nov 13 2011 lars@linux-schulserver.de
- update to 1.3.0
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Wed Dec 26 2007 lars@linux-schulserver.de
- update to 1.2.2
* Thu Nov 22 2007 lars@linux-schulserver.de
- patch yacas to build with gcc43
* Tue Sep 25 2007 lrupp@suse.de
- update to 1.2.0
* Mon Aug  6 2007 lrupp@suse.de
- update to 1.1.0:
  + removed proteus worksheet
  + removed the directories "colorcode": now you could now use
    regular expressions and such
  + fix for a memory leak related to the use of the script archive
  + large clean-up of the code
* Tue Jun 26 2007 lrupp@suse.de
- changed desktop file entry (proteusworksheet => yacas)
* Tue Jun  5 2007 lrupp@suse.de
- split devel package
- split doc package
- add --enable-archive
- added lynx to Requires as help browser
* Tue Jun  5 2007 ro@suse.de
- buildreq: libbz2 -> libbz2-1
* Sat May 19 2007 coolo@suse.de
- remove X-SuSE-translate from desktop file
* Thu May 17 2007 lrupp@suse.de
- make it build on older distributions again
* Thu Apr 19 2007 aj@suse.de
- Use texlive for building.
* Sun Apr  1 2007 lrupp@suse.de
- include hack for libtool in 10.0 and 10.1
- added libbz2 to BuildRequires for > 10.2
* Fri Mar  9 2007 lrupp@suse.de
- specfile cleanup
* Thu Feb 15 2007 lrupp@suse.de
- build with "-fno-strict-aliasing"
  (=> grower.h:203 needs to be fixed)
- added xorg-x11-devel to BuildRequires
- adapt desktopfile handling for older distributions
* Wed Jan 17 2007 lrupp@suse.de
- some fixes for proteus GUI
- added desktop entry
* Wed Jan 10 2007 lrupp@suse.de
- new version 1.0.63 (first time in buildservice)
- enable "proteus" GUI
- remove unneeded .la files
- build parallel
* Tue Nov  7 2006 meissner@suse.de
- use RPM_OPT_FLAGS
* Mon Mar 20 2006 schwab@suse.de
- Fix compiling on 64bit.
* Tue Feb  7 2006 ro@suse.de
- add missin return value in yacasnumbers.cpp
- try to add some more crazy casts
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jun 16 2005 lrupp@suse.de
- initial package 1.0.57
