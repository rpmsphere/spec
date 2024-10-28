%define theme_name ACYL

Summary: Any Color You Like metacity theme
Name: acyl-metacity-theme
Version: 0.3
Release: 3.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460749717/101067-ACYL_Metacity.tar.bz2
URL: https://www.gnome-look.org/p/1007300/
BuildArch: noarch

%description
A minimalistic metacity theme that follows the gnome color settings.
I used the simple-slim theme as base.

%prep
%setup -q -c
tar xf %{theme_name}_Metacity_%{version}.tar.bz2

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/metacity-1
cp ACYL_Metacity_0.3_Borders/metacity-1/metacity-theme-1.xml $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/metacity-1

%files
%{_datadir}/themes/%{theme_name}/metacity-1/metacity-theme-1.xml

%changelog
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
