%undefine _debugsource_packages

Name:           winusb
License:        GPL v2
Group:          Utilities/System
Version:        1.0.11
Release:        10.1
Summary:        Create your own usb stick windows installer
URL:            https://en.congelli.eu/prog_info_winusb.html
BuildRequires:  gcc-c++ libstdc++-devel wxGTK2-devel gzip
BuildRequires:  ghostscript-core ImageMagick
Source0:        https://en.congelli.eu/download/winusb/%{name}-%{version}.tar.gz

%description  
WinUSB is a simple tool that enable you to create your own usb stick windows
installer from an iso image or a real DVD.
This package contains two programs:
- WinUSB-gui: a graphical interface which is very easy to use.
- winusb: the command line tool.
Supported images: Windows Vista, Seven+ installer for any language and any
version (home, pro...) and Windows PE.

%prep
%setup -q

%build
autoreconf -ifv
./configure --prefix=/usr
sed -i 's|-Wall|-Wall -fPIC|' `find . -name Makefile`
make

%install  
make install DESTDIR=%{buildroot}
# Install icon
for res in 16x16 22x22 24x24 32x32 36x36 48x48 64x64 72x72 96x96; do \
  %{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
  convert %{buildroot}%{_datadir}/pixmaps/winusbgui-icon.png -resize ${res} %{buildroot}%{_datadir}/icons/hicolor/${res}/apps/winusbgui-icon.png
done

%files
%{_bindir}/winusb*
%{_datadir}/applications/winusbgui.desktop
%{_mandir}/man1/winusb*
%{_datadir}/pixmaps/winusbgui-icon.png
%{_datadir}/winusb/data/c501-logo.png
%{_datadir}/winusb/data/icon.png
%{_datadir}/winusb/data/listDvdDrive
%{_datadir}/winusb/data/listUsb
%{_datadir}/winusb/locale/fr/LC_MESSAGES/trad.mo
%{_datadir}/winusb/locale/fr/LC_MESSAGES/wxstd.mo
%{_datadir}/icons/hicolor/*/apps/winusbgui-icon.png

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.11
- Rebuilt for Fedora
* Thu Apr 18 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0.11
- update
* Sun Dec 23 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0.10
- update
* Sun Aug 05 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0.9
- update
* Tue Jan 31 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0.7
- update
* Tue Jan 31 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.0.3
- Initial release
