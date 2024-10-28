%undefine _debugsource_packages

Name: syncwall
Summary: Wallpaper management with synchronization features
Version: 2.0.0
Release: 9.1
License: GPLv2+
Group: User Interface/Desktops
URL: https://sourceforge.net/projects/syncwall/
Source0: https://sourceforge.net/projects/syncwall/files/%{version}/SyncWall-%{version}-src.zip
BuildRequires: dos2unix
BuildRequires: qt4-devel

%description
SyncWall is quite a basic wallpaper changer with a special feature, it
is the ability to synchronize wallpaper change between several
workstations with a basic (and unsecured) client/server protocol. Each
workstation must share the same pool of files, there is no FTP or
Internet download. Another interesting feature is a simple multi
monitor support, because SyncWall is written with Qt.

%prep
%setup -q -n SyncWall-%{version}-src
dos2unix tounix.sh
sh ./tounix.sh
sed -i '943s|return(false);|return(0);|' src/3rdparty/qimageblitz/convolve.cpp

%build
cd build
qmake-qt4 INSTALL_PREFIX=%{buildroot}/usr SyncWall.pro
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
cd build
make install
# remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/syncwall
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc *.txt
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man*/*

%changelog
* Wed Apr 15 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
* Fri Jan 27 2012 Sawa <sssawwwa@wolfenstein.jp> - 3.0.712-1
- Initial package.
