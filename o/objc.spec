%undefine _debugsource_packages

Summary:	Portable Object Compiler
Summary(pl):	Przenośny kompilator obiektowego C
Name:		objc
Version:	3.3.5
Release:	22.1
License:	LGPL
Group:		Development/Tools
Source0:	http://users.telenet.be/stes/%{name}-%{version}.tar.gz
URL:		http://users.telenet.be/stes/compiler.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	objc-bootstrap
Provides:	objc-bootstrap = %{version}-%{release}
Obsoletes:	objc-bootstrap

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.

%description -l pl
Przenośny kompilator obiektowego C zawiera zbiór bibliotek obiektowego
C oraz prekompilator (translator), który generuje kod źródłowy w
czystym C.

%prep
%setup -q

%build
export CC="gcc -Wl,--allow-multiple-definition"
autoreconf -ifv
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir},%{_datadir}}
sed -i 's|/usr/man|%{buildroot}/usr/share/man|' Makefile
sed -i 's|/usr/include|%{buildroot}/usr/include|' Makefile
sed -i 's|BINDIR=/usr/bin|BINDIR=%{buildroot}/usr/bin|' */*/Makefile
sed -i 's|LIBDIR=/usr/lib|LIBDIR=%{buildroot}/usr/lib|' */*/Makefile
%ifarch aarch64
sed -i 's|/usr/lib|/usr/lib64|' */*/Makefile
%endif
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Books.txt Changes.txt Readme.txt *.html
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.o
%{_libdir}/*.ld
%{_libdir}/*.txt
%{_mandir}/man1/*
%exclude %{_mandir}/man3/*

%changelog
* Fri Jan 13 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3.5
- Rebuilt for Fedora
* Wed May 18 2005 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.32  2005/05/18 00:21:07  undefine
- up to 3.2.7
Revision 1.31  2004/11/14 19:09:02  undefine
- release 2
Revision 1.30  2004/10/10 19:26:55  paladine
- added missing BR: autoconf
Revision 1.29  2004/08/27 13:04:24  undefine
- release 1
- BR: objc-bootstrap (rel 0.9 objc provide it)
Revision 1.28  2004/08/27 00:01:05  ankry
- pl fixes
Revision 1.27  2004/08/26 23:05:53  undefine
- release 0.9, add provides objc-bootstrap
Revision 1.26  2004/08/26 22:26:50  undefine
- uncomment... should work ;)
Revision 1.25  2004/08/26 22:21:45  undefine
- revert change, next test...
Revision 1.24  2004/08/26 21:56:01  undefine
- test for amd64 - what is he doing???
Revision 1.23  2004/08/26 21:48:18  undefine
- another fix for amd64
Revision 1.22  2004/08/26 20:34:12  undefine
- fix use patch on amd64
Revision 1.21  2004/08/26 16:45:37  undefine
- update to 3.2.5
- remove bootstraping (we already have objc in our packages, so we don't
  need bootstrap again)
- release 0.1 to test build and "first build"
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
