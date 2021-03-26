%define icecreamdir %{_libexecdir}/icecc

%define major 0
%define libname icecc
%define devname icecc-devel

Summary:	Distributed p2p based compile system
Name:		icecc
Version:	1.1rc2
Release:	1.1
Epoch:		3
License:	GPLv2+
Group:		Development/C
URL:		http://en.opensuse.org/Icecream
Source0:	ftp://ftp.suse.com/pub/projects/icecream/icecream-%{version}.tar.gz
Source1:	icecream.service
Source2:	icecream-scheduler.service
Source3:	sysconfig.icecream
Source4:	icecream.sh
Source5:	icecream.csh
Source7:	logrotate.icecream
Source8:	logrotate.icecream-scheduler
Source9:	iceccd-wrapper
Source10:	icecc-scheduler-wrapper
Patch0:		icecream-0.9.7-fix-build.patch
Patch1:		harbour-3.2.0-mga-minilzo-2.8.patch
BuildRequires:	libcap-ng-devel
BuildRequires:	lzo-devel
Requires(pre):	shadow-utils
Requires(post,preun,postun):	systemd

%description
Icecream is a distributed compile system. It allows parallel compiling by
distributing the compile jobs to several nodes of a compile network running the
icecc daemon. The icecc scheduler routes the jobs and provides status and
statistics information to the icecc monitor. Each compile node can accept one
or more compile jobs depending on the number of processors and the settings of
the daemon. Link jobs and other jobs which cannot be distributed are executed
locally on the node where the compilation is started.

%files
%{_libexecdir}/icecc/icecc-create-env
%{_libexecdir}/icecc/compilerwrapper
%{_bindir}/icecc-create-env
%{_bindir}/create-env
%{_sbindir}/iceccd
%{_bindir}/icecc
%{_bindir}/icerun
%{icecreamdir}/bin/*cc
%{icecreamdir}/bin/*g++
%{icecreamdir}/bin/*c++
%{icecreamdir}/bin/clang
%{_unitdir}/icecream.service
#{_mandir}/man1/icecc.1*
#{_mandir}/man1/iceccd.1*
#{_mandir}/man7/icecream.7*
%{_prefix}/libexec/icecc/iceccd-wrapper
%config(noreplace) %{_sysconfdir}/sysconfig/icecream
%{_sysconfdir}/profile.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/icecream
%defattr(0644,root,root,1777)
%dir /var/cache/icecream
%{_libdir}/libicecc.so.%{major}*

%post
%systemd_post icecream.service

%preun
%systemd_preun icecream.service

%postun
%systemd_postun_with_restart icecream.service

%package scheduler
Summary:	Icecream scheduler
Group:		Development/C
Requires:	%{name} = %{EVRD}
Requires(post,preun):	rpm-helper

%description scheduler
%{name} scheduler.

%files scheduler
%{_sbindir}/icecc-scheduler
%{_unitdir}/icecream-scheduler.service
%{_prefix}/libexec/icecc/icecc-scheduler-wrapper
%config(noreplace) %{_sysconfdir}/logrotate.d/icecream-scheduler
#{_mandir}/man1/icecc-scheduler.1*

%post scheduler
%systemd_post icecream-scheduler.service

%preun scheduler
%systemd_preun icecream-scheduler.service

%postun scheduler
%systemd_postun_with_restart icecream-scheduler.service

%package -n %{devname}
Summary:	Icecream development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name}-devel < 3:1.0.0
Obsoletes:	%{name}-devel < 3:1.0.0

%description -n %{devname}
Icecream development files.

%files -n %{devname}
%{_libdir}/libicecc.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%prep
%setup -q -n icecream-%{version}
%patch0 -p1 -b .fix-build
#pushd minilzo
#patch1 -p5 -b .lzo

%build
./autogen.sh
%configure \
	--disable-static \
	--enable-shared --without-man
make

%install
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_sysconfdir}/profile.d
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_prefix}/libexec/icecc
install -d %{buildroot}/var/cache/icecream
install -d %{buildroot}%{_unitdir}

%makeinstall

install -m 755 %{SOURCE1}  %{buildroot}%{_unitdir}/icecream.service
install -m 755 %{SOURCE2}  %{buildroot}%{_unitdir}/icecream-scheduler.service
install -m 644 %{SOURCE3}  %{buildroot}%{_sysconfdir}/sysconfig/icecream
# nb: prefixing icecream.sh by "80" so that it is sourced after 20colorgcc.sh
install -m 644 %{SOURCE4}  %{buildroot}%{_sysconfdir}/profile.d/80icecream.sh
install -m 644 %{SOURCE5}  %{buildroot}%{_sysconfdir}/profile.d/80icecream.csh
install -m 644 %{SOURCE7}  %{buildroot}%{_sysconfdir}/logrotate.d/icecream
install -m 644 %{SOURCE8}  %{buildroot}%{_sysconfdir}/logrotate.d/icecream-scheduler
install -m 755 %{SOURCE9}  %{buildroot}/usr/libexec/icecc/iceccd-wrapper
install -m 755 %{SOURCE10} %{buildroot}/usr/libexec/icecc/icecc-scheduler-wrapper

# Fix profile locations
sed -i "s,@DEFINEDBYRPMSPEC@,%{icecreamdir},g" %{buildroot}%{_sysconfdir}/profile.d/*

cat << EOF > %{buildroot}%{_bindir}/create-env
#!/bin/bash
GCC="%{_bindir}/gcc"
GCPP="%{_bindir}/g++"

if [ ! -z $1 ]; then
   GCC=\$1
fi

if [ ! -z \$2 ]; then
   GCPP=\$2
fi

%{icecreamdir}/icecc-create-env \$GCC \$GCPP
EOF

find %{buildroot} -name *.a -o -name *.la | xargs rm

ln -fs icecc %{buildroot}%{_bindir}/icerun
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/c++
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/cc
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/clang++
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/clang
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/g++
ln -fs ../../../bin/icecc %{buildroot}%{_libexecdir}/icecc/bin/gcc
ln -fs ../../bin/icecc-create-env %{buildroot}%{_libexecdir}/icecc/icecc-create-env

%changelog
* Tue May 10 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1rc2
- Rebuild for Fedora
* Thu Sep 18 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:1.0.0-1
+ Revision: 444f449
- New version 1.0.0, enable shared library, update files
