Summary:        Math game, Multiplication Station will teach your child to add, subtract and multiply
Name:           multiplicationstation
Version:        0.6.5
Release:        1
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-0.6.5-fix-path.patch
URL:            https://new.asymptopia.org/staticpages/index.php/MultiplicationStation
License:        GPLv2+ 
Group:          Games/Boards
BuildRequires:  ImageMagick
Requires:   pygame
Requires:   python2-wxpython
BuildArch:  noarch
 
%description
Math game, Multiplication Station will teach your child to add, subtract and multiply

%prep
%setup -q -n %name
%patch0  -p0 -b .path_fix

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr Font %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/lib
cp -pr MultiplicationStation %{buildroot}%{_datadir}/%{name}/lib
cp .mstation_config_master  %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 mstation.py %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
convert -resize 48x48 mstation.ico %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
convert -resize 32x32 mstation.ico %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert -resize 16x16 mstation.ico %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=multiplicationstation
Comment=Math game will teach your child to add, subtract and multiply
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-admin.desktop << EOF
[Desktop Entry]
Name=multiplicationstation Admin
Comment=Math game will teach your child to add, subtract and multiply
Exec=%{name} -wx
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc INSTALL LICENSE README CHANGES
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop 
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Mar 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.5
- Rebuilt for Fedora
* Wed Apr 20 2011 anaselli <anaselli> 0.6.5-1.mga1
+ Revision: 89254
- imported package multiplicationstation
* Tue Apr 19 2011 Stefano Negro <stblack@gmail.com> 0.6.5-1.mga1.0
- created rpm
