%global debug_package %{nil}

Name:	altyo
Version: 0.4rc24
Release: 1.1
Summary: A Drop-down Terminal emulator
License: GPLv3
Group:  Terminals
URL:	https://github.com/linvinus/AltYo
Source0: AltYo-master.zip
BuildRequires: gtk3-devel
BuildRequires: vte291-devel
BuildRequires: vala-devel

%description
AltYo, written in Vala, depends only on libvte and gtk3.

%prep
%setup -q -n AltYo-master
#sed -i 's|(tct.bg.alpha)|tct.bg.alpha|' altyo_terminal.vala
#sed -i '2894s|%%d|%%u|' altyo_window.vala
#sed -i -e '968s|%%d|%%u|g' -e '1636s|%%d|%%u|g' altyo_settings.vala
#sed -i '/store.remove(iter);/d' altyo_settings.vala

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS README.md
%{_bindir}/%name
%{_datadir}/icons/hicolor/*/apps/%name.*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/applications/*.desktop

%changelog
* Fri Aug 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4rc24
- Rebuild for Fedora
* Sat Oct 19 2013 slick50 <lxgator at gmail.com> 0.3-1pclos2013
- Create pkg
