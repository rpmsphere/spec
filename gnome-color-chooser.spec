%global debug_package %{nil}

Name:		gnome-color-chooser
Summary:	Customize the appearance of the GNOME desktop
Version: 	0.2.5
Release:	12.5
License: 	GPLv3+
Group:		Graphical desktop/GNOME
Source0:	%{name}/%{name}-%{version}.tar.bz2
Patch:		gnome-color-chooser-0.2.5-desktop-entry.patch
URL: 		http://sourceforge.net/projects/gnomecc
BuildRequires:  libpng-devel
#BuildRequires:  libgnomeuimm26-devel
BuildRequires:  sane-backends-devel
BuildRequires:  gcc-c++, intltool
BuildRequires:  w3m, udisks2

%description
An application for customizing the appearance of the GNOME(/GTK+) desktop.
Features: change colors and sizes of GTK widgets, colorize desktop
icons, configure your gtk engines and let your current theme be
drawn by whatever gtk engine you want, etc.


%prep
%setup -q
%patch -p1

%build
export CXXFLAGS="-std=c++11 -fPIC"
%configure
%__make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%doc README THANKS NEWS AUTHORS
%_bindir/%name
%_datadir/applications/%name.desktop
%dir %_datadir/%name/
%_datadir/%name/glade/%name.glade
%_datadir/%name/profiles/compact.xml
%_datadir/%name/%name.xml
%_datadir/man/man1/%name.1*
%_datadir/pixmaps/%name.svg

%changelog
* Thu Mar 10 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuild for Fedora
* Mon Oct 05 2009 Gtz Waschk <waschk@mandriva.org> 0.2.5-1mdv2010.0
+ Revision: 453951
- import gnome-color-chooser
* Mon Oct  5 2009 Gtz Waschk <waschk@mandriva.org> 0.2.5-1mdv2010.0
- add docs
- update license
- new version
- fix build deps
* Mon Dec 03 2007 Texstar <texstar@gmail.com> 0.2.3-1pclos2007
- import into pclos 2007
