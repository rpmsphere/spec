Name: libb64
Version: 1.2.1
Release: 9.1
Summary: Base64 Encoding/Decoding Routines
License: Public-Domain
Group: System/Libraries
URL: http://libb64.sourceforge.net/
Source0: https://downloads.sourceforge.net/project/%name/%name/%name/%name-%version.zip
# PATCH-FIX-UPSTREAM do respect cflags and some other bugfixes from debian
Patch0: bufsiz-as-buffer-size.diff
Patch1: initialize-coder-state.diff
Patch2: integer-overflows.diff
Patch3: no-hardcoded-lib-path.diff
Patch4: override-cflags.diff
Patch5: static-chars-per-line.diff
# PATCH-FIX-UPSTREAM do not add Werror as it is prone to break
Patch6: disable-werror.diff
BuildRequires: gcc-c++

%description
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package devel
Summary: A library for working with base64 encoding/decoding
Group: Development/C
Requires: %name = %version-%release

%description devel
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CFLAGS="%optflags"
cp -a src src-shlib/
pushd src-shlib
CFLAGS="%optflags -fPIC" make -j1
cc -shared -Wl,-soname,%name.so.0 *.o -o %name.so.0
ln -sf %name.so.0 %name.so
popd
make -j1

%install
# We need to use different name to avoid conflict with coreutils
install -D -m755 base64/base64 %buildroot%_bindir/libb64-base64
install -D -m755 src-shlib/%name.so.0 %buildroot%_libdir/%name.so.0
mkdir -p %buildroot/%_includedir
cp -r include/b64 %buildroot/%_includedir
cd %buildroot%_libdir
ln -s %name.so.0 %name.so

%files
%doc CHANGELOG README LICENSE
%_bindir/libb64-base64
%_libdir/%name.so.0

%files devel
%_libdir/%name.so
%dir %_includedir/b64/
%_includedir/b64/*.h

%changelog
* Thu Aug 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuilt for Fedora
* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
* Wed Jan 27 2016 Anatholy Scryabin <ascryabin@cloudlinux.com> 1.2.1-2.1
- initial build for Cloud Linux
