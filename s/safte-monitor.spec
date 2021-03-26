Name:           safte-monitor
Obsoletes:      saftemon
Summary:        Linux SAF-TE SCSI enclosure monitor
Version:        0.0.5
Release:        383.1
URL:            http://oss.metaparadigm.com/safte-monitor/
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.diff
Patch1:         safte-monitor-fix.patch
Patch2:         safte-monitor.ioctl.patch
License:        GPL v2 or later
Group:          System/Monitoring

%description
saftemon reads disk enclosure status information from SAF-TE (SCSI
Accessible Fault Tolerant Enclosures). SAF-TE is a component of SES
(SCSI Enclosure Services) which is common on most SCSI disk enclosures
these days. saftemon can monitor multiple SAF-TE devices and will
automatically detect them.

The information retrieved includes power supply, temperature, audible
alarm, drive faults, array critical/failed/rebuilding state and door
lock status. saftemon logs changes in the status of these enclosure
elements to syslog and can optionally execute an alert help program
with details of the component failure.

Authors:
--------
    Michael Clark <michael@metapardigm.com>

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
sed -i '/stropts/d' src/qlogic_api.c

%build
rm -f config.cache config.log config.status
CC=gcc CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" ./configure --prefix=/usr \
	--exec-prefix=/usr \
	--sysconfdir=/etc \
	--libexecdir=/usr/%{_lib} \
	--localstatedir=/var
make CC=gcc

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/etc/init.d
install redhat/init.d/safte-monitor $RPM_BUILD_ROOT/etc/init.d/safte-monitor
install -d $RPM_BUILD_ROOT/usr/sbin
ln -s ../../etc/init.d/safte-monitor $RPM_BUILD_ROOT/usr/sbin/rcsafte-monitor
install -d $RPM_BUILD_ROOT/var/adm/fillup-templates
install redhat/sysconfig/safte-monitor $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.safte-monitor
install -d $RPM_BUILD_ROOT/etc/safte-monitor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG README README.html mathopd-1.3pl7-lite/COPYING
%config /etc/init.d/safte-monitor
/var/adm/fillup-templates/sysconfig.safte-monitor
%config(noreplace) /etc/safte-monitor.conf
%config(noreplace) /etc/safte-monitor.passwd
%dir /etc/safte-monitor
%config /etc/safte-monitor/alert
/usr/bin/safte-monitor
/usr/sbin/rcsafte-monitor
/usr/lib/safte-monitor
%defattr(-,daemon,root)
/var/run/safte-monitor
/var/log/safte-monitor

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5
- Rebuild for Fedora
* Wed Aug 26 2009 mls@suse.de
- make patch0 usage consistent
* Tue Jun 16 2009 coolo@novell.com
- fix build with glibc 2.10
* Thu Aug 28 2008 cthiel@suse.de
- fix build script
* Thu Aug  9 2007 olh@suse.de
- update ioctl arguments, the size arg is not sizeof() anymore
* Mon Jun 18 2007 dmueller@suse.de
- fix init script dependencies
* Tue Sep 12 2006 ro@suse.de
- fix another case of non-void function returning void
* Tue Jul  4 2006 aj@suse.de
- Fix build.
* Sat May 27 2006 schwab@suse.de
- Use RPM_OPT_FLAGS.
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jun 17 2005 meissner@suse.de
- use RPM_OPT_FLAGS, add include string.h in one place.
* Sun Jan 11 2004 adrian@suse.de
- build as user
* Tue Sep  2 2003 mmj@suse.de
- Add sysconfig metadata [#28930]
* Mon Jun  2 2003 ro@suse.de
- correctly install alert script
* Thu Feb 20 2003 mmj@suse.de
- Add sysconfig metadata [#22680]
- Only setup and patch in %%prep
* Fri Aug 30 2002 garloff@suse.de
- Add comment to SAFTEMONITOR_OPTIONS sysconfig variable (#18656)
* Mon Aug 19 2002 garloff@suse.de
- Add %%fillup_prereq and %%insserv_prereq (bug #17976)
* Wed Aug  7 2002 garloff@suse.de
- Renamed package to safte-monitor (trademark issues)
- Update to version 0.0.5
* Thu May  9 2002 garloff@suse.de
- Build package from saftemon-0.0.4
- Fix init script and sysconfig file to match SuSE conventions
- Move alert script to /etc/saftemon/alert
