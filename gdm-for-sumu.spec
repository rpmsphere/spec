%define _default_patch_fuzz 2

%define libselinuxver 1.27.7
%define libauditver 1.0.6
%define pango_version 1.2.0
%define gtk2_version 2.6.0
%define libglade2_version 2.0.0
%define libgnomeui_version 2.2.0
%define libgnomecanvas_version 2.0.0
%define librsvg2_version 2.0.1
%define libxml2_version 2.4.21
%define scrollkeeper_version 0.3.4
%define pam_version 0.75
%define gail_version 1.2.0
%define nss_version 3.11.1

Summary: The GNOME Display Manager for SUMU.
Name: gdm-for-sumu

# When re-basing to upstream GDM change it's version-release
# When adding new patches or ortherwise update the package
# change the otb.X relase only

# the upstream GDM release
Version: 2.16.0
# update only minor release number
Release: 56.5
# don't change
Epoch: 1

License: LGPL/GPL
Group: User Interface/X
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gdm
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gdm/gdm-%{version}.tar.bz2
Source1: gdm-pam
Source2: gdm-autologin-pam
Source3: gdmsetup-pam
Source4: po.tar.gz
# additional sources
Source5: ltmain.sh.rhel6
Source6: LINGUAS.bg

Patch1: gdm-2.16.0-change-defaults.patch
Patch4: gdm-2.13.0.4-update-switchdesk-location.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=301817
Patch6: gdm-2.8.0.2-clean-up-xsession-errors.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=301826
Patch7: gdm-2.8.0.2-merge-resources.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=349835
Patch12: gdm-2.13.0.4-audit-login.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=347798
Patch19: gdm-2.15.5-move-default-message.patch
Patch20: gdm-2.15.5-reset-pam.patch
# disabled, no smart card support for SUMU
#Patch21: gdm-2.16.0-security-tokens.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=347871
Patch24: gdm-2.15.6-wtmp.patch

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=203917
Patch25: gdm-2.16.0-indic-langs.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=357998
Patch26: gdm-2.16.0-markup.patch
Patch27: gdm-2.16.0-close.patch

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=201344
Patch28: gdm-2.16.0-desensitize-entry.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=362853
Patch29: gdm-2.16.0-photo-setup-help.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=378724
Patch30: gdm-2.16.0-punjabi.patch

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=210378
Patch32: gdm-2.16.0-reread-lang.patch

Patch33: gdm-2.16.0-cve-2006-6105.patch

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=220370
Patch34: gdm-2.16.0-fix-language-crash.patch

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=247655
Patch35: gdm-2.16.0-CVE-2007-3381.patch

# https://bugzilla.redhat.com/349721
Patch36: gdm-2.16.0-fix-system-menu-crash.patch

# https://bugzilla.redhat.com/223585
Patch37: gdm-2.16.0-fix-last-language.patch

# https://bugzilla.redhat.com/232896
Patch38: gdm-2.16.0-verify-check.patch

# https://bugzilla.redhat.com/238482
Patch39: gdm-2.16.0-fix-timed-login-booboo.patch

# https://bugzilla.redhat.com/223192
patch40: gdm-2.16.0-drop-console-translations.patch

# https://bugzilla.redhat.com/473262
patch41: gdm-2.16.0-drop-xinput-hack.patch

# https://bugzilla.redhat.com/474588
Patch42: gdm-2.16.0-handle-unplugged-devices.patch

# https://bugzilla.redhat.com/441971
Patch43: gdm-2.16.0-make-ctrl-alt-backspace-more-robust.patch

# https://bugzilla.redhat.com/226931
Patch44: gdm-2.16.0-add-te.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=239818
# https://bugzilla.redhat.com/show_bug.cgi?id=181302
Patch45: gdm-2.16.0-fix-tcp-wrappers-check.patch

Patch99: gdm-2.16.0-prune-language-list.patch
Patch100: gdm-sumu-no-docs.patch


Requires(pre): /usr/sbin/useradd
Requires(pre): /usr/bin/scrollkeeper-update
# https://bugzilla.redhat.com/show_bug.cgi?id=458331
Requires(pre): setup >= 2.5.58
Requires: gtk2 >= 0:%{gtk2_version}
Requires: libglade2 >= 0:%{libglade2_version}
Requires: libgnomeui >= 0:%{libgnomeui_version}
Requires: libgnomecanvas >= 0:%{libgnomecanvas_version}
Requires: librsvg2 >= 0:%{librsvg2_version}
Requires: libxml2 >= 0:%{libxml2_version}
Requires: pam >= 0:%{pam_version}
Requires: /etc/pam.d/system-auth
Requires: usermode
Requires: /sbin/nologin
Requires: system-logos
Requires: xorg-x11-server-utils
Requires: xorg-x11-xkb-utils
Requires: xorg-x11-xinit
Conflicts: gdm >= 2.16.0-56
BuildRequires: scrollkeeper >= 0:%{scrollkeeper_version}
BuildRequires: pango-devel >= 0:%{pango_version}
BuildRequires: gtk2-devel >= 0:%{gtk2_version}
BuildRequires: libglade2-devel >= 0:%{libglade2_version}
BuildRequires: libgnomeui-devel >= 0:%{libgnomeui_version}
BuildRequires: libgnomecanvas-devel >= 0:%{libgnomecanvas_version}
BuildRequires: librsvg2-devel >= 0:%{librsvg2_version}
BuildRequires: libxml2-devel >= 0:%{libxml2_version}
BuildRequires: usermode
BuildRequires: pam-devel >= 0:%{pam_version}
BuildRequires: fontconfig
BuildRequires: gail-devel >= 0:%{gail_version}
BuildRequires: libgsf-devel
BuildRequires: libtool automake autoconf
BuildRequires: libcroco-devel
BuildRequires: libattr-devel
BuildRequires: gettext 
BuildRequires: gnome-doc-utils
BuildRequires: libdmx-devel
BuildRequires: libselinux-devel >= %{libselinuxver}
BuildRequires: audit-libs-devel >= %{libauditver}
BuildRequires: intltool
BuildRequires: tcp_wrappers-devel
%ifnarch s390 s390x ppc64
BuildRequires: xorg-x11-server-Xorg
%endif
BuildRequires: nss-devel >= %{nss_version}
Requires: libselinux >= %{libselinuxver}
Requires: audit-libs >= %{libauditver}
Requires: login-theme-sumu >= 3.0.4

%description
This version of the GNOME Display Manager is a special edition
compiled to run with multi-seat workstations SUMU. DO NOT USE
this version as the system default display manager.

%prep
%setup -q -n gdm-%{version}

# pull in newer translations
tar xzf %{SOURCE4}

