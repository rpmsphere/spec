%define theme_name LCARS-Desktop

Summary: LCARS-Desktop theme for gdm, gtk and metacity
Name: lcarsdesktop-gnome-theme
Version: 1.2
Release: 7.1
License: GPL
Group: User Interface/Desktops
Source: %{theme_name}-%{version}.zip
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/LCARS-Desktop?content=91988
Requires: starwars-cursor-theme

%description
A Star Trek themed desktop by Chris I-B. Based on LCARS by philten.

%prep
%setup -q -n %{theme_name}
sed -i '$a CursorTheme=StarWars' index.theme
sed -i 's|frame_geometry name="normal"|frame_geometry name="normal" rounded_top_left="true" rounded_top_right="true" rounded_bottom_left="true" rounded_bottom_right="true"|' metacity-1/metacity-theme-1.xml

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/themes
mv gdm $RPM_BUILD_ROOT%{_datadir}/gdm/themes/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/themes/LCARS-Desktop/scripts_and_configs/setbg-gnome.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/gdm/themes/%{theme_name}

%changelog
* Tue Feb 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuild for Fedora
