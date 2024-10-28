Name: taskbar
Version: 2.6.1
Release: 1
License: GPLV2
Summary: Transparent taskbar
Group: User Interface/X
Source: %{name}-%{version}.tar.gz

%description
Transparent taskbar for quick access to applications.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DUSE_QT5=1 .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING INSTALL
%{_bindir}/taskbar

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.1
- Rebuilt for Fedora
