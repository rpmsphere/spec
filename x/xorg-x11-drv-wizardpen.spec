Name:           xorg-x11-drv-wizardpen
BuildRequires:  pkgconfig
#BuildRequires:  xorg-x11-server-sdk
URL:            https://launchpad.net/wizardpen
Version:        0.8.1
Release:        6.1
License:        GPLv2+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          System/X11/Servers
Summary:        Linux/HAL/udev/X11 driver for most non-Wacom graphics pads
Source:         http://launchpad.net/wizardpen/trunk/0.8/+download/xorg-input-wizardpen-%{version}.tar.bz2
# pbleser: conditionally use xf86usleep or usleep, depending on XOrg version:
Patch1:         x11-input-wizardpen-xf86usleep.patch
# pbleser: fix missing include for close() and read()
Patch2:         x11-input-wizardpen-fix_missing_includes.patch
BuildRequires:  udev
# only needed to own /etc/X11/xorg.conf.d:
BuildRequires:  xorg-x11-server-devel
# also provide original upstream name:

%description
Supported tablets: Acecad Flair II GT-504, DigiPro 5.54 Graphics Tablet,
Digital Ink Pad (A4 format), G-pen, Genius Wizardpen, Genius Mousepen, Genius
Easypen i405, Genius, iBall, Manhattan, Pentagram, QWare, Trust TB-3100, Trust
TB-5300, Trust TB-6300, UC-LOGIC, iBall Tablet PF8060, AIPTEK HyperPen 10000 U,
AIPTEK Slim Tablet U600 Premium II.

%prep
%setup -q -n "xorg-input-wizardpen-%{version}"
%patch1
%patch2

%build
%configure \
    --with-xorg-module-dir="%{_libdir}/xorg/modules" \
    --with-udev-rules-dir="%{_sysconfdir}/udev/rules.d" \
    --with-udev-settings-rules-dir="%{_sysconfdir}/udev/rules.d" \
    --with-xorg-conf-dir="%{_sysconfdir}/X11/xorg.conf.d"

%__make %{?_smp_flags}

%install
%__rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# remove .la files, not needed:
%__rm "$RPM_BUILD_ROOT%{_libdir}/xorg/modules/input"/*.la

# rename to use the name of the package for the .rules file:
%__mv "$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d"/67-{xorg-wizardpen,%{name}}.rules

%clean
%__rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc COPYING README
%config(noreplace) %{_sysconfdir}/udev/rules.d/*-%{name}.rules
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/*-wizardpen.conf
%{_bindir}/wizardpen-calibrate
%{_libdir}/xorg/modules/input/wizardpen_drv.so
%doc %{_mandir}/man4/wizardpen.4.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.1
- Rebuilt for Fedora
* Mon May 23 2011 pascal.bleser@opensuse.org
- initial version (0.8.1)
