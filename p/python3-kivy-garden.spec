%define oname kivy-garden

Name: python3-kivy-garden
Version: 0.1.5
Release: 1
Summary: The kivy garden installation script
Group: Development/Python3
License: MIT License
URL: https://github.com/kivy-garden/garden
BuildArch: noarch
Source: https://github.com/kivy-garden/garden/archive/refs/tags/v%{version}.tar.gz#/garden-%version.tar.gz
BuildRequires: python3-devel

%description
The kivy garden installation script, split into its own package for convenient
use in buildozer.

%prep
%setup -q -n garden-%{version}

%build
%py3_build

%install
%py3_install
rm -v %buildroot%_bindir/garden.bat
mv %buildroot%_bindir/garden %buildroot%_bindir/%oname

%files
%doc README.md
%_bindir/kivy-garden
%python3_sitelib/garden
%python3_sitelib/*.egg-info

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuilt for Fedora
* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt2
- initial build for ALT Sisyphus
* Sat Apr 17 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.1.4-alt1
- new version (0.1.4) with rpmgs script
