%define theme_name StarTrek

Summary: %{theme_name} icon theme
Name: startrek-icon-theme
Version: 2011
Release: 3.1
License: freeware
Group: User Interface/Desktops
Source: %{theme_name}.tar.gz
BuildArch: noarch

%description
Star Trek icon theme.
https://iconfactory.com/startrek/
https://www.iconeasy.com/iconset/trek-insignia-icons/

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Tue Feb 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2011-1
- Rebuilt for Fedora
