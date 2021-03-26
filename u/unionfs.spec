%{!?kver: %{expand: %%define kver %(uname -r)}}
%define kversion %(echo %{kver} | sed -e s/smp// - )
%define krelver %(echo %{kversion} | tr -s '-' '_')
%if %(echo %{kernel} | grep -c smp)
    %{expand:%%define ksmp -smp}
%endif

Summary: A Stackable Unification File System
Name: unionfs
Version: 1.4.3
Release: 1
Requires: %{name}-kmod >= %{version}
License: GPL
Group: System/Kernel and hardware
URL: http://www.filesystems.org/project-unionfs.html
#Source: ftp://ftp.fsl.cs.sunysb.edu/pub/unionfs/unionfs-%{version}.tar.gz
Source: unionfs-%{version}.zip
BuildRequires: 	kernel-devel

%description
Unionfs is a stackable unification file system, which can appear to
merge the contents of several directories (branches), while keeping
their physical content separate.  Unionfs is useful for unified source
tree management, merged contents of split CD-ROM, merged separate
software package directories, data grids, and more.  Unionfs allows
any mix of read-only and read-write branches, as well as insertion and
deletion of branches anywhere in the fan-out.

%package kmod
Summary: kernel modules for %{name}.
Group: System Environment/Kernel

%description kmod
Kernel modules for %{name}.


%prep
%setup -q
sed -i '88,91d' subr.c
sed -i 's/ia_mode = mode .*/ia_mode = mode ;/' inode.c

%build
make

%install
rm -rf %{buildroot}
make install PREFIX=$RPM_BUILD_ROOT/usr MODPREFIX=$RPM_BUILD_ROOT MANDIR=$RPM_BUILD_ROOT/%{_mandir}

%clean
rm -rf %{buildroot}

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sbindir}/union*
%{_mandir}/man?/*

%files kmod
/lib/modules/%{kver}/kernel/fs/unionfs/unionfs.ko

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Oct 05 2009 Wei-Lun Chao <bluebat@member.fsf.org> 1.4.3-1.ossii
- Rebuild for OSSII

* Thu Aug 06 2009 Olivier Blin <oblin@mandriva.com> 1.4-3mdv2010.0
+ Revision: 410937
- remove man page (not present in new patches)
- sync with unionfs patches from main kernel

* Wed Jun 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-2mdv2009.0
+ Revision: 225898
- rebuild

* Fri Jan 11 2008 Olivier Blin <oblin@mandriva.com> 1.4-1mdv2008.1
+ Revision: 148691
- do not trigger BUG() in notify_change when setting mode attributes
- do not use security hooks, use VFS helpers instead
- adapt to kmem_cache_create prototype (and new arguments order...)
- apply 2.6.22 and apparmor fixes from 2008.0 update kernel
- 1.4
- update URL
- do not buildrequire e2fsprogs-devel, tools are in a separate package
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 02 2007 Olivier Blin <oblin@mandriva.com> 1.3-4mdv2008.0
+ Revision: 94490
- update to new version


* Sun Feb 04 2007 Olivier Blin <oblin@mandriva.com> 1.3-3mdv2007.0
+ Revision: 116122
- do not conflict with unionfs-tools anymore

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - moved dkms post/postun deps to subpackage

* Mon Nov 13 2006 Olivier Blin <oblin@mandriva.com> 1.3-2mdv2007.1
+ Revision: 83837
- remove hardcoded make command line in dkms config file

* Mon Nov 13 2006 Olivier Blin <oblin@mandriva.com> 1.3-1mdv2007.1
+ Revision: 83806
- 1.3
- remove tools subpackage, it's now in unionfs-utils
- Import unionfs

* Tue May 16 2006 Olivier Blin <oblin@mandriva.com> 1.1.4-1mdk
- New release 1.1.4

* Thu Jan 26 2006 Olivier Blin <oblin@mandriva.com> 1.1.2-1mdk
- 1.1.2

* Thu Jan 19 2006 Olivier Blin <oblin@mandriva.com> 1.1.1-1.20060117.1mdk
- CVS snapshot (20060112)
- buildrequires e2fsprogs-devel
- add missing changelog entry

* Fri Jan 13 2006 Olivier Blin <oblin@mandriva.com> 1.1.1-1.20051124.1mdk
- CVS snapshot (20051124)

* Wed Nov 09 2005 Olivier Blin <oblin@mandriva.com> 1.1.1-1mdk
- initial release
