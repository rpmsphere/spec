%global __os_install_post %{nil}

Name:         nhi1
Summary:      Non Human Intelligence #1
URL:          https://developer.berlios.de/projects/nhi1/
Group:        Libraries
License:      GPL
Version:      0.17
Release:      11.1
Source0:      https://download.berlios.de/nhi1/NHI1-%{version}.tar.bz2
Patch0:       NHI1-va_list.patch

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%description
The goal of the NHI1 project is to create an artificial (non human)
intelligence until 2040. The core is available for C, C++, C#, JAVA,
Perl, PHP, Python, Ruby, Tcl and VB.NET.

%prep
%setup -q -n NHI1-%{version}
%ifarch aarch64
%patch 0 -p1
%endif

%build
export CFLAGS="-g -O2 -fPIE -fPIC -Wno-format-security"
( echo "#!/bin/sh"
  echo "true"
) >tclConfig.sh
chmod a+x tclConfig.sh
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --with-tclcfg-path=`pwd` \
    --with-tool-root=`pwd`

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
mv %{buildroot}%{_datadir}/html %{buildroot}%{_datadir}/doc

%files
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/doc/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17
- Rebuilt for Fedora
