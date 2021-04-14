%define theme_name    Rosa

Summary:	%{theme_name} icon theme
Name:		rosa-icon-theme
Version:	1.1.7
Release:	3.1
Source0:	rosa-icons-devel-v%{version}.tar.gz
License:	GPLv2
URL:		www.rosalinux.com
Group:		Graphical desktop/Other
BuildArch:	noarch
Requires:	gnome-icon-theme

%description
ROSA icon theme is high quality icon theme for KDE, GNOME and Xfce.
It is part of ROSA theme pack - theme for ROSA Desktop distro.
Initially based on the original icon theme Elementary by Daniel Fore
(Dan Rabbit).

%prep
%setup -q -n rosa-icons-devel-v%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%post
gtk-update-icon-cache --quiet %{_datadir}/icons/%{theme_name} || :

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.7
- Rebuilt for Fedora
* Sun Aug 26 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 1.0.27-2.res6
- add missing dist to release
* Tue Jul 10 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> - 1.0.27-1
- initial package
