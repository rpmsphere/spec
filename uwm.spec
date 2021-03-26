Summary: Ultimate Window Manager
Name: uwm
Version: 0.2.11a
Release: 3.1
License: GPL
Group: User Interface/Desktops
Source: http://softlayer-sng.dl.sourceforge.net/project/udeproject/UWM/%{name}-%{version}%20stable/%{name}-%{version}.tar.gz
URL: http://udeproject.sourceforge.net
BuildRequires: libX11-devel, libXext-devel, libXpm-devel, libXmu-devel
Provides: ude

%description
UDE - The Unix Desktop Environment is more then just
another windows manager. Designed to compensate for
the shortcomings of many other similar packages, UDE
features many innovative improvements. The project does
not use any special GUI-Libraries such as QT or GTK+ and
is based on the standard Xlibs (also to make UDE faster).
  
%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
mv $RPM_BUILD_ROOT/usr/doc $RPM_BUILD_ROOT/usr/share/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/uwm
%{_datadir}/doc/*

%changelog
* Fri Apr 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.11a
- Rebuild for Fedora
* Sat Jun 9 2001 Christian Ruppert <arc@gmx.li>
- Added package description
- Updated URL
- configure.in shold be now set up in a way so that building rpms should work
  for releases, not for snaps (where we use <SNAP$(shell date +%d%m%Y)> as
  version string which works fine for makefiles but not for rpm.spec).
* Sun Aug 8 1999 Jaime Alberto Silva <mono@andromeda.utp.edu.co>
- Created file ude.spec.in
