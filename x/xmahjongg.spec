Summary:	Colorful X solitaire Mah Jongg game
Summary(pl):	Komputerowy Mad¿ong
Name:		xmahjongg
Version:	3.7
Release:	7.1
License:	GPL
Vendor:		Little Cambridgeport Design Factory
Group:		X11/Applications/Games
Source0:	http://www.lcdf.org/xmahjongg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.lcdf.org/xmahjongg/
BuildRequires:	gcc-c++, libX11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
Real Mah Jongg is a social game that originated in China thousands of
years ago. Four players, named after the four winds, take tiles from a
wall in turn. The best tiles are made of ivory and wood; they click
pleasantly when you knock them together. Computer Solitaire Mah Jongg
(xmahjongg being one of the sillier examples) is nothing like that but
it's fun, or it must be, since there are like 300 shareware versions
available for Windows. This is for X11 and it's free.

%description -l pl
Stara, chiñska gra logiczna. Powsta³a ona w staro¿ytnym Pañstwie
Šrodka, a jej historia siêga chiñskiej dynastii Zachodniego Chou,
czyli ok. 720 roku n.e. Podobnie jak wiêkszo¶æ gier karcianych tak i
mad¿ong rozwija³ siê niezale¿nie w ró¿nych okrêgach i prowincjach
dawnych Chin, zyskuj±c niezliczone odmiany dla ró¿nej liczby
graj±cych. Ta wersja przeznaczona jest dla jednej osoby i zawiera
kilka ró¿nych zestawów klocków (dorothys, gnome, gnome2, real, thick,
dorwhite, small, thin). Wywo³uje siê je za pomoc± parametru '-t'.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7
- Rebuilt for Fedora
* Tue Jul 26 2005 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.9  2005/07/26 20:29:53  adamg
- updated to 3.7
Revision 1.8  2004/11/20 01:46:27  ankry
- one more fix
Revision 1.7  2004/11/20 01:22:45  ankry
- fixed %files, fixed build
Revision 1.6  2004/11/18 18:15:00  ankry
- added desktop, rel. 2
Revision 1.5  2004/04/12 18:54:20  qboosh
- added DESTDIR patch, moved to /usr
Revision 1.4  2003/05/28 13:03:08  malekith
- massive attack: source-md5
Revision 1.3  2003/05/25 06:28:22  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.2  2002/12/21 01:28:08  qboosh
- don't always strip on install, cleanups, added BRs
Revision 1.1  2002/12/18 18:14:35  aniou
- initial version
