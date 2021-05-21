Name: openpref
Version: 0.1.0
Release: 1
Summary: Preference game for linux
Group: Games/Cards
License: GPL
Source0: http://openpref.narod.ru/openpref.tar.gz
Source1: openpref.desktop
Source2: openpref.png
Patch0: openpref-alt-build.patch
URL: http://openpref.narod.ru/
BuildRequires: gcc-c++ qt3-devel

%description
OpenPref - Preference game for linux.

%description -l ru_RU.KOI8-R
OpenPref - ÐÒÅÆÅÒÁÎÓ ÄÌÑ Linux.

%prep
%setup -q -c
%patch0 -p1

%build
qmake %{name}.pro
%{__make}

%install
mkdir -p %buildroot%_bindir/
install -m755 -p %name %buildroot%_bindir/

mkdir -p %buildroot%_desktopdir
install -m644 -p %SOURCE1 %buildroot%_desktopdir/

mkdir -p %buildroot%{_datadir}/pixmaps/
install -m755 %SOURCE2 %buildroot%{_datadir}/pixmaps/

%clean
%__rm -rf %{buildroot}

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/pixmaps/openpref.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
* Wed May 23 2012 Tony Lo <tonylo@ossii.com.tw> 0.1.0-6
- ox2 Version
* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt5
- fix desktop file
* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt4
- add Packager tag
- convert menu file to desktop file
- buildreq
* Wed Mar 21 2007 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt3
- fix build on x86_64
* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt2.1
- rebuild with new gcc flags (-Wl,--as-needed)
* Wed Dec 28 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.0-alt2
- fix menu file
* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.0-alt1
- Initial build for Sisyphus
