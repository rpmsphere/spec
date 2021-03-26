Name:		connectk
Version:	2.0
Release:	1
Summary:	Logic Game
Group:		Amusements/Games
License:	GPL
URL:		http://www.risujin.org/connectk/
Source:		http://risujin.org/pub/connectk/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel

%description
The Connect-k family of games contains games defined by three parameters: k, p,
and q. The game is played on a Go-style (but not necessarily size) board. There
are two players, black and white, who take turn placing stones on the board.
The first player (black) plays q stones on the first turn and each player then
plays p stones on every succeeding turn. The first player to form a horizontal,
vertical, or diagonal sequence of k stones wins.

%prep
%setup -q

%build
export LIBS=-lm
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Thu Jun 25 2009 Kami <kami@ossii.com.tw> 2.0-1.ossii
- Build for OSSII
