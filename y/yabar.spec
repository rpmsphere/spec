%global debug_package %{nil}

Name: yabar
Summary: Modern and lightweight status bar for X window managers
Version: 0.4.0git
Release: 11.1
Group: x11
License: Free Software
URL: https://github.com/geommer/yabar
Source0: %{name}-master.zip
BuildRequires: pango-devel
BuildRequires: cairo-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: asciidoc
BuildRequires: libconfig-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: alsa-lib-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: wireless-tools-devel

%description
Yabar is a modern and lightweight status bar that is intended to be used
along with minimal X window managers like bspwm and i3.

Yabar has the following features:
 - Extremely configurable with easy configuration system using a single
   config file.
 - A growing set of ready-to-use internal blocks developed in plain C.
 - Pango font rendering with support of pango markup language.
 - Support for icons and images.
 - Support for transparency.
 - Multi-monitor support using RandR.
 - Entirely clickable.
 - Support for several environment variables to help button commands.
 - Multiple bars within the same session.

%prep
%setup -q -n %{name}-master

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md LICENSE CHANGELOG AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Oct 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0git
- Rebuild for Fedora
