Summary: Anti-Grain Geometry graphical rendering engine
Name:    agg
Version: 2.5
Release: 44.1
Group:   System Environment/Libraries
URL:     https://www.antigrain.com
License: GPLv2+
#Source0:  https://www.antigrain.com/%{name}-%{version}.tar.gz
Source0: %{name}-free-%{version}.tar.gz
# agg contains gpc.c, 'free for non-commercial use', we cannot ship.
# We use this script to remove the non-free code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# sh agg-generate-tarball.sh 2.5
Source1: agg-generate-tarball.sh

BuildRequires: automake, libtool, libX11-devel, freetype-devel, SDL-devel

Patch0: agg-2.4-depends.patch
Patch1: agg-2.5-pkgconfig.patch
Patch2: agg-2.5-autotools.patch

Patch101: 0001-Fix-non-terminating-loop-conditions-when-len-1.patch
Patch102: 0002-Cure-recursion-by-aborting-if-the-co-ordinates-are-t.patch
Patch103: 0003-Get-coordinates-from-previous-vertex-if-last-command.patch
Patch104: 0004-Make-rasterizer_outline_aa-ignore-close_polygon-when.patch
Patch105: 0005-Remove-VC-6-workaround.patch
Patch106: 0006-Implement-grain-merge-blending-mode-GIMP.patch
Patch107: 0007-Implement-grain-extract-blending-mode-GIMP.patch
Patch108: 0008-Declare-multiplication-and-division-operators-as-con.patch
Patch109: 0009-Add-a-static-identity-transformation.patch
Patch110: 0010-Add-renderer_scanline_aa_alpha.patch
Patch111: 0011-Avoid-division-by-zero-in-color-burn-mode.patch
Patch112: 0012-Avoid-pixel-artifacts-when-compositing.patch
Patch113: 0013-Modify-agg-conv-classes-to-allow-access-to-the-origi.patch
Patch114: 0014-Avoid-potential-zero-division-resulting-in-nan-in-ag.patch
Patch115: 0015-Ensure-first-value-in-the-gamma-table-is-always-zero.patch

%description
A High Quality Rendering Engine for C++.

%package devel
Summary: Support files necessary to compile applications with agg
Group: Development/Libraries
Requires: agg = %{version}-%{release}, freetype-devel
# for _datadir/automake ownership
Requires: automake

%description devel
Libraries, headers, and support files necessary to compile applications 
using agg.

%prep
%setup -q
%patch 0 -p1 -b .depends
%patch 1 -p1 -b .pkgconfig
%patch 2 -p0 -b .autotools
%patch 101 -p1
%patch 102 -p1
%patch 103 -p1
%patch 104 -p1
%patch 105 -p1
%patch 106 -p1
%patch 107 -p1
%patch 108 -p1
%patch 109 -p1
%patch 110 -p1
%patch 111 -p1
%patch 112 -p1
%patch 113 -p1
%patch 114 -p1
%patch 115 -p1
aclocal
autoheader
autoconf
libtoolize --force
automake --foreign --add-missing --ignore-deps
sed -i '1378d' include/agg_renderer_outline_aa.h

%build
%configure --disable-gpc -disable-static -disable-examples
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install INSTALL='install -p'
rm $RPM_BUILD_ROOT/%{_libdir}/*.la

rm -rf __dist_examples __clean_examples
cp -a examples __clean_examples
make -C __clean_examples distclean
rm -rf __clean_examples/Makefile.am __clean_examples/{win32*,macosx*,BeOS}
mkdir __dist_examples
mv __clean_examples __dist_examples/examples

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc authors copying readme news
%{_libdir}/lib*.so.*

%files devel
%doc __dist_examples/examples
%{_libdir}/*.so
%{_libdir}/pkgconfig/libagg.pc
%{_includedir}/agg2/
%{_datadir}/aclocal/libagg.m4

%changelog
* Tue Jan 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5-22
- Rebuilt for GCC 5 C++11 ABI change
* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sat Jun 22 2013 Tom Hughes <tom@compton.nu> - 2.5-18
- Update mapnik patches
* Sun May 19 2013 Tom Hughes <tom@compton.nu> - 2.5-17
- Add patches from mapnik
* Fri Feb 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.5-16
- Fix FTBFS, BZ 913873.
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-12
- Rebuilt for glibc bug#747377
* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-11
- Rebuilt for glibc bug#747377
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jan 29 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.5-9
- also remove include/agg_conv_gpc.h as it also carries a copy of the non-Free
  GPC license (upstream also recommends removing that file under
  https://www.antigrain.com/license/index.html#toc0005) (#559611)
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Feb  5 2008 Patrice Dumas <pertusus@free.fr> - 2.5-6
- remove non free files
- minor cleanups
- parallel build fails
* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 2.5-4
- clarify license
- source upstream silently changed even though version remained
  unchanged
* Tue Jun 26 2007 Caolan McNamara <caolanm@redhat.com> - 2.5-3
- Resolves: rhbz#245650 -devel Require: freetype-devel
* Mon Apr 23 2007 Caolan McNamara <caolanm@redhat.com> - 2.5-2
- Resolves: rhbz#237493 misapplied patch
* Sat Jan 06 2007 Caolan McNamara <caolanm@redhat.com> - 2.5-1
- bump to 2.5
* Fri Nov 10 2006 Caolan McNamara <caolanm@redhat.com> - 2.4-3
- Resolves: rhbz#214970 rebuild with new 2.4 sources
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.4-2.1
- rebuild
* Mon Jul 10 2006 Caolan McNamara <caolanm@redhat.com> - 2.4-2
- rh#198174# add extra links from libs to their runtime requirements
* Wed May 10 2006 Caolan McNamara <caolanm@redhat.com> - 2.4-1
- next version
* Fri Feb 17 2006 Karsten Hopp <karsten@redhat.de> 2.3-4
- add BuildRequires freetype-devel for ft2build.h
* Mon Feb 13 2006 Caolan McNamara <caolanm@redhat.com> - 2.3-3
- BuildRequires
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3-2.1
- bump again for double-long bug on ppc(64)
* Wed Feb 08 2006 Caolan McNamara <caolanm@redhat.com> - 2.3-2
- rh#180341# BuildRequires
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Wed Nov 23 2005 Caolan McNamara <caolanm@redhat.com> 2.3-1
- initial import
