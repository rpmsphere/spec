Name: shc
Version: 3.9.6
Release: 4.1
Summary: Generic shell script compiler
License: GPLv2
Group: Development/Other
URL: https://github.com/neurobin/shc
Source0: %name-%version.tar.gz

%description
A generic shell script compiler. shc takes a script, which is
specified on the command line and produces C source code. The
generated source code is then compiled and linked to produce a
stripped binary executable. Use with care.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%files
%_bindir/*
%doc AUTHORS ChangeLog COPYING README NEWS
%_mandir/man?/*

%changelog
* Sun Oct 22 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9.6
- Rebuilt for Fedora
* Thu Mar 11 2014 Ilya Mashkin <oddity@altlinux.ru> 3.8.9-alt1
- 3.8.9 (Closes: #25694)
* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 3.8.6-alt1
- 3.8.6
* Mon Jul 18 2005 Alex Yustasov <yust@altlinux.ru> 3.8.3-alt1
- 3.8.3
* Wed Jan 26 2005 Alex Yustasov <yust@altlinux.ru> 3.7-alt1
- initial release
