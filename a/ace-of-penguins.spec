%global __os_install_post %{nil}

Name: ace-of-penguins
Summary: Penguin-themed solitaire games
Version: 1.4
Release: 12.1
Group: games
License: Free Software
URL: https://www.delorie.com/store/ace/
Source0: https://www.delorie.com/store/ace/ace-%{version}.tar.gz
Source1: ace-share.zip
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: libpng12-devel

%description
The Ace of Penguins is a set of solitaire games inspired by the ones
available for MS Windows, but with a number of enhancements.

The package consists of the games Canfield, Freecell, Golf,
Mastermind, Merlin, Minesweeper, Pegged, Solitaire, Spider, Taipei
(with a level editor), and Thornq.

NOTE: If you experience problems with the F1 help key, please
make sure you have package xfonts-100dpi installed.

%prep
%setup -q -n ace-%{version}

%build
%configure
sed -i -e 's|-O2|-O2 -I/usr/include/libpng12|' -e 's|-lpng|-lpng12|' -e 's|-Wl,-z,now|-Wl,-z,now -Wl,--allow-multiple-definition|' */Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
unzip %{SOURCE1} -d %{buildroot}/usr
cd %{buildroot}/%{_bindir}
for i in *
do
mv $i ace-$i
done

%files
%doc AUTHORS ChangeLog COPYING README NEWS
%{_docdir}/*
%exclude /usr/lib/debug
%{_bindir}/ace-*
%{_libdir}/libcards.*
%{_datadir}/applications/penguin-*.desktop
%{_datadir}/icons/hicolor/48x48/apps/ace.png
%{_datadir}/lintian/overrides/%{name}
%{_mandir}/man6/ace*.6.*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Mar 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
