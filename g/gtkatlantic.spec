Summary:	Monopoly-like game client
Name:		gtkatlantic
Version:	0.4.2
Release:	1
License:	GPL
Group:		Games/Strategy
URL:		https://gtkatlantic.gradator.net/
Source:		https://gtkatlantic.gradator.net/downloads/v0.4/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel

%description
monopd is a dedicated game server daemon for playing Monopoly-like board
games. Clients connect to the server and communicate using short commands
and XML messages.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=GtkAtlantic
Comment=Monopoly-like game client
Exec=%{name}
Terminal=false
Type=Application
Icon=/usr/share/gtkatlantic/icon32x32.xpm
Categories=Game;BoardGame;
EOF

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Thu Jun 18 2009 Kami <kami@ossii.com.tw> 0.4.2-2mdk
- Build for OSSII
* Sun Mar 19 2006 Guillaume Bedot <littletux@zarb.org> 0.4.2-2mdk
- fix buildrequires to use gtk2
* Sun Mar 19 2006 Guillaume Bedot <littletux@zarb.org> 0.4.2-1mdk
- 0.4.2
- fix source URL
- mkrel
* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.3.3-2mdk
- Fix BuildRequires
* Mon Jun 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.3-1mdk
- 0.3.3
* Wed Jun 09 2004 Abel Cheung <deaddog@deaddog.org> 0.3.2-1mdk
- First Mandrake package
