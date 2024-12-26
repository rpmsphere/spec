Name: jwasm
Version: 2.18
Release: 1
License: Sybase Open Watcom Public License
Summary: MASM-compatible assembler
URL: https://jwasm.github.io/
Group: Development/Languages
Source: JWasm-%{version}.tar.gz
Patch0: jwasm-undef.patch
Patch1: jwasm-bof.patch
BuildRequires: dos2unix unzip

%description
JWasm is a free MASM-compatible assembler with these features:

* native support for output formats Intel OMF, MS Coff (32/64-bit),
  Elf (32/64-bit), Binary, Windows PE (32/64-bit) and DOS MZ.
* Instructions up to AVX are supported.
* JWasm is written in C. The source is portable and has successfully been
  tested with Open Watcom, MS VC, GCC and more.
* C header files can be converted to include files for JWasm with h2incX.
* JWasm's source code is released under the Sybase Open Watcom Public License,
  which allows free commercial and non-commercial use.

JWasm started as a fork of Open Watcom's Wasm in March 2008. Today, the part of
Wasm source lines still contained in JWasm is approximately 0.2

%prep
%setup -q -n JWasm-%{version}
#patch0 -p1
#patch1 -p1
#sed -i '/instruction table/a#include "expreval.h"' H/parser.h

%build
dos2unix *.txt
%ifarch x86_64 aarch64
IS_64=-DLONG_IS_64BITS
%endif
#make DEBUG=1 extra_c_flags="%optflags -DDEBUG_OUT -fno-strict-aliasing $IS_64" -f GccUnix.mak GccUnixD GccUnixD/omfint.o
%make_build DEBUG=1 extra_c_flags="%optflags -DDEBUG_OUT $IS_64" -f GccUnix.mak

%install
install -D build/GccUnixD/jwasm %buildroot%_bindir/jwasm

%files
%doc *.txt *.md
%_bindir/%name

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.18
- Rebuilt for Fedora
* Wed Nov 30 2016 Fr. Br. George <george@altlinux.ru> 2.12-alt1
- Update to GH current version
- Copy Regression sources
* Wed Nov 30 2016 Fr. Br. George <george@altlinux.ru> 2.11-alt1
- Initial build from FC19
* Sat Nov 30 2013 conrad@quisquis.de
- Upgrade to upstream-2.11a
* Wed Apr 24 2013 conrad@quisquis.de
- Fixed x86_64 build
- Fixed debug packages
* Mon Apr 22 2013 conrad@quisquis.de
- Upgrade to upstream-2.10
* Fri Apr 19 2013 conrad@quisquis.de
- Fixed Group header
* Fri Apr 19 2013 conrad@quisquis.de
- Added bof patch
- Avoid strict-aliasing warning in one file
* Fri Apr 19 2013 conrad@quisquis.de
- Added undef patch
* Fri Apr 19 2013 conrad@quisquis.de
- Initial project creation
