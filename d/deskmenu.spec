%define _name DeskMenu

Name: deskmenu
Version: 1.4.5
Release: 1
Summary: Root menu program for Window Manager
Summary(uk_UA): Главное меню для віконного менеджера
Summary(ru_RU): Главное меню для оконного менеджера
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source0: http://ftp.debian.org/debian/pool/main/d/deskmenu/%{name}_%{version}.tar.gz
Source1: %name.menu-method.gz
BuildRequires: fontconfig gtk2-devel
BuildRequires: libXext-devel libXt-devel autoconf

%description
%_name is a root menu program for Window Manager which is activated
by clicking the root window.

%description -l uk_UA
%_name - головне меню для віконного менеджера, активізується кліком
кнопкою мишки.

%description -l ru_RU
%_name - главное меню для оконного менеджера, активизирующееся кликом
кнопкой мышки.

%prep
%setup -q
sed -i 's/\r//g' README

%build
%configure
%__make

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
install -d -m 0755 %{buildroot}%_sysconfdir/menu-methods
gzip -dc -- %SOURCE1 > %{buildroot}%_sysconfdir/menu-methods/%name
chmod 755 %{buildroot}%_sysconfdir/menu-methods/%name
gzip --best --stdout -- debian/changelog > changelog.gz

%files
%doc AUTHORS README example_rc changelog.gz debian/README.Debian
%{_bindir}/%name
%{_mandir}/man1/*
%exclude %_sysconfdir/menu-methods/*

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.5
- Rebuilt for Fedora
* Fri Jun 16 2006 Led <led@altlinux.ru> 1.4.2-alt1
- initial build
