%global debug_package %{nil}
%global __spec_install_post %{nil}

Name:       eGTouch
Summary:    EETI eGTouch touchscreen driver
Version:    2.5.5814
Release:    1.bin
Group:      System/Packages
License:    EETI Proprietary
URL:        http://home.eeti.com.tw/drivers_Linux.html
Source0:    http://home.eeti.com.tw/touch_driver/Linux/20151022/%{name}_v%{version}.L-x.tar.gz
Source1:    99-eGTouch-dev.rules
Source2:    eGTouch.service

%description
EETI eGTouch touchscreen driver.

%prep
%setup -q -n %{name}_v%{version}.L-x
sed -i 's|/usr/local/eGTouch64withX/||' Rule/eGTouchU.desktop

%build

%install
install -d %{buildroot}/usr/bin
install -d %{buildroot}/etc
%ifarch x86_64
install -m 755 eGTouch64/eGTouch64withX/eGTouchD %{buildroot}/usr/bin/eGTouchD
install -m 755 eGTouch64/eGTouch64withX/eGTouchU %{buildroot}/usr/bin/eGTouchU
install -m 755 eGTouch64/eGTouch64withX/eCalib %{buildroot}/usr/bin/eCalib
install -m 644 eGTouch64/eGTouch64withX/eGTouchL.ini %{buildroot}/etc/eGTouchL.ini
%else
install -m 755 eGTouch32/eGTouch32withX/eGTouchD %{buildroot}/usr/bin/eGTouchD
install -m 755 eGTouch32/eGTouch32withX/eGTouchU %{buildroot}/usr/bin/eGTouchU
install -m 755 eGTouch32/eGTouch32withX/eCalib %{buildroot}/usr/bin/eCalib
install -m 644 eGTouch32/eGTouch32withX/eGTouchL.ini %{buildroot}/etc/eGTouchL.ini
%endif
#install -Dm644 %{SOURCE1} %{buildroot}/etc/udev/rules.d/99-eGTouch-dev.rules
install -Dm644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/eGTouch.service
install -Dm644 Rule/eGTouchU.png %{buildroot}%{_datadir}/pixmaps/eGTouchU.png
install -Dm644 Rule/eGTouchU.desktop %{buildroot}%{_datadir}/applications/eGTouchU.desktop
install -Dm644 Rule/52-egalax-virtual.conf %{buildroot}%{_datadir}/X11/xorg.conf.d/52-egalax-virtual.conf

%post
systemctl enable eGTouch
systemctl start eGTouch

%preun
systemctl stop eGTouch
systemctl disable eGTouch

%files
%doc readme.txt Guide/* *.pdf
%{_bindir}/eGTouchD
%{_bindir}/eGTouchU
%{_bindir}/eCalib
%config %{_sysconfdir}/eGTouchL.ini
#{_sysconfdir}/udev/rules.d/99-eGTouch-dev.rules
/usr/lib/systemd/system/eGTouch.service
%{_datadir}/pixmaps/eGTouchU.png
%{_datadir}/applications/eGTouchU.desktop
%{_datadir}/X11/xorg.conf.d/52-egalax-virtual.conf

%changelog
* Wed Nov 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.5814-1
- Update to 2.5.5814

* Mon Feb 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.4330-1
- Initial package
