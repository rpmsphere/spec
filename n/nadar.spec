%undefine _debugsource_packages

Name: nadar
Summary: A network tank battle game
Version: 2.0
Release: 9.1
Group: Amusements/Games
License: GPL
URL: https://kozos.jp/myfreesoft/#9
Source0: https://kozos.jp/myfreesoft/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXpm-devel

%description
N.A.D.A.R. is a network tank battle game. You get into a tank,
operate it, and destroy other tanks to survive!

%prep
%setup -q
sed -i '/default :/d' server/Game.c

%build
make X11BASE=/usr BINDIR=%{_bindir} MANDIR=%{_mandir}/man1

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc README.eng COPYING COPYRIGHT HISTORY
%{_bindir}/*
%{_mandir}/man1/*.1.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
