Name:		firestarter
Version:	1.0.3
Release:	25.4
Summary:	Firewall tool for GNOME
Group:		Applications/Internet
License:	GPLv2+
URL:		http://firestarter.sourceforge.net
Source0:	http://download.sourceforge.net/firestarter/firestarter-1.0.3.tar.gz
Patch0:		firestarter-1.0.3-pam.patch
Patch1:		firestarter-1.0.3-services.patch
Patch2:		firestarter-1.0.3-nobrowser.patch
Patch3:		firestarter-1.0.3-nonroutable.patch
Patch4:		firestarter-1.0.3-multicast.patch
Patch5:         statusfix.patch
# https://aur.archlinux.org/packages.php?ID=27159
Patch12: 12_firestarter_transparent_icon.patch
Patch18: 18_fix_memleak.patch
Patch99: menu-toolbar-icons-fix.patch
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libgnomeui-devel
BuildRequires:	perl-XML-Parser
BuildRequires: gcc-c++, gcc
BuildRequires: w3m udisks2
Requires:	iptables
Requires:	usermode-gtk
Requires(post):		GConf2
Requires(preun):	GConf2

%description
Firestarter is an easy-to-use, yet powerful, Linux firewall tool for GNOME.
Use it to quickly set up a secure environment using the firewall creation
wizard, or use it's monitoring and administrating features with your old
firewall scripts.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .services
#%patch2 -p1 -b .nobrowser
%patch3 -p1 -b .nonroutable
%patch4 -p1 -b .multicast
%patch5 -p1 -b .statusfix
%patch12 -p1
%patch18 -p1
%patch99 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-format-security -lX11 -Wl,--allow-multiple-definition"
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/inbound
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=${RPM_BUILD_ROOT}

mv ${RPM_BUILD_ROOT}/%{_bindir}/firestarter ${RPM_BUILD_ROOT}/%{_sbindir}
ln -s consolehelper ${RPM_BUILD_ROOT}/%{_bindir}/firestarter

touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/configuration
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/events-filter-hosts
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/events-filter-ports
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/firestarter.sh
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/firewall
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/sysctl-tuning
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/user-pre
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/user-post
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/inbound/allow-from
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/inbound/allow-service
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/inbound/forward
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/inbound/setup
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/allow-from
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/allow-service
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/allow-to
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/deny-from
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/deny-service
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/deny-to
touch ${RPM_BUILD_ROOT}/%{_sysconfdir}/firestarter/outbound/setup

%find_lang %{name}

install -p -D -m0644 firestarter.pam ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/firestarter
install -p -D -m0644 firestarter.console  ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/firestarter
install -p -D -m0755 fedora.init ${RPM_BUILD_ROOT}%{_initrddir}/firestarter

rm -f ${RPM_BUILD_ROOT}%{_datadir}/gnome/apps/Internet/firestarter.desktop
desktop-file-install --vendor fedora                   \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --add-category X-Fedora                              \
  firestarter.desktop

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
if [ "$1" = "1" ]; then
        /sbin/chkconfig --level 0123456 iptables off 2>/dev/null || :
        /sbin/chkconfig --add firestarter
        /sbin/chkconfig firestarter on
fi

%preun
if [ "$1" = "0" ]; then
	export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
	gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

	/sbin/chkconfig iptables reset 2>/dev/null || :
	/sbin/service firestarter stop >/dev/null 2>&1
	/sbin/chkconfig --del firestarter
fi

%postun
if [ "$1" = "0" ]; then
    if [ -e /etc/dhclient-exit-hooks ]; then
        NEW_CONF=`mktemp -t firestarter.XXXXXX`
        grep -v 'sh %{_sysconfdir}/firestarter/firestarter.sh start' < /etc/dhclient-exit-hooks > ${NEW_CONF}
        cat ${NEW_CONF} > /etc/dhclient-exit-hooks
    fi
fi

