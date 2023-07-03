Name: payslots
Summary: PyGtk Casino Game
Version: 0.4.1
Release: 10.1
Group: Amusements/Games
License: opensource
URL: https://www.njsoft.iz.rs/payslots/en/
Source0: %{name}.tar.gz
BuildArch: noarch

%description
PaySlots is a popular casino game. Combine fruits to score 100 or
more and then play Higher/Lower game where you can win higher
prizes or loose everything....Good Luck!

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/pixmaps
make install PREFIX=%{buildroot}/usr DATA7DIR=%{buildroot}%{_datadir}/pixmaps
sed -i 's|Game;|Game;ArcadeGame;|' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|/usr/share/icons/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
