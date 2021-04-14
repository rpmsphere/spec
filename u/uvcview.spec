Name: uvcview
Version: 20071108
Release: 6.1
Summary: A simple USB Video Camera viewer
Group: Applications/Multimedia
License: GPL2
URL: http://freshmeat.net/projects/uvcview/
Source0: http://freshmeat.net/projects/uvcview/%name-%version.tar.gz
Source1: uvcview.png
Patch0: uvcview-20070907-stop.patch
BuildRequires: gtk2-devel

%description
This program is very simple, because it is part of another software.

%prep
%setup -q
%patch0 -p1

%build
#%__autoreconf
export FLAGS="%optflags -DNDEBUG -DNO_DEBUG -D_GNU_SOURCE " LDFLAGS=-lm \
%configure
%__make CATALOGS="ru.gmo"

%install
%makeinstall CATALOGS="ru.gmo"
%find_lang %name

install -d -m 755 %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/uvcview.desktop << EOF
[Desktop Entry]
Name=UVCView
Name[ru]=просмотр камеры
Comment=A simple USB Video Camera viewer
Icon=uvcview
Categories=AudioVideo;Video;TV;
TryExec=uvcview
Exec=uvcview
Terminal=false
Type=Application
EOF

install -D -m 644 %SOURCE1 %buildroot%_datadir/pixmaps/uvcview.png

%clean
%{__rm} -rf %{buildroot}

%files -f %name.lang
%_bindir/%name
%doc ChangeLog AUTHORS
%_datadir/locale/*/LC_MESSAGES/uvcview.mo
%_datadir/applications/uvcview.desktop
%_datadir/pixmaps/uvcview.png

%changelog
* Mon Jul 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20071108
- Rebuilt for Fedora
* Fri Feb 29 2008 Hihin Ruslan <ruslandh@altlinux.ru> 20071108-alt1.1
- correct %%*_menus
* Mon Feb 25 2008 Hihin Ruslan <ruslandh@altlinux.ru> 20071108-alt1.0
- new version
* Mon Oct 29 2007 Hihin Ruslan <ruslandh@altlinux.ru> 20070907-alt1.0
- new version
* Fri Aug 31 2007 Hihin Ruslan <ruslandh@altlinux.ru> 20070607-alt1.0
- First build for ALT Linux
