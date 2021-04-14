Name:          lgeneral
Summary:       A turn-based strategy engine heavily inspired by Panzer General
Version:       1.4.3
Release:       1
License:       GPL
Group:         Amusements/Games/Strategy/Turn Based
Source0:       %{name}-%{version}.tar.gz
Source1:       %{name}.desktop
URL:           http://lgames.sourceforge.net/index.php?project=LGeneral
BuildRequires: SDL-devel SDL_mixer-devel
Requires:      %{name}-data = %{version}

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
You play single scenarios or whole campaigns turn by turn against a human player or the AI.
Entrenchment, rugged defense, defensive fire, surprise contacts, surrender, unit supply, 
weather influence, reinforcements and other implementations contribute to the tactical 
and strategic depth of the game.

Authors:
--------
   Michael Speck <http://lgames.sf.net/contact.php>
   Leo Savernik <l.savernik@aon.at>
   Peter Ivanyi  <peteri@carme.sect.mce.hw.ac.uk>

%prep
%setup -q

%build
%configure --prefix=%{_prefix} CFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%find_lang pg
cat %{name}.lang pg.lang > full.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f full.lang
%doc AUTHORS COPYING ChangeLog README.* TODO
%{_bindir}/*
%{_datadir}/lgeneral
%{_mandir}/man1/*
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
* Fri Mar 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.3
- Rebuilt for Fedora
* Thu Sep 30 2010 Frank Schaefer <schaeferf.obs@googlemail.com>
- Update to version 1.2
* Fri Apr 02 2010 Frank Schaefer <schaeferf.obs@googlemail.com>
- Fix buffer overflow during campaign loading
* Wed Mar 30 2010 Frank Schaefer <schaeferf.obs@googlemail.com>
- Compile without -D_FORTIFY_SOURCE to avoid crash when starting a new campaign
- Fix compilation for openSUSE >= 11.2
* Mon Nov 09 2009 Frank Schaefer <schaeferf.obs@googlemail.com>
- Update to 1.2beta.14
* Mon Mar 16 2009 Frank Schaefer <schaeferf.obs@googlemail.com>
- Initial openSUSE package release (1.2beta.13)
