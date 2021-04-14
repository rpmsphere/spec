%undefine _debugsource_packages
Name:       mic2
Summary:    Tools for building images for MeeGo
Version:    0.24.15git
Release:    3.1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://meego.gitorious.org/meego-developer-tools/image-creator
Source0:    %{name}-%{version}.tar.gz
Requires:   util-linux
Requires:   coreutils
Requires:   python >= 2.5
Requires:   e2fsprogs
Requires:   dosfstools >= 2.11-8
Requires:   yum >= 3.2.24
Requires:   pykickstart >= 0.96
Requires:   python-iniparse
Requires:   syslinux >= 3.82
Requires:   curl
Requires:   kpartx
Requires:   parted
Requires:   device-mapper
Requires:   zlib
Requires:   rsync
Requires:   /usr/bin/mkisofs
Requires:   wget
Requires:   cpio
Requires:   isomd5sum
Requires:   gzip
Requires:   bzip2
Requires:   squashfs-tools >= 4.0
Requires:   btrfs-progs
Requires:   python-zypp >= 0.5.7
BuildRequires:  python2-devel

%description
MeeGo Image Creator (MIC) is a tool for creating and manipulating MeeGo images.
MIC is a series of utilities that create customized images and provides an
easy-to-use development environment for the MeeGo distribution.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

make DESTDIR=%{buildroot} installman
make DESTDIR=%{buildroot} installconf
make DESTDIR=%{buildroot} installsymlinks
sed -i 's/^run_mode.*$/run_mode=0/g' %{buildroot}/etc/mic2/mic2.conf

sed -i 's|/usr/bin/python -t|/usr/bin/python2 -t|' %{buildroot}%{_bindir}/*
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%doc doc/HACKING doc/API ChangeLog
%doc doc/examples/
%doc tests/
%{_mandir}/man1/*.1.gz
%{python2_sitelib}/*
%{_bindir}/*

%changelog
* Thu Feb 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.24.15git
- Rebuilt for Fedora
