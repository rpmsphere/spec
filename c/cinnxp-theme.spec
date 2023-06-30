%define theme_name CinnXP

Summary: CinnXP theme Suite
Name: cinnxp-theme
Version: 1.0.2
Release: 4.1
License: GPLv2+
Group: User Interface/Desktops
Source0: https://cinnamon-spices.linuxmint.com/uploads/themes/3FQH-80ZG-KNKW.zip
Source1: autumn-109.jpg
URL: https://cinnamon-spices.linuxmint.com/themes/view/498
BuildArch: noarch
Requires: w2kbibo-icon-theme

%description
CinnXP by petrucci4prez based from Mint-XP (fmcgorenc) and Adwaita,
make Cinnamon look and feel like the venerable Windows XP interface.
With background by:
Simon Goldin and Jakob Senneby, https://www.goldinsenneby.com/gs/

%prep
%setup -q -n pkg
sed -i -e 's|30|36|' -e 's|26|32|' usr/share/themes/%{theme_name}/metacity-1/metacity-theme-1.xml
sed -i -e 's|CursorTheme=default|IconTheme=w2k-bibo|' -e 's|IconTheme=CinnXP|CursorTheme=CinnXP|' usr/share/themes/%{theme_name}/index.theme
cp %{SOURCE1} usr/share/themes/%{theme_name}
echo BackgroundImage=/usr/share/themes/%{theme_name}/autumn-109.jpg >> usr/share/themes/%{theme_name}/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -a usr $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Apr 27 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
