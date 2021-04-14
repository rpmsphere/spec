%undefine _debugsource_packages

Name:           ypsilon
Version:        0.9.6.update3
Release:        7.1
Summary:        R6RS Scheme implementation with concurrent garbage collector
Group:          Development/Languages
License:        GPLv2 
URL:		    http://code.google.com/p/ypsilon
Source0: 	    http://ypsilon.googlecode.com/files/%{name}-%{version}.tar.gz
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
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6.update3
- Rebuilt for Fedora
