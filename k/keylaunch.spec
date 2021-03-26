Name: keylaunch
Version: 1.3.9
Release: 2.1
Summary: Small utility for binding commands to a hot key
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source: %{name}_%version.tar.bz2
BuildRequires: libSM-devel libX11-devel dos2unix

%description
keylaunch is a small utility for binding commands to a hot key.

%prep
%setup -q
dos2unix README

%build
%configure --with-x
make

%install
make DESTDIR=%buildroot install
rm -rf %buildroot%_docdir/%name
gzip --best --stdout -- debian/changelog > changelog.gz

%files
%doc README docs/example_rc changelog.*
%_bindir/*
%_mandir/man1/*

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.9
- Rebuild for Fedora
* Tue Sep 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.9-alt1
- Version 1.3.9
* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.3-alt1.qa1
- NMU: rebuilt for updated dependencies.
* Fri Jun 16 2006 Led <led@altlinux.ru> 1.3.3-alt1
- initial build
