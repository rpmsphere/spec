Name:           wbarconf
Version:        0.7.2.1
Release:        1
Summary:        Configuration tool for wbar
Source0:        https://www.ihku.biz/wbarconf/%{name}-%{version}.tar.gz
Source1:        %{name}-0.7.2.zh_TW.po
URL:            https://kapsi.fi/~ighea/wbarconf/
Group:          Graphical desktop/Other
License:        GPL
BuildArch:      noarch
BuildRequires:  gettext
Requires:       wbar
Requires:       pygtk2

%description
wbar configuration gui written with Python and GTK+.

%description -l de
Wbar-Konfigurationsprogramm, geschrieben in Python und GTK+. 

%prep
%setup -q -n %{name}
sed -i 's/Utility/Settings;DesktopSettings/' %{name}.desktop
mkdir -p locale/zh_TW/LC_MESSAGES
msgfmt %{SOURCE1} -o locale/zh_TW/LC_MESSAGES/%{name}.mo

%install
rm -rf %{buildroot}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 locale/de/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo 
install -Dm644 locale/fi/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
install -Dm644 locale/zh_TW/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo
mkdir -p %{buildroot}%{_datadir}/wbar/iconpack/wbar.osx   
cp wbarbacks/* %{buildroot}%{_datadir}/wbar/iconpack/wbar.osx/
install -Dm644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/wbar
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2.1
- Rebuilt for Fedora
* Sun Jun 01 2008 Mario Blättermann <rpm@mandrivauser.de> 0.7.2-1mud2008.1
- update to 0.7.2
- package group changed
* Sat May 17 2008 Mario Blättermann <rpm@mandrivauser.de> 0.7.1-1mud2008.1
- update to 0.7.1
* Fri May 09 2008 Mario Blättermann <rpm@mandrivauser.de> 0.7.0-1mud2008.1
- update to 0.7.0
- extra german translation
* Sat Apr 26 2008 Mario Blättermann <rpm@mandrivauser.de> 0.6.5.1-1mud2008.1
- initial version
