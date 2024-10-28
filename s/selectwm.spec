%undefine _debugsource_packages

Summary:        Select a window manager at X startup
Summary(pl):    selectwm - wybór zarządcy okien przy starcie X
Name:           selectwm
Version:        0.4.1
Release:        7.1
License:        GPL
Group:          X11/Applications
Source0:        https://ordiluc.net/selectwm/%{name}-%{version}.tar.bz2
URL:            https://ordiluc.net/selectwm/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel

%description
selectwm is a simple but robust program that will let you pick a
window manager (or other executable) to run at X startup, and
optionally after a window manager exits. It uses the GTK+ toolkit, and
includes options like a timer to start the default window manager, and
modification of the window manager list from within selectwm.

%description -l pl
selectwm to prosty, ale użyteczny program, który pozwala wybrać
zarządcę okien (lub inny program) do uruchomienia przy starcie X oraz
opcjonalnie po zakończeniu działania zarządcy okien. Używa biblioteki
narzędziowej GTK+ i ma takie opcje, jak czas po którym uruchamia
domyślnego zarządcę okien oraz modyfikowanie listy zarządców okien z
programu.

%prep
%setup -q
sed -i 's|getline|mygetline|' src/options.c
sed -i 's|define GTK_DISABLE_DEPRECATED|undef GTK_DISABLE_DEPRECATED|' src/define.h

%build
%configure
%{__make} CFLAGS+=-Wno-format-security

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%files -f %{name}.lang
%attr(755,root,root) %{_bindir}/selectwm
%{_mandir}/man1/*

%changelog
* Sun Aug 26 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Wed Aug 04 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.13  2004/08/04 06:23:24  ankry
- i18n fixes (-po patch), rel. 4
Revision 1.12  2004/04/07 23:25:15  qboosh
- fixed build, release 3 for Ac
Revision 1.11  2003/09/09 10:24:57  ankry
- spaces -> tab
Revision 1.10  2003/05/28 13:01:49  malekith
- massive attack: source-md5
Revision 1.9  2003/05/25 06:26:38  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.8  2003/01/18 22:56:20  juandon
- removed two lines with define
Revision 1.7  2002/11/25 01:42:01  ankry
Massive attack:
- s/man[ea]d[zż][ae]r/zarządca/g
- (some) new %%doc
Revision 1.6  2002/10/02 14:40:34  kloczek
- fixed %files -f parameter.
Revision 1.5  2002/10/02 13:03:33  qboosh
- pl description, release 2
Revision 1.4  2002/09/28 16:35:53  kloczek
- added am_fixes patch
- finished (many fixes).
Revision 1.3  2002/09/28 11:24:14  grzegorz
- grr, stupid joe
Revision 1.2  2002/09/28 11:18:43  grzegorz
- adapterized
