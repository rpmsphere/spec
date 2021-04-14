%undefine _debugsource_packages

Name: swisswatch
Summary: Swiss Railway Clock for the X Window System
Version: 0.6
Release: 12.1
Group: User Interface/Desktops
License: GPL
URL: https://launchpad.net/ubuntu/+source/swisswatch
Source0: https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
BuildRequires: imake
BuildRequires: libX11-devel, libXext-devel, libXmu-devel, libXt-devel

%description
Swisswatch is a clock for the X desktop.  It relies heavily on resources for
configuration, and can be adjusted to a wide range of looks. While it can be
configured completely via resources and provides looks for a Botta (SFMoMA)
clock style, an oclock emulation and other appearances, it defaults to the
style of a Swiss Railway Clock.

%prep
%setup -q -n %{name}-0.06.orig
sed -i '/shape_gc/d' SwissWatch.c

%build
xmkmf -a
make %{?_smp_mflags}

%install
%make_install

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/X11/app-defaults/SwissWatch*
/usr/lib/X11/app-defaults

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
