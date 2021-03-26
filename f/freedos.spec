Name: freedos
License: GPL
Group: Development/DRBL
Summary: FreeDOS aims to be a complete, free, 100% MS-DOS compatible operating system.
Version: 1.0
Release: 11
Source: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.0/fdboot.img
Source1: insert-file-fdos.sh

%description
FreeDOS aims to be a complete, free, 100% MS-DOS compatible operating system.

%prep
%setup -T -c

%build

%install
install -Dm 755 %{SOURCE1} %{buildroot}/opt/drbl/sbin/insert-file-fdos.sh
install -Dm 644 %{SOURCE0} %{buildroot}/usr/lib/freedos/fdos1440.img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/drbl/sbin/insert-file-fdos.sh
/usr/lib/freedos/fdos1440.img

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Sep 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1.0-11.ossii
- Rebuild for M6(CentOS5)

* Sun Sep 24 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-11drbl
- change #!/bin/sh to #!/bin/bash for insert-file-fdos.sh.

* Tue Sep 05 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-10drbl
- new upstream, official FreeDOS 1.0.

* Thu Jul 27 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-9drbl
- sign the rpm with gpg.

* Thu Apr 13 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-8drbl
- use the FreeDOS OEM Bootdisk instead of the installation disk.

* Thu Apr 13 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-7drbl
- update insert-file-fdos.sh, make it strip some unnecessary files, and remove nbi images.
- new upstream beta9sr2.

* Mon Apr 11 2005 Steven Shiau <steven _at_ nchc org tw> 1.0-6drbl
- update insert-file-fdos.sh, make it strip some unnecessary files, and remove nbi images.

* Mon Apr 04 2005 Steven Shiau <steven _at_ nchc org tw> 1.0-5drbl
- fix the mode of fdos1440.img

* Sat Dec 11 2004 Steven Shiau <steven _at_ nchc org tw> 1.0-4drbl
- Update with new version, use freedos beta9sr1 image.

* Fri Jul 16 2004 Steven Shiau <steven _at_ nchc org tw> 1.0-3drbl
- Update with new version, use freedos beta9rc5 image.

* Tue Sep 23 2003 Steven Shiau <steven _at_ nchc org tw> 2drbl
- add script to insert files into image

* Tue Sep 23 2003 Steven Shiau <steven _at_ nchc org tw> 1drbl
- spec file modified from conectiva Linux dosemu package 1.0.2
