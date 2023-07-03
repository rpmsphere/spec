Summary:	A lightweight and highly configurable tiling window manager
Name:		wmfs
Version:	2.beta20190813
Release:	1
License:	BSD-like
Group:		X11/Window Managers
Source0:	xorg62-wmfs-gb7b8ff8.tar.gz
URL:		https://wmfs.info/
BuildRequires:	freetype-devel
BuildRequires:	imlib2-devel
BuildRequires:	libXft-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXrandr-devel

%description
WMFS (Window Manager From Scratch) is a lightweight and highly
configurable tiling window manager for X. It can be configured with a
configuration file, supports Xft (Freetype) fonts and is compliant
with the Extended Window Manager Hints (EWMH) specifications, Xinerama
and Xrandr. WMFS can be driven with Vi based commands (ViWMFS).
Optional Imlib2 support allow WMFS to draw image instead text
everywhere you want with a simple sequence.

%prep
%setup -q -n xorg62-wmfs-gb7b8ff8

%build
CFLAGS="%{optflags}"
LDFLAGS="%{optflags} -Wl,--allow-multiple-definition"
for lib in freetype2 imlib2 xrandr xinerama; do
	CFLAGS="$CFLAGS $(pkg-config --cflags $lib)"
	LDFLAGS="$LDFLAGS $(pkg-config --libs $lib)"
done
export CFLAGS LDFLAGS

./configure \
	--prefix %{_prefix} \
	--xdg-config-dir %{_sysconfdir}/xdg \
	--man-prefix %{_mandir}

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_sysconfdir}/xdg/%{name}
%{_mandir}/man1/wmfs*

%changelog
* Fri Sep 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.beta20190813
- Rebuilt for Fedora
* Wed Feb 02 2011 PLD Team <feedback@pld-linux.org>
- Revision 1.2  2011/02/02 18:19:59  sparky
- BR: xorg-lib-libXft-devel
- Revision 1.1  2011/02/01 21:26:05  uzsolt
- initial
