Summary:        Google C++ testing framework
Name:           gtest
Version:        1.6.0
Release:        4%{?dist}
License:        BSD
Group:          Development/Tools
URL:            http://code.google.com/p/googletest/
Source0:        http://googletest.googlecode.com/files/gtest-%{version}.zip
Patch0:         gtest-soname.patch
BuildRequires:  python cmake libtool
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Google's framework for writing C++ tests on a variety of platforms
(GNU/Linux, Mac OS X, Windows, Windows CE, and Symbian). Based on the
xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, various options for running the tests, and XML test report
generation.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       automake
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .0-soname

# keep a clean copy of samples.
cp -pr ./samples ./samples.orig

%build
# this is odd but needed only to generate gtest-config.
%configure
mkdir build
pushd build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_SKIP_BUILD_RPATH=TRUE -DPYTHON_EXECUTABLE=%{__python} -Dgtest_build_tests=ON ..
popd

make %{?_smp_mflags} -C build

%check
# LD_LIBRARY_PATH needed due to cmake_skip_rpath in %%build
LD_LIBRARY_PATH=$RPM_BUILD_DIR/%{name}-%{version}/build \
make test -C build

# Restore the clean copy of samples.
# To be later listed against doc.
rm -rf ./samples
mv ./samples.orig ./samples

%install
rm -rf $RPM_BUILD_ROOT
# make install doesn't work anymore.
# need to install them manually.
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/aclocal,%{_includedir}/gtest{,/internal},%{_libdir}}
# just for backward compatibility
install -p -m 0755 build/libgtest.so.*.* build/libgtest_main.so.*.* $RPM_BUILD_ROOT%{_libdir}/
(cd $RPM_BUILD_ROOT%{_libdir};
ln -sf libgtest.so.*.* $RPM_BUILD_ROOT%{_libdir}/libgtest.so
ln -sf libgtest_main.so.*.* $RPM_BUILD_ROOT%{_libdir}/libgtest_main.so
)
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
install -p -m 0755 scripts/gtest-config $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 include/gtest/*.h $RPM_BUILD_ROOT%{_includedir}/gtest/
install -p -m 0644 include/gtest/internal/*.h $RPM_BUILD_ROOT%{_includedir}/gtest/internal/
install -p -m 0644 m4/gtest.m4 $RPM_BUILD_ROOT%{_datadir}/aclocal/

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc CHANGES CONTRIBUTORS COPYING README
%{_libdir}/libgtest.so.*
%{_libdir}/libgtest_main.so.*

%files devel
%defattr(-, root, root, -)
%doc samples
%{_bindir}/gtest-config
%{_datadir}/aclocal/gtest.m4
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so
%{_includedir}/gtest

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-3
- use %%cmake macro, fix %%check, use RPM_BULID_ROOT consistently

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Akira TAGOH <tagoh@redhat.com> - 1.6.0-1
- New upstream release.
- Using autotools isn't supported in upstream anymore. switching to cmake.
- undefined reference issues seems gone now. (#813825)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Akira TAGOH <tagoh@redhat.com> j- 1.5.0-5
- Fix FTBFS issue; update libtool files instead of disabling rpath things.

* Sun Mar 20 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-4
- add patch from Dan Horák to let 'make check' work 

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-2
- add python to buildreq 

* Wed Jan 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-1
- 1.5.0
- some cleanup

* Sat Aug 26 2010 Dan Horák <dan[at]danny.cz> - 1.4.0-2
- added workaround for linking the tests on Fedora >= 13 (#564953, #599865)

* Sat Nov 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.4.0-1
- Version bump to 1.4.0.
  * New feature: the event listener API.
  * New feature: test shuffling.
  * New feature: the XML report format is closer to junitreport and can
    be parsed by Hudson now.
  * New feature: elapsed time for the tests is printed by default.
  * New feature: comes with a TR1 tuple implementation such that Boost
    is no longer needed for Combine().
  * New feature: EXPECT_DEATH_IF_SUPPORTED macro and friends.
  * New feature: the Xcode project can now produce static gtest libraries in
    addition to a framework.
  * Compatibility fixes for gcc and minGW.
  * Bug fixes and implementation clean-ups.

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-2.20090601svn257
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-1
- Version bump to 1.3.0.
  * New feature: ability to use Google Test assertions in other testing
    frameworks.
  * New feature: ability to run disabled test via
    --gtest_also_run_disabled_tests.
  * New feature: the --help flag for printing the usage.
  * New feature: access to Google Test flag values in user code.
  * New feature: a script that packs Google Test into one .h and one .cc file
    for easy deployment.
  * New feature: support for distributing test functions to multiple machines
    (requires support from the test runner).
  * Bug fixes and implementation clean-ups.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 05 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.0.0-1
- Initial build.
