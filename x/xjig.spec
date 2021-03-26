%global debug_package %{nil}
Name:           xjig
BuildRequires:  gcc-c++ 
BuildRequires:	imake
License:        Beerware, Cardware, Shareware (not restricted)
Group:          Amusements/Games/Board/Puzzle
Version:        2.4
Release:        1
Summary:        jigsaw puzzle
URL:            ftp://ftp.ac-grenoble.fr/ge/educational_games/
Source:         xjig-%{version}.tar.bz2
Source1:	xjig.png
Source2:	xjig.desktop
Patch:          xjig-%{version}.patch

%description
XJig is a puzzle, that tries to replicate a jigsaw puzzle on the screen
as close as possible. Gif-images can be loaded and sliced into pieces
and as in every jigsaw puzzle, the goal is to set the parts together
again.


Authors:
--------
    Helmut Hoenig <Helmut.Hoenig@hub.de>

%prep
%setup -q
%patch
sed -i 's|const char|char|g' gif_image.C gif_image.H gifx_image.C gifx_image.H

%build
xmkmf
make depend
make xjig

%install
rm -rf $RPM_BUILD_ROOT
make \
    DESTDIR=$RPM_BUILD_ROOT \
    BINDIR=%_prefix/games \
    MANPATH=%_mandir \
    install install.man
install -m 755 -d $RPM_BUILD_ROOT/%_prefix/share/games/xjig
install -m 644 tina.gif $RPM_BUILD_ROOT/%_prefix/share/games/xjig/

#install Desktop & Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc COPYRIGHT README
%_prefix/games/xjig
%_mandir/man1/*
%_prefix/share/games/xjig
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuild for Fedora
* Thu Jun 06 2011 Chris Lin <chris.lin@ossii.com.tw>
- Fix types
* Wed Oct 22 2008 john@ossii.com.tw
- Rebuild for M6(OSSII)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Oct 17 2003 mcihar@suse.cz
- fix path to default image
* Thu Oct 16 2003 mcihar@suse.cz
- do not build as root
- do not install to /usr/X11R6
* Thu Oct 25 2001 cihlar@suse.cz
- initial version 2.4
