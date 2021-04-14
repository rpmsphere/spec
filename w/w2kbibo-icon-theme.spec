%define theme_name w2k-bibo

Summary: %{theme_name} icon theme
Name: w2kbibo-icon-theme
Version: 0.14
Release: 4.1
License: unknown
Group: User Interface/Desktops
URL: https://www.gnome-look.org/p/1011860/
Source: %{theme_name}.tar.gz
BuildArch: noarch

%description
Windoze 2000 Icon Theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Mon Sep 12 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14
- Rebuilt for Fedora
