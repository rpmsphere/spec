Name:      compat-libicu57
Version:   57.1
Release:   2
Summary:   Compat package with icu libraries
License:   MIT and UCD and Public Domain
URL:       http://www.icu-project.org/
Source0:   http://download.icu-project.org/files/icu4c/57.1/icu4c-57_1-src.tgz
BuildRequires: doxygen, autoconf, python2

Patch1: icu.8198.revert.icu5431.patch
Patch2: icu.8800.freeserif.crash.patch
Patch3: icu.7601.Indic-ccmp.patch
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
Patch6: armv7hl-disable-tests.patch
Patch7: rhbz1360340-icu-changeset-39109.patch
Patch8: diff-icu_trunk_source_common_locid.cpp-from-39282-to-39384.patch
Patch9: rhbz1444101-icu-changeset-39671.patch
Patch10: rhbz1510932-icu-changeset-40324.patch

# Explicitly conflict with older icu packages that ship libraries
# with the same soname as this compat package
Conflicts: libicu < 58

%description
Compatibility package with libicu libraries ABI version 57.

%{!?endian: %global endian %(%{__python} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal

%prep
%setup -q -n icu
%patch1 -p2 -R -b .icu8198.revert.icu5431.patch
%patch2 -p1 -b .icu8800.freeserif.crash.patch
%patch3 -p1 -b .icu7601.Indic-ccmp.patch
%patch4 -p1 -b .gennorm2-man.patch
%patch5 -p1 -b .icuinfo-man.patch
%ifarch armv7hl
%patch6 -p1 -b .armv7hl-disable-tests.patch
%endif
%patch7 -p1 -b .rhbz1360340-icu-changeset-39109.patch
%patch8 -p1 -b .diff-icu_trunk_source_common_locid.cpp-from-39282-to-39384.patch
%patch9 -p1 -b .rhbz1444101-icu-changeset-39671.patch
%patch10 -p1 -b .rhbz1510932-icu-changeset-40324.patch

%build
pushd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
# Endian: BE=0 LE=1
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif

#rhbz856594 do not use --disable-renaming or cope with the mess
OPTIONS='--with-data-packaging=library --disable-samples'
%if 0%{?debugtrace}
OPTIONS=$OPTIONS' --enable-debug --enable-tracing'
%endif
%configure $OPTIONS

#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#681941
sed -i 's|^LIBS =.*|LIBS = -L../lib -licuuc -lpthread -lm|' i18n/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -licui18n -lc -lgcc|' io/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -lc|' layout/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../lib -licuuc -licule -lc|' layoutex/Makefile
sed -i 's|^LIBS =.*|LIBS = -nostdlib -L../../lib -licutu -licuuc -lc|' tools/ctestfw/Makefile
# As of ICU 52.1 the -nostdlib in tools/toolutil/Makefile results in undefined reference to `__dso_handle'
sed -i 's|^LIBS =.*|LIBS = -L../../lib -licui18n -licuuc -lpthread -lc|' tools/toolutil/Makefile
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

# more verbosity for build.log
sed -i -r 's|(PKGDATA_OPTS = )|\1-v |' data/Makefile

make %{?_smp_mflags} VERBOSE=1

%install
make %{?_smp_mflags} -C source install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*

# Remove files that aren't needed for the compat package
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/icu/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_sbindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/icu/
rm -rf $RPM_BUILD_ROOT%{_mandir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so.*

%changelog
* Mon Dec 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 57.1
- Rebuild for Fedora
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 57.1-1
- Initial packaging
