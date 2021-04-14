%undefine _debugsource_packages

Name:         hexdumpu
Summary:      Hex Dump Utility
URL:          http://www.catb.org/~esr/hexdump/
Group:        Filesystem
License:      BSD
Version:      1.8
Release:      4.1
Source0:      http://www.catb.org/~esr/hexdump/hexdump-%{version}.tar.gz

%description
This program provides a facility for obtaining a dump of a binary
file to stdout. The default format is a CP/M style haxadecimal dump
with byte offset in file, 16 bytes of hex and 16 bytes of alpha
representation with '.' for non-printables per line. If no filename
is given, hexdump reads from standard input.

%prep
%setup -q -n hexdump-%{version}

%build
%{__make} %{_smp_mflags}

%install
install -D -m 755 \
    hexdump $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 \
    hexdump.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
