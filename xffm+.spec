Name:  xffm+
Summary: Next generation from Rodent Apps
Version: 0.94
Release: 1
License: GPLv3+
URL: http://xffm.org/
Source0: https://sourceforge.net/projects/xffm/files/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gtk3-devel
BuildRequires: file-devel
BuildRequires: libSM-devel
#Obsoletes: rodent

%description
Xffm+ is a gtk3 advanced filemanager or it is really a graphic shell.
History of xffm:
* xftree, gtk1.x
* xffm gtk2.x
* rodent gtk2.24-3.10
* xffm+ gtk3.24

%prep
%setup -q -n %{name}-%{version}
sed -i 's|/usr/local|/usr|' CMakeLists.txt
sed -i 's|LOCALE_INSTALL_DIR "|LOCALE_INSTALL_DIR "%{buildroot}|' cmake/msgfmt.cmake

%build
%cmake .
make

%install
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -P cmake_install.cmake
mv %{buildroot}%{_bindir}/xffm %{buildroot}%{_bindir}/xffm+

%files
%doc README ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/%{name}/*/*
%{_datadir}/xml/%{name}/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
   
%changelog
* Fri Jan 10 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94
- Rebuild for Fedora
