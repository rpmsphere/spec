Summary: Ice Window Manager Themes
Name: icewm-themes-addons
Version: 1.2.26
BuildArch: noarch
Release: 6
License: LGPL
Group: X11/Window Managers
Source: icewm-themes_%version.orig.tar.gz
URL: https://packages.qa.debian.org/i/icewm-themes.html
Requires: icewm

%description
This package contains the contributed theme files for icewm. It contains nice
looking themes, emulating the look of Windows'95, OS/2 Warp 3, or produced by
phantasy of various people.

%prep
%setup -q -n icewm-themes-%version

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icewm/themes
cp -a * $RPM_BUILD_ROOT%{_datadir}/icewm/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icewm/themes/*

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.26
- Rebuilt for Fedora
