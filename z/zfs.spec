Summary:         Native ZFS for Linux
Group:           Utilities/System
Name:            zfs
Version:         0.8.4
Release:         1
License:         CDDL
URL:             http://zfsonlinux.org/
Source:          http://archive.zfsonlinux.org/downloads/zfsonlinux/zfs/%{name}-%{version}.tar.gz
BuildRequires:   zlib-devel
BuildRequires:   e2fsprogs-devel
BuildRequires:   libuuid-devel
BuildRequires:   libblkid-devel
BuildRequires:   libattr-devel
BuildRequires:   libtirpc-devel

%description
ZFS is an advanced file system and volume manager which was originally
developed for Solaris and is now maintained by the Illumos community.

ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.


%package devel
Summary:         ZFS File System User Headers
Group:           Development/Libraries
Requires:        %{name}
Requires:        zlib e2fsprogs
BuildRequires:   zlib-devel e2fsprogs-devel

%description devel
The %{name}-devel package contains the header files needed for building
additional applications against the %{name} libraries.

%package test
Summary:         ZFS File System Test Infrastructure
Group:           Utilities/System
Requires:        %{name}
Requires:        parted lsscsi

%description test
The %{name}-test package contains a test infrastructure for zpios which
can be used to simplfy the benchmarking of various hardware and software
configurations.  The test infrastructure additionally integrates with
various system profiling tools to facilitate an in depth analysis.

%package dracut
Summary:         ZFS Dracut Module
Group:           System Environment/Base
Requires:        %{name}
Requires:        dracut

%description dracut
The %{name}-dracut package allows dracut to construct initramfs images
which are ZFS aware.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --with-config=user
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYRIGHT LICENSE *.md
/sbin/mount.zfs
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/lib*
%{_mandir}/man?/*
%{_sysconfdir}/init.d/*
%{_sysconfdir}/zfs
/usr/lib/systemd/system-preset/*
/usr/lib/systemd/system/*
/usr/lib/systemd/system-generators/zfs-mount-generator
/lib/udev/rules.d/*
/lib/udev/*_id
%{_datadir}/zfs/*
/etc/sudoers.d/zfs
/etc/sysconfig/zfs
%{python3_sitelib}/*

%files devel
%{_includedir}/*
%{_datadir}/pkgconfig/*

%files test
%{_libexecdir}/zfs/*

%files dracut
/usr/lib/dracut/modules.d/90zfs/*
/usr/lib/modules-load.d/zfs.conf
/usr/lib/dracut/modules.d/02zfsexpandknowledge/module-setup.sh
%{_datadir}/initramfs-tools/conf-hooks.d/zfs
%{_datadir}/initramfs-tools/hooks/zfs
%{_datadir}/initramfs-tools/scripts/local-top/zfs
%{_datadir}/initramfs-tools/scripts/zfs
%{_datadir}/initramfs-tools/conf.d/zfs

%post
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add zfs
exit 0

%preun
[ "$1" = 0 ] && [ -x /sbin/chkconfig ] && /sbin/chkconfig --del zfs
exit 0

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.4
- Rebuilt for Fedora
