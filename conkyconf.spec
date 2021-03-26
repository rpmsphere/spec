Name: conkyconf
Summary: A script to generate conky configuration
Version: 2.9
Release: 4.1
License: GPL
Source: %{name}-%{version}.tar.bz2
BuildArch: noarch
Requires: conkyweather conky
Group: User Interface/X

%description
conkyconf creates a basic system (/etc/conky/conky.conf) or user (~/.conkyrc) conky 
configuration file including CPU, RAM and filesystems usage, CPU and mainboard temperature
sensors (if available), CPU and memory top processes, weather info and forecast, one line
of scrolling rss feed (doesn't work very well under openSUSE and Ubuntu but seems to be
fine under ArchLinux and Fedora). It can also parse and display the last lines of a log file  
of your choice. It uses conkyweather for weather info and a lua script to create color
gradients for fs and cpu bars as well as others things. The script has several command
line options and is highly configurable.  


Authors:  
--------
Agnelo de la Crotche (please_try_again) <agnelo@unixversal.com>


%prep
%setup -q

%build

%install
%{__install} -d -m 755 $RPM_BUILD_ROOT%{_bindir}
%{__install} -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/conky
%{__install} -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart
%{__install} -d -m 755 $RPM_BUILD_ROOT%{docdir}
%{__install} -m 755 conkyconf $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 conky.sh $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 compositor $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 644 conky.lua $RPM_BUILD_ROOT%{_sysconfdir}/conky
%{__install} -m 644 conky.desktop $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc COPYING 
%dir %{_sysconfdir}/conky
%{_bindir}/*
%{_sysconfdir}/conky/conky.lua
%{_sysconfdir}/xdg/autostart/conky.desktop

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9
- Rebuild for Fedora
* Fri Jan 27 2012 Agnelo de la Crotche <agnelo@unixversal.com> 2.9
- fixed (ugly) bug in conkyconf
* Tue Sep 13 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.8
- compositor, conky.sh and conkyconf updated
* Fri Sep 9 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.7
- fixed bug in compositor
- improved fs functions in conky.lua
* Tue Sep 6 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.6
- added function in conky.lua to modify update interval
* Tue Sep 5 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.5.1
- changed default interval from 1 to 5s 
- updated compositor
* Mon Sep 5 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.5
- added support for tcp_portmon
* Sat Sep 3 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.4
- more detailed file system output - including LVM and RAID
* Fri Sep 2 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.3
- added support for apcupsd
* Tue Aug 30 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.2
- do not add nvidia and rss monitoring if support not built in in conky.
* Sun Aug 28 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.1
- added support for hddtemp et nvidia in conkyconf
* Wed Aug 24 2011 Agnelo de la Crotche <agnelo@unixversal.com> 2.0
- added many functions in /etc/conky/conky.lua
- work around new line parsing bug by writing a different configuration for conky 1.8.1  
* Sun Jul 31 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.3
- added conky wrapper, autostart & compositor
* Mon Jun 20 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2
- some layout changes needed to run conky in nx session with lower resolution.
* Sat Jun  4 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.1
- better sensors and filesystems (RAID) detection.
* Fri Jun  3 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.0
- initial build
