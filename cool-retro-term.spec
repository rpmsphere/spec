Summary:	Cool Retro Terminal
Name:		cool-retro-term
Version:	1.0.0
Release:	1
License:	GPLv3+
Group:		Terminals
URL:		https://github.com/Swordfish90/cool-retro-term
#Source0:	https://github.com/Swordfish90/cool-retro-term/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:	https://codeload.github.com/Swordfish90/cool-retro-term/zip/master#/%{name}-master.zip
Source1:	qmltermwidget-0.1.0.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtdeclarative
Requires:       qt5-qtgraphicaleffects
 
%description
Cool Retro Terminal is a terminal emulator which tries to mimic the look and
feel of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -q -n %{name}-master
rm -rf qmltermwidget
tar -xf %{SOURCE1}
mv qmltermwidget-0.1.0 qmltermwidget

%build
%define optflags -Wa,--compress-debug-sections -gdwarf-4
%define ldflags %{nil}
qmake-qt5
make

%install
make install INSTALL_ROOT=%{buildroot} STRIP=true

%files
%doc README.md *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/qt5/qml/QMLTermWidget

%changelog
* Mon Jul 17 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
* Sun Jan 25 2015 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.0.0-1
+ Revision: 4e836b2
- New version 1.0.0
