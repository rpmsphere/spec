Name: gits-icewm-theme
Version: 0.2
Release: 2.1
License: GPL
Group: Graphical desktop/Icewm
URL: http://www.crash-override.net
Summary: Ghost in the Shell Theme for IceWM
BuildArch: noarch
Requires: icewm
Source: icewm_gits-0.2.tar.gz

%description
IceWM Theme inspired by Masamune Shirow's Ghost in the Shell.

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot%_datadir/icewm/themes
cp -a * %buildroot%_datadir/icewm/themes/GITS

%files
%_datadir/icewm/themes/GITS

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Fri Aug 15 2008 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt1
- Initial build for ALT Linux Sisyphus
