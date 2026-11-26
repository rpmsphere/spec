%undefine _debugsource_packages

Name: s3d
Summary: 3d network display server
Version: 0.2.2.1
Release: 1
Group: net
License: Free Software
URL: https://s3d.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRequires: libg3d-devel
#Requires: libgl1-mesa-glx
#Requires: |
#Requires: libgl1,
#Requires: libsdl1.2debian

%description
s3d is a 3d network display server which can be used as 3d desktop environment.
This package provides the display server.

%package devel
Summary: Development files for s3d

%description devel
s3d is a 3d network display server which can be used as 3d desktop environment.
This package provides the development files.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%files
%{_sysconfdir}/%{name}rc
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/lib%{name}*.so.*
%{_datadir}/%{name}

%files devel
%{_docdir}/%{name}
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/lib%{name}*.pc
%{_mandir}/man3/*.3*
%{_mandir}/man9/*.9*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2.1
- Rebuilt for Fedora
