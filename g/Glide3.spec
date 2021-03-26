Name:             Glide3
Version:          20050815
Release:          1
Summary:          Glide3 runtime for the 3Dfx Voodoo family of cards
#                 Glide3 is x86/alpha/ia64/x86_64 only, ia64 is untested
ExclusiveArch:    %{ix86} ia64 x86_64
Group:            User Interface/X Hardware Support
License:          Glide
URL:              http://glide.sourceforge.net
# Create the Glide3 tarball by using:
#   cvs -d :pserver:anonymous@cvs.glide.sourceforge.net:/cvsroot/glide \
#     co -r glide-devel-branch Glide3
#   pushd Glide3 ; find . -name CVS -type d |xargs rm -rf
#   find . -name .cvsignore | xargs rm ; popd
#   tar jcf Glide3-$(date +"%Y%m%d").tar.bz2 Glide3/
Source0:          %{name}-%{version}.tar.bz2
Source1:          glidelink.c
Patch0:           Glide3-warn.patch
BuildRequires:    libX11-devel xorg-x11-proto-devel 
# Add these to try the experimental DGA support and add DGA=1 to %{glide_flags}
# BuildRequires:  libXxf86dga-devel libXxf86vm-devel
%ifarch %{ix86}
BuildRequires:    nasm
Requires(post):   policycoreutils /sbin/ldconfig
Requires(postun): policycoreutils /sbin/ldconfig
%endif

%description
Glide3 provides the necessary low-level interface glue between the Mesa
3D graphics library, and 3Dfx Voodoo series of hardware. This package is
required by the Xorg tdfx driver in order to provide 3D acceleration
support for the 3Dfx Voodoo 3 & 5. This package also contains support for
the Voodoo 2 & 1 in order to use the 3Dfx Voodoo 2 or 1 you need the
Glide3-libGL package or a native Glide3 application.


%package devel
Summary: Development libraries and headers for Glide3
Group: Development/Libraries
Requires: Glide3 = %{version}

%description devel
Glide3-devel contains the developmental files that must be installed in order
to compile native Glide3 applications.
 

%prep
%setup -q -n Glide3
%patch0 -p1 -z .warn


%build
%ifarch %{ix86}
%define glide_flags USE_X86=1 USE_3DNOW=1 USE_MMX=1 USE_SSE=1 USE_SSE2=1 TEXUS2=1
%else
%define glide_flags TEXUS2=1
%endif

make -f makefile.linux FX_GLIDE_HW=h5 DRI=1 XPATH=/usr/X11R6/%{_lib} \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter -Wno-format-security" %{glide_flags}
mv h5/lib/libglide3.so libglide3-v5.so
make -f makefile.linux FX_GLIDE_HW=h5 realclean

make -f makefile.linux FX_GLIDE_HW=h3 DRI=1 XPATH=/usr/X11R6/%{_lib} \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter -Wno-format-security" %{glide_flags}
mv h3/lib/libglide3.so libglide3-v3.so
make -f makefile.linux FX_GLIDE_HW=h3 realclean

make -f makefile.linux FX_GLIDE_HW=cvg \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter -Wno-format-security" %{glide_flags}
mv cvg/lib/libglide3x.so libglide3-v2.so
make -f makefile.linux FX_GLIDE_HW=cvg realclean

#Sorry, no 64 bit support for Voodoo1 (yet)
%ifarch %{ix86}
make -f makefile.linux FX_GLIDE_HW=sst1 \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter -Wno-format-security" %{glide_flags}
mv sst1/lib/libglide3x.so libglide3-v1.so
make -f makefile.linux FX_GLIDE_HW=sst1 realclean
%endif


%install
rm -rf $RPM_BUILD_ROOT
%define libver 3.10.0
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/glide3

install -m 755 *.so $RPM_BUILD_ROOT/%{_libdir}
# Point to v2 by default
ln -snf libglide3-v2.so $RPM_BUILD_ROOT%{_libdir}/libglide3.so.%{libver}
ln -snf libglide3.so.%{libver} $RPM_BUILD_ROOT%{_libdir}/libglide3.so.3
ln -snf libglide3.so.%{libver} $RPM_BUILD_ROOT%{_libdir}/libglide3.so

