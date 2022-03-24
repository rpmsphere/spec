Name: xgrabcolor
Version: 1.4.6
Release: 1
License: GPLV2
Summary: Color Picker
Group: User Interface/X
Source: %{name}-%{version}.tar.gz

%description
Basic color picker.

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
%{_bindir}/xgrabcolor

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.6
- Rebuilt for Fedora
