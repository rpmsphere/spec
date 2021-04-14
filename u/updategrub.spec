Name: updategrub
Summary: A script to update Legacy Grub menu entries
Version: 1.7.2
Release: 109.1
License: GPL
Source0: %{name}-%{version}.tar.gz
Source1: findgrub-3.6.2.tar.gz
BuildArch: noarch
Requires: os-prober >= 1.49
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: dialog
Group: System Environment/Base
%define docdir %{_docdir}/%{name}-%{version}

%description
updategrub adds other Linuxes boot entries to Legacy Grub menu using
os-proper in a similar way that Grub2 does. 
findgrub/cfindgrub looks for Grub/Grub2 stage1 & stage2 and display
results.  

Authors:
--------
Agnelo de la Crotche <agnelo@unixversal.com>


%prep
%setup -q  -b 1

%build

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{docdir}
install -d -m 0755 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0755 updateLegacyGrub updateGrub2 findgrub cfindgrub grubmenu $RPM_BUILD_ROOT%{_bindir}
install -m 0644 defaults $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 0644 %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz
install -m 0644 updateGrub2.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/updateGrub2.1.gz

ln -s updateLegacyGrub $RPM_BUILD_ROOT%{_bindir}/updategrub

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING defaults
%dir %{_sysconfdir}/%{name}
%config (noreplace) %{_sysconfdir}/%{name}/defaults
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.2
- Rebuilt for Fedora
* Fri Jan 20 2012 Agnelo de la Crotche <agnelo@unixversal.com> 1.7.2
- added support for Fedora's grub-efi
- added mbr_chainload and efi_chainload
- removed chainload_windows
* Thu Jan 19 2012 Agnelo de la Crotche <agnelo@unixversal.com> 1.7.1
- function chainload_windows added in updateGrub2
* Tue Jan 17 2012 Agnelo de la Crotche <agnelo@unixversal.com> 1.7
- Added updateGrub2
* Mon Jan 9 2012 Agnelo de la Crotche <agnelo@unixversal.com> 1.6.1
- Added Fedora 16 detection to updategrub and findgrub
* Thu Dec 13 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.6
- added bootchart support to updategrub
- required os-prober 1.49
* Sun Nov 13 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5.5
- ignore usb floppy disks in findgrub
- chainload Grub 1.99 in updategrub
* Sat Nov 12 2011 Agnelo de la Crotche <agnelo@unixversal.com>
- added support for Grub 1.99 compressed core to findgrub.
* Thu Jul 14 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5.4
- put findgrub in a separate source
* Thu Jul 14 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5.3
- exclude usb devices from device mapping in findgrub/cfindgrub
* Tue Jul 12 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5.2
- improved handling of device mapping in findgrub/cfindgrub
* Mon Jul 4 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5.1
- fix some bugs and display active partitions in findgrub/cfindgrub
* Fri Jul 1 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.5
- add function checkroot
* Sun Jun 5 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.4.2
- ignore lvm partitions while comparing hds whit device.map
- fix minor bugs
* Mon Apr 25 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.4.1
- Fix SETBOOTFLAG bug 
* Sat Apr 23 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.4
- Add option -m to launch grubmenu without scanning OS.
- Add hardlink 'grubmenu' equivalent to 'updategrub -m'
* Fri Apr 22 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.3.1
- Fix some bugs in grubmenu 
* Thu Apr 21 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.3
- add interactive menu
* Wed Apr 20 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2.2-35
- apply some fixes to the spec file (thanks to Malcolm).
* Tue Apr 19 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2.2-34
- add man page
* Fri Apr 15 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2.2
- identify Legacy Grub/Grub2 
- boot Grub2 installed on partition (not MBR) with core.img rather
  then chainloading if possible.
* Fri Apr  8 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2.1
- add linux_ignore option
* Thu Apr  7 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.1
- rewrite from scratch
* Mon Apr  4 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.0
- initial build
 
