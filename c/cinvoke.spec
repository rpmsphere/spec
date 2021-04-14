%undefine _debugsource_packages

Name:         cinvoke
Summary:      Foreign Function Call Library
URL:          http://www.nongnu.org/cinvoke/
Group:        Compiler
License:      MIT-style
Version:      1.0
Release:      20080111.1
Source0:      http://download.savannah.nongnu.org/releases/cinvoke/cinvoke-%{version}.tgz
Patch:        cinvoke.patch
BuildRequires: perl

%description
C/Invoke is a library for connecting to C libraries at runtime.
This differs from the typical method of interfacing with C, which
involves writing static definitions which are then compiled to a
machine-dependant format. C/Invoke provides a runtime facility to
build descriptions of C functions and to call them, passing them
appropriate data and retrieving results. C/Invoke provides a central
repository of code to handle the platform-dependant details of
marshaling C parameters and return values.

%prep
%setup -q
%patch -p0

%build
perl ./configure.pl --prefix=%{_prefix}
%{__make} %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_includedir} \
    $RPM_BUILD_ROOT%{_libdir}
install -c -m 644 \
    lib/cinvoke.h lib/cinvoke-arch.h lib/cinvoke-archspec.h \
    $RPM_BUILD_ROOT%{_includedir}
install -c -m 644 \
    lib/libcinvoke.a \
    $RPM_BUILD_ROOT%{_libdir}

%files
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
