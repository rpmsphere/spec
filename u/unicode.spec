Name: unicode
Version: 2.1
Release: 5.1
Summary: Display unicode character properties
License: GPLv3
Group: Text tools
BuildArch: noarch
URL: http://kassiopeia.juls.savba.sk/~garabik/software/unicode/
Source0: http://kassiopeia.juls.savba.sk/~garabik/software/unicode/%{name}_%{version}.tar.gz

%description
unicode is a simple command line utility that displays
properties for a given unicode character, or searches
unicode database for a given name.

%prep
%setup -q -n %{name}

%install
mkdir -p %buildroot{%_bindir,%_mandir/man1}
install -p -m755 unicode paracode %buildroot%_bindir
install -p -m644 unicode.1 paracode.1 %buildroot%_mandir/man1

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%_bindir/*
%_mandir/man1/*
%doc README* COPYING changelog

%changelog
* Fri Feb 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.4-alt1.1
- Rebuild with Python-2.7
* Sat Mar 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.4-alt1
- 0.9.4
* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.1
- Rebuilt with python 2.6
* Wed Jul 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.2-alt1
- initial build
