%define theme_name Fitts-Natural

Summary: %{theme_name} metacity theme
Name: fitts-natural-metacity-theme
Version: 0.3
Release: 2.1
License: CC by-nc-sa
Group: User Interface/Desktops
Source: Fitts-Natural.tar.gz
URL: https://gnome-look.org/content/show.php/Fitts?content=139285
BuildArch: noarch

%description
A theme inspired by:
https://gnome-look.org/content/show.php/Natural+metacity+-+Mockup.?content=120245
This Metacity theme tries to use "big" buttons to make it easy to click on them.

%prep
%setup -q -n %{theme_name}

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
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
