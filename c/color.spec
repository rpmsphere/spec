Summary:	ANSI coloring tool
Summary(pl):	Narzêdzie do kolorowania ANSI
Name:		color
Version:	1.2
Release:	3.1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://runslinux.net/projects/color/%{name}-%{version}.tar.gz
# Source0-md5:	17938f68c0ad3060111446c34922fdf2
URL:		http://runslinux.net/?page_id=10

%description
Color is a convenience tool to ease the use of ANSI coloring in your
shell scripts by hiding the escape sequences through command
substitution.

%description -l pl
Color jest wygodnym narzêdziem u³atwiaj±cym u¿ywanie kolorowania ANSI
w skryptach shellowych poprzez ukrycie sekwencji ANSI przed
u¿ytkownikiem, zastêpuj±c je podstawianiem komend.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG README
%{_bindir}/color

%changelog
* Fri Feb 18 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2-1
- Rebuilt for Fedora

* Mon Aug 21 2006 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: color.spec,v $
Revision 1.16  2006/08/21 14:45:04  darekr
- updated to 1.2, new URL

Revision 1.15  2006/07/08 22:55:40  darekr
- pass CC

Revision 1.14  2005/12/24 20:28:40  darekr
- specify URL

Revision 1.13  2004/08/25 20:29:12  domelu
- rel. 4 to rebuild

Revision 1.12  2003/11/26 10:32:12  speedy
- release 3

Revision 1.11  2003/08/06 16:48:21  kloczek
- mo¿e wrescie kto¶ wykasuje to konto ?

Revision 1.10  2003/05/26 16:24:49  malekith
- massive attack: adding Source-md5

Revision 1.9  2003/05/25 05:46:19  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.8  2003/01/20 19:36:36  qboosh
- typo, fixed Group

Revision 1.7  2002/09/11 11:55:45  blues
- release 2 - new doc, license changed, use compilation flags - STBR

Revision 1.6  2002/04/25 16:06:10  arturs
fixed a small typo

Revision 1.5  2002/02/23 01:44:57  kloczek
- adapterized.

Revision 1.4  2002/02/22 23:28:45  kloczek
- removed all Group fields translations (our rpm now can handle translating
  Group field using gettext).

Revision 1.3  2002/02/04 00:29:13  ankry
- de/pl Group translation

Revision 1.2  2002/01/28 09:05:51  qboosh
- typo, removed template.spec changelog

Revision 1.1  2002/01/27 18:16:08  filon
- useful package, install it with cvsq
