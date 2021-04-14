Name:           kseg
Version:        0.403
Release:        226.1
License:        GPL-2.0+
Summary:        A Simulator of Euclidean Geometry
URL:            http://www.mit.edu/~ibaran
Group:          Productivity/Scientific/Math
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.xpm
Source10:       kseg_mn.qm
# PATCH-FIX-UPSTREAM add missing include
Patch0:         kseg-assert.patch
# PATCH-FIX-UPSTREAM use the home directory for locale and examples
Patch1:         kseg-KSEG_HOME.patch
# PATCH-FIX-UPSTREAM use the language specific locale for helps
Patch2:         kseg-setFilePath.patch
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  qt3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KSEG is a program for exploring Euclidean geometry. You can create a
construction, such as a triangle with a circumcenter, then, as you drag
verteces of the triangle, you can see the circumcenter moving in real
time. KSEG is very fast even in big and recursive constructions and may
well be used in math lessons in school.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
# fix home path
sed -i "s|@KSEG_HOME@|%{_datadir}/%{name}|g" main.cpp

%build
qmake QTDIR=$QTDIR LIBS=" -lm -L$QTDIR/lib -lqt-mt -lz"
make QTDIR=$QTDIR LIBS=" -lm -L$QTDIR/lib -lqt-mt -lz" KSEG_HOME="%{_datadir}/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/{examples,pics,locale}
install -Dm755 kseg          $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m644 *.qm *.html $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/
install -p -m644 examples/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/examples/
install -p -m644 pics/*      $RPM_BUILD_ROOT%{_datadir}/%{name}/pics/
# install additional locales
install -m644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/

# install desktop icon and entry
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING AUTHORS README README.translators VERSION
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%changelog
* Fri Aug 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.403
- Rebuilt for Fedora
* Wed Feb 15 2012 lars@linux-schulserver.de
- fix copyright header in specfile
* Thu Jan 12 2012 coolo@suse.com
- change license to be in spdx.org format
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
- cleanup the specfile
* Sat Mar 22 2008 lars@linux-schulserver.de
- added translation into Mongolian
- added patch for distribution default LanguageDir and
  QuickPlayDirectory (kseg-KSEG_HOME.patch)
- try to find the right language help file automatically
  (kseg-setFilePath.patch)
- added kseg icon for menu entry
* Fri Mar 21 2008 lars@linux-schulserver.de
- also package the img, html and qm files into %%_datadir/%%name
* Mon Mar 17 2008 lars@linux-schulserver.de
- update to 0.403:
  + uses qmake for building
  + build on Qt 3.x without the compatibility headers
  + Traditional Chinese translation and help file included
* Wed Feb 15 2006 stbinner@suse.de
- fixed .desktop file
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Sat Aug 16 2003 adrian@suse.de
- add desktop file
* Wed Aug  6 2003 uwedr@suse.de
- Update to version 0.4
* Tue Feb 25 2003 aj@suse.de
- Include missing assert.h.
* Tue Nov 19 2002 ro@suse.de
- build with qt3
* Tue Jun 11 2002 ro@suse.de
- fix linking on lib64 platforms
* Fri Apr 19 2002 coolo@suse.de
- fix for gcc 3.1
* Fri Nov  9 2001 ro@suse.de
- use qt-devel-packages in neededforbuild
* Fri Jun  8 2001 uwedr@suse.de
- Spec file created from kseg-0.3.tar.gz
