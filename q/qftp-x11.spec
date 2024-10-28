%global _name qftp

Name: qftp-x11
Version: 1.5.10
Release: 1
License: GPLV2
Summary: A user interface for Ftp file transfer
Group: User Interface/X
URL: https://hugo.pereira.free.fr/software/index.php?page=package&package_list=software_list_qt&package=qftp
Source: https://hugo.pereira.free.fr/software/tgz/%{_name}-%{version}.tar.gz
BuildRequires: qt5-qtbase-devel

%description
It provides the functionalities of a basic file manager, both on the local and
on the remote side, as well as file transfer using either clipboard(copy/paste)
or drag-and-drop. It stores multiple login informations for future re-use and
also offer the unsecure possibility to store connection password.

%prep
%setup -q -n %{_name}-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DUSE_QT5=1 .
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install
mv %{buildroot}%{_bindir}/%{_name} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING INSTALL
%{_bindir}/%{name}

%changelog
* Fri Dec 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.10
- Rebuilt for Fedora
