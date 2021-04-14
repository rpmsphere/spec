%define theme_name AppleArt

Summary: %{theme_name} icon theme
Name: appleart-icon-theme
Version: 3.0.1
Release: 4.1
License: GPL
Group: User Interface/Desktops
URL: http://www.noobslab.com/2013/06/apple-art-icons-for-ubuntu.html
Source: %{theme_name}_%{version}.tar.gz
BuildArch: noarch

%description
AppleArt is an icon theme that contains a complete set of icons for GNOME.
All icons with high resolution 256x256 px are in SVG vector format.

%prep
%setup -q -n %{theme_name}
sed -i 's|Example=start-here|Example=folder|' index.theme
sed -i 's|\[en_GB\]||' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
