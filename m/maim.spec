Name: maim
Version: 5.4.68
Release: 13.1
Summary: Flexible screenshotting utility
License: GPL-3.0+
Group: Graphics
URL: https://github.com/naelstrof/maim
Source: https://github.com/naelstrof/%name/archive/v%version.tar.gz#/%name-%version.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: imlib2-devel
BuildRequires: libicu-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libslopy-devel
BuildRequires: glm-devel
BuildRequires: mesa-libGL-devel

%description
maim (Make Image) is a utility that takes screenshots of your desktop
using imlib2. It's meant to overcome shortcomings of scrot and performs
better in several ways.

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Thu Jan 18 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.4.68
- Rebuilt for Fedora
* Fri Jun 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.41-alt1
- initial build for ALT Linux Sisyphus
* Fri Jun 26 2015 nemysis@gmx.ch
- Update to 3.3.41, no changelog entry
- Change Source0 Web URL, to have right maim-3.3.41.tar.gz
- Add BuildRequires for cmake and gengetopt
- Add BuildRoot
- Use %%{name} instead of maim
- Switch to manual installation, because in Source isn't install command
- Add Documentation
- Add %%changelog
* Mon Oct 20 2014 rneuhauser@suse.cz
- maim-2.3.17
* Fri Oct 17 2014 rneuhauser@suse.cz
- maim-2.2.13
