%undefine _debugsource_packages

Name:		qtcardgame
Version: 0.9.3.11
Release: 21.1
License:	GPL
Source0:	cardgameengine-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Group:		Amusements/Games
Summary:	Gard Game Engine
Vendor:		Claus Ilginnis <claus@ilginnis.de>
URL:		https://trex-online.no-ip.info/projects/cardgameengine/
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, make, pkgconfig, pkgconfig(QtCore), pkgconfig(QtGui)

%description
Write your own card games! Just implement the rules as JavaScript and start
playing. The integrated Qt Debugger will help you a lot.

%prep
%setup -q -n cardgameengine-%{version}

%build
pushd src
lrelease-qt4 %{name}.pro
qmake-qt4
make
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 0755 src/CardGame $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__install} -Dp -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3.11
- Rebuilt for Fedora
* Thu Dec 01 2011 TI_Eugene <ti.eugene@gmail.com> 09.3
- Initital build in OBS
