%define theme_name Blackbird

Summary: Dark Desktop Suite for Xfce
Name: blackbird-gnome-theme
Version: 0.4
Release: 10.1
License: GPLv2+, CC-BY-SA 3.0+
Group: User Interface/Desktops
Source0: %{theme_name}-%{version}.tar.gz
Source1: %{theme_name}-index.theme
URL: https://github.com/shimmerproject/Blackbird
BuildArch: noarch
Requires: awoken-icon-theme
Requires: shimmer-backgrounds

%description
Copyright 2012 Simon Steinbeiß and Satyajit Sahoo.

%prep
%setup -q -n %{theme_name}-%{version}
cp %{SOURCE1} index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
