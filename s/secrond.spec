Summary:   Cron daemon supporting seconds
Name:      secrond
Version:   0.41
Release:   1
License:   GPLv3
Group:     Applications/System
Source0:   https://launchpad.net/secrond/trunk/0.41/+download/%{name}-%{version}.tar.gz
URL:       https://launchpad.net/secrond

%description
Secrond is a light-weight cron implementation that allows running of
user-specified programs at periodic scheduled times, handling tasks
in intervals of seconds rather than minutes, as well as hours and days.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 755 src/secrond $RPM_BUILD_ROOT/usr/sbin

# write initscript
mkdir -p $RPM_BUILD_ROOT/etc/init.d
sed -e 's,/usr/local/sbin/secrond,/usr/sbin/secrond,g' < misc/init.sh >$RPM_BUILD_ROOT/etc/init.d/secrond
chmod 755 $RPM_BUILD_ROOT/etc/init.d/secrond

# secrond config
mkdir -p $RPM_BUILD_ROOT/etc/secrond
install -m 644 misc/schedule $RPM_BUILD_ROOT/etc/secrond

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_sbindir}/%{name}
%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/%{name}

%post
/sbin/chkconfig --add secrond

%preun
if [ $1 = 0 ]; then
	/sbin/service secrond stop > /dev/null 2>&1
	/sbin/chkconfig --del secrond
fi

rm -rf /usr/doc/secrond/ /usr/sbin/secrond
rm -f /etc/init.d/secrond
mv -f /etc/secrond/schedule /etc/secrond/schedule.rpmoves

%Changelog
* Tue May 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.41
- Rebuilt for Fedora
* Thu Sep 27 2011 Baron. Wan <baron.wan@ossii.com.tw> - 0.41-2.ox2
- create .spec file, and debug it.
