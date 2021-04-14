Name:           burg-themes
Version:        1.98.20100623
Release:        3.1
Summary:        Themes for BURG
Group:          System Environment/Base
License:        GPLv3+
URL:            http://code.google.com/p/burg/
# bzr branch lp:burg
Source0:        %{name}-%{version}.zip
BuildArch:      noarch
Requires:       burg

%description
This package contains fonts and common configuration script for all themes.

%prep
%setup -q -c

%build

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot/%{name}
cp -a * $RPM_BUILD_ROOT/boot/%{name}

%clean    
rm -rf $RPM_BUILD_ROOT

%files
/boot/%{name}/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.98.20100623
- Rebuilt for Fedora
