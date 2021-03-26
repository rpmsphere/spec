%define theme_name AnyColorYouLike

Summary:        Any Color You Like icon theme
Name:           acyl-icon-theme
Version:        0.9.4
Release:        4.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Any+Color+You+Like?content=102435
Source0:        ACYL_Icon_Theme_%{version}.tar.bz2
BuildArch:      noarch

%description
Another release of the acyl icons! YAY! The cli interface is now totally
dropped so if you cant live without it you should refrain from uppgrading.

%package -n acyl
Summary: Config tool for the Any Color You Like icon theme
Requires: %{name}

%description -n acyl
Config tool for the Any Color You Like icon theme.

%prep
%setup -q -n ACYL_Icon_Theme_%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/acyl << EOF
#!/bin/bash
cd %{_datadir}/acyl
./script_gui.py
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/acyl
mkdir -p $RPM_BUILD_ROOT%{_datadir}/acyl
sed -i 's|#! usr|#!/usr|' scalable/scripts/current_state/current_version
cp -a scalable/scripts/* $RPM_BUILD_ROOT%{_datadir}/acyl
sed -i 's|Settings;|Settings;DesktopSettings;|' scalable/other/acyl.desktop
install -Dm644 scalable/other/acyl.desktop $RPM_BUILD_ROOT%{_datadir}/applications/acyl.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
rm -rf scalable/other scalable/scripts
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' $RPM_BUILD_ROOT%{_datadir}/acyl/script_pycolor
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' $RPM_BUILD_ROOT%{_datadir}/acyl/script_gui.py

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%files -n acyl
%{_bindir}/acyl
%{_datadir}/acyl
%{_datadir}/applications/acyl.desktop

%changelog
* Tue Oct 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
