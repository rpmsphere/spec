Name:          briskola
Version:       1.0.0
Release:       2.1
Summary:       A clone of the Italian card game Briscola
Summary(it):   BrisKola è un clone del gioco di carte italiano della Briscola.
Group:         Graphical Desktop/Applications/Games
URL:           http://www.briskola.net
Source:        http://www.briskola.net/files/briskola-%{version}.tar.gz
License:       GPL
BuildRequires: cmake
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libICE-devel
BuildRequires: openssl-devel
BuildRequires: libpng-devel
BuildRequires: qt4-devel
BuildRequires: libSM-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: zlib-devel

%description
BrisKola is a clone of the Italian card game Briscola.
This is a classic Italian game, surely one of the most popular, thanks to the simplicity of the rules and the modest skills required to players. 

%description -l it
BrisKola è un clone del gioco di carte della  Briscola.
E' in classico gioco di carte, sicuramente uno dei più popolarim grazie alla semplicità delle regole e all'abilità modesta richiesta ai giocatori

%prep
%setup -q

%build
%cmake --build build .
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/briskola                         
%{_datadir}/applications/briskola.desktop  
%{_datadir}/briskola/background/*.png
%{_datadir}/briskola/cards/*.png                           
%{_datadir}/briskola/decks/*.png
%{_datadir}/briskola/icons/*.png
%{_datadir}/briskola/misc/*.png
%{_datadir}/briskola/text/*.png
%{_datadir}/pixmaps/*.png
%doc README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora

* Tue Nov 17 2009 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 1.0.0-1mamba
- package created by autospec
