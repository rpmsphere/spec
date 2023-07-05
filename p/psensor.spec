Summary:	A Graphical Temperature Monitor
Name:		psensor
Version:	1.2.1
Release:	1
URL:		https://wpitchoune.net/blog/psensor/
License:	GNU General Public License version 2
Group:		System/Monitoring
Source0:	https://wpitchoune.net/psensor/files/%{name}-%{version}.tar.gz
Requires:	lm_sensors hddtemp
BuildRequires:	make gcc lm_sensors-devel cairo-devel
BuildRequires:	GConf2-devel desktop-file-utils gtk3-devel
BuildRequires:	help2man libnotify-devel libcurl-devel json-c-devel libatasmart-devel libgtop2-devel libmicrohttpd-devel

%description
Psensor is a graphical hardware temperature monitor for Linux.
It can monitor:
* the temperature of the motherboard and CPU sensors (using lm-sensors).
* the temperature of the NVidia GPUs (using XNVCtrl).
* the temperature of ATI/AMD GPUs (not enabled in Ubuntu PPAs or official
  distribution repositories, see the instructions for enabling its support).
* the temperature of the Hard Disk Drives (using hddtemp or libatasmart).
* the rotation speed of the fans (using lm-sensors).
* the CPU usage (since 0.6.2.10 and using Gtop2).

%prep
%setup -q
sed -i 's|!is_error(obj)|obj != NULL|' src/rsensor.c

%build
%configure
sed -i 's|-Wall -Werror|-Wno-incompatible-pointer-types|' src/server/Makefile
make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/doc/%{name}
%{_datadir}/glib-2.0/schemas/psensor.gschema.xml
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/man/man1/%{name}*.1.*
%{_datadir}/icons/*/*/*/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuilt for Fedora
* Thu Dec 30 2010 djs_core <admin@djscore.org> - 0.5.1
- update to new version
* Thu Nov 04 2010 djs_core <admin@djscore.org> - 0.4.4
- update to new version
* Mon Sep 27 2010 djs_core <admin@djscore.org> - 0.4.3
- update to new version
* Wed Sep 08 2010 djs_core <admin@djscore.org> - 0.4.0
- update to new version
* Mon Aug 23 2010 djs_core <admin@djscore.org> - 0.3.2
- update to new version
* Mon Jul 19 2010 djs_core <admin@djscore.org> - 0.3.1
- update to new version
* Sat Jun 19 2010 djs_core <admin@djscore.org> - 0.2.6
- update to new version
* Tue Jun 15 2010 djs_core <admin@djscore.org> - 0.2.5
- update to new version
* Mon Jun 7 2010 djs_core <admin@djscore.org> - 0.2.4
- update to new version
* Sun Jun 6 2010 djs_core <admin@djscore.org> - 0.2.3
- update to new version
* Thu Jun 3 2010 djs_core <admin@djscore.org> - 0.2.2
- initial package
