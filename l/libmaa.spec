Name: libmaa
Version: 1.3.2
Release: 5.1
Summary: Software for RFC 2229
License: GPLv2, LGPLv2
Group: System/Libraries
URL: http://sourceforge.net/projects/dict/
Source: %name-%version.tar

%description
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol.

%package devel
Summary: Development files of libmaa
Group: Development/C
Requires: %name = %version-%release

%description devel
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

This package contains development files of libmaa.

%package doc
Summary: Documentation for libmaa
Group: Development/Documentation
BuildArch: noarch

%description doc
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

This package contains development documentation for libmaa.

%prep
%setup -q

%build
autoreconf
export CFLAGS="%{optflags} -Wno-error"
%configure
make

%install
%makeinstall
install -d %buildroot%_docdir/%name
install -p -m644 doc/*.ps %buildroot%_docdir/%name

%files
%doc COPYING* ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%exclude %_libdir/*.a
%exclude %_libdir/*.la

%files doc
%_docdir/%name

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.2
- Rebuilt for Fedora
* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2
* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- NMU: 1.3.1 (gcc-4.6 ready)
* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0
- Disabled devel-static package
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt for debuginfo
* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for soname set-versions
* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
