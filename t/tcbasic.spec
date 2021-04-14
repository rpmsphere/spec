Summary: A small BASIC Interpreter written in C
Name: tcbasic
Version: 2.2.0
Release: 2.1
License: GPLv3
Group: Development/Languages
Source: https://github.com/tcort/tcbasic/releases/download/v%{version}/tcbasic-%{version}.tar.gz
URL: https://github.com/tcort/tcbasic/

%description
The interpreter implements the Tiny BASIC dialect of BASIC with added
support for floating point numbers and many of the built-in mathematical
functions in Dartmouth BASIC.

%prep
%setup -q

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%doc AUTHORS CONTRIBUTING.md COPYING HACKING.md README.md
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.*

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
