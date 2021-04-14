Name: 		wbar
Version: 	2.3.4
Release: 	1
Summary:	Quick Launch Bar
Source0:	http://wbar.googlecode.com/files/%{name}-%{version}.tgz
Source1:        %{name}-2.3.4.zh_TW.po
Source2:        %{name}.cfg
URL:		http://code.google.com/p/wbar/
Group:		User Interface/Desktops
License:	GPL
BuildRequires: 	libX11-devel
BuildRequires:	libstdc++-devel
BuildRequires:	imlib2-devel
BuildRequires:	freetype-devel
BuildRequires:	zlib-devel
BuildRequires:	gtk2-devel
BuildRequires:	libglade2-devel

%description
wbar is a quick launch bar. Its fast, light and cool eye-candy.
Its hacked in c++ trying to keep code as readable as possible with out
sacrificing speed. It works directly on top of X to avoid going throug
a lot of layers. Initially developed for Fluxbox, then tested on
WindowMaker, Xfce, Gnome, etc. Since version 1.0 can run on top of
desktops such as xfdesktop or nautilus with the -above-desk switch.

%description -l de
Wbar ist eine schnelle, leichtgewichtige und augenschmeichelnde
Schnellstartleiste. Das Programm wurde in C++ geschrieben, um
ohne Geschwindigkeitseinbußen den Code so leserlich wie möglich
zu halten. Es arbeitet direkt auf der X-Oberfläche. Ursprünglich
für Fluxbox entwickelt, später getestet mit WindowMaker, Xfce,
Gnome usw. Seit Version 1.0 wird Wbar mit Hilfe der Option
-above-desk im Vordergrund angezeigt und durch Desktopmanager
wie Xfdesktop oder Nautilus nicht mehr überdeckt.

%prep
%setup -q
echo zh_TW >> po/LINGUAS
cp %{SOURCE1} po/zh_TW.po

%build
%configure
sed -i 's|-Werror=format-security|-Wno-error|' Makefile */Makefile
make
cp %{SOURCE2} etc/wbar.cfg

%install
%__rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_sysconfdir}/%{name}.d/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc THANKS ChangeLog AUTHORS COPYING NEWS README
%{_bindir}/%{name}*
%{_datadir}/man/man1/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_sysconfdir}/bash_completion.d/%{name}
%{_sysconfdir}/%{name}.d
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/*/man1/%{name}*
%{_datadir}/pixmaps/%{name}
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.4
- Rebuilt for Fedora
* Sat Feb 09 2008 Mario Blättermann <rpm@mandrivauser.de> 1.3.3-1mud2008.0
- fork for mandrivauser.de, adjustments to mandriva rpm policy
- added german description
- added menu entry
* Tue Oct 23 2007 Pascal Bleser <guru@unixtech.be> 1.3.3-0.pm.2
- added Requires for imlib2-loaders (for PNG support)
* Fri Sep 28 2007 Pascal Bleser <guru@unixtech.be> 1.3.3-0.pm.1
- new upstream version
* Sun Sep 16 2007 Pascal Bleser <guru@unixtech.be> 1.3.2-0.pm.1
- new package
