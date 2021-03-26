Summary: 	A CLI system information tool written in BASH
Name:           neofetch
Version:        2.0.2
Release:        1
License: 	MIT
Group: 		Shells
URL:		https://github.com/dylanaraps/neofetch
Source0:	https://github.com/dylanaraps/neofetch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: 	noarch

%description
Neofetch displays information about your system next to an image, your OS logo,
or any ascii file of your choice. 

%prep
%setup -q

%build
%make_build

%install
%make_install

%files
%{_bindir}/neofetch
%{_mandir}/man1/neofetch.1.*
%{_datadir}/neofetch

%changelog
* Fri Jan 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.2
- Rebuild for Fedora
* Thu Dec 15 2016 Rosa <rosa@abf.rosalinux.ru> 2.0.2-1
- (1ada75e) Automatic import for version 2.0.2-1
