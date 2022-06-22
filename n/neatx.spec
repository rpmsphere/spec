Name: neatx
Version: 0.3.1
Release: 1
Summary: Open Source NX server
Group: Networking/Remote access
License: GPLv2
URL: http://code.google.com/p/neatx/
Source: http://neatx.googlecode.com/files/%name-%version.tar.gz
Source1: README.ALT
Source2: %name.conf
Requires: nx
Requires: openssl
Requires: nc
Requires: dbus-x11
Requires: binutils
Requires: Xdialog
#Requires: %_bindir/xvt
Requires: python2-%name
Conflicts: freenx-server
Conflicts: tacix-freenx
BuildRequires: python2-devel
#BuildRequires: python2-docutils
 
%package -n python2-%name
Summary: Python2 module for %name
Group: Development/Python
BuildArch: noarch

%description
Neatx is an Open Source NX server, similar to the commercial NX server from NoMachine.

%description -n python2-%name
Python2 module for %name

%prep
%setup -q

%build
export PYTHON=/usr/bin/python2
#./autogen.sh
%configure --localstatedir=%_var
%__make

%install
rm -rf %buildroot
%makeinstall
mkdir -p %buildroot%_var/lib/nxserver/home
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir
ln -s ../../%_libdir/%name/nxserver-login-wrapper %buildroot%_bindir/nxserver
install -m644 %SOURCE1 %buildroot%_docdir/%name
install -m644 %SOURCE2 %buildroot%_sysconfdir/%name.conf

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_libdir}/%{name}/*

%pre
/usr/sbin/groupadd nx 2> /dev/null ||:
/usr/sbin/useradd -g nx -G utmp -d /var/lib/nxserver/home/ -s %_bindir/nxserver \
       -c "NX System User" nx 2> /dev/null ||:
if [ ! -d %_datadir/fonts/misc ] && [ ! -e %_datadir/fonts/misc ] && [ -d %_datadir/fonts/bitmap-fonts ]
then
   ln -s %_datadir/fonts/bitmap-fonts %_datadir/fonts/misc
fi

%files
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/nxserver
%_libdir/%name
%_datadir/%name
%attr(2770,root,nx) %_var/lib/%name
%dir %_var/lib/nxserver
%attr(2750,nx,nx) %_var/lib/nxserver/home
%_docdir/%name

%files -n python2-%name
%python2_sitelib/%name

%clean
rm -rf %buildroot

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Thu Jul 09 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt2
- fix work
- add README.ALT
- replace default config
* Wed Jul 08 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus (not tested)
