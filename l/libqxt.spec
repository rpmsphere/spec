Name:		libqxt
Version:	0.6.2
Release:	16
Summary:	Qt extension library
Group:		System Environment/Libraries
License:	CPL or LGPLv2
URL:		https://bitbucket.org/libqxt/libqxt/wiki/Home
Source0:	http://bitbucket.org/libqxt/libqxt/get/v%{version}.tar.bz2
# Fix DSO linking
Patch0:		libqxt-linking.patch
# To support multimedia keys when using clementine
# Patch sent to upstream. They want to reimplement it more cleanly.
# We will use this patch until upstream reimplements it.
# http://dev.libqxt.org/libqxt/issue/75
Patch1:		libqxt-media-keys.patch
# Fix wrong header includes RHBZ#733222
# http://dev.libqxt.org/libqxt/issue/112/wrong-include-in-qxtnetworkh
Patch2:		libqxt-header-fix.patch
# Fix build with GCC 6
# https://bugzilla.redhat.com/show_bug.cgi?id=1305223
Patch3:		libqxt-gcc6.patch
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	avahi-devel
BuildRequires:	db4-devel
BuildRequires:	libXrandr-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-devel

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
LibQxt, an extension library for Qt, provides a suite of cross-platform
utility classes to add functionality not readily available in the Qt toolkit.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	avahi-compat-libdns_sd-devel
Requires:	avahi-devel
Requires:	db4-devel
Requires:	qt4-devel

%description	devel
This package contains libraries and header files for developing applications
that use LibQxt.

%prep
%setup -q -n %{name}-%{name}-v%{version}
%patch0 -p1 -b .linking
%patch1 -p1 -b .mediakeys
%patch2 -p1 -b .includes
%patch3 -p1 -b .gcc6

# We don't want rpath
sed -i '/RPATH/d' src/qxtlibs.pri

%build
# Does not use GNU configure
./configure -verbose \
	    -qmake-bin %{_qt4_qmake} \
	    -prefix %{_prefix} \
	    -libdir %{_libdir}
# manually running qmake here may end up being fragile, if so,
# introducing a qmake wrapper is the next best thing -- rex
%{qmake_qt4} -r
make %{?_smp_mflags}
make %{?_smp_mflags} docs

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

# We are installing these to the proper location
rm -fr $RPM_BUILD_ROOT%{_prefix}/doc/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS CHANGES *.txt LICENSE README
%{_qt4_libdir}/*.so.*

%files devel
%doc examples/ doc/html/
%{_qt4_headerdir}/*
%{_qt4_libdir}/*.so
%{_qt4_plugindir}/designer/*.so
%{_qt4_datadir}/mkspecs/features/qxt*.prf

%changelog
* Fri Oct 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuilt for Fedora
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Mon Mar 07 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.6.2-11
- Fix FTBFS with GCC 6 (#1305223)
* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.6.2-10
- use %%qmake_qt4 macro to ensure proper build flags
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.2-8
- Rebuilt for GCC 5 C++11 ABI change
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sat Nov 26 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.2-1
- Update to 0.6.2
* Thu Aug 25 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.1-3
- Fix wrong includes RHBZ#733222
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Thu Nov 25 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.1-1
- Update to 0.6.1
* Sun Jul 18 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.0-3
- Include patch to support for mod4 in qxtglobalshortcut
- Include patch to support multimedia keys
* Tue Apr 20 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.0-2
- This is the real 0.6.0 (upstream changed their tarball)
* Sun Apr 11 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.0-1
- Use qt4 macros more extensively.
- Update to 0.6.0 final.
* Wed Apr 07 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.0-0.2.20100407hg
- New snapshot. The previous tarball got damaged somehow.
- Remove configure tests hack. Upstream fixed it upon our warning.
* Sat Mar 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6.0-0.1.20100327hg
- Initial build
