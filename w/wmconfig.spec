Summary:	Window Manager Configurator
Summary(de):	Window Manager Configurator
Summary(es):	Configurador de Administradores de ventanas
Summary(fr):	Configurateur de gestionnaires de fenętres
Summary(pl):	Konfigurator zarządców okien
Summary(pt_BR):	Configurador de gerenciadores de janelas
Summary(tr):	Pencere denetleyicisi ayarlarý
Name:		wmconfig
Version:	1.5.1
Release:	1
License:	GPLv2
Group:		X11/Window Managers/Tools
Source0:	http://www.arrishq.net/files/%{name}-%{version}.tar.gz
Source1:	%{name}-README.PLD
URL:		http://www.arrishq.net/
BuildRequires:	autoconf
BuildRequires:	automake

%description
This is a program that will generate menu configurations for different
window managers available for the X11 system. It is an attempt to gain
some form of abstractization of the menu configuration across some
window managers. Currently it supports: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%description -l es
Este es un programa que crea configuraciones de menú para diferentes
administradores de ventana disponibles para el sistema X11. Es un
intento de abstraer una configuración única entre estos diferentes
administradores. Actualmente soporta: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%description -l pl
Ten program ułatwia konfigurowanie menu w różnych zarządcach okien
dostępnych dla systemu X11. W tej chwili wspiera następujące programy:
FVWM2, FVWM95, Afterstep, MWM, IceWM, KDE, WindowMaker.

%description -l pt_BR
Este é um programa que gera configuraçőes de menu para diferentes
gerenciadores de janela disponíveis para o sistema X11. É uma
tentativa de abstrair uma configuraçăo única entre esses diferentes
gerenciadores. Atualmente suporta: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%prep
%setup -q
cp %{SOURCE1} README.PLD

%build
autoreconf -ifv
%configure
make

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README* TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1x.*
%{_sysconfdir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1
- Rebuilt for Fedora
* Sun Jan 02 2005 PLD Team <feedback@pld.org.pl>
- Revision 1.64  2005/01/02 15:00:08  kloczek
- updated to 1.2.3.
- Revision 1.63  2004/09/16 20:38:16  kloczek
- updated to 1.2.1.
