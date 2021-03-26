Summary: A text-mode video game
Name: myman
Version: 0.7.1
Release: 5.1
Group: Amusements/Games
License: BSD
Source: %{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/myman/

%description
MyMan is a video game for color and monochrome text
terminals in the genre of Namco\'s Pac-Man. It has been
ported to a variety of operating systems using the
following for user interaction: ncurses, PDcurses,
Curses, sysV-curses, S/Lang slcurses, Win32 console, raw
stdio and termios, GGI, Allegro, aalib, libcaca, TWin,
and Carbon. It includes many maze variations and several
tile and sprite sets, ranging from large ASCII art
through large pseudo-bitmap Unicode or CP437 graphics to
single characters.

%prep
%setup -q

%build
%configure
make CFLAGS="${CFLAGS:-%optflags}" CXXFLAGS="${CXXFLAGS:-%optflags}" FFLAGS="${FFLAGS:-%optflags}"

%install
mkdir -p "%{buildroot}"
%make_install MAKEWHATIS=: MANDB=:

%clean
rm -rf %{buildroot}

%files
%doc %{_datadir}/doc/%{name}-%{version}/*
%{_bindir}/%{name}
%{_bindir}/%{name}.command
%{_bindir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}
%{_mandir}/man6/%{name}*.6.*

%changelog
* Tue Feb 24 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.1
- Rebuild for Fedora
* Tue Sep 30 2008 Benjamin C. Wiley Sittler <bsittler@gmail.com> 0.7.1-1
- initial RPM spec file created
