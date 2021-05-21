Summary: Portable command line archive file manager
Name: patool
Version: 1.8
Release: 4.1
Source0: http://cloud.github.com/downloads/wummel/patool/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Archiving/Compression
BuildArch: noarch
BuildRequires: python
URL: http://wummel.github.io/patool/

%description
Various archive types can be created, extracted, tested and listed by
patool. The advantage of patool is its simplicity in handling archive
files without having to remember a myriad of programs and options.

The archive format is determined by the file(1) program and as a
fallback by the archive file extension.

patool supports 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc),
ARJ (.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio),
DEB (.deb), DMS (.dms), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz),
LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), TAR (.tar),
XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo) formats. It relies on helper
applications to handle those archive formats (for example bzip2 for
BZIP2 archives).

The archive formats TAR (.tar), ZIP (.zip), BZIP2 (.bz2) and GZIP (.gz)
are supported natively and do not require helper applications to be
installed.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc doc/*.txt
%{_bindir}/patool
%{python_sitelib}/*
%{_mandir}/man1/patool.1.*

%changelog
* Thu Jul 23 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Sun Jan 13 2013 umeabot <umeabot> 0.16-4.mga3
+ Revision: 362462
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon May 28 2012 shlomif <shlomif> 0.16-3.mga3
+ Revision: 248717
- Fix the build with PYTHONDONTWRITEBYTECODE=1
- imported package patool
