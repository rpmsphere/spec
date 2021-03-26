Name:           tuncfg
Summary:        TUN/TAP Device Driver
Version:        1
Release:        4.1
Group:          Productivity/Networking/System
BuildRequires:  gcc patch
Source0:        tuncfg.tar.bz2
# PATCH-FIX-UPSTREAM tuncfg.patch adam@mizerski.pl -- fixes. (changing long to int makes it work on 64bit)
Patch0:         tuncfg.patch
License:        BSD

%prep
%setup -n %name
%patch0 -p1

%build
gcc tuncfg.c -o tuncfg -fno-strict-aliasing %optflags

%install
%__install -D -m 700 tuncfg $RPM_BUILD_ROOT/sbin/tuncfg

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%attr(700,root,root) /sbin/tuncfg
%doc LICENSE

%description
Tuncfg is a tunneling device management and configuration daemon.

The idea is that tuncfg encapsulates all root-level functionality
normally required by a private networking software. Namely -

* creation of tunneling devices; this requires an access to.
/dev/net/tun file, which _usually_ has 700 access mask

* configuration of the tunneling device using ifconfig, which is
always a root-level operation

Tuncfg must be run with superuser privileges. It will daemonize and
open a listening domain socket /var/run/tuncfg.sock.

Upon accepting the connection on this socket, it will issue an open()
call for /dev/net/tun file (thus instantiating the tunneling device).
and pass obtained FD to the peer process. It will also query and pass
the MAC address of the device to the peer process.

It will then listen for ifconfig requests from the peer. The request.
contains just an IP address and mask. Tuncfg will lookup the tun.
device the peer owns and will assign IP/mask to it using system().
call for ipconfig command.

'tuncfg' starts the daemon (it won't start twice, there's a check)
'tuncfg -d' starts the console version (useful for debugging)

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuild for Fedora
* Mon Apr 12 2010 adam@mizerski.pl
- added "#include <sys/file.h>" and "-fno-strict-aliasing"
* Sun Apr 11 2010 adam@mizerski.pl
- added %%optflags and 3rd argument to open
* Sun Mar  7 2010 adam@mizerski.pl
- new package
