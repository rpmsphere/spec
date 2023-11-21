Name:               aewan
Version:            1.0.01
Release:            6.1
Summary:            Multi-Layered ASCII Art and Animation Editor
# https://prdownloads.sourceforge.net/aewan/aewan-%{version}.tar.gz
Source:             aewan-%{version}.tar.bz2
Patch1:             aewan-fixes.patch
URL:                https://aewan.sourceforge.net/
Group:              Productivity/Graphics/Bitmap Editors
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:      zlib-devel ncurses-devel
BuildRequires:      gcc make glibc-devel
BuildRequires:      autoconf automake libtool

%description
Aewan is a curses-based program that allows for the creation and editing of
ASCII art.
The user is able to move the cursor around the screen by means of the arrow
keys and "paint" characters by pressing the corresponding keys. There are
dialog boxes that allow the user to choose foreground and background colors,
as well as bold and blink attributes. The user may also select rectangular
areas of the canvas in order to move, copy, and paste them.

What sets Aewan apart from similar projects is the fact that it can work with
multiple layers and has the ability to turn transparency and visibility on and
off for each layer.
Instead of using the layers for compositing, it is also possible to use the
layers as frames for an animation, thus enabling the user to create ASCII
animations.
The file format is easy to parse, so it is easy to write a terminal-based
application that uses the Aewan files to display onscreen.
Aewan has been tested on the Linux terminal, rxvt, xterm, and the FreeBSD
console.

%prep
%setup -q
%patch1

%build
%configure
sed -i 's|-Werror=format-security||' Makefile
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc CHANGELOG COPYING README TODO
%{_bindir}/aecat
%{_bindir}/aemakeflic
%{_bindir}/aewan
%doc %{_mandir}/man1/aecat.1.*
%doc %{_mandir}/man1/aemakeflic.1.*
%doc %{_mandir}/man1/aewan.1.*
%doc %{_mandir}/man5/aewan.5.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.01
- Rebuilt for Fedora

* Mon Jul 12 2010 pascal.bleser@opensuse.org
- initial package
