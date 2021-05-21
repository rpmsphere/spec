Summary: 	Extra Menu Module for Enlightenment E17
Name: 		e_modules-extramenu
Version: 	0.2.1
Release: 	20101111
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://code.google.com/p/e17mods/wiki/Trash
Source: 	%{name}-%version.tar.gz
BuildRequires:	evas-devel
BuildRequires:	ecore-devel 
BuildRequires:	edje-devel 
BuildRequires:	edje
BuildRequires:	efreet-devel
BuildRequires:	enlightenment-devel
BuildRequires:	e_dbus-devel
BuildRequires:	libelementary-devel
Buildrequires:	gettext-devel
Buildrequires:  libxkbfile-devel
Buildrequires:	ImageMagick
Buildrequires:  libXcomposite-devel
Buildrequires:	cvs
Requires:	efreet	

%description
This is a simple module initially written for the OpenGeu distribution.
The module is able to generate as many new submenu as you want in the
enlightenemnt main menu. The new menus can have unlimited submenus and the 
names can be translated trough a simple file text file.

The menu are generated from .menu files as per FreeDesktop standards. So you
can also use all the existing (fdo compliant) menus.

The module will search in '~/.e/e/extra_menu' and '/usr/share/menus' directory
for new menu to create. Every menu need 3 files (the .menu, .directory and
optionally a .desktop for the menu icons).

%prep
%setup -q

%build
%define Werror_cflags %nil
./autogen.sh --disable-static --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post 
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/enlightenment/modules/extramenu

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri Jan 21 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101111-4pclos2010
- rebuild

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101111-3pclos2010
- rebuild

* Fri Nov 12 2010 Texstar <texstar at gmail.com> 20101111-2pclos2010
- rebuild against e libs

* Thu Nov 11 2010 Texstar <texstar at gmail.com> 20101111-1pclos2010
- create package
