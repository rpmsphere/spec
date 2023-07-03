%define Name Oroborus
Name: oroborus
Version: 2.0.20
Release: 4.1
Summary: Small window manager for the X Window System
Summary(uk_UA): Маленький віконний менеджер для X Window System
Summary(ru_RU): Маленький оконный менеджер для X Window System
License: GPL
Group: Graphical desktop/Other
URL: https://www.oroborus.org/
Source0: https://ftp.debian.org/debian/pool/main/o/oroborus/%{name}_%{version}.tar.gz
Source1: %name-icons.tar.bz2
Source2: start%name
Source3: %{name}rc
Source4: %name.startup
Patch: %name-2.0.18-man.patch
BuildRequires: imake libSM-devel libXext-devel libXpm-devel

%description
The main aim of %Name is to be small and light with very few fancy
features, so there are no docks, no taskbars, no root menus and no
icons. These can be added quite easily by either using %Name with
GNOME or using some other applications that provide the required
functionality.

%description -l uk_UA
Головна мета %Name - бути маленьким і легким з дуже небагатьма
"модними" властивостями; таким чином немає ніяких доків, панелей задач,
головних меню та значків. Вони можуть бути вельми легко додані шляхом
використання %Name з GNOME або за допомогою інших додатків, які
забезпечують необхідну функціональність.

%description -l ru_RU
Главная цель %Name - быть маленьким и лёгким с очень немногими
"модными" свойствами; таким образом нет никаких доков, панелей задач,
главных меню и значков. Они могут быть весьма легко добавлены путём
использования %Name с GNOME или с помощью других приложений,
обеспечивающих необходимую функциональность.

%package themes
Summary: Themes for %Name Window Manager
Summary(uk_UA): Теми для віконного менеджера %Name
Summary(ru_RU): Темы для оконного менеджера %Name
Group: Graphical desktop/Other
Requires: %name
BuildArch: noarch

%description themes
Themes for %Name Window Manager.

%description -l uk_UA themes
Теми для віконного менеджера %Name.

%description -l ru_RU themes
Темы для оконного менеджера %Name.

%prep
%setup -q -a 1
%patch -p1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
%__make

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
install -pD -m 644 %name-64.xpm %{buildroot}%{_datadir}/pixmaps/%name.xpm
install -pD -m 0755 %SOURCE2 %{buildroot}%{_bindir}/start%name
chmod 755 %{buildroot}%{_bindir}/start%name
install -d -m 0755 %{buildroot}%{_sysconfdir}/X11/%name
install -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/X11/%name/startup
install -m 0755 %SOURCE3 %{buildroot}%{_sysconfdir}/X11/%name/%{name}rc

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog README TODO example.%{name}rc
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_datadir}/%name
%dir %{_datadir}/%name/schemes
%dir %{_datadir}/%name/themes
%{_datadir}/%name/defaults
%{_datadir}/%name/schemes/*
%{_datadir}/%name/themes/%name
%{_datadir}/pixmaps/*.xpm
#{_sysconfdir}/X11/wmsession.d/*
%dir %{_sysconfdir}/X11/%name
%config(noreplace) %{_sysconfdir}/X11/%name/*

%files themes
%{_datadir}/%name/themes/QNX
%{_datadir}/%name/themes/agua
%{_datadir}/%name/themes/beos
%{_datadir}/%name/themes/cruxish
%{_datadir}/%name/themes/e017
%{_datadir}/%name/themes/gorillaworm
%{_datadir}/%name/themes/next
%{_datadir}/%name/themes/pillage
%{_datadir}/%name/themes/platinum
%{_datadir}/%name/themes/slimline
%{_datadir}/%name/themes/windows
%{_datadir}/%name/themes/defold
%{_datadir}/%name/themes/bluecurve
%{_datadir}/%name/themes/mkultra
%{_datadir}/%name/themes/Elberg_Red
%{_datadir}/%name/themes/Elberg_Green
%{_datadir}/%name/themes/Elberg_Blue

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.20
- Rebuilt for Fedora
* Mon Sep 24 2007 Led <led@altlinux.ru> 2.0.18-alt5
- updated %%{_sysconfdir}/X11/%%name/startup
- cleaned up spec
* Sat Jun 09 2007 Led <led@altlinux.ru> 2.0.18-alt4
- fixed and cleaned up spec
* Sat Aug 19 2006 Led <led@altlinux.ru> 2.0.18-alt3
- fixed %%files sections
* Fri Jun 16 2006 Led <led@altlinux.ru> 2.0.18-alt2
- changed in %%name startup file
* Fri Jun 16 2005 Led <led@altlinux.ru> 2.0.18-alt1
- initial build
- added %%name-2.0.18-man.patch
