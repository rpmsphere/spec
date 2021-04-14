%undefine _debugsource_packages

Name: crunch
Version: 3.6
Release: 7.1
Summary: Wordlist generator
License: GPL
Group: Security/Networking
URL: http://sourceforge.net/projects/crunch-wordlist/
Source: https://sourceforge.net/projects/crunch-wordlist/files/crunch-wordlist/%name-%version.tgz

%description
crunch is a wordlist generator where you can specify a standard character set or
a character set you specify. crunch can generate all possible combinations and
permutations.

%prep
%setup -q
sed -i 's|sudo ||' Makefile

%build
%make_build

%install
%make_install install \
    DESTDIR=%buildroot \
    INSTALL_OPTIONS= \
    DOCDIR=%_docdir/%name

%files
%{_docdir}/%name/COPYING
%{_bindir}/*
%{_datadir}/%name
%{_mandir}/man1/*

%changelog
* Fri Jun 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6
- Rebuilt for Fedora
* Fri Jun 20 2014 Afanasov Dmitry <ender@altlinux.org> 3.6-alt1
- first build
