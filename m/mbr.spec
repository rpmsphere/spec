Summary: Master Boot Record for IBM-PC compatible computers
Name: mbr
Version: 1.1.9
Release: 1
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
URL: http://packages.debian.org/unstable/admin/mbr
BuildRequires: dev86

%description
This is used in booting Linux from the hard disk. The MBR runs first,
then transfers control to LILO, which transfers control to the Linux
kernel.

%prep
%setup -q
find -name Makefile.in | xargs -r perl -pi -e 's/\B-Werror\b//g'

%build
%configure
%{__sed} -i 's/_syscall2(int, vm86, unsigned long, fn, struct vm86plus_struct \*, v86)/int vm86(unsigned long fn, struct vm86plus_struct \* v86)/' harness/vm86.c
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sbindir}/install-mbr
%{_mandir}/*/install-mbr.8*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.9
- Rebuild for Fedora
* Mon Apr 23 2007 Olivier Blin <oblin@mandriva.com> 1.1.9-1mdv2008.0
+ Revision: 17242
- buildrequire dev86
- build without Werror (the debian way not to fix strict aliasing errors)
- 1.1.9
- Import mbr
* Thu Jan 12 2006 Olivier Blin <oblin@mandriva.com> 1.1.5-2mdk
- add Exclusivearch %%ix86, vm86.h is not supported on X86-64
  (thanks Iurt, I owe you a beer)
* Tue Dec 27 2005 Olivier Blin <oblin@mandriva.com> 1.1.5-1mdk
- initial release
