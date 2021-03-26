Name:           ucg
Version:        0.3.3git
Release:        1
Summary:        An extremely fast grep-like tool specialized for searching large bodies of code
Group:          Development/Tools
License:        GPLv3+
URL:            https://github.com/gvansickle/ucg
Source0:        ucg-master.zip
#Source0:        https://github.com/gvansickle/ucg/releases/download/%{version}/universalcodegrep-%{version}.tar.gz
BuildRequires:  pkgconfig(libpcre)

%description
UniversalCodeGrep (ucg) is an extremely fast grep-like tool specialized for
searching large bodies of source code. It is intended to be largely
command-line compatible with Ack, to some extent with ag, and where appropriate
with grep. Search patterns are specified as PCRE regexes.

ucg is intended to address the impatient programmer's code searching needs. ucg
is written in C++11 and takes advantage of the concurrency (and other) support
of the language to increase scanning speed while reducing reliance on
third-party libraries and increasing portability. Regex scanning is provided by
the PCRE library, with its JIT compilation feature providing a huge performance
gain on most platforms.

As a consequence of its use of these facilities and its overall design for
maximum concurrency and speed, ucg is extremely fast; up to 30x faster than Ack
in some cases.

%prep
%setup -q -n ucg-master

%build
autoreconf -ifv
%configure
%make_build

%install
%make_install

%files
%doc README.md NEWS.md AUTHORS
%license COPYING
%exclude /usr/share/doc/universalcodegrep
%{_bindir}/*
%{_mandir}/man1/ucg.1.*

%changelog
* Wed Apr 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3git
- Rebuild for Fedora
* Sun Sep 23 2018 umeabot <umeabot> 0.2.1-2.mga7
  (not released yet)
+ Revision: 1301527
- Mageia 7 Mass Rebuild
* Wed Apr 06 2016 shlomif <shlomif> 0.2.1-1.mga6
+ Revision: 999025
- Some cleanups to the .spec.
- Importing universalcodegrep
* Mon Feb 08 2016 Gary R. Van Sickle <grvs@users.sourceforge.net> 0.2.1
- Updated Version: for upstream version 0.2.1.
- Added NEWS.md to doc section.
* Thu Dec 31 2015 Gary R. Van Sickle <grvs@users.sourceforge.net> 0.2.0
- Initial version of the package.
