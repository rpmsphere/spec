%define theme_name Somatic

Summary: %{theme_name} icon theme
Name: somatic-icon-theme
Version: 0.2
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: ICON-%{theme_name}-%{version}.tar.gz
BuildArch: noarch

%description
%{theme_name} icon theme.

%prep
%setup -q -n %{theme_name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
