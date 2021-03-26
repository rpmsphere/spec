%define theme_name Orion

Summary: Orion GNOME theme
Name: orion-gnome-theme
Version: 1.5
Release: 11.1
License: GPLv3
Group: User Interface/Desktops
Source0: %{theme_name}-%{version}.tar.gz
Source1: 836.jpg
URL: https://github.com/shimmerproject/Orion
BuildArch: noarch
Requires: gtk-murrine-engine
Requires: dmz-cursor-themes
Requires: squarebeam-icon-theme

%description
Orion is a modern light theme for Gnome. It supports Gnome, Unity, XFCE
and Openbox. The theme is compatible with GTK 3.6 and 3.8. It also includes
a GTK 2.0 theme using Murrine engine.

%prep
%setup -q -n %{theme_name}-%{version}
sed -i -e 's|DMZ-Black|dmz-aa|' -e '10i IconTheme=Square-Beam' index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/836.jpg' index.theme
sed -i 's|gtk:custom(wm_.*,\(.*\))|\1|' metacity-1/metacity-theme-2.xml

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
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora
