Name:		infector
Version:	0.3
Release:	1
Summary:	A GTK+-2 Ataxx game
Group:		Amusements/Games
License:	GPL
URL:		http://infector.mangobrain.co.uk/
Source:		http://infector.mangobrain.co.uk/downloads/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel
BuildRequires:	gtkmm24-devel
BuildRequires:	libglademm24-devel

%description
Infector is a simple, clean implementation of the board games Ataxx and Hexxagon.
It features support for two or four players (two only on hexagonal boards),
a rudimentary AI player, and network play. Currently it has only been built and
tested on Linux and Windows.

%prep
%setup -q

%build
./configure --prefix=/usr
#sed -i '66,71d' data/Makefile.am
sed -i '465,470d' data/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

install -Dm644 data/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/infector.png
echo -e 'Name[zh_TW]=傳染者\nComment[zh_TW]=類似經典的 Ataxx 遊戲' >> data/%{name}.desktop
install -Dm644 data/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/infector.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Thu Jun 25 2009 Kami <kami@ossii.com.tw> 0.3-1.ossii
- Build for OSSII
