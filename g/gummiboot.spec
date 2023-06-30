Name:           gummiboot
Version:        45
Release:        10.1
Summary:        Simple EFI Boot Manager
Group:          System/Boot and Init
License:        LGPLv2+
URL:            https://freedesktop.org/wiki/Software/gummiboot
# git clone git://anongit.freedesktop.org/gummiboot
# cd gummiboot/
# ./autogen
# ./configure
# make distcheck
Source0:	%{name}-%{version}.tar.xz
BuildRequires:  gnu-efi-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  docbook-style-xsl

%description
gummiboot is a simple UEFI boot manager which executes configured EFI
images. The default entry is selected by a configured pattern (glob)
or an on-screen menu.

gummiboot operates on the EFI System Partition (ESP) only. gummiboot
reads simple and entirely generic boot loader configuration files;
one file per boot loader entry to select from.

Configuration file fragments, kernels, initrds, other EFI images need
to reside on the ESP.

%prep
%setup -q
sed -i '40i #include <sys/sysmacros.h>' src/setup/setup.c

%build
./autogen.sh
%configure --with-efi-ldsdir=%{_libdir}/gnuefi
cp -a /usr/include/*.h /usr/include/sys /usr/include/bits /usr/include/gnu .
%ifarch aarch64
sed -i -e 's|-mno-sse||' -e 's|-mno-mmx||' Makefile
%endif
%make_build

%install
%make_install

%post
/usr/bin/gummiboot update >/dev/null 2>&1 || :

%files
%doc README LICENSE
%{_bindir}/gummiboot
%{_mandir}/man8/*
/usr/lib/gummiboot

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 45
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 45-3.mga5
+ Revision: 743578
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 45-2.mga5
+ Revision: 680047
- Mageia 5 Mass Rebuild
* Sun Jun 29 2014 tmb <tmb> 45-1.mga5
+ Revision: 641035
- run autogen.sh before build
- update to v 45
* Mon Dec 23 2013 tmb <tmb> 42-1.mga4
+ Revision: 560206
- update to v42 for bootsplash support
* Tue Oct 22 2013 umeabot <umeabot> 38-2.mga4
+ Revision: 541673
- Mageia 4 Mass Rebuild
* Sun Oct 13 2013 tmb <tmb> 38-1.mga4
+ Revision: 496328
- update to v38
* Sun Mar 31 2013 colin <colin> 29-1.mga3
+ Revision: 406860
- New version: 29
- New version: 28
* Sat Feb 23 2013 tmb <tmb> 23-1.mga3
+ Revision: 400161
- BR xsltproc
- add group
  + colin <colin>
    - Import Fedora Package
* Wed Feb 20 2013 Kay Sievers <kay@redhat.com> - 23-1
- version 23
* Tue Feb 19 2013 Kay Sievers <kay@redhat.com> - 22-1
- version 22
* Mon Feb 18 2013 Kay Sievers <kay@redhat.com> - 21-1
- version 21
* Mon Feb 18 2013 Kay Sievers <kay@redhat.com> - 20-1
- version 20
* Mon Feb 11 2013 Kay Sievers <kay@redhat.com> - 19-1
- version 19
* Fri Feb 08 2013 Kay Sievers <kay@redhat.com> - 18-1
- version 18
* Sun Feb 03 2013 Kay Sievers <kay@redhat.com> - 17-1
- version 17
* Thu Jan 24 2013 Kay Sievers <kay@redhat.com> - 16-1
- version 16
* Wed Jan 23 2013 Kay Sievers <kay@redhat.com> - 15-1
- version 15
* Tue Jan 22 2013 Kay Sievers <kay@redhat.com> - 14-1
- version 14
* Mon Jan 21 2013 Kay Sievers <kay@redhat.com> - 13-1
- version 13
* Mon Jan 21 2013 Kay Sievers <kay@redhat.com> - 12-1
- version 12
* Sat Jan 19 2013 Kay Sievers <kay@redhat.com> - 11-1
- version 11
* Thu Jan 17 2013 Kay Sievers <kay@redhat.com> - 10-1
- initial packaging
