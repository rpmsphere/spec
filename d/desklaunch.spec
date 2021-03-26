Name: desklaunch
Version: 1.1.5
Release: 1
Summary: Small utility for creating desktop icons
License: GPL
Group: Graphical desktop/Icewm
URL: http://www.oroborus.org
Source0: %url/debian/dists/sid/main/source/x11/%{name}_%version.tar.gz
Patch0: %name-1.1.3-alt-errfmt.patch
BuildRequires: libX11-devel libXpm-devel gcc glibc-devel
Summary(ru_RU): Утилита для запуска иконок с десктопа

%description
DeskLaunch is a small utility for creating desktop icons using pixmaps.
A simple click will launch the desired application.
User should manually create its own desktop by editing ~/.desklaunchrc file.

%description -l ru_RU
DeskLaunch служит для размещения запускаемых значков на Рабочем столе.
Одинарный щелчок мыши по значку запускает назначенное приложение.

Список приложений, а также состав и координаты значков пользователь
редактирует самостоятельно, вручную исправляя файл .desklaunchrc
в своём домашнем каталоге.

%prep
%setup -q
%patch0 -b .errfmt

%build
%__make

%install
rm -rf %{buildroot}
%__install -pD %name %{buildroot}%{_bindir}/%name
%__install -pD -m644 debian/%name.1 %{buildroot}%{_mandir}/man1/%name.1

%files
%{_bindir}/%name
%{_mandir}/man1/%name.1*
%doc README debian/changelog debian/example_rc

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.5
- Rebuild for Fedora
* Mon Feb 20 2006 Ilya G. Evseev <evseev@altlinux.ru> 1.1.5-alt1
- updated to new version 1.1.5
* Mon Oct 10 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.1.4-alt2
- fixed case in URL macro
* Tue Aug 30 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.1.4-alt1
- update to new version
* Mon Jan 31 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.1.3-alt1
- initial ALT build
