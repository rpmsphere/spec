Name:           gnotime
Version:        2.4.1
Release:        14%{?dist}
Summary:        Tracks and reports time spent

Group:          Applications/Productivity
License:        GPLv2+
URL:            http://gttr.sourceforge.net/
Source0:        http://downloads.sf.net/gttr/%{name}-%{version}.tar.gz
#Patch0:         gnotime-2.3.0-description-column.patch
#Patch1:         gnotime-2.3.0-apiversion.patch

BuildRequires:  compat-gtkhtml314-devel
BuildRequires:  guile-devel
BuildRequires:  scrollkeeper
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  qof-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  GConf2

Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
A combination of stop-watch, diary, consultant billing system, and project
manager.  Gnotime allows you to track the amount of time you spend on a task,
associate a memo with it, set a billing rate, print an invoice, as well as
track the status of other projects.

Some people may remember Gnotime in its previous incarnations as GTT
(Gnome Time Tracker) when it was part of the Gnome Utils package.  It has
been split out, renamed, and greatly enhanced since then.

%prep
%setup -q

#%%patch0 -p0
#%%patch1 -p0

sed -i 's/\(Icon=.*\)\.png/\1/' gnotime.desktop.in

%build
%configure
make %{?_smp_mflags} LIBS="-lm"

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Gnotime puts it's locale translations into gnotime-2.0.mo but it's gnome
# help files into html/gnotime....
%find_lang  %{name} --with-gnome
%find_lang  %{name}-2.0 --with-gnome
cat %{name}-2.0.lang >> %{name}.lang

# Gnotime uses scrollkeeper to track help data.  Unfortunately, it needs to
# install at package install, not build install.  So uninstall it now.
rm -rf %{buildroot}%{_localstatedir}

desktop-file-install --delete-original \
                     --remove-category=Application --remove-category=GTK \
                     --dir=%{buildroot}%{_datadir}/applications \
                     %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
# TODO: Inform upstream
#make check
desktop-file-validate %{buildroot}%{_datadir}/applications/gnotime.desktop

%pre
%gconf_schema_prepare gnotime

%post
%gconf_schema_upgrade gnotime
scrollkeeper-update -q -o %{_datadir}/omf/gnotime || :

%preun
%gconf_schema_remove gnotime

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/omf/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man[^3]/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.1-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.1-5
- Gconf triggers fixes
- Add check section w/ make check and verify desktop-file
- Fix desktop-file for deprecated groups and vendor
- Drop linking w/ X11 in make
- Other small fixups

* Fri Aug 23 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-4
- GConf fixes.
- Fix icon cache handling.
- Enable parallel make.
- Drop api-version patch.

* Thu Aug 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-3
- Drop versioning of qof BR.

* Mon Jul 29 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-2
- Removed legacy macros for review.

* Thu Jul 18 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-1
- Latest upstream.

* Fri May 31 2013 Peter Ajamian <peter@pajamian.dhs.org> 2.3.0-8.1
- Require gtkhtml314 since we can't use gtkhtml3 4.x with a gtk+2 program

* Mon Jan 03 2011 Jon Ciesla <limb@jcomserv.net> - 2.3.0-8
- Rebuild for gtkhtml, patch for new API version.

* Fri Jun 25 2010 Jon Ciesla <limb@jcomserv.net> - 2.3.0-7
- Fix for dsolink FTBFS, BZ 599886.

* Wed Sep 30 2009 Hans de Goede <hdegoede@redhat.com> - 2.3.0-6
- Really fix FTBFS

* Thu Jul 30 2009 Jon Ciesla <limb@jcomserv.net> - 2.3.0-5
- Add libgnomeui-devel BR to fix FTBFS.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Jon Ciesla <limb@jcomserv.net> - 2.3.0-2
- Fixed Description column text, BZ 480087.

* Tue Feb 19 2008 Jon Ciesla <limb@jcomserv.net> - 2.3.0-1
- Upgrade to 2.3.0.
- Updated guile version dep to 1.8.
- Dropped gtkhtml315 patch, fixed upstream.
- Dropped drag and drop patch, fixed upstream.
- Dropped unapplied install scripts patch.
- Dropped autoconf BR.
- Added libXScrnSaver-devel BR.

* Wed Feb 13 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-4
- Rebuild for gcc-4.3

* Fri Dec 7 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-3
- Upstream's fix needed some fuzz cleanups.
- Fix the desktop file's Icon definition.

* Fri Dec 7 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-2
- Fix for reordering projects via drag and drop.

* Fri Oct 26 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-1
- Upstream bugfix release.

* Wed Aug 29 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.2-10
- Update qof patch for differences in how headers are included from each
  other in qof-0.7.2.

* Wed Aug 29 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.2-9
- Update qof patch for renamed headers in qof-0.7.2.

