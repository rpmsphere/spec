Summary: Graphical remote administration system
Name: tightvnc
Version: 1.3.10
Release: 18.2
License: GPL
Group: User Interface/Desktops
URL: http://www.tightvnc.com/
Source0: http://dl.sf.net/vnc-tight/%{name}-%{version}_unixsrc.tar.bz2
Source1: tcpd.h
Source2: https://www.tightvnc.com/logo/tightvnc-logo-90x90.png
BuildRequires: imake, desktop-file-utils
BuildRequires: zlib-devel, libjpeg-devel, perl-interpreter
BuildRequires: libX11-devel, libXaw-devel
BuildRequires: nss_nis
BuildRequires: tcp_wrappers
Provides: vnc

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.

TightVNC is an enhanced VNC distribution. This package contains
a client which will allow you to connect to other desktops running
a VNC or a TightVNC server.

%package server
Summary: TightVNC server
Group: User Interface/X
Provides: vnc-server

%description server
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.

TightVNC is an enhanced VNC distribution. This package is a TightVNC
server, allowing others to access the desktop on your machine.

%prep
%setup -q -n vnc_unixsrc
cp %{SOURCE1} include/

%{__perl} -pi -e 's|/usr/local/vnc/classes|%{_datadir}/vnc/classes|;' vncserver
%{__perl} -pi -e 's|unix/:7100|unix/:-1|;' vncserver
%{__perl} -pi -e 's|^# (\$colorPath) = .+$|$1 = "/usr/share/X11/rgb";|' vncserver

%{__cat} <<EOF >vncservers.sysconfig
# The VNCSERVERS variable is a list of display:user pairs.
#
# Uncomment the line below to start a VNC server on display :1
# as my 'myusername' (adjust this to your own).  You will also
# need to set a VNC password; run 'man vncpasswd' to see how
# to do that.
#
# DO NOT RUN THIS SERVICE if your local area network is
# untrusted!  For a secure way of using VNC, see
# <URL:http://www.uk.research.att.com/vnc/sshvnc.html>.

# VNCSERVERS="1:myusername"
EOF

%{__cat} <<EOF >vncviewer.desktop
[Desktop Entry]
Name=Tightvnc VNC Viewer
Comment=Connect to a VNC server
Icon=tightvnc
Exec=vncviewer
Terminal=false
Type=Application
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >vncserver.sysv
#!/bin/bash
#
# Init file for TightVNC Server
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 91 35
# description: TightVNC remote X administration daemon.
#
# processname: Xvnc

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 1

