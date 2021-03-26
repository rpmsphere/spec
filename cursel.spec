Summary:	Form and menu language interpreter
Summary(pl):	Interpreter języka formularzy i menu
Name:		cursel
Version:	0.2.4
Release:	2.3
License:	GPL
Group:		Applications/Terminal
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	autoconf
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	ncurses-devel
BuildRequires:	objc

%description
CURSEL is a FMLI implementation, a small language that allows you to
quickly make a form- and menu- based character interface to shell
scripts and other programs.

%description -l pl
CURSEL jest implementacją FMLI (Form and Menu Language Interpreter).
Niewielki język pozwalający na szybkie tworzenie interfejsu
użytkownika do skryptów powłoki lub innych programów.

%prep
%setup -q
sed -i '37i #define YY_NO_UNISTD_H 1' lex.lm
sed -i '/unistd\.h/d' *.m

%build
autoconf
%configure
make \
	OBJC="%{_bindir}/objc -Wc:%{optflags} -fcommon -I/usr/include/ncurses"\
	LIBS="-lform -lmenu -lncurses %{optflags}"

%install
install -d $RPM_BUILD_ROOT%{_bindir}
make install BINDIR=$RPM_BUILD_ROOT%{_bindir}

%files
%doc README TODO CHANGES
%{_bindir}/*

%changelog
* Tue Jan 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuild for Fedora
* Tue Dec 13 2005 PLD Team <feedback@pld-linux.org>
- All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.17  2005/12/13 18:01:46  glen
- adapterized (avoid macros with /usr/include/{ncurses,freetype}*)
Revision 1.16  2004/11/27 22:18:17  darekr
- updated to 0.2.2
- URL
Revision 1.15  2004/08/11 10:04:26  qboosh
- BR: ncurses-ext-devel
Revision 1.14  2004/03/28 16:42:42  qboosh
- release 5 for Ac
Revision 1.13  2003/05/26 16:24:51  malekith
- massive attack: adding Source-md5
Revision 1.12  2003/05/25 05:46:31  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.11  2002/08/02 22:31:26  marcus
- rel.4.
- use new %%doc
Revision 1.10  2002/08/02 22:28:30  marcus
- fixed building on ppc
Revision 1.9  2002/05/21 23:12:46  kloczek
perl -pi -e "s/^automake -a -c -f --foreing/\%\{__automake\}/; \
             s/^automake -a -c -f/\%\{__automake\}/; \
	     s/^autoconf/\%\{__autoconf\}/"
Revision 1.8  2002/04/25 16:08:19  arturs
fixed a small typo
Revision 1.7  2002/02/22 23:28:46  kloczek
- removed all Group fields translations (our rpm now can handle translating
  Group field using gettext).
Revision 1.6  2002/01/18 02:12:38  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"
Revision 1.5  2002/01/16 19:42:58  misiek
- fix build on archs other than builders arch; release 3
Revision 1.4  2001/10/11 12:19:39  qboosh
- typo, BuildRequires: autoconf
Revision 1.3  2001/08/09 21:18:06  blues
- Release 2
- ac 2.5 ready
Revision 1.2  2001/04/22 02:25:10  kloczek
- cosmetics.
Revision 1.1  2001/04/19 15:57:26  misiek
FMLI (Form and Menu Language Interpreter) implementation
