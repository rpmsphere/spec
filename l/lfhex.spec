%undefine _debugsource_packages

Name: lfhex
Summary: Large file hex editor
Version: 0.42
Release: 7.1
Group: Applications/Editors
License: GPL
URL: https://stoopidsimple.com/lfhex
Source0: https://stoopidsimple.com/files/%{name}-%{version}.tar.gz
BuildRequires: qt-devel

%description
lfhex is an application for viewing and editing files in hex, octal,
binary, or ascii text. The main strength of lfhex is its ability to
work with files much larger than system memory or address space.

%prep
%setup -q
sed -i '22i #include <sys/types.h>' src/expr.h
sed -i 's|/usr/local/bin|%{buildroot}/usr/bin|' src/%{name}.pro

%build
cd src
qmake-qt4
make ||:
sed -i -e 's|expr.tab.c|expr_yacc.cpp|' -e 's|expr.tab.h|expr_yacc.h|' expr_yacc.cpp
make

%install
cd src
%make_install

%files
%doc CONTRIBUTORS COPYING README
%{_bindir}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.42
- Rebuilt for Fedora
