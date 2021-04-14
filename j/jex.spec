Summary: The programmer's editor
Name: jex
Version: 2.0
Release: 4.1
License: GPL
Source : http://users.telenet.be/jbosman/jex2.tgz
Group: X11/Utilities
URL: http://users.telenet.be/jbosman/applications.html
BuildRequires: motif-devel

%description
Jex is the ultimate programmer's editor for Unix. Version 2 of jex,
With a lot of new features, one of them is syntaxhighlighting.

%prep
%setup -q -n jex2
sed -i '1i #include <errno.h>' debug/dbgfunc.c

%build
make

%install
install -Dm755 jex2 %{buildroot}%{_bindir}/jex

%files
%doc TODO
%{_bindir}/jex

%changelog
* Wed Jun 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Sat Mar 20 1999 Joris Struyve 1.3.7
- Initial package
