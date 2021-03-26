Name:               moblock
Version:            0.8
Release:            8.1
Summary:            Blocks Connections from/to Hosts listed in Peerguardian Files
Source:             moblock-%{version}.tar.bz2
Source1:            moblock.lr
Source2:            moblock.init
Source3:            moblock.sysconfig
Patch1:             moblock-fix_makefile.patch
Patch2:             moblock-fix_includes.patch
Patch3:             moblock-paths.patch
URL:                http://moblock.berlios.de/
Group:              Productivity/Networking/Security
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      libnetfilter_queue-devel
BuildRequires:      gcc make glibc-devel pkgconfig

%description
MoBlock is a linux console application that blocks connections from/to hosts
listed in a file in peerguardian format (guarding.p2p). It uses iptables
ipqueue userspace library and it is very light in resource usage (cpu, ram).

%prep
%setup -q -n moblock
%patch1
%patch2
%patch3
%__chmod 0644 COPYING

%build
%__make %{?jobs:-j%{jobs}} \
    CC="%__cc" \
    OPTFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 moblock "$RPM_BUILD_ROOT%{_sbindir}/moblock"

%__install -d "$RPM_BUILD_ROOT%{_sysconfdir}/moblock"

%__install -D -m0644 "%{SOURCE1}" "$RPM_BUILD_ROOT/etc/logrotate.d/%{name}"
%__install -D -m0755 "%{SOURCE2}" "$RPM_BUILD_ROOT/etc/init.d/%{name}"
%__install -d "$RPM_BUILD_ROOT/usr/sbin"
%__ln_s "../../etc/init.d/%{name}" "$RPM_BUILD_ROOT/usr/sbin/rc%{name}"
%__install -D -m0644 "%{SOURCE3}" "$RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.%{name}"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc COPYING README Changelog
%dir %{_sysconfdir}/moblock
%{_sbindir}/moblock
%config(noreplace) /etc/logrotate.d/%{name}
/etc/init.d/%{name}
/usr/sbin/rc%{name}
/var/adm/fillup-templates/sysconfig.%{name}

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora

* Sun Aug  1 2010 pascal.bleser@opensuse.org
- initial package (0.8)
