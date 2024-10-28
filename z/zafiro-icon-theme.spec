%define theme_name Zafiro

Summary: %{theme_name} icon theme
Name: zafiro-icon-theme
Version: 1.1
Release: 1
License: GPLv3.0
Group: User Interface/Desktops
URL: https://github.com/zayronxio/Zafiro-icons
Source: %{URL}/archive/%{version}.tar.gz#/%{theme_name}-icons-%{version}.tar.gz
BuildArch: noarch

%description
Minimalist icons created with the flat-desing technique, utilizing washed out
colors and always accompanied by white. The priority is simplicity.

%prep
%setup -q -n %{theme_name}-icons-%{version}
sed -i 's|{theme_name}-icons|{theme_name}|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a */ index.theme $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%doc CREDITS LICENSE.md README.md
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Oct 22 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
