%global debug_package %{nil}

Name: trayer
Version: 1.1.6
Release: 2.1
License: BSD
Group: Graphical desktop/Other
Summary: Lightweight GTK2-based systray
Source: %name-%version.tar.gz
URL: https://github.com/sargon/trayer-srg
BuildRequires: libXext-devel libXmu-devel gtk2-devel gdk-pixbuf2-xlib-devel

%description
trayer is a small program designed to provide systray functionality
present in GNOME/KDE desktop environments for window managers which
do not support that function. System tray is a place, where various
applications put their icons, so they are always visible presenting
status of applications and allowing user to control programs.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%buildroot/usr install
install -D -m644 man/trayer.1 %buildroot%_mandir/man1/%name.1

%files
%_bindir/trayer
%_mandir/man1/*.1.*
%doc COPYING README

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.6
- Rebuild for Fedora
* Sat Apr 20 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1.5-alt1
- 1.1.5
- use trayer-srg fork
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.5-alt2.qa1
- NMU: rebuilt for debuginfo.
* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt2
- fix build
* Sun Aug 15 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt1
- first build for Sisyphus
