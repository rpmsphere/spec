Name:           briquolo
Version:        0.5.7
Release:        13.4
Summary:        3D Action Breakout with Explosions and Other Effects
License:        GPL-2.0+
Group:          Amusements/Games/3D/Other
URL:            http://briquolo.free.fr/
Source0:        http://briquolo.free.fr/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.png
Patch0:         %{name}-gcc43.patch
Patch1:         %{name}-libpng.patch
Patch2:         %{name}-desktop.patch
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libpng-devel
BuildRequires:  mesa-libGL-devel

%description
Briquolo features an appealing and scenic 3D view of where the action
takes place. The combination of different fullscreen views and stunning
audio/visual power-up effects ties the player to the virtual scenery of
this revamped version of Breakout.

%prep
%setup -q
%patch0
%patch1
%patch2
sed -i 's|-Wall|-Wall -std=gnu++11|' configure.ac

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -D -m 0644 desktop/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README README.fr
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.7
- Rebuilt for Fedora
* Mon May 21 2012 joop.boonen@opensuse.org
- Added missing BuildRequires automake
- Cleaned the spec file up
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Thu May 13 2010 prusnak@suse.cz
- fix libpng calls (libpng.patch)
* Fri Nov 27 2009 prusnak@suse.cz
- updated to 0.5.7
* Mon Dec  3 2007 ro@suse.de
- fix build with gcc-4.3 (gcc43.patch)
* Sat Jul 14 2007 coolo@suse.de
- fixed BuildRequires
* Tue Jun 26 2007 bk@suse.de
- update to 0.5.6: fixes some bugs and the window is resizeable now
* Tue Sep  5 2006 meissner@suse.de
- build with RPM_OPT_FLAGS
* Fri Jan 27 2006 nadvornik@suse.cz
- fixed BuildRequires
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Dec 19 2005 pth@suse.de
- Include iconv.h in MOGL_Police.h to get iconv_t defined.
* Thu Dec  8 2005 pth@suse.de
- Fix aliasing violations
- Fix other compiler warnings
* Thu Jul 28 2005 sndirsch@suse.de
- added libmikmod to #neededforbuild
* Tue May 24 2005 pth@suse.de
- Add forward declarations as needed.
- Use gettext for *all* error messages.
- Add German translations for the new messages.
* Fri May 13 2005 pth@suse.de
- Add AM_GETTEXT_VERSION
- Fix structure being used partially uninitialized
* Sat Apr 23 2005 sndirsch@suse.de
- update to release 0.5.3
  * obsoletes briquolo-0.5.2.diff
- briquolo-0.5.3.diff: don't use upstream desktop file
* Wed Mar  9 2005 sndirsch@suse.de
- added desktop icon (Bug #71792)
* Sat Mar  5 2005 sndirsch@suse.de
- added german translations
* Sat Mar  5 2005 sndirsch@suse.de
- update to release 0.5.2:
  * Unicode support
  * two new languages: Russian and Belarussian
* Tue Jan 25 2005 uli@suse.de
- update -> 0.5 (enhanced collision system, minor improvements)
* Wed Feb 11 2004 sndirsch@suse.de
- update to release 0.4.2
- removed patch; no longer required
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Tue Aug 12 2003 sndirsch@suse.de
- added desktop file
* Fri Aug  8 2003 bk@suse.de
- 3D Action Breakout using Explosions and other effects
