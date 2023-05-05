%global debug_package %{nil}

Name:       risintech-touch-driver
Summary:    RiSinTech touchscreen driver
Version:    3.0.5
Release:    1.bin
Group:      System/Packages
License:    Free, Proprietary
URL:        http://www.risintech.com.tw/support.htm
Source0:    http://www.risintech.com.tw/download/%{name}-%{version}-install-i.rar
BuildRequires: unar
Requires: libXrandr libXi libusb

%description
RiSinTech touchscreen driver.

%prep
%setup -T -c
unar %{SOURCE0} 
cd %{name}-%{version}-install-i
tar xf linux-touch-driver.tgz

%build

%install
cd %{name}-%{version}-install-i
install -Dm644 tpdef.conf %{buildroot}%{_sysconfdir}/tpdef.conf
cd linux-touch-driver
install -Dm755 99-setscreen-def.sh %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/99-setscreen-def.sh
install -Dm644 pcspkr.modules %{buildroot}%{_sysconfdir}/sysconfig/modules/pcspkr.modules
%ifarch x86_64
cd x86_64
%else
cd i686
%endif
install -d %{buildroot}/usr/local/bin
install -m755 chgxorg setparams touch_utility setpdrv FreeDraw LinearAp closedev setdev debug_tool %{buildroot}/usr/local/bin
install -Dm755 libPct.so.1.0 %{buildroot}%{_libdir}/%{name}/libPct.so.1.0
ln -sf libPct.so.1.0 %{buildroot}%{_libdir}/%{name}/libPct.so
ln -sf libPct.so.1.0 %{buildroot}%{_libdir}/%{name}/libPct.so.1
install -Dm755 libtouchapi.so.1.0-newudev %{buildroot}%{_libdir}/%{name}/libtouchapi.so.1.0
ln -sf libtouchapi.so.1.0 %{buildroot}%{_libdir}/%{name}/libtouchapi.so
ln -sf libtouchapi.so.1.0 %{buildroot}%{_libdir}/%{name}/libtouchapi.so.1
install -Dm755 libLinear.so.1.0-newudev %{buildroot}%{_libdir}/%{name}/libLinear.so.1.0
ln -sf $LIB_DIR/libLinear.so.1.0 %{buildroot}%{_libdir}/%{name}/libLinear.so
ln -sf $LIB_DIR/libLinear.so.1.0 %{buildroot}%{_libdir}/%{name}/libLinear.so.1
install -Dm755 22.1/risintech_drv.so %{buildroot}%{_libdir}/xorg/modules/input/risintech_drv.so
echo 1 > %{buildroot}%{_sysconfdir}/tpinit

%post
/usr/sbin/ldconfig
setdev --mouse default
setpdrv -s -y
chgxorg -y 2 1

%postun -p /sbin/ldconfig

%files
%doc %{name}-%{version}-install-i/ReadMe.txt
/usr/local/bin/*
%{_libdir}/%{name}
%config %{_sysconfdir}/tpdef.conf
%{_sysconfdir}/tpinit
%{_sysconfdir}/sysconfig/modules/pcspkr.modules
%{_sysconfdir}/X11/xinit/xinitrc.d/99-setscreen-def.sh
%{_libdir}/xorg/modules/input/risintech_drv.so

%changelog
* Thu Oct 27 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.5
- Initial package
