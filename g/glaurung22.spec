Summary:        A very strong, UCI compatible Chess engine
Name:           glaurung22
Version:        2.2
Release:        4.36
License:        GPL-2.0
Group:          Amusements/Games/Board/Chess
URL:            http://www.glaurungchess.com/
Source:         %{name}.tar.bz2
Source1:	x%{name}
Source2:	%{name}.sh
Source3:	%{name}-polyglot.sh
Source4:	glaurung.6
Source5:	%{name}.ini
Source6:	Book.bin
Patch0:		%{name}-openSUSE-Factory-fix_linking.patch
Patch1:		%{name}-openSUSE-Factory-gcc44.patch
Patch2:         glaurung22-no-buildtime.patch
BuildRequires:  gcc-c++ dos2unix
Recommends:	polyglot xboard

%description
This is a very strong chess engine, finished 4th place at internatonal ChessWar X. 
It uses the UCI (universal chess interface), for chess engines as communication protocol. 
This means to play against it, you have to use an UCI capable interface, like knights or an xboard adapter like polyglot. 

Authors:
--------
		Tord Romstad <tord@glaurungchess.com>
		Oliver Korff <ok@xynyx.de> (manual page, taken from Debian upstream)
		Salvo Spitaleri (opening book "Book.bin") 


%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p1
dos2unix Readme.txt
dos2unix src/COPYING

%build
cd src
# use Book.bin as default book with UCI
sed -i 's/book\.bin/Book\.bin/g' search.cpp ucioption.cpp
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6/
install -m 755 src/glaurung $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/x%{name}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-polyglot
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man6/
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc src/COPYING Readme.txt
%{_bindir}/*%{name}*
%{_datadir}/%{name}
%{_mandir}/man6/glaurung.6*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuild for Fedora
* Mon Aug 31 2009 AxelKoellhofer@web.de
- added a polyglot startup script (i.e. for use with xboard)
  simply typing "xboard -fcp glaurung22-polyglot" (engine = white) 
  or "xboard -scp glaurung22-polyglot" (engine = black) will work
* Thu Aug 27 2009 AxelKoellhofer@web.de
- modified startup 
  The two scripts /usr/bin/glaurung22 and /usr/bin/xglaurung22 
  both check if there is a $HOME/.glaurung22 directory
  containing an opening book and a polyglot ini-file;
  if not, the files are copied from /usr/share/glaurung22.
  In this way every user can run a "personalized" configuration
  as all of the configuration stuff is handled within $HOME.
* Wed Aug 26 2009 AxelKoellhofer@web.de
- fixed wrong error message in xboard-script if polyglot is not installed
* Sun Aug 23 2009 AxelKoellhofer@web.de
- patches rewritten (better fix for linking)
- various little fixes (xboard startscript and specfile)
* Fri Aug 21 2009 AxelKoellhofer@web.de
- first build for openSUSE, version 2.2
