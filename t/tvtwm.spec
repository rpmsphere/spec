%undefine _debugsource_packages

Summary: Tom's virtual Tab Window Manager
Name: tvtwm
Version: 0.pl11
Release: 10.1
License: BSD-type
Group: User Interface/X
Source0: tvtwm.pl11.tar.gz
Source1: tvtwm-bitmaps.tar.gz
BuildRequires: imake
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: libXext-devel
BuildRequires: libXmu-devel
BuildRequires: xorg-x11-xbitmaps

%description
tvtwm is a superset of the X11R5 release of twm (Tom's Window Manager),
written by Tom LaStrange.  Much of the early functionality, which is
described in more detail in README.old, was added by Tom LaStrange himself.
Since then, tvtwm has fallen under my control, and I've added some things
myself.

The major benefit of tvtwm over twm is the "Virtual Desktop".  This
allows you do define a substitute root window that is larger than your
display area.  This new virtual root window is the parent for all of your
X clients.  tvtwm provides a "Panner" which will let you see a scaled down
representation of the whole virtual desktop.  Using this panner, and keys
bound to functions added to tvtwm, you can move around this desktop to
have your physical display showing only part of the whole desktop.  Thus,
you can have sections of your desktop assigned to particular tasks, or
just use it to keep from having 20 million layers of windows.  :-)

%prep
%setup -q -n tvtwm
sed -i '45i #include <stdio.h>' gram.y
sed -i 's|static char \*m4_defs|char *m4_defs|' parse.c

%build
xmkmf -a
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/X11/twm
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 tvtwm %{buildroot}%{_bindir}/tvtwm
install -m 0444 system.twmrc %{buildroot}/usr/lib/X11/twm/system.twmrc
install -m 0444 tvtwm.man %{buildroot}%{_mandir}/man1/tvtwm.1
mkdir -p %{buildroot}%{_includedir}/X11
cd %{buildroot}%{_includedir}/X11
gzip -dc %{SOURCE1} | tar xf -
rm bitmaps/xm_*
chmod 0644 bitmaps/*
chmod 0755 bitmaps

%files
/usr/lib/X11/twm/system.twmrc
%{_includedir}/X11/bitmaps/*
%{_bindir}/tvtwm
%{_mandir}/man1/tvtwm.1.*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.pl11
- Rebuilt for Fedora
