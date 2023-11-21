%undefine _debugsource_packages
%undefine _auto_set_build_flags
%global __global_ldflags -Wl,-z,relro -lm -ldl

Summary: Palm Doc file format conversion
Summary(ru_RU.KOI8-R): Конвертор файлов в/из Palm Doc формат
Name: txt2pdbdoc
Version: 1.4.4
Release: 6.1
Source0: %{name}-%{version}.tar.gz
Source1: haodoo2html.sh
Group: Text tools
License: GPL
URL: https://homepage.mac.com/pauljlucas/software/txt2pdbdoc
Patch0: %{name}-%{version}-haodoo.patch

%description
Converts plain text files to/from the Doc format used by PalmPilots;
also utilities to convert HTML files to Doc and vice versa; There was
only one other such utility, unixdoc, out there and the code was
pretty crufty and not documented, so I cleaned it up, rewrote chunks
of it, and documented it.

%description -l ru_RU.KOI8-R
Конвертор текстовых файлов в/из Doc формат используемый на Palm.
Так же содержит утилиту для конвертации HTML в текст удобный
для чтения на Palm.

%prep
%setup -q
%patch0 -p1
cp INSTALL.README INSTALL
touch NEWS

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -Dm755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/haodoo2html

%files
%doc README INSTALL.README AUTHORS COPYING ChangeLog
%{_mandir}/man?/*
%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jul 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.4
- Rebuilt for Fedora
* Sat Nov 13 2004 Vasya Borisov <vasy@altlinux.ru> 1.4.4-alt1
- New version 1.4.4:
  - This version adds the -D option to suppress checking of a Doc file's
type/creator.
  - This version also fixes a small bug in printing an error message (it printed
the wrong file name).
  - Removed -b as a decode option from usage message.
* Thu May 20 2004 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt1
- Spec clean
* Fri Nov 14 2003 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt2
- Add russian description
* Fri Oct 03 2003 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt1
- Initial release for Sisyphus
