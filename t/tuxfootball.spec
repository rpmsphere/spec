Summary: A 2D football game
Name: tuxfootball
Version: 0.1.1
Release: 1
Source0: https://downloads.sourceforge.net/tuxfootball/%{name}-%{version}.tar.gz
Source1: %{name}.png
License: GPL
Group: Games/Sports
URL: https://tuxfootball.sourceforge.net
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel

%description
Tux Football is a 2D football game reminiscent of sensible soccer and Kick Off from days gone past.

%prep
%setup -q

%build
cp /usr/share/automake-*/config.guess .
./configure --prefix=/usr
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m644 %{buildroot}/usr/doc/tuxfootball/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -rf %{buildroot}/usr/doc/
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Tux Football
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;X-MandrivaLinux-MoreApplications-Games-Sports;
EOF

%files
%{_docdir}/%{name}-%{version}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
* Thu Jun 18 2009 Kami <kami@ossii.com.tw> 0.1.1-2pclos2007
- Build for OSSII
* Fri Feb 15 2008 Texstar <texstar@gmail.com> 0.1.1-2pclos2007
- update
* Fri Feb 15 2008 P. K. Frederic <pkfric@yahoo.com> 0.1.1-1pclos2007
- first RPM for PCLinuxOS
