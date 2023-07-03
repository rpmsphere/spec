Name: 	 	peksystray
Summary: 	Small system tray requiring only X
Version: 	0.4.0
Release: 	9.1
Source:		%{name}-%{version}.tar.bz2
Patch0:		peksystray-0.4.0-fix-str-fmt.patch
Patch1:		peksystray-0.4.0-fix-link.patch
URL:		https://peksystray.sourceforge.net/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	pkgconfig(x11)

%description
Peksystray is a small system tray (also called notification tray) designed for
all the light window managers supporting docking. As more and more
applications use a small icon in the system tray to provide additonal
fonctionalities and information, it becomes useful for everyone to have
access to them. While "heavy" window managers (Gnome, KDE...) come with a
systrem tray embedded in the rest of the desktop, lighter window managers
(WindowMaker, fluxbox...) don't have this feature. Peksystray is a very simple
and light implementation of a system tray for any window manager supporting
docking, conforming to the System Tray Freedesktop standard.

Peksystray provides a window where icons will automatically add up depending
on the requests from the applications. Both the size of the window and the
size of the icons can be selected by the user. If the window is full, it can
automatically display another window in order to display more icons.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog THANKS REFS README NEWS TODO
%{_bindir}/%name

%changelog
* Fri May 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.4.0-6
+ Revision: 2f0c542
- MassBuild#464: Increase release tag
