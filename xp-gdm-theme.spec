%define theme_name XP

Summary: %{theme_name} theme for GDM
Name: xp-gdm-theme
Version: 1.0
Release: 3.1
License: GPL
Group: User Interface/Desktops
Source: %{theme_name}_Ubuntu.tar.gz
BuildArch: noarch

%description
Contains the %{theme_name} theme for GDM.

%prep
%setup -q -n %{theme_name}_Ubuntu

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gdm/themes/%{theme_name}
cp -a * %{buildroot}%{_datadir}/gdm/themes/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/gdm/themes/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