install -p -m 644 swlibs/fxmisc/3dfx.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 h5/glide3/src/g3ext.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 h5/glide3/src/glide.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 h5/glide3/src/glidesys.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 h5/glide3/src/glideutl.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 swlibs/fxmisc/linutil.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 h5/incsrc/sst1vid.h $RPM_BUILD_ROOT/%{_includedir}/glide3
install -p -m 644 swlibs/texus2/lib/texus.h $RPM_BUILD_ROOT/%{_includedir}/glide3


%clean
rm -rf $RPM_BUILD_ROOT


%ifarch %{ix86}
%post
/sbin/ldconfig
# Set SELinux file_context in the policy
semanage fcontext -a -t textrel_shlib_t '%{_libdir}/libglide3-v.\.so' 2>/dev/null || :
# Actually change the context
chcon -t textrel_shlib_t %{_libdir}/libglide3-v?.so || :
%else
%post -p /sbin/ldconfig
%endif

%ifarch %{ix86}
%postun
/sbin/ldconfig
# SELinux support
if [ $1 -eq 0 ]; then  # final removal
  semanage fcontext -d -t textrel_shlib_t '%{_libdir}/libglide3-v.\.so' 2>/dev/null || :
fi
%else
%postun -p /sbin/ldconfig
%endif


%files
%doc COPYING
%{_libdir}/libglide3.so.3
%{_libdir}/libglide3.so.%{libver}
%ifarch %{ix86}
%{_libdir}/libglide3-v1.so
%endif
%{_libdir}/libglide3-v2.so
%{_libdir}/libglide3-v3.so
%{_libdir}/libglide3-v5.so