%patch1 -p1 -b .change-defaults
%patch4 -p1 -b .update-switchdesk-location
%patch6 -p1 -b .clean-up-xsession-errors
%patch7 -p1 -b .merge-resources
%patch12 -p1 -b .audit-login
%patch19 -p1 -b .move-default-message
%patch20 -p1 -b .reset-pam
# disabled for SUMU
#%patch21 -p1 -b .security-tokens
%patch24 -p1 -b .wtmp
%patch25 -p1 -b .indic-langs
%patch26 -p1 -b .markup
%patch27 -p1 -b .close 
%patch28 -p1 -b .desensitize-entry
#%patch29 -p1 -b .photo-setup-help
%patch30 -p1 -b .punjabi
%patch32 -p1 -b .reread-lang
%patch33 -p1 -b .cve-2006-6105
%patch34 -p1 -b .fix-language-crash
%patch35 -p1 -b .cve-2007-3381
%patch36 -p1 -b .fix-system-menu-crash
%patch37 -p1 -b .fix-last-language
%patch38 -p1 -b .verify-check
%patch39 -p1 -b .fix-timed-login-booboo
%patch40 -p1 -b .drop-console-translations
%patch41 -p1 -b .drop-xinput-hack
%patch42 -p1 -b .handle-unplugged-devices
%patch43 -p1 -b .make-ctrl-alt-backspace-more-robust
%patch44 -p1 -b .add-te
%patch45 -p1 -b .fix-tcp-wrappers-check
#%patch99 -p1 -b .prune-language-list
%patch100 -p1 -b .no-docs

%build
cp -f %{SOURCE1} config/gdm
cp -f %{SOURCE2} config/gdm-autologin
cp -f %{SOURCE3} gdmsetup-pam
cp -f %{SOURCE5} ltmain.sh

autoreconf
#intltoolize --force --copy
#aclocal-1.9
#libtoolize --force --copy
#automake-1.9 --add-missing
#autoconf
#autoheader
%configure --with-pam-prefix=%{_sysconfdir} \
	   --enable-console-helper \
	   --disable-scrollkeeper  \
	   --with-selinux
find po/ -name "*.po*" | grep -v bg | xargs rm -f
cp -f %{SOURCE6} po/LINGUAS
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Init
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/PreSession
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/PostSession

make install DESTDIR=$RPM_BUILD_ROOT

# remove all desktop files - not needed
find %{buildroot}/ -name "*.desktop" | xargs rm -f

# docs go elsewhere
rm -rf $RPM_BUILD_ROOT/%{_prefix}/doc

# create log dir
mkdir -p $RPM_BUILD_ROOT/var/log/gdm

# remove the gdm Xsession as we're using the xdm one
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Xsession
(cd $RPM_BUILD_ROOT%{_sysconfdir}/gdm; ln -sf ../X11/xinit/Xsession .)

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

# remove the other gnome session file, since we put it in gnome-session
rm -rf $RPM_BUILD_ROOT%{_datadir}/xsessions

# use consolehelper for gdmsetup
(cd $RPM_BUILD_ROOT/usr/bin; ln -sf consolehelper gdmsetup)

# broken install-data-local in gui/Makefile.am makes this necessary
(cd $RPM_BUILD_ROOT%{_bindir} && ln -sf gdmXnestchooser gdmXnest)

rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

