Name: icnc
Version: 1.2.300
Release: 3.1
Summary: Intel(R) Concurrent Collections for C++
License: see LICENSE file
Group: Development/C++
URL: https://icnc.github.io/
Source: %name-%version.tar.gz
BuildRequires: gcc-c++ cmake doxygen tbb-devel
Provides: libcnc

%description
CnC makes it easy to write C++ programs which take full advantage of the available parallelism.
Through its portabilty and composability (with itself and other tools) it provides future-proof scalability.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %version-%release
Provides: libcnc-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%cmake -DLIB=%_libdir
make

%install
%make_install

%files
%_libdir/*.so.*

%files devel
%_includedir/cnc
%_libdir/*.so
%_datadir/icnc

%changelog
* Thu Aug 30 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.300
- Rebuild for Fedora
* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0.100git-alt1
- initial build for ALT Linux Sisyphus
