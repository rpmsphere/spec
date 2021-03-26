%define _localstatedir %{_var}
%global __python %{__python3}

Name:           jgmenu
Version:        3.5
Release:        1
Summary:        Small X11 menu intended to be used with openbox and tint2
Group:          Graphical desktop/Other
License:        GPLv2
URL:            https://github.com/johanmalm/jgmenu/wiki
Source0:        https://github.com/johanmalm/jgmenu/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libmenu-cache)

%description
- jgmenu is a stand-alone, simple and contemporary-looking menu application
  for Linux and BSD.
- Although it was originally written to be used with openbox and tint2,
  it is not in any way dependent on these and runs well with other panels
  and window managers.
- It is hackable with a clean, small code base.
- It can display the following types of menu (or any combination of):
  o  bespoke menu using a jgmenu flavoured CSV format
  o  application menu (XDG compatible) with localisation support
  o  openbox XML menu including pipe-menus
- It can display SVG, PNG and XPM icons.
- It has UTF-8 search support.
- It is highly customizable (e.g. colours, alignment, margins, padding,
  transparency).
- It can synchronise with xsettings, GTK and tint2 settings.
- It does not depend on any toolkits such as GTK and Qt, but uses cairo and
  pango to render the menu directly onto an X11 window.

%prep
%setup -q

%build
%make_build prefix=%{_prefix} libexecdir=%{_libdir}/%{name}

%install
%make_install prefix=%{_prefix} libexecdir=%{_libdir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Fri Nov 29 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.5
- Rebuild for Fedora
* Tue Jun 12 2018 kekepower <kekepower> 1.0-1.mga7
+ Revision: 1236628
- Update to version 1.0
* Mon May 28 2018 kekepower <kekepower> 0.9.1-1.mga7
+ Revision: 1232807
- Update to version 0.9.1
- Remove merged upstream patch
* Sat May 26 2018 kekepower <kekepower> 0.9-2.mga7
+ Revision: 1232257
- Add upstream patch for a file read bug
* Mon May 21 2018 kekepower <kekepower> 0.9-1.mga7
+ Revision: 1231282
- imported package jgmenu
