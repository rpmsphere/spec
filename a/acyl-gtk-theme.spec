%define theme_name ACYL

Summary:        Any Color You Like GTK theme
Name:           acyl-gtk-theme
Version:        0.4
Release:        7.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/1078547/
Source0:        https://dl.opendesktop.org/api/files/download/id/1460966595/101017-ACYL_gtk_0.4.tar.bz2
Source1:        %{theme_name}-index.theme
Source2:        https://www.wallpapersonly.net/wallpapers/any-colour-you-like-1920x1080.jpg
BuildArch:      noarch
Requires:       acyl-metacity-theme
Requires:       acyls-icon-theme

%description
The purpose of this gtk theme was to create something minimalistic that also
follows the gnome color settings. It uses the murrine, industrial and hc engine.
All of them comes pre installed in at least Ubuntu, probably in many other
distributions too.

%prep
%setup -q -n %{theme_name}_gtk_%{version}
cp %{SOURCE1} index.theme
cp %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