%files -f %{name}.lang
%doc README ChangeLog AUTHORS TODO COPYING CREDITS
%attr(755,root,root) %{_sbindir}/firestarter
%{_bindir}/firestarter
%{_initrddir}/firestarter
%{_sysconfdir}/gconf/schemas/firestarter.schemas
%{_sysconfdir}/pam.d/firestarter
%{_sysconfdir}/security/console.apps/%{name}
%dir %attr(700,root,root) %{_sysconfdir}/firestarter
%dir %attr(700,root,root) %{_sysconfdir}/firestarter/inbound
%dir %attr(700,root,root) %{_sysconfdir}/firestarter/outbound
# ghosted
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/configuration
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/events-filter-hosts
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/events-filter-ports
%ghost %config(missingok,noreplace) %attr(700,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/firestarter.sh
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/firewall
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/sysctl-tuning
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/user-pre
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/user-post
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/inbound/*
%ghost %config(missingok,noreplace) %attr(400,root,root) %verify(not md5 mode mtime size) %{_sysconfdir}/firestarter/outbound/*
# end ghosted
%{_sysconfdir}/firestarter/non-routables
%{_datadir}/applications/fedora-firestarter.desktop
%{_datadir}/pixmaps/*
%{_datadir}/firestarter

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-19
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-18
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0.3-17
- Rebuild for selinux ppc32 issue.

* Thu Jun 26 2007 Damien Durand <splinux@fedoraproject.org> - 1.0.3-16
- Fix BR
- Fix active connections status

* Sun Jun 17 2007 Damien Durand <splinux@fedoraproject.org> - 1.0.3-15
- Remove old doc
- Fix pam configuration

* Wed Sep 27 2006 Damien Durand <splinux@fedoraproject.org> - 1.0.3-14
- Fix Documentation

* Wed Sep 27 2006 Damien Durand <splinux@fedoraproject.org> - 1.0.3-12
- Devel branch rebuild

* Mon Apr 17 2006 Michael A. Peters <mpeters@mac.com> - 1.0.3-11
- Patch4 - Fix bug #189067 (Avahi)

* Fri Feb 17 2006 Michael A. Peters <mpeters@mac.com> - 1.0.3-10
- Devel branch rebuild

* Thu Feb 02 2006 Michael A. Peters <mpeters@mac.com> - 1.0.3-9
- fix non routables per http://www.iana.org/assignments/ipv4-address-space
- fixes bug 179685

* Mon Jan 30 2006 Michael A. Peters <mpeters@mac.com> - 1.0.3-8
- fixed %post script for dhcp exit script (bug #160431)

* Tue Jan 17 2006 Michael A. Peters <mpeters@mac.com> - 1.0.3-7
- add CUPS and APCUPSD to services
- don't open browser window since it runs as root (bug #178040)
- add PDF documentation
- some spec file cleanup

* Thu Aug 18 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.3-6
- rebuilt

* Tue Jun 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- remove work-around from 1.0.3-5 again, bug has been fixed

* Sat Jun 25 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.3-5
- temporarily add BR libpng-devel to work-around a broken
  cairo-devel package, which is pulled in and breaks the pkg-config
  dependency chain (#161688)

* Thu Jun  2 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.0.3-3
- patch to remove hardcoded PAM module paths (#158929)

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.0.3-2
- rebuilt

* Sun Jan 30 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0.3-1
- 1.0.3.

* Sun Dec 19 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0.1-1
- 1.0.1.

* Fri Nov 19 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0.0-1
- 1.0 final.

* Mon Nov 15 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0.0-0.1.rc1
- 1.0.0rc1.

* Wed Sep 22 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.9-0.fdr.0.4.b3.2
- 0.9.9b3.2.
- Don't uninstall schema in preun if we're doing an upgrade.

* Mon Sep 13 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.9-0.fdr.0.3.b3.1
- 0.9.9b3.1.

* Mon Aug 30 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.9-0.fdr.0.2.b2
- 0.9.9b2.

* Sun Aug 29 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.9-0.fdr.0.1.b1
- 0.9.9b1.

* Thu May 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.3-0.fdr.2
- GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 (#1570)

* Tue May 04 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.3-0.fdr.1
- Update to 0.9.3.
- Install/Uninstall schemas in post/preun.
- Req(post,preun) GConf2.

* Wed Oct 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.9
- Removed aesthetic comments.
- Corrected permissions of source files.
- Brought spec more in line with current template.

* Wed Aug 13 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.8
- Added patch to reconginze Linux 2.6 kernels.
- Added patch to fix crash on KDE3 tray updates.

* Wed Aug 06 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.7
- For %%{_sysconfdir}/firestarter now using verify, not ghost.

* Tue Aug 05 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.6
- Cleanup is now done in postun (rather than post, which is silly).

* Sat Aug 02 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.5
- Remove firestarter references from /etc/dhclient-exit-hooks in post.

* Mon Jul 28 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.4
- Fixed Pam typo.
- ghost config files.

* Thu Jul 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.3
- Req usermode-gtk.
- Wrapped post script.
- pam_xauth entry -> optional.

* Fri Jul 18 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.2-0.fdr.2
- Readded Epoch: 0.
- Split pam.d and console.apps files into separate SOURCE files.
- Removed hard-coded paths.
- Added explicit epochs.
- Added Req iptables.
- Package now owns %%{_sysconfdir}/firestarter.

* Fri Jun 13 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.2-0.fdr.1
- Updated to 0.9.2.
- Removed Epoch:0.
- buildroot -> RPM_BUILD_ROOT.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9.1-0.fdr.7
- Added desktop-file-utils to BuildRequires.
- Changed category to X-Fedora-Extra.
- Added Epoch:0.

* Tue Mar 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-0.fdr.6
- removed %postun.

* Tue Mar 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-0.fdr.5
- Moved menu entry to System Tools.
- removed redundant ldconfig.
- removed extra chkconfig.

* Mon Mar 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-0.fdr.4
- Made the .desktop file an external file.
- corrected BuildRequires.
- corrected %files

* Wed Mar 08 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-0.fdr.3
- Cleaned up spec

* Wed Mar 05 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-0.fdr.2
- Cleaned up spec

* Wed Feb 26 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9.1-1.fedora.1
- Initial Fedora release (0.9.1).

* Tue Aug 06 2002 Tomas Junnonen <majix@sci.fi>
- Updated requirements to GNOME2 level
- Removed all requirements related to the documentation generation

* Tue Jun 25 2002 Paul Drain <pd@cipherfunk.org>
- Merged some compatible cleanups from the FreshRPMS (http://freshrpms.net)
  specfile.

* Wed Apr 24 2002 Paul Drain <pd@cipherfunk.org>
- build dependancy cleanups

* Mon Apr 22 2002 Paul Drain <pd@cipherfunk.org>
- gnome-doc-tools is no longer required to build the RPM

* Tue Jan 08 2002 Roy-Magne Mo <rmo@sunnmore.net>
- Clean up specfile, and use rpm4 macros
- Remove docuementation tools as requirements
- Add gnome-doc-tools and then some as buildprereq
- Add initscripts to prereq
- used %makeinstall macro instead of old make install
- no use specifying runlevels at the commandline, this
  should be specified in the initscripts itself
- Added gnome-core as requirements

* Mon Jan 07 2002 Tomas Junnonen <majix@sci.fi>
- preun now doesn't explicitly delete the init script,
  caused problem with package upgrades.
- Moved the init scripts to external files

* Tue Oct 23 2001 Paul Drain <pd@cipherfunk.org>
- Added sgmltools and openjade to build requirements

* Tue Oct 16 2001 Paul Drain <pd@cipherfunk.org>
- Updated build dependancies

* Mon Jul 09 2001 Paul Drain <pd@cipherfunk.org>
- Fixed documentation directory
- Added sysconfdir variable instead of hardcoding /etc

* Thu Jun 01 2000 Tomas Junnonen <majix@sci.fi>
- Significant changes to allow use of consolehelper

* Wed May 31 2000 Tomas Junnonen <majix@sci.fi>
- Fixed problem with CFLAGS and LDADD usage of " and `

* Mon May 29 2000 Tomas Junnonen <majix@sci.fi>
- First spec file
