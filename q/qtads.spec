Name:           qtads
Summary:        GUI multimedia interpreter for TADS games
Version:        2.1.7
Release:        8.4
Source0:        http://downloads.sourceforge.net/project/qtads/qtads-2.x/%{version}/%{name}-%{version}.tar.bz2
URL:            http://qtads.sourceforge.net
License:        GPLv2+
Group:          Amusements/Games/Other
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ qt4-devel SDL-devel SDL_mixer-devel SDL_sound-devel

%description
QTads is a cross-platform multimedia interpreter for Tads (Text Adventure
Development System) games. Both Tads versions in use today (Tads 2 and Tads 3
are supported. MIDI, Ogg Vorbis, MP3, and WAV sound formats are supported.

TADS is a programming language written by Michael J. Roberts, designed to
implement text-adventure games (Interactive Fiction), similar to those
developed by Infocom in 1980-1990, as well as other companies (like Legend
Entertainment, Level 9, etc). If you liked games like "Zork", "Adventure",
"Trinity", or "Eric the Unready", you'll feel right at home.

%prep
%setup -q
sed -i 's|Game;|Game;AdventureGame;|' share/applications/%{name}.desktop

%build
qmake-qt4 \
    QMAKE_CFLAGS="$RPM_OPT_FLAGS -fpermissive" \
    QMAKE_CXXFLAGS="$RPM_OPT_FLAGS -fpermissive"
make %{?_smp_mflags}

%install
install -Dm755 qtads $RPM_BUILD_ROOT%{_bindir}/qtads
mkdir -p $RPM_BUILD_ROOT/usr
cp -a share $RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING INSTALL NEWS README HTML_TADS_LICENSE
%{_mandir}/man6/*
%{_bindir}/qtads
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Thu Dec 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.7
- Rebuilt for Fedora
* Thu Dec 29 2011 - realnc@gmail.com
New upstream release: 2.1.2
* Sun Feb 19 2011 - realnc@gmail.com
New upstream release: 2.1.1
* Sun Jan 30 2011 - realnc@gmail.com
New upstream release: 2.1.0
* Fri Jan 14 2011 - realnc@gmail.com
New upstream release: 2.0.2
* Thu Jan 12 2011 - realnc@gmail.com
First working version
