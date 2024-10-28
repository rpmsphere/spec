Summary:        GNU Smalltalk
Name:           gnu-smalltalk
Version:        3.2.91
Release:        1
License:        GPLv2+ with exceptions
Group:          Development/Languages
URL:            https://smalltalk.gnu.org/

Source:         ftp://alpha.gnu.org/gnu/smalltalk/smalltalk-%{version}.tar.gz
Source1:        gnu-smalltalk.desktop
Source2:        gnu-smalltalk.svg

Patch1:         gst-3.2.5-am.patch
Patch2:         gst-3.2.3-ltdl.patch
Patch3:         gst-3.2.5-inf.patch
Patch4:         gst-3.2.5-emacs.patch
Patch5:         gst-3.2.5-tk86.patch
Patch6:         gst-3.2.5-format.patch

# seems only little endian arches are supported
# eg. https://bugzilla.redhat.com/show_bug.cgi?id=1269811
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le

Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

#Requires:       emacs-filesystem

#Obsoletes:      emacs-gnu-smalltalk <= 3.2.5-10
#Obsoletes:      emacs-gnu-smalltalk-el <= 3.2.5-10

#Provides:       emacs-gnu-smalltalk <= 3.2.5-10
#Provides:       emacs-gnu-smalltalk-el <= 3.2.5-10

BuildRequires:  tk-devel
BuildRequires:  gtk2-devel
BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
BuildRequires:  readline-devel
BuildRequires:  emacs
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  texinfo
BuildRequires:  zlib-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  libffi-devel
BuildRequires:  pkgconfig
BuildRequires:  zip
BuildRequires:  mesa-libGL-devel
BuildREquires:  mesa-libGLU-devel
BuildRequires:  desktop-file-utils

