Name:           zyx-liveinstaller
Version:        0.2.4
Release:        2
Summary:        Install a running LiveOS rebootlessly

Group:          Applications/System
License:        GPLv3
URL:            http://cloudsession.com/dawg/projects/zyx-liveinstaller/
Source0:        http://cloudsession.com/dawg/downloads/%{name}/%{name}-%{version}.tar.bz2
Patch0:		distro-ox.patch
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
Requires:       usermode


%description
This installer will perfrom a traditional LiveOS installation,
however instead of installing a fresh copy of the LiveOS to
disk to be used on the next reboot, it live migrates the running
LiveOS's root filesystem to disk.  In this fashion it does not
require a reboot to begin using the installed system.


%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/zyx-liveinstaller.desktop
mv $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version} $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_sbindir}/*
%{python_sitelib}/rli/
%attr(0644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(0644,root,root) %config(noreplace) /etc/pam.d/%{name}
%attr(0644,root,root) %config(noreplace) /etc/security/console.apps/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat May 08 2010 Sebastian Dziallas <sebastian@when.com> - 0.2.4-1
- new upstream release

* Wed Nov 18 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.17-2
- rebuild to use correct source file

* Wed Nov 18 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.17-1
- update to new upstream release

* Thu Oct 29 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.16-1
- update to new upstream release

* Sun Oct 18 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.14-1
- update to new upstream release
- adjust source url

* Sat Oct 10 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.13-1
- update to new upstream release

* Sat Sep 26 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.12-1
- update to new upstream release

* Sat Sep 12 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.11-1
- update to new upstream release

* Fri Aug 21 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.10-2
- adjust buildroot according to guidelines

* Sun Aug 16 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.10-1
- update to new upstream release
- fix some file locations

* Fri Aug 14 2009 Sebastian Dziallas <sebastian@when.com> - 0.1.9-2
- adopt .spec file from Douglas McClendon
- minor tweaks and changes to fit the guidelines

* Sat Aug 8 2009 Douglas McClendon <dmc@viros.org> - 0.1.9-1
- tweak stupid .present delay workaround (for Guitar-ZyX-0.3)
- catch stderr in /var/log/zyx-liveinstaller.log, and more debug output
- attempt to unmount targets that have been automounted under /media
- genericize attempted unmount of live-osimg-min automounted under /media

* Tue Jul 28 2009 Douglas McClendon <dmc@viros.org> - 0.1.8-1
- zyx only: minor typo, remove liveos lvm devices from list
- rework internal device representation, fixing pre-f11 lvm problem
- add temporary special case for soas live-osimg-min mounting oddity
- more info added to BUGS/FAQ/README

* Mon Jul 27 2009 Douglas McClendon <dmc@viros.org> - 0.1.7-1
- vastly improve FAQ

* Sat Jul 25 2009 Douglas McClendon <dmc@viros.org> - 0.1.6-1
- remove zyx special lvm names from list (like for f11)
- use UUID= in fstab and grub.config, primarily to make 
  grubby happy, but also for consistency with anaconda.
- remove attempted workaround of issue with pre-first-reboot 
  hibernate.  Until grub(?) bug fixed, user must work around 
  at the grub-prompt-instead-of-unhibernation by typing e.g.
  # assuming /boot is on /dev/sda1
  grub> root (hd0,0)
  grub> setup (hd0)
  grub> reboot
  :( sigh...

* Fri Jul 17 2009 Douglas McClendon <dmc@viros.org> - 0.1.5-1
- trying harder to deal with /tmp tmpfs
- noted grubby problems in BUGS

* Fri Jul 17 2009 Douglas McClendon <dmc@viros.org> - 0.1.4-1
- removed facility for launcher desktop icon from xinit,
  but changed .desktop so it is shown under System Tools.
- better/fixed freeing of livemedia resources
- desensitized incompletely implemented installation abort
- try to migrate f11 live-only tmpfs's to rootfs
- support rootfs and swap on lvm
- support wholedisk targets (still need choice exclusion logic)
- top review text now uses long device names rather than short
- output is now logged to /var/log/rliveinst.log
- support ZyX LiveOS again, for now, with same backend
- misc bugfixes and refactorings

* Mon Jul 13 2009 Douglas McClendon <dmc@viros.org> - 0.1.3-1
- workaround fedora/grub problem by disabling hibernate autoboot
  - which I never liked anyway

* Mon Jul 13 2009 Douglas McClendon <dmc@viros.org> - 0.1.2-1
- really fix the grub configuration

* Sun Jul 12 2009 Douglas McClendon <dmc@viros.org> - 0.1.1-1
- fixed bugs with grub configuration
- better banner png compression
- red highlights for unselectable volumes (due to prior selection)
- misc cleanups

* Mon Jul 06 2009 Douglas McClendon <dmc@viros.org> - 0.1-1
- initial release and packaging
