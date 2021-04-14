%undefine _debugsource_packages

Name: cortina
Summary: Wallpaper changer for gnome
Version: 1.1.1
Release: 8.1
Group: User Interface/Desktops
License: GPL
URL: https://launchpad.net/cortina
Source0: https://launchpad.net/cortina/trunk/1.1.1/+download/cortina_1.1.1-0~6~oneiric1.tar.gz
BuildRequires: qt4-devel

%description
Cortina can rotate wallpapers by time and works as an tray application
with an configuration interface. Is a simple wallpaper changer for GNOME
desktop, lightweight and perform all its task quicky and swiftly.

%prep
%setup -q -n recipe-{debupstream}-0~{revno}
sed -i -e 's|path = /|path = %{buildroot}/|' -e 's|lrelease|lrelease-qt4|' Cortina.pro

%build
qmake-qt4
make %{?_smp_mflags}

%install
make install
install -Dm644 %{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/qt4/translations/%{name}
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
