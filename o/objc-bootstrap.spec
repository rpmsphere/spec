Summary:	Portable Object Compiler - bootstrap version
Summary(pl.UTF-8):	Przenośny kompilator obiektowego C - wersja do inicjacji
Name:		objc-bootstrap
Version:	3.3.25
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	https://users.telenet.be/stes/%{name}-%{version}.tar.gz
URL:		https://users.telenet.be/stes/compiler.html
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.
This version is destined only to bootstrap objc compiler.

%description -l pl.UTF-8
Przenośny kompilator obiektowego C zawiera zbiór bibliotek obiektowego
C oraz prekompilator (translator), który generuje kod źródłowy w
czystym C. Ta wersja jest przeznaczona wyłącznie do inicjacji
właściwego kompilatora objc.

%prep
%setup -q

%build
%configure --with-cplus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
%{__make} install INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc BOOTSTRAP
%{_bindir}/*

%changelog
* Fri Jan 13 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3.4
- Rebuilt for Fedora
* Sat Feb 02 2008 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.30  2008/02/02 23:05:38  undefine
- up to 3.2.8
Revision 1.29  2007/02/13 07:16:50  glen
- tabs in preamble
Revision 1.28  2007/02/12 00:49:14  baggins
- converted to UTF-8
Revision 1.27  2004/08/27 00:01:05  ankry
- pl fixes
Revision 1.26  2004/08/26 23:09:13  undefine
- bootstrap version for objc, only in pure c, without libraries... etc.
  but enough to bootstrap objc. it shouldn't be never used, and if build
  only to supported...
Revision 1.20  2004/03/30 09:51:53  qboosh
- release 2
Revision 1.19  2004/03/30 09:32:49  qboosh
- patch fix
Revision 1.18  2004/03/30 09:25:01  qboosh
- lib64 hacks
Revision 1.17  2004/03/30 07:04:50  qboosh
- fixed
Revision 1.16  2004/03/30 07:01:08  qboosh
- proper aux dirs
Revision 1.15  2004/03/30 06:14:53  qboosh
- refresh config.sub for amd64
Revision 1.14  2003/10/30 23:33:46  ankry
- objekt -> obiekt
Revision 1.13  2003/07/01 22:10:14  areq
- 3.1.32
Revision 1.12  2003/06/20 10:26:30  mmazur
- prekompiler hehe :)
Revision 1.11  2003/05/28 13:00:01  malekith
- massive attack: source-md5
Revision 1.10  2003/05/25 05:51:16  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.9  2002/11/27 22:06:25  juandon
- new %%doc
Revision 1.8  2002/02/22 23:29:20  kloczek
- removed all Group fields translations (oure rpm now can handle translating
  Group field using gettext).
Revision 1.7  2002/01/18 02:14:05  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"
Revision 1.6  2002/01/16 20:04:12  kloczek
- cosmetics.
Revision 1.5  2001/12/24 22:20:28  filon
- updated to 3.1.27 (bugfixes, of course :-) )
Revision 1.4  2001/08/09 21:34:27  blues
- more ac changes
Revision 1.3  2001/08/09 21:31:11  agaran
s/configure/configure2_13/
for ac-2.5
Revision 1.2  2001/04/19 15:42:33  misiek
avoid conflict with tcl manuals
Revision 1.1  2001/04/19 15:08:11  misiek
new. Object C precompiler/translator into plain C.
