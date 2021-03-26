Summary:	Software tools for game theory
Name:		gambit
Version:	15.0.0
#Version:	16.0.1
Release:	8.1
License:	GPLv2+
Group:		Sciences/Mathematics
URL:		http://www.gambit-project.org/
Source0:	http://sourceforge.net/projects/gambit/files/gambit15/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	wxGTK3-devel

%description
Gambit is a set of software tools for doing computation on finite,
noncooperative games. These comprise a graphical interface for
interactively building and analyzing general games in extensive or
strategy form; a number of command-line tools for computing Nash
equilibria and other solution concepts in games; and, a set of file
formats for storing and communicating games to external tools.

%prep
%setup -q
sed -i -e 's|inline double abs|inline double myabs|' -e 's|pivVal = abs|pivVal = fabs|' src/liblinear/ludecomp.imp

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -fi
# enumpoly is not supported on 64 bit
%configure --disable-enumpoly
make

%install
%make_install

rm -rf %{buildroot}%{_includedir}

# install games
mkdir -p %{buildroot}%{_datadir}/%{name}/games
cp contrib/games/* %{buildroot}%{_datadir}/%{name}/games/

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# install menu icons
install -d %{buildroot}%{_datadir}/pixmaps
convert src/gui/bitmaps/gambit.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Fri May 27 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 15.0.0
- Rebuild for Fedora
* Wed Oct 22 2014 Rosa <rosa@abf.rosalinux.ru> 14.1.0-1
+ Revision: 92bb73f
- Automatic import for version 14.1.0-1
