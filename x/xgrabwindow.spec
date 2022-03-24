Name: xgrabwindow
Version: 1.2.5
Release: 1
License: GPLV2
Summary: Window Information Summary
Group: User Interface/X
Source: %{name}-%{version}.tar.gz

%description
Get X properties of a given window.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DUSE_QT5=1 .
make -j4

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL
%{_bindir}/xgrabwindow

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.5
- Rebuilt for Fedora
