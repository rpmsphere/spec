%define theme_name Baku

Summary: %{theme_name} icon theme
Name: baku-icon-theme
Version: 0.2
Release: 5.1
License: GPL
Group: User Interface/Desktops
URL: http://robrene.deviantart.com/art/Baku-icon-theme-145678957
Source: http://www.deviantart.com/download/145678957/Baku_icon_theme_by_robrene.zip
BuildArch: noarch

%description
It is the collection of all my favourite tango-styled icons, made into a theme
so you can enjoy it too! It holds many icons not seen in any other icon-theme
so far! I merely collected a lot of icons and packaged them for your pleasure.
I also tweaked already existing icons by other artists to fit in this theme.

Picon is a little graphical tool I wrote that allows you to change the folder
icon set and the branding of your theme really easily.

%prep
%setup -q -c
tar xf Baku.tar.gz
sed -i 's|Example=start-here|Example=folder|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a 8x8 16x16 22x22 24x24 32x32 scalable picon index.theme picon.py $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/picon << EOF
#!/bin/bash
cd %{_datadir}/icons/%{theme_name}
exec python2 picon.py
EOF

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/icons/Baku/picon.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README CHANGELOG
%attr(755,root,root) %{_bindir}/picon
%{_datadir}/icons/%{theme_name}*

%changelog
* Sat Apr 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
