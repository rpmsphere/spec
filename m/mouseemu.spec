Summary:	Program that emulates mouse clicks
Name:		mouseemu
Version:	0.15
Release:	1
License:	GPL
Group:		System/Configuration/Hardware
URL:		https://www.geekounet.org/powerbook/files
Source0:	https://www.geekounet.org/powerbook/files/%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.rules
Patch1:		%{name}-nousb-noadb.patch.bz2
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-nofork.patch
Patch4:		%{name}-usage-cleanup.patch
Patch5:		%{name}-manpage.patch
Patch6:		%{name}-rescan.patch
Patch7:		%{name}-syslog.patch
Patch8:		%{name}-pidfile.patch
Requires:	procps, udev

%description
A program that will allows the keyboard to send mouse events.
It can be used to configure right, middle and scroll buttons via 
the keyboard when you do not have a mouse with these buttons 
available (like for example on iBooks, pBooks, and macBooks).

%prep
%setup -q -n %{name}
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}

install -d %{buildroot}/{%{_sbindir},%{_sysconfdir}/{rc.d/init.d,sysconfig,udev/rules.d,modprobe.preload.d},%{_mandir}/man8}

install mouseemu %{buildroot}/%{_sbindir}
install -m644 %{SOURCE1}	%{buildroot}/%{_sysconfdir}/rc.d/init.d/%{name}
install -m644 %{SOURCE2}	%{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -m644 %{SOURCE3}	%{buildroot}/%{_sysconfdir}/udev/rules.d/90-mouseemu.rules
install -m644 mouseemu.8	%{buildroot}/%{_mandir}/man8/mouseemu.8

cat >  %{buildroot}/%{_sysconfdir}/modprobe.preload.d/%{name} <<EOF
evdev
uinput
EOF

%clean
rm -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
  /sbin/chkconfig --add mouseemu ||:
fi

%preun
if [ "$1" = 0 ]; then
  /sbin/service mouseemu stop
  /sbin/chkconfig --del mouseemu || :
fi 

%files
%doc README
%attr(744,root,root) %{_sbindir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(744,root,root) %{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/udev/rules.d/90-%{name}.rules
%{_sysconfdir}/modprobe.preload.d/%{name}
%{_mandir}/man8/mouseemu*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15
- Rebuilt for Fedora
* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.15-4mdv2009.0
+ Revision: 252783
- rebuild
- fix no-buildroot-tag
* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.15-2mdv2008.1
+ Revision: 121753
- kill (multiple!) definitions of %%buildroot on Pixel's request
- import mouseemu
* Tue Sep 19 2006 Danny Tholen <obiwan@mailmij.org> 0.15-2mdv2007.0
- Make initscrpt depend on syslog
- Work around very weird problem with prcsys by loading modules
    via modprobe.preload.d
* Mon Sep 04 2006 Danny Tholen <obiwan@mailmij.org> 0.15-1mdv2007.0
- update to 0.15 (patch0 was merged)
- init script tweak to work better with pbbuttonsd
- mkrelify
- spec fixes
- disable patch1 for the moment (conflicts with 4)
- patches from debian:
	-add mouseemu.rules for udev (source3, depends on patch6)
	-fix nofork option (patch3)
	-put man page in correct dir (update patch2)
	-cleanup usage code (patch4)
	-update man page (patch5)
	-add rescan option (patch6)
	-log to syslog (patch7)
	-write pidfile (patch8)
* Wed Mar 09 2005 Danny Tholen <obiwan@mailmij.org> 0.14-2mdk
- fixes to initscript, restarts pbbuttonsd if its running
- huge patch to block keyboard if emulation keys are pressed (patch0) 
- patch2 to be able to use $RPM_OPT_FLAGS
- fix rpmlint errors
* Fri Feb 25 2005 Danny Tholen <obiwan@mailmij.org> 0.14-1mdk
- initial release, spec adopted from pld
- nousb and noadb options from pld patch1
