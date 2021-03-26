%global debug_package %{nil}

Name:		displaylink-driver
Version:	5.3.1.34
Release:	1.bin
Summary:	DisplayLink VGA/HDMI USB Graphics Software
Group:		User Interface/X Hardware Support
License:	freeware
URL:		http://www.displaylink.com/downloads/ubuntu
Source0:	%{name}-%{version}.run
Source1:        %{name}.service
Source2:	99-displaylink.rules
Source3:        displaylink.sh
Source4:        %{name}_udev.sh
Requires:	evdi

%description
This is a graphics software for DisplayLink USB devices.

%define logfile /var/log/displaylink/%{name}.log

%prep
%setup -T -c
cp %{SOURCE0} .
chmod +x %{name}-%{version}.run
./%{name}-%{version}.run --noexec --keep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/libexec/displaylink        \
	$RPM_BUILD_ROOT/usr/lib/systemd/system/		\
	$RPM_BUILD_ROOT/usr/lib/systemd/system-sleep	\
	$RPM_BUILD_ROOT/etc/udev/rules.d/		\
	$RPM_BUILD_ROOT/var/log/displaylink/		\
	$RPM_BUILD_ROOT/opt
ln -s /usr/libexec/displaylink $RPM_BUILD_ROOT/opt/displaylink

# Binaries
# Don't copy libusb-1.0.so.0.1.0 it's already shipped by libusbx
# Don't copy libevdi.so, we compiled it from source

cd %{name}-%{version}

%ifarch x86_64
cp -a x64-ubuntu-1604/DisplayLinkManager $RPM_BUILD_ROOT/usr/libexec/displaylink/
%endif

%ifarch %ix86
cp -a x86-ubuntu-1604/DisplayLinkManager $RPM_BUILD_ROOT/usr/libexec/displaylink/
%endif

# Firmwares
cp *.spkg $RPM_BUILD_ROOT/usr/libexec/displaylink/

# systemd/udev
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/etc/udev/rules.d/
install -m755 %{SOURCE4} $RPM_BUILD_ROOT/usr/libexec/displaylink/udev.sh

# pm-util
install -m755 %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/systemd/system-sleep/

%post
udevadm control -R
udevadm trigger
for device in $(grep -lw 17e9 /sys/bus/usb/devices/*/idVendor); do
  udevadm trigger --action=add "$(dirname "$device")"
done
/usr/libexec/displaylink/udev.sh START

%files
%doc %{name}-%{version}/LICENSE %{name}-%{version}/3rd_party_licences.txt
/usr/lib/systemd/system/%{name}.service
/usr/lib/systemd/system-sleep/displaylink.sh
/etc/udev/rules.d/99-displaylink.rules
/usr/libexec/displaylink
/opt/displaylink

%preun
/usr/libexec/displaylink/udev.sh remove

%postun
/usr/bin/systemctl daemon-reload

%changelog
* Tue Jul 28 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.1.34
- Rebuild package
* Sun Feb 19 2017 Richard Hofer <rofer@rofer.me> 1.3.52
- Bump downloaded version to 1.3.52
- Note support for DL-6xxx devices
* Tue Oct 11 2016 Aaron Aichlmayr <waterfoul@gmail.com> 1.2.64
- Bump downloaded version to 1.2.64
* Tue Oct 04 2016 Victor Rehorst <victor@chuma.org> 1.2.55-2
- Fix systemd-sleep support for DisplayLink driver 1.2.58 (which is now current for v1.2)
* Thu Sep 22 2016 Santiago Saavedra <ssaavedra@gpul.org> 1.2.55-1
- Bump upstream version for both evdi and DisplayLink driver
* Mon May 30 2016 Santiago Saavedra <ssaavedra@gpul.org> 1.1.65-5
- Add systemd-sleep support
* Tue May 24 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-4
- Really copy the libevdi.so from the sources
* Sun May 22 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-3
- Add missing libdrm-devel BR
* Tue May 17 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-2
- Update to daemon 1.1.62 (with a zip file called 1.1.68, sigh)
* Tue May 17 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-1
- Update to 1.1.65
* Tue May 10 2016 Bastien Nocera <bnocera@redhat.com> 1.1.61-1
- Update to 1.1.61
* Thu Apr 28 2016 Bastien Nocera <bnocera@redhat.com> 1.0.453-1
- Update to 1.0.453
- Compile the library from source
* Mon Dec 14 2015 Bastien Nocera <bnocera@redhat.com> 1.0.335-1
- Update to 1.0.335
* Mon Sep 07 2015 Bastien Nocera <bnocera@redhat.com> 1.0.138-4
- Disable debuginfo subpackage creation
* Mon Sep 07 2015 Bastien Nocera <bnocera@redhat.com> 1.0.138-3
- Create RPM directly from downloaded zip file
- Add LICENSE
- Create i386 RPM
* Sun Sep 6  2015 Eric Nothen <enothen@gmail.com> - 1.0.138-2
- Modified installed kernels detection section to be more precise
* Wed Sep 2  2015 Eric Nothen <enothen@gmail.com> - 1.0.138-1
- Updated driver to version 1.0.138, as published by DisplayLink
* Wed Aug 19 2015 Eric Nothen <enothen@gmail.com> - 1.0.68-2
- Changed udev rule to detect devices based on vendor rather than model
* Thu Aug 13 2015 Eric Nothen <enothen@gmail.com> - 1.0.68-1
- Initial package based on module version 1.0.68 available at http://www.displaylink.com/downloads/ubuntu.php
