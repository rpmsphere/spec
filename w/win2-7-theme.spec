Summary:        Windows 7 Transformation Pack
Name:           win2-7-theme
Version:        6.8.3
Release:        4.1
URL:            https://gnome-look.org/content/show.php/Win2-7+Pack?content=113264
License:        GPL
Group:          User Interface/Desktops
Source:         %{name}-%{version}.tar.gz
#Source:        Win2-7Pack_v6.8.3_Multilang_Aero_MD5_85061ac4b24868e9d1a33cf0d69ad34b.tar.lzma
BuildArch:      noarch

%description
Even from its start in late 2009 as an Gnome Icon pack, the Win2-7 Packs
goal has not changed...To be the most comprehensive, easily installable,
customizable and most user friendly Windows 7 Transformation Pack on earth
for the Gnome Desktop! :D

%prep
%setup -q
sed -i '/Font/d' themes/*/index.theme

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
cp -a backgrounds fonts icons sounds themes $RPM_BUILD_ROOT%{_datadir}
echo BackgroundImage=/usr/share/backgrounds/Win2-7/Win2-7Pixmap.jpg >> $RPM_BUILD_ROOT%{_datadir}/themes/Win2-7Classic/index.theme
echo BackgroundImage=/usr/share/backgrounds/Win2-7/Win2-7Reflect.png >> $RPM_BUILD_ROOT%{_datadir}/themes/Win2-7Darth-Vader/index.theme

%files
%doc *.txt
%{_datadir}/*/*

%changelog
* Tue Feb 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 6.8.3
- Rebuilt for Fedora
* Mon Jan 31 2011 Lawrence Rogers <lrr@cert.org>
- based on Win2-7Pack_v6.2_Multilang_Aero_MD5_40d356e31af6a09e67800c7775fb7eff.tar.lzma
