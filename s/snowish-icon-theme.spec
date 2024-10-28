%define theme_name SnowIsh

Summary: %{theme_name} icon theme
Name: snowish-icon-theme
Version: 1.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: %{theme_name}-%{version}_PNG.tar.bz2
BuildArch: noarch

%description
%{theme_name} icon theme.

%prep
%setup -q -n %{theme_name}-%{version}_PNG

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
rm -rf index.theme~
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
