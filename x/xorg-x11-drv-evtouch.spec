#define _disable_ld_no_undefined 1

Name:       xorg-x11-drv-evtouch
Version:    0.8.8
Release:    27.1
Summary:    Linux-Touchscreen Driver for X
Group:      System/X11
License:    MIT
URL:        http://www.conan.de/touchscreen/evtouch.html
Source:     http://www.conan.de/touchscreen/xf86-input-evtouch-%{version}.tar.bz2
# Debian patches
Patch0:     01_fix_warnings.patch
Patch1:     02_calibration_1.6.patch
Patch2:     03_server-1.6-ftbfs.diff
Patch3:     04_server-1.7-ftbfs.diff
# (tmb)  buildfixes for x11-server 1.10
Patch4:     evtouch-replace-LocalDevicePtr-with-InputInfoPtr.patch
Patch5:     evtouch-remove-libc-wrapper-usage-for-xcalloc-xalloc-xfree.patch
Patch6:     evtouch-use-a-local-variable-for-history_size.patch
Patch7:     evtouch-purge-unused-close_proc.patch
Patch8:     evtouch-add-mode-field-to-InitValuatorAxisStruct.patch
Patch9:     evtouch-adjust-to-new-PreInit.patch
# needed for ev_calibrate:
Requires:	gnu-free-fonts-common
BuildRequires:  libX11-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-server-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}
Requires: xorg-x11-server-common

%description
Evtouch is a Touchscreen-Driver for X.

%prep
%setup -q -n xf86-input-evtouch-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export CURSORDIR=%{_datadir}/xf86-input-evtouch
%configure --enable-evcalibrate
%__make

%install
rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.calibration
%{_libdir}/xorg/modules/input/evtouch_drv.la
%{_libdir}/xorg/modules/input/evtouch_drv.so
%{_libdir}/xf86-input-evtouch
%{_datadir}/xf86-input-evtouch

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.8
- Rebuild for Fedora
* Wed Jun 06 2012 tmb <tmb> 0.8.8-12.mga3
+ Revision: 256318
- rebuild for core/release
* Fri Jun 01 2012 tv <tv> 0.8.8-11.mga3
+ Revision: 252988
- rebuild b/c of ia32 failure
* Wed May 30 2012 tv <tv> 0.8.8-10.mga3.nonfree
+ Revision: 250203
- rebuild for new X.org server
* Sat Mar 10 2012 tv <tv> 0.8.8-9.mga2
+ Revision: 222537
- requires fonts-ttf-freefont (needed for ev_calibrate, mga#1346)
* Tue Dec 06 2011 tmb <tmb> 0.8.8-8.mga2
+ Revision: 177511
- submit to core/release
* Sat Oct 08 2011 tv <tv> 0.8.8-7.mga2
+ Revision: 153101
- rebuild for xserver-1.11
* Sat Mar 05 2011 tmb <tmb> 0.8.8-6.mga1
+ Revision: 65053
- fix build with x11-server 1.10
  + tv <tv>
    - rebuild for new xserver-1.10
* Fri Feb 11 2011 tmb <tmb> 0.8.8-4.mga1
+ Revision: 50133
- imported package x11-driver-input-evtouch