[ -x %{_bindir}/Xvnc ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/vncservers"
VNCSERVERS=""

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="Xvnc"
desc="TightVNC remote administration daemon"

start() {
    echo -n $"Starting $desc ($prog):"
    ulimit -S -c 0 &>/dev/null
    for display in ${VNCSERVERS}; do
        echo -n "${display} "
        unset BASH_ENV ENV
        initlog $INITLOG_ARGS -c \
            "su ${display##*:} -c \"cd ~${display##*:} && [ -f .vnc/passwd ] && vncserver :${display%%:*} ${VNCSERVERARGS[${display%:*}]}\""
        RETVAL=$?
        [ "$RETVAL" -ne 0 ] && break
    done
    [ "$RETVAL" -eq 0 ] && success $"vncserver startup" || failure $"vncserver start"
    echo
    [ "$RETVAL" -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $desc ($prog): "
    for display in ${VNCSERVERS}; do
        echo -n "${display} "
        unset BASH_ENV ENV
        initlog $INITLOG_ARGS -c \
            "su ${display##*:} -c \"vncserver -kill :${display%%:*}\" &>/dev/null"
    done
    RETVAL=$?
    [ "$RETVAL" -eq 0 ] && success $"vncserver shutdown" || failure $"vncserver shutdown"
    echo
    [ "$RETVAL" -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

restart() {
    stop
    start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart|reload)
    restart
    ;;
  condrestart)
    [ -e %{_localstatedir}/lock/subsys/$prog ] && restart
    RETVAL=$?
    ;;
  status)
    status $prog
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
%ifarch aarch64
sed -i 's|-Dlinux LinuxMachineDefines|-Dlinux -D__aarch64__|' Xvnc/config/cf/linux.cf
%endif
### Use xinit's Xclients script to start the session (bug #52711)
patch < vnc-xclients.patch

xmkmf -a
%{__make} World CDEBUGFLAGS="-O2 -g -pipe -Wall"
cd Xvnc
%configure
sed -i 's|ar clq|ar cq|' `find . -name Makefile`
%{__make} CDEBUGFLAGS="-O2 -g -pipe -Wall" \
    EXTRA_DEFINES="-DUSE_LIBWRAP=1" \
    EXTRA_LIBRARIES="-lwrap -lnss_nis -Wl,--allow-multiple-definition"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
    %{buildroot}%{_mandir}/man1/ \
    %{buildroot}%{_datadir}/vnc/
./vncinstall %{buildroot}%{_bindir} %{buildroot}%{_mandir}

%{__cp} -apR classes %{buildroot}%{_datadir}/vnc/

%{__install} -Dp -m0755 vncserver.sysv %{buildroot}%{_initrddir}/vncserver
%{__install} -Dp -m0644 vncservers.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/vncservers

%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/tightvnc.png
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor ""    \
        --dir %{buildroot}%{_datadir}/applications \
        vncviewer.desktop

%clean
%{__rm} -rf %{buildroot}

%post server
/sbin/chkconfig --add vncserver

%preun server
if [ $1 -eq 0 ]; then
    /sbin/service vncserver stop &>/dev/null || :
    /sbin/chkconfig --del vncserver
fi

%postun server
/sbin/service vncserver condrestart &>/dev/null || :

%files
%doc ChangeLog LICENCE.TXT README WhatsNew Xvnc/bug-report Xvnc/RELNOTES*
%doc %{_mandir}/man1/vncviewer.*
%{_bindir}/vncviewer
%{_datadir}/applications/vncviewer.desktop

%files server
%doc ChangeLog LICENCE.TXT README WhatsNew Xvnc/bug-report Xvnc/RELNOTES*
%doc %{_mandir}/man1/Xvnc.*
%doc %{_mandir}/man1/vncserver.*
%doc %{_mandir}/man1/vncconnect.*
%doc %{_mandir}/man1/vncpasswd.*
%config %{_initrddir}/vncserver
%config %{_sysconfdir}/sysconfig/vncservers
%{_bindir}/Xvnc
%{_bindir}/vncserver
%{_bindir}/vncpasswd
%{_bindir}/vncconnect
%{_datadir}/vnc
%{_datadir}/pixmaps/tightvnc.png

%changelog
* Mon Jul 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.10
- Rebuilt for Fedora
* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 1.3.9-3 - 6211+/dag
- Improved sysv script to include VNCSERVERARGS. (Arturo Díaz Rosemberg)
* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 1.3.9-2
- Added fix for rgb.txt support. (Alberto Lusiani)
* Tue May 08 2007 Dag Wieers <dag@wieers.com> - 1.3.9-1
- Updated to release 1.3.9.
* Wed Oct 18 2006 Dag Wieers <dag@wieers.com> - 1.3.8-1
- Updated to release 1.3.8.
* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 1.2.9-3
- Fixed dependency on xorg-x11 instead of XFree86 on fc2. (Christopher V. Browne)
* Sat Apr 17 2004 Dag Wieers <dag@wieers.com> - 1.2.9-2
- Fixed the vncserver script to check for Xvnc instead of sockd. (Alfredo Milani-Comparetti)
* Wed Mar 10 2004 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Don't obsolete vnc, just conflict. (Reuben Thomas)
* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 1.2.9-0
- Updated to release 1.2.9.
* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Updated to release 1.2.8.
* Fri Jan 17 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Initial package. (using DAR)
