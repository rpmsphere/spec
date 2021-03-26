%define _hardened_build 1
%global selinux_variants mls strict targeted
%global selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)

Name:		bitcoin
Version:	0.8.6
Release:	1.1
Summary:	Peer-to-peer digital currency
Group:		Applications/System
License:	MIT
URL:		http://bitcoin.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-linux.tar.gz
Source3:	bitcoin.init
Source4:	bitcoin.te
Source5:	bitcoin.fc
Source6:	bitcoin.if
Patch1:		bitcoin-0.6.3-boostmt.patch
Patch3:		bitcoin-0.7.2-fhs-paths.patch
BuildRequires:	qt-devel >= 1:4.6 qrencode-devel openssl-compat-bitcoin-devel miniupnpc-devel boost-devel >= 1.47.0 db4-devel
BuildRequires:	checkpolicy, selinux-policy-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libdb4-cxx-devel
Requires:	qt >= 4.6 miniupnpc qrencode boost >= 1.47.0
Requires:	openssl-compat-bitcoin-libs >= 1.0.0j

%package server
Summary:	Peer-to-peer digital currency
Requires(pre):	shadow-utils
Requires(post): chkconfig
Requires(post):		/usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts
Requires(postun): initscripts
Requires(postun):	/usr/sbin/semodule, /sbin/restorecon, /sbin/fixfiles
%if "%{selinux_policyver}" != ""
Requires:	selinux-policy >= %{selinux_policyver}
Requires:	policycoreutils-python
%endif
Requires:	boost >= 1.47.0
Requires:	openssl-compat-bitcoin-libs >= 1.0.0j

%description
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network.

Bitcoin is also the name of the open source software which enables the
use of this currency.

This package provides Bitcoin, a user-friendly wallet manager for
personal use.

%description server
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network.

This package provides bitcoind, a wallet server and command line tool
for manipulating a remote bitcoind server.

%prep
%setup -q -n %{name}-%{version}-linux
# Strip OS X resource forks that upstream accidentally bundled
find . -name "._*" -delete
%if 0%{fedora} < 20
%patch1 -p1
%endif
%patch3 -p1

# Prep SELinux policy
mkdir SELinux
cp -p %{SOURCE4} %{SOURCE5} %{SOURCE6} SELinux
# Remove prebuilt binaries, if present
rm -fr bin

%build
# Build bitcoin GUI
pushd src
test -d /usr/lib64/qt4/bin && \
	QMAKE=/usr/lib64/qt4/bin/qmake || \
	QMAKE=/usr/lib/qt4/bin/qmake

%if 0%{fedora} < 20
$QMAKE BOOST_LIB_SUFFIX=-mt OPENSSL_INCLUDE_PATH=/opt/openssl-compat-bitcoin/include OPENSSL_LIB_PATH=/opt/openssl-compat-bitcoin/lib BDB_INCLUDE_PATH=/usr/include/libdb4 BDB_LIB_PATH=%{_libdir}/libdb4 USE_UPNP=1 USE_DBUS=1 USE_QRCODE=1 LIBS=-Wl,-rpath,/opt/openssl-compat-bitcoin/lib
%else
$QMAKE OPENSSL_INCLUDE_PATH=/opt/openssl-compat-bitcoin/include OPENSSL_LIB_PATH=/opt/openssl-compat-bitcoin/lib BDB_INCLUDE_PATH=/usr/include/libdb4 BDB_LIB_PATH=%{_libdir}/libdb4 USE_UPNP=1 USE_DBUS=1 USE_QRCODE=1 LIBS=-Wl,-rpath,/opt/openssl-compat-bitcoin/lib
%endif
make %{?_smp_mflags} CFLAGS="%{optflags}"

# Build bitcoind
pushd src
make -f makefile.unix %{?_smp_mflags} CFLAGS="%{optflags}" OPENSSL_INCLUDE_PATH=/opt/openssl-compat-bitcoin/include OPENSSL_LIB_PATH=/opt/openssl-compat-bitcoin/lib BDB_INCLUDE_PATH=/usr/include/libdb4 BDB_LIB_PATH=%{_libdir}/libdb4 LDFLAGS=-Wl,-rpath,/opt/openssl-compat-bitcoin/lib

popd
popd
# Build SELinux policy
pushd SELinux
for selinuxvariant in %{selinux_variants}
do
# FIXME: Create and debug SELinux policy
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv bitcoin.pp bitcoin.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
popd

