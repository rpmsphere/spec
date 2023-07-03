Summary: Command-line tools for extracting data for XCF files
Name: xcftools
Version: 1.0.8.20130212
Release: 1
License: GPL
Group: Applications
Source0: https://freeheimdall.spdns.org/files/%{name}-%{version}.tar.gz
URL: https://henning.makholm.net/software
BuildRequires: cmake
BuildRequires: libpng-devel

%description
Xcftools is a set of fast command-line tools for extracting information from
the Gimp's native file format XCF. The tools are designed to allow efficient
use of layered XCF files as sources in a build system that use 'make' and
similar tools to manage automatic processing of the graphics.

%prep
%setup -q
sed -i -e 's|png_voidp_NULL|NULL|' -e 's|png_error_ptr_NULL|NULL|' src/xcf2png.c
rename 10 1 *.10

%build
cmake .
make

%install
install -d %{buildroot}%{_bindir}
install -m755 xcfview bin/* %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m644 *.1 %{buildroot}%{_mandir}/man1

%files
%doc ChangeLog README TRANSLATION
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Sun Jan 01 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8.20130212
- Rebuilt for Fedora
