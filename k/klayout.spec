%undefine _debugsource_packages

Name:           klayout
Version:        0.25.7
Release:        1
Summary:        GDS2 chip layout Viewer
License:        GPL-2.0+
Group:          System/Filesystems
URL:            http://www.klayout.de
Source0:        http://www.klayout.de/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         build-sh.diff
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  qt-devel
BuildRequires:  ruby-devel >= 2.0.0
BuildRequires:  pkgconfig

%description
GDS2 viewer for the chip design engineer. The main objective was to focus on the basic
functionality but adding some useful features that many, even commercial viewers don't have:
* shows the design as it is
* can animate layers to make them blink or scroll the fill pattern.
* display a layer "marked" by drawing a small cross on all shapes.
All comes wrapped in a nice, Qt based state of the art GUI. Usage of the viewer
is simple and is similar to that of other tools.

%prep
%setup -q
#patch0

%build
%ifarch x86_64 aarch64
TARGET="linux-64-gcc-release"
%else
TARGET="linux-32-gcc-release"
%endif
sed -i 's|-m64||g' build.sh
sed -i 's|RUN_MAKE=1|RUN_MAKE=0|' build.sh
#QTBIN=$(dirname $(pkg-config --variable=moc_location QtCore))
#QTLIB=`pkg-config --variable=libdir QtCore`
QTBIN=/usr/lib64/qt5/bin
QTLIB=/usr/lib64
QTINC=%{_includedir}/qt5

./build.sh
#./build.sh -platform $TARGET \
#           -bin %{buildroot}%{_bindir} \
#           -build `pwd` \
#           -qtbin $QTBIN \
#           -qtinc $QTINC \
#           -qtlib $QTLIB \
#           -option %{?jobs:-j%jobs}

cd build-release
sed -i 's|-Wall|-Wall -std=gnu++14|' Makefile */Makefile */*/Makefile */*/*/Makefile
sed -i 's|-isystem /usr/include ||g' rba/rba/Makefile
make

%install
cd build-release
%make_install
cd ..
install -d %{buildroot}%{_bindir}
mv bin-release/%{name} bin-release/strm* %{buildroot}%{_bindir}
mv bin-release %{buildroot}%{_libdir}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 etc/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc LICENSE COPYRIGHT README.md Changelog*
%{_bindir}/*
%{_libdir}/lib%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jan 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.25.7
- Rebuilt for Fedora
* Mon Sep 23 2013 burnus@net-b.de
- Update to 0.22.9
  * Bug fixes
* Wed Sep  4 2013 burnus@gmx.de
- Strip binary
- Changes for RHEL/CentOS 5
* Tue Sep  3 2013 burnus@gmx.de
- Change build.sh to be buildable with both openSUSE/SLES
  and RHEL/CentOS 6
* Mon Sep  2 2013 burnus@net-b.de
- Update to 0.22.8
  * "gds2" now is recognized as extension of GDS files.
  * OASIS writer performance is significantly better now
  * Bug fixes
- Fix spec for CentOS/RHEL/Fedora
* Thu Feb  7 2013 joop.boonen@opensuse.org
- Build version 0.22.5
- Cleaned the spec file up
* Fri Dec 25 2009 lars@linux-schulserver.de
- update to 0.19.3
* Thu Apr 24 2008 lars@linux-schulserver.de
- initial version 0.14
