%define _name imagewriter

Summary:	A GUI to write .img files to USB Keys
Name:		usb-imagewriter
Version:	0.1.3
Release:	1
License:	GPLv2
Group:		Applications/System
URL:		https://launchpad.net/%{name}
Source0:	https://ppa.launchpad.net/ogra/ppa/ubuntu/pool/main/u/usb-imagewriter/%{name}_%{version}.orig.tar.gz
BuildArch:	noarch
Requires:	pygtk2-libglade

%description
A GUI to write .img files like the ones created by the
ubuntu-mobile team for UME to a USB Key for installing
the image to mobile devices and netbooks.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -Dm 755 imagewriter %{buildroot}%{_bindir}/%{_name}
install -dm 755 %{buildroot}/usr/lib/%{_name}
install lib/imagewriter.py lib/find_devices.sh %{buildroot}/usr/lib/%{_name}
install -dm 755 %{buildroot}%{_datadir}/%{_name}
install share/%{name}/%{_name}.glade share/%{name}/header.png %{buildroot}%{_datadir}/%{_name}
install -dm 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{_name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Icon=media-flash
Exec=imagewriter
Name=ImageWriter
Name[zh_TW]=映像檔寫入閃碟
Comment=A GUI to write .img files to USB Keys
Comment[zh_TW]=將 .img 檔寫入 USB 隨身碟的工具
Categories=Appkication;System;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}/usr/lib/imagewriter/imagewriter.py

%clean 
rm -rf %{buildroot}

%files
%doc COPYING TODO
%attr(755,root,root) %{_bindir}/%{_name}
%{_datadir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
/usr/lib/%{_name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora
