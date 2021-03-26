%define _name plpevtch

Name:       xorg-x11-drv-%{_name}
Version:    0.5.0
Release:    1
Summary:    Xorg X11 plp evtouch input driver
Group:      System/X11
License:    MIT
URL:        http://www.plop.at/en/touchscreen.html
Source:     http://download.plop.at/files/plpevtch/xf86-input-%{_name}-%{version}.tar.gz
BuildRequires: xorg-x11-server-devel

%description
The plpevtch driver is an eventdevice driver for touchscreens under Xorg 7.x.

%prep
%setup -q -n xf86-input-%{_name}-%{version}

%build
%configure --prefix=/usr
%__make

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%doc README COPYING ChangeLog
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-plpevtch.pc
%{_libdir}/xorg/modules/input/plpevtch_drv.la
%{_libdir}/xorg/modules/input/plpevtch_drv.so

%changelog
* Tue Feb 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuild for Fedora
