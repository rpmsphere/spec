Name:           bluemoon
Version:        2.12
Release:        8.1
Summary:        Blue Moon card solitaire
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Card
URL:            http://www.catb.org/~esr/bluemoon/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - bluemoon-2.12-Makefile.patch -- add $(DESTDIR), png and desktop, fix conflict with bluez
Patch0:         %{name}-2.12-Makefile.patch
# PATCH-FIX-UPSTREAM - bluemoon-2.12-bluemoon.desktop.patch -- change executable
Patch1:         %{name}-2.12-bluemoon.desktop.patch
# PATCH-FIX-UPSTREAM - bluemoon-2.12-bluemoon.c.patch -- fix 'File is compiled without RPM_OPT_FLAGS'
Patch2:         %{name}-2.12-bluemoon.c.patch
BuildRequires:  ncurses-devel

%description
This 52-card solitaire starts with the entire deck shuffled and
dealt out in four rows. The aces are then moved to the left end of
the layout, making 4 initial free spaces. You may move to a space
only the card that matches the left neighbor in suit, and is one
greater in rank. Kings are high, so no cards may be placed to their
right (they create dead spaces).

When no moves can be made, cards still out of sequence are reshuffled
and dealt face up after the ends of the partial sequences, leaving
a card space after each sequence, so that each row looks like a
partial sequence followed by a space, followed by enough cards to
make a row of 14. A moment's reflection will show that this game
cannot take more than 13 deals. A good score is 1-3 deals, 4-7 is
average, 8 or more is poor.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%files
%doc COPYING NEWS README
%{_bindir}/%{name}-catb
%{_mandir}/man6/%{name}-catb.6*
%{_datadir}/appdata/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
* Mon Apr 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.12
- Rebuilt for Fedora
* Mon Dec 22 2014 nemysis@gmx.ch
- Use for patches %%{name}-version instead of %%{name}-%%{version}
* Sun Dec 21 2014 nemysis@gmx.ch
- Initial package creation
