%undefine _debugsource_packages

Name:           gnome-quod
Summary:        Board game to make a square from pieces
Version:        0.2.0
Release:        16.1
License:        GPL3
URL:            https://sourceforge.net/projects/gquod
Group:          Amusements/Games/Board
Vendor:         openSUSE-Education
Source:        %{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  gtkmm24-devel >= 2.10
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gcc-c++
BuildRequires:  librsvg2-devel
BuildRequires:  libxml++-devel >= 2.10
BuildRequires:  intltool

%description
Quod, a game invented by G. Keith Still, has simple rules, but playing well
requires sophisticated strategy. The goal of the game is to place pieces on a
grid so that they make a square. The player who makes a square first wins.
Squares can be any size and orientation, and players have a limited supply of
blocking pieces, which adds to the complexity and interest.

Authors:
--------
    Vlad Volodin

%prep
%setup -q

%build
export CXXFLAGS="-std=c++11 -fpermissive -fPIC"
%configure

%install
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS README NEWS THANKS
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/quod.png
%dir %{_datadir}/pixmaps/gnome-quod
%{_datadir}/pixmaps/gnome-quod/*
%dir %{_datadir}/gnome-quod
%{_datadir}/gnome-quod/*

%changelog
* Sun Mar 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Mon Dec  8 2008 kirill.kirillov@gmail.com
- Initial build of 0.1.5
