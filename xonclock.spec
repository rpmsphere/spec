%global debug_package %{nil}

Summary: On-screen analog clock
Name: xonclock
Version: 0.0.9.2
Release: 6.1
License: GPL
Group: Applications/Multimedia
URL: http://xonclock.sourceforge.net/
Source: http://dl.sf.net/xonclock/xonclock-%{version}.tar.gz
BuildRequires: libtiff-devel, libjpeg-devel, libpng-devel, libpng12-devel, desktop-file-utils
BuildRequires: freetype-devel, libX11-devel, libXext-devel, libXpm-devel, libXrender-devel, libXft-devel

%description
Xonclock is a simple on-screen analog clock.

%prep
%setup -q

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Xonclock
Comment=On-screen analog clock
Exec=xonclock
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
Icon=/usr/share/xonclock/skins/xonclock.png
EOF

sed -i 's|<png.h>|<libpng12/png.h>|' src/loaders/png.c

%build
./configure --prefix=/usr CFLAGS="-I/usr/include/freetype2 -lm -lpng12 -lXrender"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor ""               \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/xonclock*
%{_bindir}/xonclock
%{_datadir}/xonclock/
%{_datadir}/applications/*xonclock.desktop

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.9.2
- Rebuild for Fedora
* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.9.2-1 - 7982/dag
- Updated to release 0.0.9.2.
* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.9.1-1
- Updated to release 0.0.9.1.
* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.8.9-1
- Updated to release 0.0.8.9.
* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.8.8-1
- Updated to release 0.0.8.8.
* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.8.6-1
- Updated to release 0.0.8.6.
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.8.5-1
- Initial package.
