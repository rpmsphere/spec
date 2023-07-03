Name: nuages
Summary: A tool for 3D reconstruction from parallel cross-sections
Version: 4.1
Release: 4.1
Group: Applications/Engineering
License: shareware
URL: https://www.inria.fr/centre/sophia/
Source0: %{name}-%{version}.tar.gz

%description
The nuages package contains a tool for extracting contours
from images. The input format is a simple ascii file (see man
prepros for a format description). Several contour sets can be
found on this server (ftp-sop.inria.fr) in prisme/NUAGES/Contours.
There is also a conversion tool that can read the contour format
used at NASA.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS+=-Wno-format-security

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYRIGHT README
%{_bindir}/*
%{_libdir}/lib*.a
%{_mandir}/man1/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1
- Rebuilt for Fedora
