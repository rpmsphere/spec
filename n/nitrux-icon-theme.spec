%define theme_name NITRUX

Summary: %{theme_name} icon theme
Name: nitrux-icon-theme
Version: 3.0.5
Release: 3.1
License: CC BY-NC-ND 3.0
Group: User Interface/Desktops
URL: https://deviantn7k1.deviantart.com/art/Nitrux-OS-Icons-293634207
Source: nitrux.zip
BuildArch: noarch

%description
A collection of over 6,000 hand crafted, infinitely scalable vector icons.
Nitrux OS Icons are a Simple, Clean & minimal Icon set, these icons have
been all beautifully designed and are great when wanting a minimal look.
Using a minimalistic approach to designing these we avoid cluttered desktops.

%prep
%setup -q -c
cp %{theme_name}/COPYING %{theme_name}/CREDITS .
rm */COPYING */CREDITS */icon-theme.cache

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/icons

%files
%doc README-Icons COPYING CREDITS
%{_datadir}/icons/%{theme_name}*

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.5
- Rebuilt for Fedora