%files devel
%dir %{_includedir}/glide3
%{_includedir}/glide3/*
%{_libdir}/libglide3.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20050815
- Rebuild for Fedora

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20050815-7
- Autorebuild for GCC 4.3

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-6
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-5
- FE6 Rebuild

* Fri Apr 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-4
- Add scripts to set SELinux type for the .so files to textrel_shlib_t
  on i386, because of the non PIC asm used on i386 (bz 187484).

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-3
- Bump release and rebuild for new gcc4.1 and glibc.
- add %% for consistency with my other packages

* Mon Jan 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-2
- Add modular Xorg BuildReqs
- Add a patch which fixes gcc4.1 warnings

* Mon Aug 15 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 20050815-1
- Add -soname to linkerflags, so that we report the correct soname,
  otherwise rpm can't properly resolve dependencies because of the
  symlink stuff we do (merged upstream).

* Sat Aug 13 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 20050813-1
- Work together with upstream to keep Glide alive, use upstream CVS
  glide-devel-branch as a base.
- Intergrate all our patches into upstream CVS glide-devel-branch.
- New upstream branch (re)adds support for Voodoo1 (sst1).
- Make Voodoo2 (cvg) code 64 bit clean (merged upstream).

* Mon May  9 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- Change -L/usr/X11R6/lib to -L/usr/X11R6/lib64 when building on
  x86_64 .
- Add an %%ifarch around the install command for the v2 version.
- Modify the description to match the current state of affairs.

* Thu May  5 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- More x86_64 fixes added to Glide-64bit.patch.
- Removed ancient Conflicts: XFree86-libs = 4.1.0

* Wed May  4 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- Tested amd3dnow code on a voodoo2, works for me (tm). Enabled
  amd3dnow code on i386 for now.
- Added FX_GLIDE_I386 AM-conditonal and define, only use and build
  cpudtect.s when this is set. This should fix the cpudtect assemble problem
  on x86_64. Made this part of Glide-64bit.patch.

* Mon May  2 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- Fix amd3dnow code for cvg(voodoo2) so that it not only compiles but
  also links. Still untested, so still disabled.

* Sun May  1 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- Added a patch which fixes PIC compilation of amd3dnow asm code
  for h3 and h5 and which fixes compilation of amd3dnow code in general
  for cvg. Currently amd3dnow support is still disabled because it doesn't
  work on my voodoo2 (linking problem).
- replaced configure with %%configure

* Sat Apr 30 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- Removed unnescearry makefile mods from Glide3-gcc4.patch. The option
  I added disabled another warning then the one I was trying to get disabled.
- Replaced glide-ia64.patch with Glide-64bit.patch this patch adds support
  for x86_64 and has lots of "long" replaced with "unsigned long" so that
  the code stays 100%% the same on i386.
- Made the use of the new 64bit patch unconditional (iow for all archs).
- Fixed Glide3-fixes.patch so that compilation with the 64bit patch applied
  actually works.
- Don't build support for voodoo2 / cvg on 64 bit archs since the 64bit patch
  only adds 64bit support for voodoo3 & 5 / h3 & h5.

* Tue Apr 26 2005 Hans de Goede <j.w.r.degoede@hhs.nl>
- added x86_64 to ExclusiveArch list
- apply glide-ia64.patch for x86_64
- added Glide3-gcc4.patch which fixes all gcc4 errors
- first attempt to clean up the specfile a bit

* Sat Sep 4 2004 Hans de Goede <j.w.r.degoede@hhs.nl>
- added Glide3-fixes.patch which:
  * Generally do everything needed to get this to compile on FC3test1
  * replaces gcc3-patch with a patch which fixes the macros instead of
    the caller of the macros
  * replaces and fixes libtool patch
  * replaces and improves gcc34 patch
  * also fix this all for voodoo2
  * fixes a bug in g3df.c which caused some of the test programs to fail
- also compile for Voodoo 2 (cvg)
- do the make install for the Voodoo 5 (h5) build not the (h3) since the
  h5 headers define some additional texture types which Mesa 6 needs to compile
- made the symlink point to voodoo2 by default, since the XFree included mesa
  which is used for h3 and h5 knows how to load the correct Glide itself.
  Maybe we should reintroduce glidelink, since the symlink will still be needed
  for native glide apps on h3 and h5.
- removed unused automake version detection macros
- removed Prereq ldconfig, rpm should pick this up automaticly
- removed conflicting parts from glide-ia64 patch, these are all handled
  in an architecture indepent way in Glide3-fixes.patch, move it back to
  position 0.

* Mon Jul  5 2004 Mike A. Harris <mharris@redhat.com> 20010520-33
- Moved glide-ia64 patch from position 0 to position 50 as we no longer
  build Glide3 on these architectures.  The patch should be reworked to apply
  cleanly after all of the other patches we apply that are required for our
  real builds.  Currently it will just fail to apply.  (#126734)

* Wed Jun 23 2004 Mike A. Harris <mharris@redhat.com>
- Fixed missing dependancy in Glide3

* Fri Jun 18 2004 Alan Cox <alan@redhat.com>
- Fixed gcc 3.4 compile breakage. It remains to see if it works. If not
  I'd try turning off aliasing in gcc

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 19 2004 Mike A. Harris <mharris@redhat.com> 20010520-30
- Fixes from Alan Cox, who got Glide3 to build in Fedora Core devel:
  - Added Glide3-gcc3.patch, Glide3-new-libtool.patch
  - Use aclocal instead of aclocal-1.4, and automake instead of automake-1.4
  - Run aclocal before libtoolize
- Added with_glide3_devel macro, enabled by default for now, which disables
  the creation of the Glide3-devel subpackage.  XFree86 4.2.0 and later seem
  to dlopen() Glide3 now and not require it during build time, so there is not
  any need to include Glide3-devel any longer.  This needs to be install
  tested and runtime tested first however, so we still include Glide3-devel
  for now.
- Changed Prereq: /sbin/ldconfig to Requires(post,postun): /sbin/ldconfig

* Fri Feb 27 2004 Mike A. Harris <mharris@redhat.com> 20010520-29
- Added COPYING file to %%doc in files list (#115945)

* Thu Jan 29 2004 Mike A. Harris <mharris@redhat.com> 20010520-28
- Rebuild for Fedora Core 2

* Mon Sep  1 2003 Mike A. Harris <mharris@redhat.com> 20010520-27
- Rebuild 20010520-26 for Cambridge, for self hosting chocolatey goodness
- ia64 wont compile anymore and the problems are far too large to bother
  fixing.  Glide3 is now supported only on x86/alpha

* Tue Aug  5 2003 Elliot Lee <sopwith@redhat.com> 20010520-26
- Fix autoconf version

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 20010520-25
- rebuilt

* Fri Dec 20 2002 Mike A. Harris <mharris@redhat.com> 20010520-24
- Reworded the -devel package description for bug (#79477)

* Mon Nov 25 2002 Mike A. Harris <mharris@redhat.com> 20010520-23
- Bump and rebuild to pick up Alpha which did not get built in -22 somehow

* Sat Nov 23 2002 Mike A. Harris <mharris@redhat.com> 20010520-22
- Moved comment from XFree86 package to here on how to create Glide3 tarball

* Fri Nov 22 2002 Mike A. Harris <mharris@redhat.com> 20010520-21
- Remove /usr/lib/libglide3.{a,la} from buildroot since we dont ship them
- Use _libdir, _includedir everywhere
- Remove redundant ExcludeArch directive for s390

* Thu Oct  3 2002 Mike A. Harris <mharris@redhat.com> 20010520-20
- All-arch rebuild
- Added "Exclusivearch: {ix86}, alpha, ia64" as Glide3 is not ported to
  other arches and likely never ever will be.  That way lays madness.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 20010520-18
- automated rebuild

* Wed May 29 2002 Elliot Lee <sopwith@redhat.com> 20010520-17
- Make it specify the auto* tool versions explicitly.

* Tue May 28 2002 Mike A. Harris <mharris@redhat.com> 20010520-16
- Rebuilt with gcc 3.1 with new GNU autoconk/autobreak/libfool
- Added Glide3-new-autotools-bugfix.patch to fix problems with Glide automake
  files.

* Wed Apr  3 2002 Mike A. Harris <mharris@redhat.com> 20010520-13
- Removed glidelink cruft entirely.
- Simplified spec install stage, filelist, etc to minimize error potential
- Fixed dangling symlink bug (#61521)

* Sun Mar 10 2002 Mike A. Harris <mharris@redhat.com> 20010520-12
- Removed all the old /usr/lib/lib* files, and removed the /usr/lib/glide3
  directory.  Moved the Voodoo 3 and voodoo 5 glide libs directly into
  /usr/lib where the XFree86 4.2.0 tdfx dri driver will load them automatically.

* Thu Feb 21 2002 Mike A. Harris <mharris@redhat.com> 20010520-11
- Made glidelink conditional, and disabled by default, as it is not needed
  in XFree86 4.2.0 as Mesa now loads the proper Glide3 library on its own.
- Added buildrequires kudzu-devel (#59960)

* Sat Jan 26 2002 Mike A. Harris <mharris@redhat.com> 20010520-10
- Added autoconf version detection and override via __automake so Glide3 will
  build on any Red Hat Linux 7.* or rawhide system without specfile editing.
- Added -q flag to setup section

* Fri Jan 25 2002 Mike A. Harris <mharris@redhat.com> 20010520-9
- Fixed a build failure on ia64 with the ia64 patch

* Fri Jan 25 2002 Mike A. Harris <mharris@redhat.com> 20010520-8
- Undeprecated the Glide3 package that was merged into XFree86 packaging as
  it seemed to create more problems than it solved.  Took the RHL 7.2 package
  as a starting point, and deintegrated Glide from the XFree86 4.2.0 package
  back to separate packaging.  Bumped release up to -8
- Changed Copyright tag to License
- Added Glide3-redhat-cleanup-1.patch to clean up some compiler warnings.
- Added Conflicts: XFree86-libs = 4.1.0 and Conflicts: XFree86-devel = 4.1.0
- Fixed BuildRoot with _tmppath

* Mon Feb 19 2001 Bill Nottingham <notting@redhat.com>
- fix typo in ia64 patch, only apply patch on alpha/ia64 (#27889)

* Thu Dec 21 2000 Bill Nottingham <notting@redhat.com>
- fix alpha asm (rth@redhat.com)

* Wed Dec 20 2000 Bill Nottingham <notting@redhat.com>
- update CVS
- build in 7.1 tree

* Wed Aug 23 2000 Bill Nottingham <notting@redhat.com>
- initial packaging
