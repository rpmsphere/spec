%undefine _debugsource_packages

Name:           ypsilon
Version:        0.9.6.update3
Release:        7.1
Summary:        R6RS Scheme implementation with concurrent garbage collector
Group:          Development/Languages
License:        GPLv2 
URL:		    https://code.google.com/p/ypsilon
Source0: 	    https://ypsilon.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
Ypsilon is an implementation of the Scheme programming language which conforms
to the latest standard R6RS. It achieves a remarkably short garbage collection
pause time and improved performance during parallel execution because it
implements mostly concurrent garbage collection, which is optimized for the
multi-core CPU system.

It implements the full features of R6RS and the R6RS standard libraries. It
also features a built-in foreign function interface for integration with C,
while maintaining a small package footprint.
 
%prep
%setup -q
%ifarch aarch64
sed -i 's|x86_64|aarch64|' src/sysdep.h
sed -i -e 's|-msse2 -mfpmath=sse||' -e 's|-m32||' -e 's|-march=i686|-march=native|' Makefile
%endif

%build
make PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc license.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/%{name}.*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6.update3
- Rebuilt for Fedora
