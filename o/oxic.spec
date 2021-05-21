Summary: Tools for building images for OX Linux
Name: oxic
Version: 0.6
Release: 1
License: GPLv2
Group: System Environment/Base
Source0: %{name}-%{version}.tar.gz
Url: http://www.moblin.org/
Requires: util-linux
Requires: coreutils
Requires: python >= 2.5
Requires: e2fsprogs
Requires: dosfstools >= 2.11-8
Requires: yum > 3.0
Requires: pykickstart >= 0.96
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
Requires: curl
Requires: kpartx
Requires: zlib
Requires: rsync
Requires: /usr/bin/mkisofs
BuildRequires: python
BuildRequires: python-devel
BuildRequires: zlib-devel

%description 
Tools for generating OX Linux live images.

%prep
%setup -n %{name}-%{version}

%build
%{__python} setup.py build
%{__make} extra/squashfs-tools/mksquashfs.moblin

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT -O1 
rm -rf $RPM_BUILD_ROOT/usr/lib/python*/site-packages/pykickstart
rm -rf $RPM_BUILD_ROOT/usr/lib/python*/site-packages/iniparse
%{__install} -m 755 extra/squashfs-tools/mksquashfs.moblin $RPM_BUILD_ROOT/%{_bindir}/
%{__install} -m 755 extra/syslinux/isohybrid.moblin $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%doc HACKING API examples/ tests/
%dir %{_libdir}/python*/site-packages/oxic
%{_libdir}/python*/site-packages/oxic/*
%{_libdir}/python*/site-packages/oxic-*
%_bindir/oxic
%_bindir/moblin-livecd-iso-to-disk
%{_bindir}/mksquashfs.moblin
%{_bindir}/isohybrid.moblin

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Fri Feb 06 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.6-1.ossii
- Rebuild for OSSII

* Mon Jan 26 2009 Anas Nashif <anas.nashif@intel.com> 0.5-4.1
- Update to version 0.5

* Tue Jan 13 2009 Ding Jian-feng <jian-feng.ding@intel.com> 2.0.1
- Import mic package to moblin-mdi
