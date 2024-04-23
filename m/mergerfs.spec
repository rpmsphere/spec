%undefine _debugsource_packages

Name: mergerfs
Version: 2.40.2
Release: 1
Summary: A FUSE union filesystem
Group: File tools
License: MIT
URL: https://github.com/trapexit/mergerfs
Source: https://github.com/trapexit/mergerfs/releases/download/%version/%name-%version.tar.gz
BuildRequires: gcc-c++ libattr-devel fuse-devel
BuildRequires: pandoc libtool

%description
mergerfs is similar to mhddfs, unionfs, and aufs. Like mhddfs in that it also
uses FUSE. Like aufs in that it provides multiple policies for how to handle
behavior.

%prep
%setup -q
#echo "#pragma once" > src/version.hpp
#echo "static const char MERGERFS_VERSION[] = \"%{version}\";" >> src/version.hpp

%build
make %{?_smp_mflags}
make man

%install
%make_install PREFIX=%_prefix
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%files
%doc README.md
%{_bindir}/*
/sbin/*
%{_mandir}/man1/*.1*
%{_libdir}/%{name}

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.40.2
- Rebuilt for Fedora
* Wed Oct 21 2015 Terechkov Evgenii <evg@altlinux.org> 2.7.0-alt1
- 2.7.0
- fsck subpackage (dont require python for main package)
* Mon Sep  7 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.0-alt1
- 2.4.0
* Sat Sep  5 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0
* Sat Aug 22 2015 Terechkov Evgenii <evg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Linux Sisyphus
