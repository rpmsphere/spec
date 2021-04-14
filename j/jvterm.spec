Name: jvterm
License: GPL
Group: User Interface/Desktops
Summary: A terminal emulator based on SDL
Version: 0.2.6
Release: 5.1
Source0: http://seehuhn.de/media/programs/jvterm-0.2.6.tar.gz
URL: http://seehuhn.de/pages/jvterm
BuildRequires: freetype-devel, SDL-devel, SDL_gfx-devel, SDL_image-devel

%description
Jvterm is a terminal emulator, somewhat similar to the Linux text console or
the XTerm terminal emulator. Usually it runs in fullscreen mode, so you can
use it to make your X11 desktop look like a boring text console ;-)

%prep
%setup -q

%build
%configure
%__make LIBS+=' -lm'

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

sed -i 's|/usr/bin/env python|/usr/bin/python2|' $RPM_BUILD_ROOT/usr/bin/jvterm-imview

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS TODO COPYING
%{_bindir}/jvterm*
%{_mandir}/man1/jvterm*

%changelog
* Mon Mar 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.6
- Rebuilt for Fedora