# Bitcoin doesn't include a "make install" so we have to do it ourselves.
# This is just as well since everything is going into standard locations.
%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp src/contrib/debian/examples/bitcoin.conf bitcoin.conf.example
# Install bitcoin GUI
pushd src
install -D -m755 -p bitcoin-qt %{buildroot}%{_bindir}/bitcoin-qt
mkdir -p -m 755 %{buildroot}%{_datadir}/pixmaps
install -D -m644 -p share/pixmaps/*.{png,xpm,ico} %{buildroot}%{_datadir}/pixmaps/
install -D -m644 -p contrib/debian/bitcoin-qt.desktop %{buildroot}%{_datadir}/applications/bitcoin-qt.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/bitcoin-qt.desktop
install -D -m644 -p contrib/debian/bitcoin-qt.protocol %{buildroot}%{_datadir}/kde4/services/bitcoin-qt.protocol
# Install bitcoind
install -D -m755 -p src/bitcoind %{buildroot}%{_sbindir}/bitcoind
install -D -m755 -p %{SOURCE3} %{buildroot}%{_initrddir}/bitcoin
install -d -m750 -p %{buildroot}%{_localstatedir}/lib/bitcoin
install -d -m750 -p %{buildroot}%{_sysconfdir}/bitcoin
install -D -m644 -p contrib/debian/examples/bitcoin.conf %{buildroot}%{_sysconfdir}/bitcoin/bitcoin.conf
install -D -m644 -p contrib/debian/manpages/bitcoind.1 %{buildroot}%{_mandir}/man1/bitcoind.1
install -D -m644 -p contrib/debian/manpages/bitcoin.conf.5 %{buildroot}%{_mandir}/man5/bitcoin.conf.5
gzip %{buildroot}%{_mandir}/man1/bitcoind.1
gzip %{buildroot}%{_mandir}/man5/bitcoin.conf.5
popd
# Install SELinux policy
for selinuxvariant in %{selinux_variants}
do
	install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
	install -p -m 644 SELinux/bitcoin.pp.${selinuxvariant} \
		%{buildroot}%{_datadir}/selinux/${selinuxvariant}/bitcoin.pp
done

%clean
rm -rf %{buildroot}

%pre server
getent group bitcoin >/dev/null || groupadd -r bitcoin
getent passwd bitcoin >/dev/null ||
	useradd -r -g bitcoin -d /var/lib/bitcoin -s /sbin/nologin \
	-c "Bitcoin wallet server" bitcoin
exit 0

%post server
/sbin/chkconfig --add bitcoin
for selinuxvariant in %{selinux_variants}
do
	/usr/sbin/semodule -s ${selinuxvariant} -i \
		%{_datadir}/selinux/${selinuxvariant}/bitcoin.pp \
		&> /dev/null || :
done
# FIXME This is less than ideal, but until dwalsh gives me a better way...
/usr/sbin/semanage port -a -t bitcoin_port_t -p tcp 8332
/usr/sbin/semanage port -a -t bitcoin_port_t -p tcp 8333
/usr/sbin/semanage port -a -t bitcoin_port_t -p tcp 18333
/sbin/fixfiles -R bitcoin-server restore &> /dev/null || :
/sbin/restorecon -R %{_localstatedir}/lib/bitcoin || :

%preun server
if [ $1 -eq 0 ] ; then
    /sbin/service bitcoin stop >/dev/null 2>&1
    /sbin/chkconfig --del bitcoin
fi

%postun server
if [ "$1" -ge "1" ] ; then
	/sbin/service bitcoin condrestart >/dev/null 2>&1 || :
else
	/sbin/fixfiles -R bitcoin-server restore &> /dev/null || :
fi
if [ $1 -eq 0 ] ; then
	# FIXME This is less than ideal, but until dwalsh gives me a better way...
	/usr/sbin/semanage port -d -p tcp 8332
	/usr/sbin/semanage port -d -p tcp 8333
	/usr/sbin/semanage port -d -p tcp 18333
	for selinuxvariant in %{selinux_variants}
	do
		/usr/sbin/semodule -s ${selinuxvariant} -r bitcoin \
		&> /dev/null || :
	done
	/sbin/fixfiles -R bitcoin-server restore &> /dev/null || :
	[ -d %{_localstatedir}/lib/bitcoin ] && \
		/sbin/restorecon -R %{_localstatedir}/lib/bitcoin \
		&> /dev/null || :
fi

%files
%doc COPYING README.md bitcoin.conf.example
%{_bindir}/bitcoin-qt
%{_datadir}/applications/bitcoin-qt.desktop
%{_datadir}/kde4/services/bitcoin-qt.protocol
%{_datadir}/pixmaps/*

%files server
%doc COPYING README.md
%dir %attr(750,bitcoin,bitcoin) %{_localstatedir}/lib/bitcoin
%dir %attr(750,bitcoin,bitcoin) %{_sysconfdir}/bitcoin
%doc SELinux/*
%{_sbindir}/bitcoind
%{_initrddir}/bitcoin
%config(noreplace) %{_sysconfdir}/bitcoin/bitcoin.conf
%{_mandir}/man1/bitcoind.1.gz
%{_mandir}/man5/bitcoin.conf.5.gz
%{_datadir}/selinux/*/bitcoin.pp

%changelog
* Fri Jan 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.6
- Rebuild for Fedora
* Wed Oct 16 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.5-2
- Remove bitcoind and bitcoin-qt launcher scripts no longer used upstream
- Ship upstream example config file
* Sat Oct 05 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.5-1
- Update for Bitcoin 0.8.5.
* Wed Sep 04 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.4-1
- Update for Bitcoin 0.8.4.
- Strip OS X resource forks from upstream tarball.
- Use default SELinux context for /etc/bitcoin directory itself;
  fixes SELinux denial against updatedb.
* Fri Jul 05 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.3-1
- Update for Bitcoin 0.8.3.
* Sun Jun 02 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.2-2
- Fixed bitcoin-server dependency for new openssl packages
* Sun Jun 02 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.2-1
- Update for Bitcoin 0.8.2.
* Fri Mar 29 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.1-3
- Added missing openssl and boost Requires for bitcoin-server
* Sun Mar 24 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.1-2
- Added missing SELinux dependencies
- Updated for RHEL: Now build against a private copy of Boost
* Thu Mar 21 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.8.1-1
- Update for Bitcoin 0.8.1.
- Removed Patch2 (qt 4.6 compatibility) as it has been accepted upstream
* Tue Jan 29 2013 Michael Hampton <bitcoin@ringingliberty.com> 0.7.2-3
- Mass rebuild for corrected package signing key
* Mon Dec 17 2012 Michael Hampton <bitcoin@ringingliberty.com> 0.7.2-1
- Update for Bitcoin 0.7.2.
- Update for separate OpenSSL package openssl-compat-bitcoin.
* Wed Aug 22 2012 Michael Hampton <bitcoin@ringingliberty.com> 0.6.3-1
- Initial package
