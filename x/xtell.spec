Name: xtell
Version: 2.10.7
Release: 5.1
License: GPL
URL: http://melkor.dnp.fmph.uniba.sk/~garabik/xtell.html
Source: xtell_%{version}.tar.gz
Group: Networking/Daemons
Summary: Simple messaging xlient and server
BuildRequires: libident-devel
BuildRequires: readline-devel

%description
xtell is a sort of networked write.

%prep
%setup -q

%build
make LDFLAGS+=" -Wl,--allow-multiple-definition -lreadline -lident"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/

cp xtell ${RPM_BUILD_ROOT}%{_bindir}
cp xtelld ${RPM_BUILD_ROOT}%{_sbindir}

cp xtell.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/xtell.1
cp xtelld.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/xtelld.8
								
%post
chgrp tty %{_sbindir}/xtelld
chmod g+s %{_sbindir}/xtelld
cp -f /etc/inetd.conf /etc/inetd.conf.rpmsave
cat /etc/inetd.conf.rpmsave | grep -v '^xtell\>' | grep -v "End of inetd.conf" > /etc/inetd.conf
echo "# xtelld" >> /etc/inetd.conf
echo "xtell	stream	tcp	nowait	nobody	%{_sbindir}/tcpd	%{_sbindir}/xtelld" >> /etc/inetd.conf
echo >> /etc/inetd.conf
echo "# End of inetd.conf" >> /etc/inetd.conf
cp -f /etc/services /etc/services.rpmsave
cat /etc/services.rpmsave | grep -v '^xtell\>' | grep -v "End of services" > /etc/services
echo 'xtell	4224/tcp			# xtell server' >> /etc/services
echo >> /etc/services
echo "# End of services" >> /etc/services
killall -HUP inetd

%postun
cp -f /etc/inetd.conf /etc/inetd.conf.rpmsave.postun
cat /etc/inetd.conf.rpmsave.postun | grep -v '^xtell\>' > /etc/inetd.conf
cp -f /etc/services /etc/services.rpmsave.postun
cat /etc/services.rpmsave.postun | grep -v '^xtell\>' > /etc/services
echo "# End of services" >> /etc/services
killall -HUP inetd

%files
%doc README 
%{_mandir}/man1/xtell.1.*
%{_mandir}/man8/xtelld.8.*
%{_bindir}/xtell
%attr(-,root,tty) %{_sbindir}/xtelld

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.10.7
- Rebuilt for Fedora
* Mon Mar 15 1999 Radovan Garabik <garabik@fmph.uniba.sk>
- New release
* Fri Mar  5 1999 Radovan Garabik <garabik@fmph.uniba.sk>
- New release
* Sat Dec 20 1998 Radovan Garabik <garabik@fmph.uniba.sk>
- Initial release
