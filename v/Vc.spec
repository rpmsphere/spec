%global debug_package %{nil}

Name:           Vc
Version:        1.4.1
Release:        3.1
Summary:        Collection of SIMD Vector Classes
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/VcDevel/Vc/
Source0:        https://github.com/VcDevel/Vc/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

%package devel
Summary:        Development Files for Vc
Group:          Development/Libraries/C and C++

%description devel
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides development headers needed to build software using Vc.

%package doc
Summary:        API documentation for Vc
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description doc
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides the API documentation

%package static
Summary:        Vc Static Library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description static
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides the Vc static library.

%prep
%setup -q

%build
mkdir build
cd build
%cmake ..\
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_TESTING=OFF
make %{?_smp_mflags}

cd ../doc
doxygen
cd ..

%install
cd build
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a ../README.md ../doc/html %{buildroot}%{_docdir}/%{name}

%files doc
%{_docdir}/%{name}

%files devel
%license LICENSE
%{_includedir}/Vc
%{_libdir}/cmake/Vc

%files static
%{_libdir}/libVc.a

%changelog
* Wed Nov 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuild for Fedora
* Tue Feb 20 2018 stefan.bruens@rwth-aachen.de
- Drop ExclusiveArch, Vc 1.3.3 is no longer x86 only
  Add default_to_scalar_implementation_for_unknown_arch.patch
- Split documentation to subpackage
- Drop redundant %%doc in front of %%_docdir
- Remove unneeded fdupes BuildRequires
* Thu Feb 15 2018 asterios.dramis@gmail.com
- Update to version 1.3.3:
  * Support for AVX2 gather instructions.
  * Shift optimizations
  * Preliminary support for compiling to non-x86 targets (uses only
    the Scalar ABI)
  * Resolve failing static assertions, moving the relevant tests to
    unit tests
  * Fixed is_simd_vector and is_simd_mask traits to consider the
    ElementType too.
- Added a patch "fix_i686_build.patch" to fix build on i686.
* Mon May 15 2017 idonmez@suse.com
- Update to version 1.3.2
  * Resolve warning from GCC 6 about ignored attributes
  * Support for Kaby Lake detection
* Thu Mar  9 2017 idonmez@suse.com
- Update to version 1.3.1
  * swap(v[i], v[j]) did not compile. Vc 1.3.1 overloads the swap
    function and thus enables swapping scalars into/out of vector
    and mask objects.
  * The spline example has moved to the new Vc-examples-nonfree
    repository since it has a license that restricts redistribution.
* Fri Jan 27 2017 idonmez@suse.com
- Repackage without examples/spline see
  https://github.com/VcDevel/Vc/issues/150 for details.
* Thu Oct 27 2016 idonmez@suse.com
- Update to version 1.3.0
  * Too many changes to list, please see
    https://github.com/VcDevel/Vc/releases for details.
* Tue Oct  6 2015 asterios.dramis@gmail.com
- Update to 0.7.5:
  * compilation warnings fixed
  * detect Haswell and Broadwell CPUs (#6)
  * bugfix: AVX::Mask::operator== returned incorrect answers on a
    few masks
  * more thorough mask testing
  * detect and work around clang 3.6 bug with AVX codegen (#20)
  * subscript workaround for GCC 5.1 and 5.2 (#9)
  * merge vc_compile_for_all_implementations from master, making it
    more robust
  * fix isfinite usage with ICC (#8)
* Fri Sep 11 2015 mpluskal@suse.com
- Use cmake macro
- Cleanup spec file with spec-cleaner
* Fri Aug  7 2015 normand@linux.vnet.ibm.com
- add ExclusiveArch %%{ix86} x86_64
  because not supported asm lines for other architectures
* Wed Mar 25 2015 asterios.dramis@gmail.com
- Updated License to "LGPL-3.0+ and GPL-3.0+".
* Thu Mar 19 2015 asterios.dramis@gmail.com
- Added Requires: Vc-devel in the Vc-devel-static subpackage.
* Wed Mar 18 2015 asterios.dramis@gmail.com
- Fix Source0 URL.
* Sat Jan 10 2015 asterios.dramis@gmail.com
- Update to 0.7.4:
  * fixed several compile errors / warnings with newer or old C++ compilers
  * support clean compilation with more -W flags
  * fixed compilation when compiling without optimization
  * added operator-- to Vector<T>
  * Copying Memory now uses SIMD move instructions
  * Vc::Allocator<T> now uses a minimum alignment of the SIMD types of the
    chosen Vc implementation. Thus making it useable for containers of builtin
    types.
* Sat Oct 26 2013 asterios.dramis@gmail.com
- Update to 0.7.3:
  * more thorough feature tests in the cmake scripts (-mfma / -stdlib=libc++)
  * work around bogus warnings (mostly clang)
  * fixed binary operators of Mask types
  * fixed ifdef logic that lead to ICC not seeing the always_inline attributes
  * support for Intel Family 6 Model 47 CPU detection
  * fixed Vc/IO for libc++ and GCC on Windows
  * fixed a compilation error in Vc::Scalar::abs
  * fixed Vc::Scalar::sincos to use a safe fallback and ::sincos(f) on with
    glibc
* Sun Jun 30 2013 asterios.dramis@gmail.com
- Disable compilation of tests (fixes fails in OBS due to required build
  power).
* Sun Jun 30 2013 asterios.dramis@gmail.com
- Update to 0.7.2:
  * Improved documentation
  * Detect and support AMD Piledriver CPUs (prefers FMA over FMA4)
  * Support clang with libc++
  * More workarounds for compiler quirks
  * Bugs fixed:
    + Fixed VectorTuple to work without using namespace Vc.
    + SSE::sfloat_m::operator!= was broken.
    + SSE::sfloat_m::isMix was broken.
    + Buildsystem: Detection of CPU flags was broken on Linux
    + Fixed compilation for targets that don't support POPCNT.
    + Fixed debug builds that use log(-1). It returns NaN instead of asserting
    now.
    + No warning for nested foreach_bit loops anymore
* Sun May 19 2013 asterios.dramis@gmail.com
- Revoke last change (it does not solve the failures).
* Sun May 19 2013 asterios.dramis@gmail.com
- Disable parallel build, often fails in OBS.
* Sat Apr 20 2013 asterios.dramis@gmail.com
- Update to 0.7.1:
  * MSVC support: workaround bugs in MSVC; AVX is still mostly miscompiled by
    MSVC, but Vc::SSE works fine now
  * GCC on Windows support
  * Improved support for old GCC versions
  * Speed and FMA4 improvements to trigonometric functions
  * Fixed a few inconsistencies
  From 0.7.0:
  * Major polishing, making it more intuitive and portable
- Removed fix_install_libdir.patch (fixed upstream).
- Don't build latex devel docs (removed all texlive build requirements).
* Tue Feb 19 2013 asterios.dramis@gmail.com
- Initial rpm release (version 0.6.1).
- Added a patch (fix_install_libdir.patch) to make the package install the
  library in the correct libdir (lib or lib64).