* Sat Aug 18 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.2-8
- Update license tag.
- Rebuild for changes in Fedora's build tools.
- Patch to deal with new gtkhtml.

* Sun Sep 03 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-7
- Remove testing of --disable-schemas-install which will not work until a
  patch makes it upstream.

* Fri Sep 01 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-6
- Rebuild for FC6.
- Add intltool as a BR.
- Rebuild against qof-0.7.  Change the patch to also link against the qof
  deprecated.h header as gnotime is now using deprecated, gnc-date functions.

* Fri May 12 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-5
- Remove the libXt fake BR: as it shouldn't be needed on FC5+.
- Attempt rebuild for new guile.

* Mon Feb 13 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-4
- Bump and rebuild for FC5.

* Sun Jan 29 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-3
- Work around autoconf macro brokenness with an extra BuildRequires.
- No longer send HUP to gconfd.  This is no longer necessary in FC5+.

* Sun Jan 29 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-2
- Modular xorg BuildRequires.

* Sun Jan 15 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-1
- Rebuild against new qof-0.6.1.
- Patch to fix the build for the qof-0.6 series.
 
* Fri Sep 30 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.2-0
- Update to 2.2.2.
- Remove all patches as they've been merged upstream.
- Build with internal qof as gnotime now depends on 0.6.0 which has not yet
  been released.  Only build for devel/testing until we can use a released
  version of qof.

* Thu Aug 18 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-11
- Fix the patch level on the new gtkhtml3 patch.

* Thu Aug 18 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-10
- Fix build for gtkhtml3-3.7.
- Fix gtkhtml test to fail if gtkhtml3 is not installed.
  
* Wed Aug 17 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-9
- Add dist tag.
- Rebuild for devel.
 
* Mon May 2 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-8
- Add a patch adapted from the gnotime tracker.  Original patch by
  goedson-users.sf.net.  SF Tracker: 1171394.  This allows separate setting
  of the idle project and no project timeouts.

* Wed Mar 30 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-7
- Rebuild for FC4t1.
- Fix typo in the %%pre scriptlet.
- Require(pre): GConf2.
  
* Sat Mar 19 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.2.1-6
- Fix up scriptlets to properly install and uninstall gconf schemas via
  gconftool-2.
- Fix gtkhtml3 detection so 3.6 (as used in FC4) is detected.

* Sat Nov 27 2004 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.2.1-5
- Patch to fix a crash when invoking gnome_help.
- Patch to wordwrap diary notes.

* Thu Sep 30 2004 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.2.1-0.fdr.4
- New patch to fix the Activity entry in the popup menu.

* Sat Aug 7 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.2.1-0.fdr.3
- Patch to fix gnome help invocation.
- Submitted upstream.

* Mon Jul 19 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.2.1-0.fdr.2
- Combined gtkhtml3/qof patch that has the gtkhtml3 fix and work to allow
  building with a system installed libqof.
- Build with a system installed libqof.
- Patch to fix the inclusion of headers in C source.
- Update the .desktop patch to use false on "Needs Terminal".

* Sun Jul 11 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.2.1-0.fdr.1
- Upgrade to 2.2.1.
- Remove extraneous BuildRequires.
- Change .desktop fix-ups into a patch to submit upstream.
- Remove doc patches as they've gone in upstream.
- Patch to fix building with libgtkhtml3.0
- And require automake, autoconf, etc because the gtkhtml patch applies to
  configure.in.  Decided this is preferable to a postautogen patch because it
  takes too much effort for someone to QA a huge postautogen patch.
- Patch to the idle timer to properly work with kernel-2.6's /proc/interrupts
- Removed smp flags as this version isn't smp-able.

* Mon Feb 02 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.4
- Fix preun script which was calling gconftool on straw rather than gnotime.
- Add desktop-file-utils Requires and use them to (re)install the .desktop
  file so we can add --vendor and --add-category X-Fedora
- Add StartupNotify to the desktop file

* Wed Dec 31 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.3
- Change the build process back to patching as there is no consensus and I
  agree with the patching argument rather than autogen-in-spec argument.
- Make sure the gconf schema gets installed into the sysconfigdir
- Use gconftool-2 in the post/postun scripts to install the schema into gconf.
- Make scrollkeeper non-optional.  Since most other fedora packages using
  scrollkeeper require it and not having scrollkeeper tends to make help
  unusable.

* Sun Dec 28 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.2
- Fix up the BuildRequires -- if one package will pull in another
  automatically, then do not explicitly list it.
- Change the build process.  Instead of generating a post-autogen patch and
  patching the distributed source, run autogen.sh to regenerate the build
  infrastructure.  (This is necessary in the first place because the doc
  build structure needed to be modified.)

* Mon Dec 15 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.1
- Initial Fedora RPM release.
- Partially adapted from the gnotime.spec.in by Eric Anderson
  <eric.anderson[AT]cordata.net> from the Red Hat directory in the gnotime
  distribution.