%description
GNU Smalltalk is an implementation that closely follows the
Smalltalk-80 language as described in the book `Smalltalk-80: the
Language and its Implementation' by Adele Goldberg and David Robson.
The Smalltalk programming language is an object oriented programming
language.

Unlike other Smalltalks (including Smalltalk-80), GNU Smalltalk
emphasizes Smalltalk's rapid prototyping features rather than the
graphical and easy-to-use nature of the programming environment.

Therefore, even though we have a nice GUI environment including a class
browser, the goal of the GNU Smalltalk project is currently to produce a
complete system to be used to write your scripts in a clear, aesthetically
pleasing, and philosophically appealing programming language.

%package devel
Summary: Development Stuff for the GNU Smalltalk package
Group: Development/Libraries
#Requires: automake
Requires: pkgconfig
%description devel
This Package contains header files and other stuff provided by
GNU Smalltalk.

You will need this package, if you want to extent GNU Smalltalk
with functions written in C.

%prep
%setup -q -n smalltalk-%{version}
#%patch 1 -p1 -b .auto
#%patch 2 -p1 -b .ltdl
#%patch 3 -p1 -b .inf
#%patch 4 -p1 -b .emx
#%patch 5 -p1 -b .tk86
%patch 6 -p1 -b .format

%build
libtoolize
autoreconf --force --install
rm -rf lib-src/lt*
CFLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack"
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} \
  --enable-static=no --enable-shared=yes --disable-rpath --disable-relocatable \
  --with-system-libsigsegv \
  --with-system-libffi=yes \
  --with-system-libltdl=yes \
  --with-imagedir=%{_libdir}/%{name}
#  --with-lispdir=%{_emacs_sitelispdir}/gnu-smalltalk \
#  --with-lispstartdir=%{_emacs_sitestartdir} \

make %{?_smp_mflags}

cd doc

for i in gst*; do
  sed -e 's!%{_libdir}!/usr/lib(64)!g' \
      -e 's!/usr/lib!/usr/lib(64)!g' \
      -e 's!/usr/share/gnu-smalltalk/kernel!/usr/lib(64)/gnu-smalltalk/kernel!g' \
      $i >$i.new
  mv -f $i.new $i
done

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -c -p" install

#mkdir -p  ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}

#mv ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/gnu-smalltalk/site-start.d/* \
#   ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}

#rmdir ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/gnu-smalltalk/site-start.d

rm -rf $RPM_BUILD_ROOT/%{_libdir}/libgst*a*
rm -rf $RPM_BUILD_ROOT/%{_libdir}/gnu-smalltalk/*.la

rm -rf $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.a

rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir

cd $RPM_BUILD_ROOT/%{_mandir}/man1

rm gst-reload.1
ln -sf ./gst-load.1 gst-reload.1

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps

desktop-file-install \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mv $RPM_BUILD_ROOT/%{_mandir}/man1/gst.1 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1
mv $RPM_BUILD_ROOT/%{_bindir}/gst $RPM_BUILD_ROOT/%{_bindir}/%{name}

%post
/sbin/install-info %{_infodir}/gst.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/gst-base.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/gst-libs.info %{_infodir}/dir || :
/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/gst.info %{_infodir}/dir || :
  /sbin/install-info --delete %{_infodir}/gst-base.info %{_infodir}/dir || :
  /sbin/install-info --delete %{_infodir}/gst-libs.info %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_bindir}/gst-blox
%{_bindir}/gst-convert
%{_bindir}/gst-doc
%{_bindir}/gst-load
%{_bindir}/gst-package
%{_bindir}/gst-reload
%{_bindir}/gst-remote
%{_bindir}/gst-sunit
%{_bindir}/gst-browser
%{_bindir}/gst-profile

%{_libdir}/libgst.so.*
%{_libdir}/libgst-gobject.so.*

%{_infodir}/gst.info*
%{_infodir}/gst-*.info*

%{_datadir}/smalltalk
%{_libexecdir}/smalltalk

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/gst-*

%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg

#{_emacs_sitelispdir}/gnu-smalltalk/*.elc
%{_emacs_sitestartdir}/*.elc
#{_emacs_sitelispdir}/gnu-smalltalk/*.el
%{_emacs_sitestartdir}/*.el
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/*.elc

%doc AUTHORS COPYING COPYING.DOC COPYING.LIB ChangeLog 
%doc NEWS README THANKS TODO

%{_libdir}/smalltalk
%{_libdir}/gnu-smalltalk

%files devel
%{_bindir}/gst-config
%{_libdir}/libgst.so
%{_libdir}/libgst-gobject.so
%{_libdir}/pkgconfig/gnu-smalltalk.pc

%{_datadir}/aclocal/*.m4

%{_includedir}/gst.h   
%{_includedir}/gstpub.h 
%{_includedir}/gst-gobject.h

%changelog
* Fri May 10 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.5
- Rebuilt for Fedora
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sun Jan 21 2018 My Karlsson <mk@acc.umu.se> - 3.2.5-21
- Fix rpmlint issues
* Sun Jan 21 2018 My Karlsson <mk@acc.umu.se> - 3.2.5-20
- Rebuilt for gdbm 1.14
* Tue Sep 26 2017 My Karlsson <mk@acc.umu.se> - 3.2.5-19
- Use mariadb-connector-c instead of mariadb-libs (rhbz#1494077)
* Mon Sep 25 2017 My Karlsson <mk@acc.umu.se> - 3.2.5-18
- Disable -Wno-format
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.2.5-14
- Rebuild for readline 7.x
* Mon Nov 28 2016 Dan Horák <dan[at]danny.cz> - 3.2.5-13
- switch to ExclusiveArch with little endian arches only
* Sun Nov 27 2016 Marcus Karlsson <mk@acc.umu.se> - 3.2.5-12
- Build with --disable-relocatable
* Fri Nov 25 2016 Marcus Karlsson <mk@acc.umu.se> - 3.2.5-11
- Remove emacs sub-package to comply with packaging guidelines
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Thu Jun  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.5-7
- aarch64 doesn't have prelink
- Update Power64 macro
- Cleanup spec
* Thu May 29 2014 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.5-6
- Fix dependencies issues
* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sat Jun  8 2013 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.5-3
- Fix wrong BR to gtk2-devel
* Wed May 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.5-2
- Rename inhibit-first-line-modes-regexps (#968063)
* Mon Apr  8 2013 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.5-1
- New upstream release
- Reformating changelog entries
- Remove obsolete RPM statements
- User emacs-nox insteadof emacs for a BR
- Add Patch to fix issue in tutorial.texi
- Disbable 'mach check'
- enable SMP build
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
- Replace interp->result to Tcl_GetStringResult(interp)
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.2.4-1.2
- rebuild with new gmp without compat lib
* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 3.2.4-1.1
- rebuild with new gmp
* Wed Mar 23 2011 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.4-1
- New upstream release
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Dec 18 2010 Jochen Schmitt <JOchen herr-schmitt de> - 3.2.3-1
- New upstream release
* Sun Nov 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.2.2-2 
- rebuild (libsigsegv)
* Sun Aug  1 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2.2-1
- New upstream release
* Fri Jun 25 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-6
- gnu-smalltalk seems to be smp compilant now
* Thu Jun 24 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-5
- Reorganisation of the gnu-smalltalk emacs packages
* Thu Jun 24 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-4
- Add desktop file for gst-browser
* Wed Jun 23 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-3
- Put emacs files in a subdirectory
- Using standard emacs rpm macros
- Reformatting SPEC file
* Wed Jun 23 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-2
- Rebuild
* Sun May  2 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.2-1
- New upstream release
* Thu Mar 11 2010 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-8
- Remove embedded ltdl (#563974, CVE-2009-3736)
- Rebuild agains new gdbm (so namber was bumped)
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sun Jul  5 2009 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-6
- Fix license tag
* Sun May 24 2009 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-5
- Fix dependency issue
* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-4
- Supporting noarch subpackages
* Tue Mar  3 2009 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-3
- Fix retcode source issue
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sun Oct 19 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.1-1
- New upstream release
* Sun Aug 10 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.4-2
- Add zip as BR
- New upstream release
* Sun Jun  8 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.3-2
- Disable 'make check'
* Wed May 14 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.3-1
- New upstream release
* Thu Apr 17 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.2-4
- Patch configure.ac to make version independency from libffi
* Sat Mar 08 2008 Xavier Lamien <lxtnow[at]gmail.com> - 3.0.2-2
- Updated release.
- Disable x86_64 arch, because 'make test' fails on this arch
* Sun Feb 17 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.1-3
- Use system libffi
* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.1-1
- New upstream release
* Mon Jan 21 2008 Jochen Schmitt <Jochen herr-schmitt de> - 3.0-1
- New upstream release
* Thu Jan 03 2008 Alex Lancaster <alexlan fedoraproject.org> - 2.3.6-8
- Rebuild for Tcl 8.5
* Sun Nov 18 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-7
- Fix broken Changelog
* Thu Oct 25 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-6
- Add upstream multilib patch
* Wed Oct 24 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-4
- Another try to fix the multilib issue
* Mon Oct 22 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-3
- Create new subpackage to solve mulitlib issue (#341341)
* Sun Sep  9 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-2
- Remove build path from gst.im
- Temporarly disable ppc64
* Thu Sep  6 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.6-1
- New upstream release
* Thu Aug  9 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.5-3
- Try to fix smp_mflags issue
* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.5-2
- Changing license tag
* Sun Jun  3 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.5-1
- New upstream release
* Wed May 30 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.4-4
- Remove references to sigseg lib shiped with the package
* Mon May 28 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.4-1
- New upstream release
* Sun Mar 18 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.3-5
- Include Publish.st patch
* Tue Mar 13 2007 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.3-4
- Fix wrong paths in gst.im
* Wed Feb 14 2007 Jochen Schmitt <s4504kr@zeus.herr-schmitt.de> - 2.3.3-3
- New upstream release
* Tue Feb 13 2007 Jochen Schmitt <s4504kr@zeus.herr-schmitt.de> - 2.3.2-6
- Solve multilib issue (#228175)
* Sun Feb 11 2007 Jochen Schmitt <s4504kr@zeus.herr-schmitt.de> - 2.3.2-5
- Rebuild to fix broken deps.
* Wed Jan 31 2007 Jochen Schmitt <s4504kr@zeus.herr-schmitt.de> - 2.3.2-4
- New upstream release
* Wed Dec 13 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.1-1
- New upstream release
* Thu Dec  7 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.3-4
- Exclude x86_64 bc/ build failure
* Thu Dec  7 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.3-3
- Fix wrong lib option in gst-config
* Wed Dec  6 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.3-2
- Fix wrong Requires
- Fix gst-package.in file
* Tue Dec  5 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.3-1
- New upstream release
* Wed Nov 29 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2c-4
- Remove files which will be gone in gnu-smalltalk-2.3
* Tue Nov 28 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2c-3
- Cleanup configure section
- Try to preserve timestamps
* Mon Nov 27 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2c-2
- Done some cleanup on configure step
- Add Patch to fix broken gst-config
* Mon Nov 20 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2c-1
- New upstream release
* Mon Feb 20 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-8
- Add libtool as BuildRequires
- Add LIBTOOL=/usr/bin/libtool at the make step
* Tue Jan 31 2006 Jochen Schmitt <jochen herr-schmitt de> - 2.2-7
- Fix rpmlint errors
* Tue Jan 10 2006 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-6
- Added --disable-rpath
- Added --enable-static=no
- fix broken Shebangs
* Tue Dec 13 2005 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-5
- Deps from -devel and -emacs more strict
- Move libgst.so.* to main package
* Wed Dec  7 2005 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-4
- remove dep to lightning
* Sun Dec  4 2005 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-3
- Add aclocal
- Add depend to lightning
* Tue Nov 29 2005 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-2
- Rename package
- install-info for gst-base and gst-libs
- move libgst.so to devel package
* Thu Nov 24 2005 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-1
- Initial RPM
