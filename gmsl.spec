Name: gmsl
Version: 1.1.8
Release: 1
Summary: GNU Make Standard Library
License: BSD
Group: Development/Tools
URL: https://gmsl.sourceforge.io/
Source: https://sourceforge.net/projects/gmsl/files/GNU%20Make%20Standard%20Library/v%version/%name-%version.tar.gz
BuildArch: noarch
Requires: make

%description
The GNU Make Standard Library (GMSL) is a collection of functions implemented
using native GNU Make functionality that provide list and string manipulation,
integer arithmetic, associative arrays, stacks, and debugging facilities.

%prep
%setup -q -c

%install
install -d %buildroot%_includedir
install -p -m644 gmsl __gmsl %buildroot%_includedir

%files
%doc README *.html gmsl-tests
%_includedir/*

%changelog
* Tue Sep 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.8
- Rebuild for Fedora
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1
- Initial build for Sisyphus
