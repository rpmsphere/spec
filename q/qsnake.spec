%undefine _debugsource_packages

Name:           qsnake
Version:        1.0.2
Release:        1.1
License:        GPL
Source0:        qsnake-linux.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Group:          Amusements/Games
Summary:        Qt Snake game
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, make, pkgconfig, pkgconfig(QtCore), pkgconfig(QtGui)
URL:            https://www.linux-apps.com/p/1109362/

%description
QSnake is a game similar to Snake from old Nokia phones.

%prep
%setup -q -n %{name}

%build
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 0755 qsnake $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__install} -Dp -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Fri Jan 20 2012 TI_Eugene <ti.eugene@gmail.com> 0.0.1
- Initital build in OBS