# drop unsupported themes
rm -rf $RPM_BUILD_ROOT%{_datadir}/gdm/themes/*

%find_lang gdm

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -M -u 42 -d /var/gdm -s /sbin/nologin -r gdm > /dev/null 2>&1
/usr/sbin/usermod -d /var/gdm -s /sbin/nologin -a -G audio gdm >/dev/null 2>&1
# ignore errors, as we can't disambiguate between gdm already existed
# and couldn't create account with the current adduser.
exit 0

%post
/sbin/ldconfig
scrollkeeper-update

touch --no-create /usr/share/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q /usr/share/icons/hicolor
fi

# if the user already has a config file, then migrate it to the new
# location; rpm will ensure that old file will be renamed

custom=/etc/gdm/custom.conf

if [ $1 -ge 2 ] ; then
    if [ -f /usr/share/gdm/config/gdm.conf-custom ]; then
	oldconffile=/usr/share/gdm/config/gdm.conf-custom
    elif [ -f /etc/X11/gdm/gdm.conf ]; then
	oldconffile=/etc/X11/gdm/gdm.conf
    fi

    # Comment out some entries from the custom config file that may
    # have changed locations in the update.  Also move various
    # elements to their new locations.

    [ -n "$oldconffile" ] && sed \
    -e 's@^command=/usr/X11R6/bin/X@#command=/usr/bin/Xorg@' \
    -e 's@^Xnest=/usr/X11R6/bin/Xnest@#Xnest=/usr/X11R6/bin/Xnest@' \
    -e 's@^BaseXsession=/etc/X11/xdm/Xsession@#BaseXsession=/etc/X11/xinit/Xsession@' \
    -e 's@^BaseXsession=/etc/X11/gdm/Xsession@#&@' \
    -e 's@^BaseXsession=/etc/gdm/Xsession@#&@' \
    -e 's@^Greeter=/usr/bin/gdmgreeter@#Greeter=/usr/libexec/gdmgreeter@' \
    -e 's@^RemoteGreeter=/usr/bin/gdmlogin@#RemoteGreeter=/usr/libexec/gdmlogin@' \
    -e 's@^GraphicalTheme=Bluecurve@#&@' \
    -e 's@^BackgroundColor=#20305a@#&@' \
    -e 's@^DefaultPath=/usr/local/bin:/usr/bin:/bin:/usr/X11R6/bin@#&@' \
    -e 's@^RootPath=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/X11R6/bin@#&@' \
    -e 's@^HostImageDir=/usr/share/hosts/@#HostImageDir=/usr/share/pixmaps/faces/@' \
    -e 's@^LogDir=/var/log/gdm@#&@' \
    -e 's@^PostLoginScriptDir=/etc/X11/gdm/PostLogin@#&@' \
    -e 's@^PreLoginScriptDir=/etc/X11/gdm/PreLogin@#&@' \
    -e 's@^PreSessionScriptDir=/etc/X11/gdm/PreSession@#&@' \
    -e 's@^PostSessionScriptDir=/etc/X11/gdm/PostSession@#&@' \
    -e 's@^DisplayInitDir=/var/run/gdm.pid@#&@' \
    -e 's@^RebootCommand=/sbin/reboot;/sbin/shutdown -r now;/usr/sbin/shutdown -r now;/usr/bin/reboot@#&@' \
    -e 's@^HaltCommand=/sbin/poweroff;/sbin/shutdown -h now;/usr/sbin/shutdown -h now;/usr/bin/poweroff@#&@' \
    -e 's@^ServAuthDir=/var/gdm@#&@' \
    -e 's@^Greeter=/usr/bin/gdmlogin@Greeter=/usr/libexec/gdmlogin@' \
    -e 's@^GraphicalTheme=Default@#&@' \
    -e 's@^RemoteGreeter=/usr/bin/gdmgreeter@RemoteGreeter=/usr/libexec/gdmgreeter@' \
    $oldconffile > $custom
fi

if [ $1 -ge 2 -a -f $custom ] && grep -q /etc/X11/gdm $custom ; then
   sed -i -e 's@/etc/X11/gdm@/etc/gdm@g' $custom
fi

/usr/sbin/gdm-safe-restart >/dev/null 2>&1 || :

%postun
/sbin/ldconfig
scrollkeeper-update
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f gdm.lang
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO

%dir %{_sysconfdir}/gdm
%{_sysconfdir}/gdm/Xsession
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
# disabled for sumu
#%config %{_sysconfdir}/gdm/securitytokens.conf
%config %{_sysconfdir}/gdm/XKeepsCrashing
%config %{_sysconfdir}/gdm/locale.alias
%config %{_sysconfdir}/gdm/Init/*
%config %{_sysconfdir}/gdm/PostLogin/*
%config %{_sysconfdir}/gdm/PreSession/*
%config %{_sysconfdir}/gdm/PostSession/*
%config %{_sysconfdir}/gdm/modules/*
%config %{_sysconfdir}/pam.d/gdm
%config %{_sysconfdir}/pam.d/gdmsetup
%config %{_sysconfdir}/pam.d/gdm-autologin
%config %{_sysconfdir}/security/console.apps/gdmsetup
%dir %{_sysconfdir}/gdm/Init
%dir %{_sysconfdir}/gdm/PreSession
%dir %{_sysconfdir}/gdm/PostSession
%dir %{_sysconfdir}/gdm/PostLogin
%dir %{_sysconfdir}/gdm/modules
%{_datadir}/pixmaps
%{_datadir}/icons
%{_datadir}/gdm
%{_datadir}/applications
%{_libdir}/gtk-2.0/modules/*.so
%{_bindir}/*
%{_libexecdir}/*
%{_sbindir}/*
%dir %{_localstatedir}/log/gdm

%attr(1770, root, gdm) %dir %{_localstatedir}/gdm

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Nov 23 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Nov 06 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 1:2.16.0-56_5.el6otb
- disable gdm-rh-security-token-helper - this causes unnecessary SELinux errors
  and is not used for multi-seat configurations.

* Tue Nov 02 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 1:2.16.0-56_4.el6otb
- use el6otb as dist tag

* Fri Oct 29 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 1:2.16.0-56.otb.3
- fix the Requires on login-theme-sumu so theme can be updated later

* Mon Sep 13 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 1:2.16.0-56.otb.2
- rename the package to gdm-for-sumu
- add comments about versioning
- added Conflicts with the stock gdm package
- added Requires for the login theme

* Sat Sep 11 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 1:2.16.0-56.otb.1
- branch off own version
- change obsolete Prereq to Requires(pre)
- change PACKAGE_VERSION macro to version
- update BuildRoot to current packaging guidelines
- update Name and Description
- remove the -docs subpackage
- define default patch fuzz level
- use updated copy of ltmain.sh from libtool-2.2.6-15.5.el6
- change BuildRequires tcp_wrappers to tcp_wrappers-devel
  because the -devel package split from the main one
- remove translations that we don't need and add our own LINGUAS file
- add patch to skip building of docs and remove doc related dirs
- don't package any .desktop files and remove related files/actions/dependencies

* Fri May 15 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-56
- Resolves: #239818 181302
- Fix tcp wrappers detection on 64-bit

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-55
Resolves: #196054
- Fix docs subpackage Requires

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-53
Resolves: #196054
- Add docs subpackage

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-52
Resolves: #226931
- Add te_IN translations

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-51
Resolves: #441971
- Make ctrl-alt-backspace at the login screen more robust

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-50
Resolves: #458331
- Add GDM to audio group by default.

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-49
Resolves: #474588
- Don't crash if defined extended input device is unplugged
  Patch by Olivier Fourdan.

* Tue May 12 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-48
Resolves: #239818
- Rebuild with tcp_wrappers build requires

* Fri Jan 23 2009 Ray Strode <rstrode@redhat.com> - 1:2.16.0-47
Resolves: #473262
- Fix pointer on tablet devices.

* Fri Mar 29 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-46
Resolves: #215855
- Work around issue in SECMOD_CancelWait() that was preventing
  smart card helper from exiting

* Thu Mar 28 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-45
Resolves: #215855
- Refinement to last patch to better manage new smart card helper

* Mon Mar 17 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-44
Resolves: #215855
- More work on pcsc-lite getting confused after fork

* Mon Mar 10 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-43
Resolves: #223192
- Drop more messages I missed

* Thu Mar  6 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-42
Resolves: #223192
- Drop even more consoles message translations that were found
  during qa testing

* Tue Feb 12 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-41
Resolves: #223192
- Drop more consoles message translations that were found
  during qa testing

* Fri Jan 18 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-40
Resolves: #210827
- Only honor cancel requests when blocking in the pam conversation
  waiting for user input (the only time it makes sense to cancel).
  Doing it at other times was causing spurious "authentication failure"
  messages.

* Thu Jan 17 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-39
Resolves: #215855
- Work around issue where PKCS11 module gets confused after fork

* Tue Jan 15 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-38
Resolves: #223192
- Drop translations of console messages in locales that the console
  doesn't support

* Mon Jan 14 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-37
Resolves: #238482
- Remove superfluous username from the end of timed login message

* Mon Jan 14 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-36
Resolves: #253563
- Write utmp entries again

* Mon Jan 14 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-35
Resolves: #232896
- Remove unneccesary code that was creating spurious audit
  entries.  Patch by Tomas Mraz.
- apply patch mentioned in last changelog entry

* Mon Jan 14 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-34
Resolves: #223585
- Fix problem in chinese translation.  Patch by Huang Peng.

* Fri Jan 11 2008 Ray Strode <rstrode@redhat.com> - 1:2.16.0-33
Resolves: #349721
- Fix gdm crash after kde indirect session

* Mon Jul 30 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.0-31.0.1
- CVE-2007-3381
Resolves: 247659

* Mon Jan  8 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.0-31
- change 200d character to 200c character in ml.po 

* Mon Jan  8 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.0-30
Resolves: #220370
- add function prototypes to fix crash in language selector on
x86-64.  Patch by Bill Nottingham.

* Mon Jan  8 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.0-29
Resolves: #219121
- drop in ml.po file

* Fri Dec 15 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-28
- Fix CVE-2006-6105

* Thu Dec 14 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-26
- Update translations from upstream (#219121)

* Sun Dec 10 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-25
Resolves: #210378
- Apply patch to flush translation cache when locale changes 

* Thu Dec  7 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-24
Resolves: #210378
- The patch from -23 and -23 needed a bit of work to get the
  entire screen to update.

* Wed Dec  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-23
Resolves: #210378
- actually apply patch mentioned in 2.16.0-22

* Wed Dec  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-22
Resolves: 210378
- reread system locale on slave startup (bug 210378)

* Wed Dec  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-21
Resolves: 218441
- fix chinese, patch Peng Huang <phaung@redhat.com> 

* Mon Nov 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-20
- Use Punjabi, not Panjabi (#217122)

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-19
- Fix a segfault in the language pruning patch (#204044)
 
* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-18
- Make photosetup help button work (#198138)
- Fix small issues in gdmsetup (#208225)

* Sun Oct 15 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-17.el5
- prefer secmod db security token driver over hard coded 

* Sat Oct 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-16.el5
- have security token monitor helper process kill itself when
  the communication pipe to the main process goes away (bug
  210677).

* Thu Oct 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-15.el5
- desensitize entry fields until pam asks for input, so if pam
  doesn't initially ask for input (like in smart card required
  mode) the user can't type something and confuse gdm (bug 201344)

* Fri Oct  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-14.el5
- Migrate users config from RHEL4 theme to RHEL5 theme on upgrade
  (bug 205091)

* Fri Oct  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-13.el5
- Add -br to X command line to ensure we get a black root window on
  start up.

* Thu Oct  5 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-12.el5
- make smart card event monitoring more reliable (bug 208018)

* Wed Sep 20 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-10.el5
- reset pam patch didn't get updated in 2.16.0-5.el5 sync up

* Tue Sep 19 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-9.el5
- Add as_IN, si_LK to language list (bug 203917) 

* Mon Sep 18 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-8.el5
- fix a problem in the smart card forking code

* Mon Sep 18 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-7.el5
- fix a problem in the driver loading code (bug 206882)

* Fri Sep 15 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-6.el5
- don't leak pipe fds (bug 206709)

* Thu Sep 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-5.el5
- resync from fc6 branch
- drop junky themes

* Thu Sep 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0-4.fc6
- update security token patch to not poll

* Fri Sep  8 2006 Jesse Keating <jkeating@redhat.com> - 1:2.16.0-3.fc6
- Apply correct defaults patch

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-2.fc6
- Change the default theme to FedoraDNA
- Bump redhat-artwork requirement

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-1.fc6
- Update to 2.16.0

* Sat Aug 26 2006 Karsten Hopp <karsten@redhat.com> - 1:2.15.10-2.fc6
- buildrequire inttools as this isn't a requirement of scrollkeeper anymore
  and thus missing from the buildroot

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.10-1.fc6
- Update to 2.15.10
- Drop upstreamed patch

* Fri Aug 4 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.9-1
- update to 2.15.9

* Fri Aug 4 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.7-2
- update gdmsetup pam file to use config-util stacks

* Thu Aug 3 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.7-1
- update to 2.15.7
- drop selinux patch that I don't think was ever finished

* Thu Aug 3 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-14
- fix face browser
  (http://bugzilla.gnome.org/show_bug.cgi?id=349640)
- fix error message reporting
  (http://bugzilla.gnome.org/show_bug.cgi?id=349758)

* Sun Jul 23 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-13.el5
- resync from fc6 branch

* Fri Jul 21 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-13
- simply all the security token code by only using one pam stack
- drop lame kill on token removal feature

* Fri Jul 21 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-12
- move authcookies out of home directories to prevent problems
  on nfs/afs mounted home directories (bug 178233).

* Fri Jul 21 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-11
- really fix annoying dialog problem mentioned in 2.15.6-6

* Wed Jul 19 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-10
- center cursor on xinerama head (bug 180085)

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> -  1:2.15.6-10.el5
- turn back on graphical greeter

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> -  1:2.15.6-9.el5
- add RHEL-4 prune languages patch
- merge latest fc6 changes 

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-9
- add "kill all sessions on token removal" feature

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-8
- reenable session keyring support in pam module (bug 198629)

* Mon Jul 17 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-7
- make security token support use its own config file in
  preparation for modularizing it.

* Mon Jul 17 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-6
- fix off-by-one in the process-all-ops patch that was causing
  an anoying dialog to pop up on each login

* Sun Jul 16 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-5
- add initial wtmp and btmp logging support

* Fri Jul 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-4
- fix bug in security token support

* Fri Jul 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-3
- fix hang in gdmsetup

* Fri Jul 14 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-2
- put new pam module at top of stack (bug 198629)

* Wed Jul 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.6-1
- Update to 2.15.6

* Wed Jul 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.5-4
- add new pam module to pam files to support kernel session keyring

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.15.5-3.1
- rebuild

* Tue Jul 11 2006 Ray Strode <rstrode@redhat.com> 1:2.15.5-3
- add initial support for smart card security tokens

* Fri Jul 7 2006 Ray Strode <rstrode@redhat.com> 1:2.15.5-2
- add patch to process all operations when more than one comes
  in really quickly
- move default "Please enter your username" message to the
  greeter instead of the slave so that it doesn't get stacked if
  a pam module has a non default message
- add new message for reseting the current login operation
  (like the cancel button does, but accessible via the gdm fifo)

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> 1:2.15.5-1
- Update to 2.15.5

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> 1:2.15.3-8
- replace automake14 buildreq with automake

* Thu Jun  8 2006 Ray Strode <rstrode@redhat.com> 1:2.15.3-7
- fix CVE-2006-2452

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1:2.15.3-6
- buildrequire the server so that we get the path right in the config file

* Tue Jun 06 2006 Karsten Hopp <karsten@redhat.de> 1:2.15.3-5
- buildrequire libdmx-devel

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-4
- Require system-logos, not fedora-logos

* Tue May 23 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.3-3
- Support xdm -nodaemon option (bug 192461)

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-2
- Add missing BuildRequires (#192494)

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-1
- Update to 2.15.3

* Wed May 10 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.0-1
- Update to 2.15.0

* Wed Apr 26 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.14.4-2
- Update to 2.14.4

* Wed Apr 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.14.1-4
- fix libexecdir substitution problem in configuration file

* Tue Apr 11 2006 Ray Strode <rstrode@redhat.com> - 1:2.14.1-3
- Add gdmthemetester.in to the mix (upstream bug 338079)

* Tue Apr 11 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.14.1-2
- Update to 2.14.1

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 1:2.14.0-1
- Update to 2.14.0

* Tue Mar  7 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.9-4
- Follow Solaris's lead and default to AlwaysRestartServer=True
  (may work around bug 182957)

* Mon Mar  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.9-3
- migrate users with baseXsession=/etc/X11/gdm/Xsession to
  /etc/X11/xinit/Xsession

* Mon Mar  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.9-2
- disable sounds completely when disabled in configuration file
 (upstream bug 333435)

* Tue Feb 28 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.9-1
- Update to 2.13.0.9
- Use new %%post section, written by 
  Michal Jaegermann <michal@harddata.com> (bug 183082)

* Sat Feb 25 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.8-6
- fix a broken link

* Fri Feb 24 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.8-5
- change some /etc/X11 bits in the spec file to /etc

* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.8-3
- add server entry for accel-indirect branch of xorg

* Wed Feb 15 2006 Ray <rstrode@redhat.com> and Matthias <mclasen@redhat.com> - 1:2.13.0.8-2
- malloc memory that is later freed

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.8-1
- update to 2.13.0.8

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.7.0.2006.02.12-2
- migrate custom.conf settings with /etc/X11/gdm to /etc/gdm

* Sun Feb 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.7.0.2006.02.12-1
- update to cvs snapshot
- move gdm to /etc instead of /etc/X11
- move custom gdm.conf to sysconfdir instead of symlinking from
  datadir (bug 180364)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.0.7-2.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.0.7-2
- Make gdmsetup use consolehelper
- Don't use deprecated pam_stack

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.0.7-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.7-1
- update to 2.13.0.7

* Mon Jan 30 2006 Bill Nottingham <notting@redhat.com>
- silence gdm-safe-restart

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.5-7
- sed -ie isn't the same as sed -i -e (we want the latter)

* Wed Jan 18 2006 Christopher Aillon <caillon@redhat.com> - 1:2.13.0.5-6
- Add patch to fix clock to default to 24h in locales that expect it (175453)

* Tue Jan 17 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.5-1
- update to 2.13.0.5 (bug 178099)

* Tue Jan 17 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.4-5
- add new theme by Diana Fong, Máirín Duffy, and me

* Mon Jan 16 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.4-4
- improve migration snippet (bug 177443). 

* Fri Jan 13 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.4-3
- migrate X server configuration for pre-modular X configurations.
  Problems reported by Dennis Gregorovic <dgregor@redhat.com>

* Mon Jan 9 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.4-2
- use xinit Xsession again.

* Mon Jan 9 2006 Ray Strode <rstrode@redhat.com> - 1:2.13.0.4-1
- update to 2.13.0.4

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 16 2005 Ray Strode <rstrode@redhat.com> - 1:2.8.0.4-13
- Don't fallback to xsm, try gnome-session instead
- Require xorg-x11-xinit

* Mon Nov 14 2005 Ray Strode <rstrode@redhat.com> - 1:2.8.0.4-12
- Make sure that dbus-launch gets called if available

* Mon Nov 14 2005 Ray Strode <rstrode@redhat.com> - 1:2.8.0.4-11
- Don't use X session / setup files anymore.
- Don't install early login init scripts
- remove xsri dependency
- don't prune language lists anymore

* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> - 1:2.8.0.4-10
- also fix default xsession for where its moved in modular X

* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> - 1:2.8.0.4-9
- change requirements for modular X
- patch to find x server with modular X

* Thu Oct 20 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.4-8
- redhat-artwork was busted, require new version

* Tue Oct 18 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.4-7
- zero-initialize message buffer,
  bug fixed by Josh Parson (jbparsons@usdavis.edu) (bug 160603)
- fix typo in redhat-artwork requires line

* Mon Oct 17 2005 Steve Grubb <sgrubb@redhat.com> 1:2.8.0.4-6
- add login audit patch (bug 170569)

* Mon Oct 17 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.4-5
- bump redhat-artwork requirement to get rid of the boot
  throbber for now, since it seems to have reappeared
  mysteriously (bug 171025)

* Thu Oct 13 2005 Dan Walsh <dwalsh@redhat.com> 1:2.8.0.4-4
- Change to use getseuserbyname

* Thu Sep 28 2005 Dan Walsh <dwalsh@redhat.com> 1:2.8.0.4-3
- Fix selinux not to fail when in permissive mode

* Thu Sep 27 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.4-2
- remove flexiserver from menus

* Thu Sep  8 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.4-1
- update to 2.8.0.4

* Tue Sep  6 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.2-4
- Apply clean up patch from Steve Grubb (gnome bug 315388).

* Tue Aug 30 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.2-3
- Prune language list of installed languages
- Make config file noreplace again (bug 167087).

* Sat Aug 20 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.2-2
- hide throbber

* Fri Aug 19 2005 Ray Strode <rstrode@redhat.com> 1:2.8.0.2-1
- update to 2.8.0.2
- disable early login stuff temporarily

* Thu Aug 18 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-18
- rebuild

* Wed Aug 10 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-17
- Prune uninstalled languages from language list.

* Mon May 23 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-16
- Make sure username/password incorrect message gets displayed
  (bug 158127).
- reread system locale before starting gdm in early login mode 
  (bug 158376).

* Thu May 19 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-15
- Take out some syslog spew (bug 157711).

* Thu May 12 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-14
- Fix processing of new-line characters that got broken
  in 2.6.0.8-11 (bug 157442).

* Tue May  3 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-12
- Fix processing of non-ascii characters that got broken
  in 2.6.0.8-11, found by Miloslav Trmac <mitr@redhat.com>,
  (bug 156590).

* Thu Apr 28 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-11
- Fix halt command (bug 156299)
- Process all messages sent to the greeter in a read, not just
  the first

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1:2.6.0.8-10
- silence %%postun

* Tue Apr 26 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-9
- Change default standard greeter theme to clearlooks and 
  default graphical greeter theme to Bluecurve specifically.

- Change default path values (bug 154280)

* Mon Apr 25 2005 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.8-8
- for early-login, delay XDMCP initialization until allow-login

* Sun Apr 24 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-7
- calling gdm_debug and g_strdup_printf from signal handlers are
  bad news (Spotted by Mark McLoughlin <markmc@redhat.com>).

* Tue Apr 19 2005 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.8-6
- Add a throbber for early login

* Mon Apr 18 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-5
- Don't install gnome.desktop to /usr/share/xsessions (bug 145791)

* Thu Apr 14 2005 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.8-4
- Don't do early-login if firstboot is going to run
- Make early-login work with timed and automatic logins

* Wed Apr 13 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-3
- Don't hard code dpi setting to 96.0, but instead look at
  Xft.dpi

* Wed Apr 13 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-2
- touch /var/lock/subsys/gdm-early-login so gdm gets killed on
  runlevel changes (bug 154414)
- don't try to use system dpi settings for canvas text (bug 127532)
- merge resource database from displays other than :0

* Sat Apr  2 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.8-1
- update to 2.6.0.8
- add new init scripts to support early-login mode

* Tue Mar 29 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.7-8
- Add a --wait-for-bootup cmdline option.

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1:2.6.0.7-6
- Update the GTK+ theme icon cache on (un)install

* Fri Mar 11 2005 Alexandre Oliva <aoliva@redhat.com> 1:2.6.0.7-5
- fix patch for bug 149899 (fixes bug 150745)

* Wed Mar 09 2005 Than Ngo <than@redhat.com> 1:2.6.0.7-4
- add OnlyShowIn=GNOME;

* Mon Feb 28 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.7-3
- seteuid/egid as user before testing for presence of
  user's home directory (fixes bug 149899)

* Thu Feb 10 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.7-2
- Turn off "switchdesk" mode by default which accidentally got 
  turned on by default in 2.6.0.5-4

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.7-1
- Update to 2.6.0.7

* Tue Jan 25 2005 Ray Strode <rstrode@redhat.com> 1:2.6.0.5-11
- Fix bug in greeter sort-session-list patch where selecting
  a session did nothing (bug 145626)

* Thu Dec 9 2004 Dan Walsh <dwalsh@redhat.com> 1:2.6.0.5-10
- Remove pam_selinux from gdmsetup pam file

* Wed Dec  1 2004  Ray Strode  <rstrode@redhat.com> 1:2.6.0.5-9 
- Look up and use username instead of assuming that user entered 
  login is cannonical.  Patch from
  Mike Patnode <mike.patnode@centrify.com> (fixes bug 141380).

* Thu Nov 11 2004  Ray Strode  <rstrode@redhat.com> 1:2.6.0.5-8 
- Sort session list so that default session comes out on top
  (fixes bug 107324)

* Wed Nov 10 2004  Ray Strode  <rstrode@redhat.com> 1:2.6.0.5-7 
- Make desktop file symlink instead of absolute (bug 104390)
- Add flexiserver back to menus

* Wed Oct 20 2004  Ray Strode  <rstrode@redhat.com> 1:2.6.0.5-6 
- Clean up xses if the session was successfullly completed.
  (fixes bug #136382)

* Tue Oct 19 2004  Ray Strode  <rstrode@redhat.com> 1:2.6.0.5-5 
- Prefer nb_NO over no_NO for Norwegian (fixes bug #136033)

* Thu Oct  7 2004 Alexander Larsson <alexl@redhat.com> - 1:2.6.0.5-4
- Change default greeter theme to "Default", require 
  redhat-artwork with Default symlink.

* Wed Sep 29 2004 Ray Strode <rstrode@redhat.com> 1:2.6.0.5-3
- Check if there is a selected node before using iterator.
  (fixes bug #133329).

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> 1:2.6.0.5-2
- Don't mess with gdmphotosetup categories.  Upstream categories
  are fine.

* Mon Sep 20 2004 Ray Strode <rstrode@redhat.com> 1:2.6.0.5-1
- update to 2.6.0.5

* Tue Aug 3 2004 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.3-5
- fix messed up changelog

* Tue Aug 3 2004 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.3-4
- rebuilt

* Thu Aug 2 2004 Ray Strode <rstrode@redhat.com> 1:2.6.0.3-3
- rebuilt

* Mon Jul 26 2004 Bill Nottingham <notting@redhat.com> 1:2.6.0.3-2
- fix theme (#128599)

* Thu Jun 17 2004 Ray Strode <rstrode@redhat.com> 1:2.6.0.3-1
- update to 2.6.0.3 (fixes bug #117677)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 21 2004 Matthias Clasen <mclasen@redhat.com> 1:2.6.0.0-5
- rebuild

* Mon May 17 2004 Than Ngo <than@redhat.com> 1:2.6.0.0-4
- add patch to build gdm-binary with PIE

* Thu Apr 22 2004 Mark McLoughlin <markmc@redhat.com> - 1:2.6.0.0-3
- Update the "use switchdesk" message to only be display when
  switchdesk-gui is installed and to not reference a non existant
  menu item (bug #121460)

* Fri Apr  2 2004 Colin Walters <walters@redhat.com> 1:2.6.0.0-2
- Always put session errors in /tmp, in preparation for
  completely preventing gdm from writing to /home/

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 1:2.6.0.0-1
- update to 2.6.0.0

* Tue Mar 16 2004 Dan Walsh <dwalsh@redhat.com> 1:2.5.90.3-1
- Use selinux patch again

* Tue Mar 16 2004 Dan Walsh <dwalsh@redhat.com> 1:2.5.90.3-1
- Stop using selinux patch and use pam_selinux instead.

* Wed Mar 10 2004 Alex Larsson <alexl@redhat.com> 1:2.5.90.2-1
- update to 2.5.90.2

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.90.1-1
- update to 2.5.90.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 03 2004 Warren Togami <wtogami@redhat.com> 1:2.4.4.5-9
- add two lines to match upstream CVS to xdmcp_sessions.patch
  Fully resolves #110315 and #113154

* Sun Feb 01 2004 Warren Togami <wtogami@redhat.com> 1:2.4.4.5-8
- patch30 xdmcp_session counter fix from gdm-2.5.90.0 #110315
- automake14 really needed, not automake
- BR libcroco-devel, libcroco-devel, libattr-devel, gettext
- conditionally BR libselinux-devel
- explicit epoch in all deps
- make the ja.po time format change with a sed expression rather than
  overwriting the whole file (Petersen #113995)

* Thu Jan 29 2004 Jeremy Katz <katzj@redhat.com> - 1:2.4.4.5-7
- fix build with current auto*

* Tue Jan 27 2004 Jeremy Katz <katzj@redhat.com> 1:2.4.4.5-5
- try a simple rebuild for libcroco abi change

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.5-4
- Fix call to is_selinux_enabled

* Fri Jan 16 2004 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.5-3
- Use /sbin/reboot and /sbin/poweroff instead of consolehelper version

* Thu Oct 30 2003 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.5-2.sel
- turn on SELinux

* Mon Oct 20 2003 Jonathan Blandford <jrb@redhat.com> 2:2.4.4.5-1
- get rid of the teal

* Fri Oct 17 2003 Jonathan Blandford <jrb@redhat.com> 1:2.4.4.5-1
- new version

* Thu Oct  9 2003 Jonathan Blandford <jrb@redhat.com> 1:2.4.4.3-6.sel
- new patch from George to fix #106189
- change bg color in rhdefaults patch
- turn off SELinux

* Thu Oct 8 2003 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.3-6.sel
- turn on SELinux

* Tue Oct  7 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.4.3-5
- Fix greeter line-breaking crash (rest of #106189)

* Tue Oct  7 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.4.3-4
- Set the BaseXSession properly in the config.
- This fixes parts of bug #106189

* Mon Oct  6 2003 Havoc Pennington <hp@redhat.com> 1:2.4.4.3-3
- change DefaultSession=Default.desktop to DefaultSession=default.desktop
- SELinux off again

* Fri Oct 3 2003 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.3-2.sel
- turn on SELinux

* Thu Oct  2 2003 Havoc Pennington <hp@redhat.com> 1:2.4.4.3-1
- 2.4.4.3
- --without-selinux for now, since libselinux not in the buildroot

* Mon Sep 8 2003 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.0-4
- turn off SELinux

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 1:2.4.4.0-3.sel
- turn on SELinux

* Thu Sep  4 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.4.0-2
- Use the right default session (#103546)

* Wed Sep  3 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.4.0-1
- update to 2.4.4.0
- update to georges new selinux patch

* Fri Aug 29 2003 Elliot Lee <sopwith@redhat.com> 1:2.4.2.102-2
- Remove scrollkeeper files

* Tue Aug 26 2003 George Lebl <jirka@5z.com> 1:2.4.2.102-1
- updated to 2.4.2.102
- removed outdated patches
- Use Xsetup_0 only for :0 since that's the way it works
  for xdm
- remove the gnome.desktop file, its going into gnome-session

* Thu Aug 14 2003 Havoc Pennington <hp@redhat.com> 1:2.4.1.6-1
- update to latest bugfix version on george's advice
- remove setlocale patch that's upstream
- remove console setup patches that are upstream

* Thu Jun 12 2003 Dan Walsh <dwalsh@redhat.com> 2.4.1.3-9
- Port to SELinux

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Sun May 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- fix post: localstatedir -> _localstatedir

* Thu May  1 2003 Havoc Pennington <hp@redhat.com> 1:2.4.1.3-6
- enable UTF-8 for CJK

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Thu Feb 20 2003 Owen Taylor <otaylor@redhat.com>
- Run the error dialogs under /bin/sh --login, so we
  get lang.sh, and thus unicode_start running. Fixes
  the X-doesn't-start dialog showing up as random
  blinking characters.

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 1:2.4.1.3-2
- nuke buildreq Xft

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 1:2.4.1.3-1
- upgrade to 2.4.1.3

* Mon Feb  3 2003 Matt Wilson <msw@redhat.com> 1:2.4.1.1-6
- added gdm-2.4.1.1-64bit.patch to fix 64 bit crash in cookie
  generation (#83334)

* Mon Feb  3 2003 Owen Taylor <otaylor@redhat.com>
- Add patch to fix problem where setting LC_COLLATE=C would give LC_MESSAGES=wa_BE (#82019)

* Thu Jan 30 2003 Matt Wilson <msw@redhat.com> 1:2.4.1.1-3
- fix pam.d entry, pam_env wasn't properly patched
- disable optimizations on x86_64 to work around gcc bug

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 20 2003 Owen Taylor <otaylor@redhat.com>
- Upgrade to 2.4.1.1 (Fixes #81907)
- Redirect stdout of kill to /dev/null (#80814)

* Thu Jan  9 2003 Havoc Pennington <hp@redhat.com>
- 2.4.1.0
- add patch from george to ask "are you sure?" for shutdown/reboot since it's now just one click away

* Thu Dec 19 2002 Havoc Pennington <hp@redhat.com>
- 2.4.0.12
- update new patch for no-utf8-in-cjk
- drop patch to photo setup, now upstream
- drop confdocs patch now upstream
- move all the gdm.conf changes into single "rhconfig" patch
- remove "sid-fix" patch now upstream

* Mon Nov 11 2002 Nalin Dahyabhai <nalin@redhat.com> 2.4.0.7-14
- remove the directory part of module specifications from the PAM config files,
  allowing the same PAM config to work for either arch on multilib boxes

* Thu Sep  5 2002 Owen Taylor <otaylor@redhat.com>
- Change zh_CN entry in language menu to zh_CN.GB18030

* Thu Sep  5 2002 Akira TAGOH <tagoh@redhat.com> 2.4.0.7-12
- copied gdm-ja.po to ja.po.

* Mon Sep  2 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem where gdm was opening ~/.xsession-errors itself to bad effect

* Sat Aug 31 2002 Havoc Pennington <hp@redhat.com>
- include ja.po with new date format

* Wed Aug 28 2002 Havoc Pennington <hp@redhat.com>
- remove noreplace on gdm.conf #71309
- make gnome-gdmsetup absolute, #72910

* Wed Aug 28 2002 Havoc Pennington <hp@redhat.com>
- put /usr/X11R6/bin in path for now fixes #72781
- use proper i18n algorithm for word wrap, #71937
- remove greek text from language picker due to lack 
  of greek font
- reorder PAM config file #72657

* Wed Aug 28 2002 Havoc Pennington <hp@redhat.com>
- improve gdmsetup icon
- remove GNOME session, we will instead put it in gnome-session
- apply patch from george to make gdmphotosetup file selector 
  work

* Mon Aug 26 2002 Elliot Lee <sopwith@redhat.com> 2.4.0.7-6
- Patches for #64902, #66486, #68483, #71308
- post-install script changes from the gdm.spec mentioned in #70965
- noreplace on gdm.conf for #71309

* Sun Aug 25 2002 Havoc Pennington <hp@redhat.com>
- put in a patch from george to fix some setsid()/kill() confusion
  possibly fixing #72295
- turn off UseCirclesInEntry for now, fixes #72433

* Tue Aug 20 2002 Alexander Larsson <alexl@redhat.com>
- Set UseCirclesInEntry to true in config

* Thu Aug 15 2002 Havoc Pennington <hp@redhat.com>
- rename Gnome session to GNOME, this was just bugging me

* Thu Aug  8 2002 Havoc Pennington <hp@redhat.com>
- 2.4.0.7 with bugfixes George kindly did for me, 
  including mnemonics for the graphical greeter
- use Wonderland gtk theme for the nongraphical greeter
- remove patches that are now upstream

* Tue Jul 30 2002 Havoc Pennington <hp@redhat.com>
- update rhconfig patch
- use pam_timestamp for the config tool
- link to a desktop file in redhat-menus
- update .gnome2 patch, filed upstream bug
- 2.4.0.4
- rebuild with new gail, librsvg2

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Require redhat-artwork, make the default greeter theme Wonderland
- Look for all configuration in .gnome2 not .gnome. This avoids problems 
  with changes in the set of session/lang.
- Remove English from locale.alias, make most locales UTF-8
- Call find_lang with the right name

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild for new libs
- put gdm-autologin pam config file in file list, hope
  its absence wasn't deliberate
- use desktop-file-install

* Mon Jun 10 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Mon Jun 10 2002 Havoc Pennington <hp@redhat.com>
- 2.4.0.0

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 2.3.90.3

* Tue May 14 2002 Matt Wilson <msw@redhat.com> 2.3.90.2.90-1
- pulled from current CVS, named it 2.3.90.2.90-1

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- rebuild for new libs
- add URL tag

* Mon Feb 11 2002 Alex Larsson <alexl@redhat.com> 2.3.90.1.90-1
- Updated to a cvs snapshot that has the new greeter.

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide

* Tue Sep  4 2001 Havoc Pennington <hp@redhat.com>
- fix #52997 (ukrainian in language list)

* Fri Aug 31 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Wed Aug 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- set SESSION to true in console.apps control file

* Tue Aug 14 2001 Havoc Pennington <hp@redhat.com>
- change default title font to work in CJK, #51698

* Wed Aug  8 2001 Bill Nottingham <notting@redhat.com>
- fix %pre for using /var/gdm as home dir

* Sun Aug  5 2001 Nalin Dahyabhai <nalin@redhat.com>
- Tweak PAM setup for gdmconfig to match other consolehelper users

* Fri Aug  3 2001 Owen Taylor <otaylor@redhat.com>
- Set RUNNING_UNDER_GDM when running display init script
- Run xsri as the background program

* Thu Aug 02 2001 Havoc Pennington <hp@redhat.com>
- Change how session switching works, #49480
- don't offer to make Failsafe the default, #49479

* Thu Aug 02 2001 Havoc Pennington <hp@redhat.com>
- clean up some format string mess, and don't
  log username to syslog, #5681
- own some directories #50692

* Wed Aug 01 2001 Havoc Pennington <hp@redhat.com>
- require/buildrequire latest gnome-libs, to compensate
  for upstream crackrock. #50554

* Tue Jul 31 2001 Havoc Pennington <hp@redhat.com>
- get rid of GiveConsole/TakeConsole, bug #33710

* Sun Jul 22 2001 Havoc Pennington <hp@redhat.com>
- use Raleigh theme for gdm

* Thu Jul 19 2001 Havoc Pennington <hp@redhat.com>
- depend on usermode, xinitrc
 
* Thu Jul 19 2001 Havoc Pennington <hp@redhat.com>
- build requires pam-devel, should fix #49448

* Mon Jul 16 2001 Havoc Pennington <hp@redhat.com>
- log to /var/log/gdm/*

* Mon Jul 16 2001 Havoc Pennington <hp@redhat.com>
- make Halt... power off

* Tue Jul 10 2001 Havoc Pennington <hp@redhat.com>
- gdm user's homedir to /var/gdm not /home/gdm

* Mon Jul 09 2001 Havoc Pennington <hp@redhat.com>
- put pam.d/gdm back in file list

* Sun Jul 08 2001 Havoc Pennington <hp@redhat.com>
- upgrade to 2.2.3.1, pray this fixes more than it breaks

* Thu Jul 05 2001 Havoc Pennington <hp@redhat.com>
- add "rpm" user to those not to show in greeter 

* Tue Jul 03 2001 Havoc Pennington <hp@redhat.com>
- Upgrade to 2.2.3
- require usermode since configure script now checks for it

* Fri Jun 01 2001 Havoc Pennington <hp@redhat.com>
- Prereq for scrollkeeper-update

* Thu May 30 2001 Havoc Pennington <hp@redhat.com>
- New CVS snap with the "no weird sessions" options; 
  more default settings changes

* Wed May 30 2001 Havoc Pennington <hp@redhat.com>
- Change a bunch of default settings; remaining fixes will involve C hacking

* Wed May 30 2001 Havoc Pennington <hp@redhat.com>
- After, oh, 2 years or so, finally upgrade version and set
  release to 1. Remove all hacks and patches, pretty much;
  this will break a few things, will be putting them back 
  via GNOME CVS. All changes should go in 'gdm2' module in 
  CVS for now.

  This RPM enables all kinds of features that I'm going to turn
  off shortly, so don't get excited about them. ;-)

* Thu Mar 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- reinitialize pam credentials after calling initgroups() -- the
  credentials may be group memberships

* Mon Mar 19 2001 Owen Taylor <otaylor@redhat.com>
- Fix colors patch

* Thu Mar 15 2001 Havoc Pennington <hp@redhat.com>
- translations

* Mon Mar  5 2001 Preston Brown <pbrown@redhat.com>
- don't screw up color map on 8 bit displays

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- Don't define and use "ver" and "nam" at the top of the spec file
- use %%{_tmppath}

* Tue Feb 13 2001 Tim Powers <timp@redhat.com>
- don't allow gdm to show some system accounts in the browser bugzilla
  #26898

* Fri Jan 19 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese translation.

* Tue Jan 02 2001 Havoc Pennington <hp@redhat.com>
- add another close() to the fdleak patch, bugzilla #22794

* Sun Aug 13 2000 Owen Taylor <otaylor@redhat.com>
- Return to toplevel main loop and start Xdcmp if enabled
  (Bug #16106) 

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Wed Aug 02 2000 Havoc Pennington <hp@redhat.com>
- Requires Xsession script

* Wed Jul 19 2000 Owen Taylor <otaylor@redhat.com>
- Italian is better as it_IT than it_CH (bugzilla 12425)

* Mon Jul 17 2000 Jonathan Blandford <jrb@redhat.com>
- Don't instally gdmconfig as it doesn't work.

* Fri Jul 14 2000 Havoc Pennington <hp@redhat.com>
- Rearrange code to avoid calling innumerable system calls
  in a signal handler

* Fri Jul 14 2000 Havoc Pennington <hp@redhat.com>
- Verbose debug spew for infinite loop stuff

* Fri Jul 14 2000 Havoc Pennington <hp@redhat.com>
- Try to fix infinite loops on X server failure

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Havoc Pennington <hp@redhat.com>
- Remove Docdir

* Mon Jun 19 2000 Havoc Pennington <hp@redhat.com>
- Fix file descriptor leak (Bugzilla 12301)

* Mon Jun 19 2000 Havoc Pennington <hp@redhat.com>
- Apply security errata patch we released for 6.2
- Add Gnome.session back, don't know when it disappeared or why

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Fri May 19 2000 Havoc Pennington <hp@redhat.com>
- rebuild for the Winston tree

* Fri Feb 04 2000 Havoc Pennington <hp@redhat.com>
- Modify Default.session and Failsafe.session not to add -login option to bash
- exec the session scripts with the user's shell with a hyphen prepended
- doesn't seem to actually work yet with tcsh, but it doesn't seem to 
  break anything. needs a look to see why it doesn't work

* Fri Feb 04 2000 Havoc Pennington <hp@redhat.com>
- Link PreSession/Default to xdm/GiveConsole
- Link PostSession/Default to xdm/TakeConsole

* Fri Feb 04 2000 Havoc Pennington <hp@redhat.com>
- Fix the fix to the fix (8877)
- remove docs/gdm-manual.txt which doesn't seem to exist from %doc

* Fri Feb 04 2000 Havoc Pennington <hp@redhat.com>
- Enhance 8877 fix by not deleting the "Please login" 
  message

* Fri Feb 04 2000 Havoc Pennington <hp@redhat.com>
- Try to fix bug 8877 by clearing the message below 
  the entry box when the prompt changes. may turn 
  out to be a bad idea.

* Mon Jan 17 2000 Elliot Lee <sopwith@redhat.com>
- Fix bug #7666: exec Xsession instead of just running it

* Mon Oct 25 1999 Jakub Jelinek <jakub@redhat.com>
- Work around so that russian works (uses koi8-r instead
  of the default iso8859-5)

* Tue Oct 12 1999 Owen Taylor <otaylor@redhat.com>
- Try again

* Tue Oct 12 1999 Owen Taylor <otaylor@redhat.com>
- More fixes for i18n

* Tue Oct 12 1999 Owen Taylor <otaylor@redhat.com>
- Fixes for i18n

* Fri Sep 26 1999 Elliot Lee <sopwith@redhat.com>
- Fixed pipewrite bug (found by mkj & ewt).

* Fri Sep 17 1999 Michael Fulbright <drmike@redhat.com>
- added requires for pam >= 0.68

* Fri Sep 10 1999 Elliot Lee <sopwith@redhat.com>
- I just update this package every five minutes, so any recent changes are my fault.

* Thu Sep 02 1999 Michael K. Johnson <johnsonm@redhat.com>
- built gdm-2.0beta2

* Mon Aug 30 1999 Michael K. Johnson <johnsonm@redhat.com>
- built gdm-2.0beta1

* Tue Aug 17 1999 Michael Fulbright <drmike@redhat.com>
- included rmeier@liberate.com patch for tcp socket X connections

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- fix to handling ancient gdm config files with non-standard language specs
- dont close display connection for xdmcp connections, else we die if remote
  end dies. 

* Fri Apr 16 1999 Michael Fulbright <drmike@redhat.com>
- fix language handling to set GDM_LANG variable so gnome-session 
  can pick it up

* Wed Apr 14 1999 Michael Fulbright <drmike@redhat.com>
- fix so certain dialog boxes dont overwrite background images

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- do not specify -r 42 to useradd -- it doesn't know how to fall back
  if id 42 is already taken

* Fri Apr 9 1999 Michael Fulbright <drmike@redhat.com>
- removed suspend feature

* Mon Apr 5 1999 Jonathan Blandford <jrb@redhat.com>
- added patch from otaylor to not call gtk funcs from a signal.
- added patch to tab when username not added.
- added patch to center About box (and bring up only one) and ignore "~"
  and ".rpm" files.

* Fri Mar 26 1999 Michael Fulbright <drmike@redhat.com>
- fixed handling of default session, merged all gdmgreeter patches into one

* Tue Mar 23 1999 Michael Fulbright <drmike@redhat.com>
- remove GNOME/KDE/AnotherLevel session scripts, these have been moved to
  the appropriate packages instead.
- added patch to make option menus always active (security problem otherwise)
- added jrb's patch to disable stars in passwd entry field

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- made sure /usr/bin isnt in default path twice
- strip binaries

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- fixed to use proper system path when root logs in

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- linked Init/Default to Red Hat default init script for xdm
- removed logo from login dialog box

* Mon Mar 15 1999 Michael Johnson <johnsonm@redhat.com>
- pam_console integration

* Tue Mar 09 1999 Michael Fulbright <drmike@redhat.com>
- added session files for GNOME/KDE/AnotherLevel/Default/Failsafe
- patched gdmgreeter to not complete usernames
- patched gdmgreeter to not safe selected session permanently
- patched gdmgreeter to center dialog boxes

* Mon Mar 08 1999 Michael Fulbright <drmike@redhat.com>
- removed comments from gdm.conf file, these are not parsed correctly

* Sun Mar 07 1999 Michael Fulbright <drmike@redhat.com>
- updated source line for accuracy

* Fri Feb 26 1999 Owen Taylor <otaylor@redhat.com>
- Updated patches for 1.0.0
- Fixed some problems in 1.0.0 with installation directories
- moved /usr/var/gdm /var/gdm

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- moved files from /usr/etc to /etc

* Tue Feb 16 1999 Michael Johnson <johnsonm@redhat.com>
- removed commented-out #1 definition -- put back after testing gnome-libs
  comment patch

* Sat Feb 06 1999 Michael Johnson <johnsonm@redhat.com>
- initial packaging
