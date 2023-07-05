Summary: Unified Configuration API for Linux Installation
Name: systemconfigurator
Version: 2.2.11
Release: 4.1
License: GPL
URL: https://systemconfig.sourceforge.net
Group: Applications/System
Source: %{name}-%{version}.tar.gz
Requires: perl-AppConfig
BuildArch: noarch
BuildRequires: perl-AppConfig
BuildRequires: perl-ExtUtils-MakeMaker
AutoReqProv: off

%description
Provides an API for various installation and configuration processes that are
otherwise inconsistent between the many Linux distributions, and the many
architectures they run on.  For example, you can configure the bootloader
on a system in a general way - you don't need to know anything about the
particular boot loader on the system.  You can update the network settings
of a system, without knowing the distribution or the format of its network
configuration files.

%prep
%setup -q

%build
mkdir -p %{buildroot}/usr/share/man/man5
perl Makefile.PL PREFIX=%{buildroot}%{prefix} INSTALLSITELIB=%{buildroot}/usr/lib/systemconfig INSTALLMAN1DIR=%{buildroot}/usr/share/man/man1 INSTALLMAN3DIR=%{buildroot}/usr/share/man/man3 INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1 INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3 INSTALLSITEBIN=%{buildroot}/usr/bin INSTALLSITESCRIPT=%{buildroot}/usr/bin
make

%install
make install
rm -rf %{buildroot}/usr/lib/systemconfig/auto*
find %{buildroot}/ -name perllocal.pod | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%doc TODO 
%doc CREDITS 
%doc CHANGELOG 
%doc README
%doc INSTALL 
%doc README.yaboot
%doc COPYING
%doc sample.cfg
%doc docs/design.pod 
%{_bindir}/*
%{_mandir}/man?/*
/usr/lib/systemconfig

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.11
- Rebuilt for Fedora
* Thu Nov 08 2007 Erich Focht -> 2.2.11-1
- allowing now UUID and LABEL devices
- fixed check for grub
* Mon Oct 22 2007 Erich Focht
- added kboot support for PS3
- sanity checking of devices (by Bernard)
- version 2.2.10-2
* Mon Apr 22 2007 Erich Focht
- version 2.2.9 tag/release
* Fri Mar 30 2007 Erich Focht
- Added debian support which was in the OSCAR pkgsrc repository, provided
  by Geoffroy Vallee. Also added an extension of the syntax for supporting
  xen virtual machines.
* Mon Mar 26 2007 Erich Focht
- Added scconf-tool, a tool for querying and manipulating the 
  /etc/systemconfig/systemconfig.conf file from shell scripts. 
- Added scconf-bootinfo, a helper tool for detecting boot information.
  Used by the kexec boot method of systemimager.
* Wed Mar 21 2007 Erich Focht
- Patches to bring systemconfigurator to the level of the version included
  into OSCAR 5.0 (sc-2.2.7-12ef). In order to avoid confusion, updating the
  version number to 2.2.8-1. Changes are listed below:
  * Wed Oct 25 2006 Erich Focht]
  - fixing issue with unknown additional scsi device (oscar bug #274).
  * Fri Sep 15 2006 Erich Focht
  - locating "env" with "which". Path to env is different in SuSE and RedHat.
  * Wed Aug 23 2006 Erich Focht
  - added check for --no-floppy support of grub (RHEL3 doesn't support it)
  - made functions in Grub.pm more OO. Needed for storing "nofloppy" capability
    centrally, in the object instance.
  * Mon Aug 07 2006 Erich Focht
  - added --no-floppy to grub calls as suggested by Andrea Righi.
  * Mon Jul 17 2006 Erich Focht
  - added <HOSTID>, <HOSTID+nnn> and <HOSTID-nnn> hostname dependent
    variable replacement (in the global APPEND block of the BOOT section).
* Fri Nov 24 2006 Erich Focht <efocht@hpce.nec.com>
- first step in merging with changes from the OSCAR tree
- changes correspond to systemconfigurator distributed with OSCAR 4.2
* Sat Mar 26 2005 Sean Dague <sean@dague.net> 2.2.2-1
- add Erich Focht's kernel version detector changes
- update hardware detection module to FC3 & Mandrake 10.1 based lists
* Fri Mar 25 2005 Sean Dague <sean@dague.net> 2.2.1-1
- fixed to work with fedora, which does this differently from mdk and suse
* Thu Mar 24 2005 Sean Dague <sean@dague.net> 2.2.0-1
- added support for modprobe.conf
- clean up spec file
- upped release number
* Sun Sep 19 2004 dann frazier <dannf@dannf.org> 2.0.10-1
- New release
* Tue Aug 21 2001 Sean Dague <japh@us.ibm.com>
- Added %doc sections for devel docs
* Tue Aug 14 2001 Sean Dague <japh@us.ibm.com>
- Added prebuild for man 5 directory
* Mon Jul 16 2001 Sean Dague <japh@us.ibm.com>
- Initial spec file.
