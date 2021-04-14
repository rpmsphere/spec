%define theme_name Paranoid

Summary:        Paranoid GTK & Metacity theme
Name:           paranoid-theme
Version:        0.4
Release:        12.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://fedora-art.org/content/show.php/Paranoid?content=136003
Source0:        Paranoid 0.4.zip
Source1:        paranoid_naturalmystic.png
Requires:       gtk-murrine-engine, gtk-equinox-engine
BuildArch:      noarch
Requires:       xskhse-cursor-theme
Requires:       hilights-icon-theme

%description
A Gnome gtk2 Desktop Theme by monkeymagico.
Runs on Murrine, Equinox and Pixbuf Engines.
Color Changeable, Standard color screen 1.

%prep
%setup -q -n "%{theme_name} %{version}"
sed -i -e 's|%{theme_name} %{version}|%{theme_name}|' -e 's|AnyColorYouLike|Hi-Lights|' index.theme
sed -i 's|CursorTheme=default|CursorTheme=XSKHSE|' index.theme
sed -i 's|backgrounds|themes|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Jul 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
