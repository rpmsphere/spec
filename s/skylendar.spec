Name:           skylendar
Version:        4.1.2nn
Release:        2
License:        GPL-2.0
Summary:        Astrology software
URL:            https://sourceforge.net/projects/skylendar
Group:          Science/Astrology
Source0:        https://cfhcable.dl.sourceforge.net/project/skylendar/%{name}-%{version}.tar.xz
#PATCH-FIX-OPENSUSE skylendar-fix-qt-error.patch malcolmlewis@opensuse.org -- Add missing QT include.
#Patch0:         skylendar-fix-qt-error.patch
#PATCH-FIX-OPENSUSE skylendar-add-missing-linker-flag.patch malcolmlewis@opensuse.org -- Add missing dl linker flag.
#Patch1:         skylendar-add-missing-linker-flag.patch
#PATCH-FIX-OPENSUSE skylendar-fix-no-return.patch malcolmlewis@opensuse.org -- Fix no-return-in-nonvoid-function rpmlint error.
#Patch2:         skylendar-fix-no-return.patch
#PATCH-FIX-OPENSUSE skylendar-fix-desktop-files.patch malcolmlewis@opensuse.org -- Fix desktop category and mimetype duplicate.
#Patch3:         skylendar-fix-desktop-files.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fontpackages-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  mkfontdir
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(zlib)
Requires:       postgresql-server >= 9.3.0
Requires:       perl >= 5.16
Requires:       perl(XML::DOM) >= 1.44
Requires:       perl(DBD::Pg)

%description
A powerful, portable and modern design astrology program, based on the swisseph
library, with multitasking charts and data stored in a SQL database
(postgresql). Many charts and options.

%prep
%setup -q -n %{name}-4.1.2
#-%{release}
#-%{version}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
sed -i 's|pgsql/libpq-fe.h|libpq-fe.h|' src/astrosql.h
sed -i 's|pgsql/libpq/libpq-fs.h|libpq/libpq-fs.h|' src/astrosql.cpp

%build
%cmake -DCMAKE_BUILD_Type=Release .
%cmake_build

%install
%cmake_install
#Fix desktop file icon location
mkdir -p %{buildroot}%{_datadir}/pixmaps
pushd %{buildroot}%{_datadir}
mv icons/* pixmaps/
popd
#Remove files we install with %%doc
rm -f %{buildroot}%{_datadir}/skylendar/{HISTORY.txt,README,COPYING}
#Remove development lib
rm -f %{buildroot}%{_libdir}/libskyldr.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README HISTORY.txt
%license COPYING
%{_bindir}/skylendar
%{_bindir}/skyservice
%{_bindir}/skydmin
%{_datadir}/applications/skylendar.desktop
%{_datadir}/applications/skydmin.desktop
%{_datadir}/skylendar
%{_libdir}/lib*
%{_datadir}/pixmaps/skylendar.png
%{_datadir}/pixmaps/skydmin.png
%{_datadir}/pixmaps/skif.png
%{_datadir}/mime/packages/skif.xml
%{_datadir}/fonts/truetype/skylendar.ttf

%changelog
* Fri Sep 04 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.2nn
- Rebuilt for Fedora
* Sat Feb  2 2019 malcolmlewis@opensuse.org
- Add skylendar-fix-qt-error.patch: Add missing QT include.
- Add skylendar-add-missing-linker-flag.patch: Add missing dl
  linker flag.
- Add skylendar-fix-no-return.patch: Fix no-return-in-nonvoid-
  function rpmlint error.
- Add skylendar-fix-desktop-files.patch: Fix desktop category and
  mimetype duplicate.
