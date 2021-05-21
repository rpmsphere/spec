Name: uchardet
Summary: Universal charset detection
Version: 0.0.1
Release: 7.1
Group: Development/Tools
License: MPL 1.1
URL: http://code.google.com/p/uchardet/
Source0: http://uchardet.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: cmake

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package devel
Summary: Development files for uchardet
Requires: %{name}

%description devel
Header files and Libraries for the package uchardet.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuilt for Fedora
