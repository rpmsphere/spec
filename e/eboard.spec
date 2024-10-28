Name:           eboard
Version:        1.1.1
Release:        18.1
Summary:        Chess board interface for ICS
Group:          Amusements/Games
License:        GPLv2+
URL:            https://www.bergo.eng.br/eboard/
Source0:        https://dl.sf.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        eboard.desktop
Source2:        eboard.png
Patch0:         eboard-1.1.1-gcc44.patch
Patch1:         eboard-1.1.1-dlopen.patch
Patch2:         eboard-1.1.1-png.patch
BuildRequires:  libstdc++-devel
BuildRequires:  libpng-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  perl
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils

%description
Eboard provides a chess board interface to ICS (Internet Chess Servers)
like FICS and to chess engines like GNU Chess, Sjeng and Crafty.

%prep 
%setup -q
%patch 0 -p1 -b .gcc44
%patch 1 -p1 -b .dlopen
%patch 2 -p1 -b .png

%build
export EXTRAFLAGS=`echo '%{optflags} -Wno-format-security' | sed 's/  / /g; s/ /:/g'`
./configure --prefix="/usr" --man-prefix="%{_mandir}" --extra-flags="$EXTRAFLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
desktop-file-install --vendor "" --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
install -Dm644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS COPYING Documentation/*.txt INSTALL README TODO
%{_bindir}/eboard
%{_bindir}/eboard-addtheme
%{_bindir}/eboard-config
%{_datadir}/eboard/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/eboard.6*
%{_mandir}/man1/eboard-addtheme.1*
%{_mandir}/man1/eboard-config.1*

%changelog
* Mon May 18 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Sat Jan 18 2014 Bryan Seitz <seitz@ghettoforge.org> - 1.1.1-12
- Import into GhettoForge
* Thu Jan 17 2013 Manuel Wolfshant <wolfy@fedoraproject.org> - 1.1.1-12
- Fix FTBS because of png & incorrect EXTRAFLAGS
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Mar 3 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.1.1-6
- Fix build with new linker
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Mar 21 2009 Marek Mahut <mmahut@fedoraproject.org> - 1.1.1-4
- RHBZ#485307 -  wrong category in desktop file
* Tue Mar 3 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.1.1-3
- Fix build with GCC 4.4
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Jul 30 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.1.1-1
- Initial build
