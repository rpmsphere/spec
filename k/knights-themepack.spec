Name:          knights-themepack
Version:       0.5.9
Release:       2.1
Summary:       Knights themes
Group:         Graphical Desktop/KDE/Games
URL:           https://knights.sourceforge.net/
Source:        https://downloads.sourceforge.net/knights/knights-themepack-%{version}.tar.gz
License:       GPL
BuildArch:     noarch
Requires:      knights

%description
Knights is a chess interface for the K Desktop Environment. Knights works 
with all XBoard compatible chess engines, FICS, and .pgn files. This is a 
themes package for to control the GUI of the game.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/knights/themes
cp * %{buildroot}%{_datadir}/knights/themes

%files
%{_datadir}/knights/themes
%doc AUTHORS COPYING README

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.9
- Rebuilt for Fedora
* Sun Jun 01 2008 gil <puntogil@libero.it> 0.5.9-1mamba
- package created by autospec
