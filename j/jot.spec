%undefine _debugsource_packages

Name: jot
Version: 11.1
Release: 5.1
Source: %{name}-%{version}.tar
Patch0: %name-urandom.patch
URL: https://www.freebsd.org/cgi/cvsweb.cgi/src/usr.bin/jot
Summary: A simple tool that prints random or sequential data
Summary(ru_RU.UTF-8): Выводит данные по возрастанию, убыванию по одному элементу на строку
License: BSD
Group: Text tools

%description
Jot prints numbers, in arithmetic sequence or according to some simple
random generators.

%description -l ru_RU.UTF-8
Athena jot (или просто jot) выводит данные, обычно числа, по
возрастанию, убыванию, произвольные или повторяющиеся, по одному
элементу на строку.

%prep
%setup -q
%patch 0 -p1
sed -i -e 's|strlcpy|strncpy|' -e 's|strlcat|strncat|' jot.c

%build
#cc -D'__FBSDID(x)=' -D'arc4random()=random()' -O2 %name.c -o %name
cc -D'__FBSDID(x)=' -O2 %name.c -o %name

%install
mkdir -p %buildroot%_bindir %buildroot%_mandir/man1
install -m755 %name %buildroot%_bindir/
install %name.1 %buildroot%_mandir/man1

%files
%_bindir/%name
%_mandir/man1/%name.*

%changelog
* Fri Apr 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 11.1
- Rebuilt for Fedora
* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 10.2-alt1
- Autobuild version bump to 10.2
* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 10.1-alt1
- Autobuild version bump to 10.1
* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 10.0-alt1
- Autobuild version bump to 10.0
* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 9.2-alt1
- Autobuild version bump to 9.2
- Switch to RELENG regular update
* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.43-alt1
- Autobuild version bump to 1.43 (no code changed, just version up)
- Recode spec from koi8-r to utf8
* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 1.42-alt2
- Using autobuild scheme
* Tue May 10 2011 Fr. Br. George <george@altlinux.ru> 1.42-alt1
- Version up
* Sun Sep 05 2010 Fr. Br. George <george@altlinux.ru> 1.41-alt1
- Version up
* Thu Nov 08 2007 Fr. Br. George <george@altlinux.ru> 1.37-alt1
- Initial build for ALT
