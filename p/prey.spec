Name: prey
Summary: Tracking your stolen laptop
Version: 0.5.3
Release: 9
License: GPLv3
Group: Monitoring
Source: http://preyproject.com/releases/%{version}/%{name}-%{version}-linux.zip
Source1: prey-config.desktop
URL: http://preyproject.com/
Requires: curl, scrot, groff, gstreamer, perl-Net-SSLeay, perl-IO-Socket-SSL, mpg123, ImageMagick, traceroute
BuildArch: noarch

%description
Prey is a lightweight application for tracking your stolen laptop.

Prey comprises a shell scripts which calls out on a regular basis
to either a server run by prey project, or a url nominated by 
system administration. A graphical configuration tool is also provided
which is used to maintain the simple config file.

%prep
%setup -q -n prey

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
install -m 755 %{SOURCE1} prey-config.desktop
install -m 755 prey-config.desktop $RPM_BUILD_ROOT%{_datadir}/applications/

cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

cat << EOF > $RPM_BUILD_ROOT%_sysconfdir/cron.d/%name
 */20 * * * * root /usr/share/prey/prey.sh > /var/log/prey.log
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/prey/platform/linux/prey-config.py %{buildroot}%{_datadir}/prey/modules/lock/platform/linux/prey-lock

%files
%doc README LICENSE
%{_datadir}/%{name}
%{_sysconfdir}/cron.d/prey
%{_datadir}/applications/prey-config.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jul 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3
- Rebuild for Fedora
* Wed Jun 08 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.5.3-3mdv2011.0
+ Revision: 683312
- bump new version
- config tool on menu
* Tue Jun 07 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.5.3-2
+ Revision: 683110
- new version
-Change on SPEC
* Mon May 16 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.5.3-1
+ Revision: 675128
- first version of the package
- Created package structure for prey.
