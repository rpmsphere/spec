Summary:	Window Snipping Tool
Name:		ksnip
Version:	1.4.0
#Version:	1.5.0
Release:	1
License:	GPLv2
Group:		Graphics 
URL:		https://github.com/DamirPorobic/ksnip
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(xfixes)

%description
Screenshot tool inspired by Windows Snipping Tool and made with Qt4 for Linux.

%prep
%setup -q
sed -i 's|DESTINATION /bin|DESTINATION /usr/bin|' CMakeLists.txt

%build
%cmake
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Dec 20 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
* Wed Aug 16 2017 Rosa <rosa@abf.rosalinux.ru> 1.3.1-1
- (010e863) Automatic import for version 1.3.1-1
