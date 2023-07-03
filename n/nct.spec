Summary:	Tetris-like game extended by colors
Summary(es):	Juego tipo Tetris, mejorado con ayuda de colores.
Summary(pl):	Tetriso-podobna gra rozszerzona o kolorki
Summary(pt_BR):	Jogo tipo Tetris, incrementado por cores, multinível
Name:		nct
Version:	1.4
Release:	7.1
License:	GPL
Group:		Applications/Games
Source0:	https://ftp.yar.ru/pub/source/nct/%{name}-%{version}.tar.gz
URL: https://lav.yar.ru/programs.html
BuildRequires:	ncurses-devel
#Requires(post):	fileutils

%description
Tetris-like game, extended by colors. Light colors can be replaced by
heavy ones, playing various levels at the same time. Number of colors
can be chosen, in case of one color we get classic game.

%description -l es
Juego tipo Tetris, mejorado con ayuda de colores. Colores suaves
pueden reemplaz arse por colores más fuertes, así se juega de manera
simultánea con varios nivel es. Puede escogerse el número de colores,
si se escoge sólo uno, se tendrá el ju ego tetris clásico.

%description -l pl
Tetriso-podobna gra, rozszerzona o kolorki. Jasne kolorki mogą być
zastępowane przez ciemne, można grać na różnych poziomach w tym samym
czasie. Liczba kolorków może być swobodnie dobierana, w przypadku
jednego koloru mamy do czynienia z klasycznym tetrisem.

%description -l pt_BR
Jogo tipo tetris, incrementado por cores. Cores leves podem ser
sobrepostas por cores mais pesadas, jogando-se com vários níveis
simultaneamente. O número de cores pode ser escolhido, e caso se
escolha apenas uma, se tem o Tetris clássico.

%prep
%setup -q

%build
CFLAGS="%{optflags} -I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_localstatedir}/games
%{__make} install DESTDIR=$RPM_BUILD_ROOT
touch	$RPM_BUILD_ROOT%{_localstatedir}/games/%{name}.score

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch %{_localstatedir}/games/%{name}.score
%{__chown} root.games %{_localstatedir}/games/%{name}.score
%{__chmod} 0664 %{_localstatedir}/games/%{name}.score

%files
%doc README NEWS
%attr(2755,root,games) %{_bindir}/%{name}
%attr(0664,root,games) %ghost %{_localstatedir}/games/%{name}.score

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Thu Oct 3 2002 PLD Team <feedback@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl
Revision 1.6  2002/10/03 09:41:50  qboosh
- added Requires(post), release 2
Revision 1.5  2002/09/07 10:42:05  undefine
- yet more cosmetics
Revision 1.4  2002/09/07 05:50:56  kloczek
- more cosmetics.
Revision 1.3  2002/09/06 22:53:50  kloczek
- cosmetics.
Revision 1.2  2002/09/06 22:36:02  undefine
- ac/am, ncurses-devel...
- it works
Revision 1.1  2002/09/06 22:23:44  undefine
- initial PLD version
Baasedon spec by Rodrigo Barbosa <rodrigob@conectiva.com>
