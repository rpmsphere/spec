%ifarch i386
%define _target i686-linux
%define _target_cpu i686
%define _target_os linux
%endif
%define kmod_name kqemu

Name:           %{kmod_name}
Version:        1.3.0
Release:        0.5.pre11
Summary:        The QEMU Accelerator Module (KQEMU)

Group:          System Environment/Kernel
License:        GPLv2
URL:            http://fabrice.bellard.free.fr/qemu
Source0:        http://fabrice.bellard.free.fr/qemu/kqemu-%{version}pre11.tar.gz
Source1:        %{kmod_name}.init
Source2:        %{kmod_name}.udev

Requires: chkconfig, initscripts, qemu
BuildRequires: kernel-devel

%{!?kversion: %define kversion %(uname -r)}
%define kernel_path /lib/modules/%{kversion}
%define kver_name %(echo %{kversion} | tr - _)

%description
The QEMU Accelerator Module increases the speed of QEMU when a PC is 
emulated on a PC. It runs most of the target application code directly 
on the host processor to achieve near native performance. 

%package kmod
##Release:        %(echo %{kversion} | tr - _).0.5.pre11
Summary:        Kernek module for the QEMU Accelerator Module (KQEMU)
Requires:	kernel = %kversion

%description kmod
The QEMU Accelerator Module increases the speed of QEMU when a PC is 
emulated on a PC. 

%prep
%setup -q -n kqemu-%{version}pre11
%build
./configure \
	--libdir=%{_libdir} \
	--extra-cflags="$RPM_OPT_FLAGS" \
%if 0%fedora >=10
	--kernel-path=%{_usrsrc}/kernels/%{kversion}
%else
	--kernel-path=%{_usrsrc}/kernels/%{kversion}-%{_target_cpu}
%endif

make

%install
%__rm -rf $RPM_BUILD_ROOT

%__mkdir_p %{kernel_path}/misc
if [ -f kqemu.ko ] ; then 
   module=kqemu.ko
else
   module=kqemu.o
fi
mkdir -p $RPM_BUILD_ROOT%{kernel_path}/misc
install -p -m 744 $module $RPM_BUILD_ROOT%{kernel_path}/misc

mkdir -p $RPM_BUILD_ROOT%{_initrddir}
install -pm 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/kqemu

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/60-kqemu.rules

%clean
%__rm -rf $RPM_BUILD_ROOT

%post kmod
if [ $1 -eq 1 ]; then
  /sbin/chkconfig --add kqemu ||:
#  /sbin/service kqemu start || :
fi

%preun kmod
if [ "$1" = 0 ]; then
  /sbin/service kqemu stop
  /sbin/chkconfig --del kqemu || :
fi 


%files kmod
%defattr(-,root,root,-)
%doc Changelog COPYING LICENSE README tests *.html
%config %{_sysconfdir}/udev/rules.d/60-kqemu.rules
%{_initrddir}/kqemu
%{kernel_path}/misc/*


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Wed Oct  17 2008 Wind <yc.yan@ossii.com.tw> - 1.3.0-0.5.pre11
- Rebuild for OSSII.
* Mon Jan  7 2008 kwizart < kwizart at gmail.com > - 1.3.0-0.4.pre11
- Fix ExclusiveArch: i586 i686 x86_64
- install the module with the right perms
* Sat Jan  5 2008 kwizart < kwizart at gmail.com > - 1.3.0-0.3.pre11
- Some more cleans
- Add ExclusiveArch: i386 x86_64
* Fri Nov  2 2007 kwizart < kwizart at gmail.com > - 1.3.0-0.2.pre11
- Clean for rpmfusion merge
* Fri Feb 09 2007 kwizart < kwizart at gmail.com > - 1.3.0-0.1.pre11
- Initial GPL Release.
