Name:          liblauncher
Version:       0.3.6
Release:       1
Summary:       A library to build launchers
Group:         System Environment/Libraries
License:       GPLv3 and LGPLv3
URL:           https://launchpad.net/%{name}
Source0:       http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
# Fix building on Fedora 13: https://bugs.launchpad.net/liblauncher/+bug/580194
Patch0:        0001-Fix-building-with-implicit-DSO-change-in-Fedora-13.patch
BuildRequires: GConf2-devel
BuildRequires: libwncksync-devel
BuildRequires: mate-menus-devel, libmate

%package devel
Summary:       A library to build launchers
Group:         Development/Libraries
Requires:      pkgconfig >= 1:0.14
Requires:      %{name} = %{version}-%{release}

%description
%{name} is a library to build launchers.

%description devel
The %{name}-devel package includes the header files for the
%{name} library.

%prep
%setup -q
%patch0 -p1
sed -i 's/-Werror//' configure*
sed -i 's/gnome/mate/' configure* launcher.pc.in tests/Makefile.*
sed -i -e 's/gmenu/matemenu/' -e 's/GMenu/MateMenu/g' -e 's/GMENU/MATEMENU/' launcher/launcher-menu.c launcher/Makefile*
autoreconf

%build
%configure --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}-0.3.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING COPYING.GPL
%{_libdir}/%{name}-0.3.so.*

%files devel
%doc AUTHORS COPYING COPYING.GPL
%{_includedir}/launcher-0.3/launcher/launcher-application.h
%{_includedir}/launcher-0.3/launcher/launcher-appman.h
%{_includedir}/launcher-0.3/launcher/launcher-category.h
%{_includedir}/launcher-0.3/launcher/launcher-favorites.h
%{_includedir}/launcher-0.3/launcher/launcher-folder-bookmarks.h
%{_includedir}/launcher-0.3/launcher/launcher-folder.h
%{_includedir}/launcher-0.3/launcher/launcher-icon-utils.h
%{_includedir}/launcher-0.3/launcher/launcher-menu.h
%{_includedir}/launcher-0.3/launcher/launcher-session.h
%{_includedir}/launcher-0.3/launcher/launcher.h
%{_libdir}/%{name}-0.3.so
%{_libdir}/pkgconfig/launcher-0.3.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.6
- Rebuilt for Fedora
* Thu May 13 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 0.3.6-1
- First build
