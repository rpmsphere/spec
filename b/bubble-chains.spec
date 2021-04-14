%undefine _debugsource_packages
%global _rname chains	

Name:		bubble-chains
Version:	0.1.1
Release:	25.4
Summary:	Combine color bubbles into chains
Group:		Amusements/Games		
License:	GPLv3
URL:		http://bubble-chains.sintegrial.com/
Source0:	http://bubble-chains.sintegrial.com/files/%{_rname}-%{version}-src.7z
Source1:	%{_rname}.desktop
Source2:	%{_rname}.png
Patch0:		%{name}-%{version}-dirs.patch	
BuildRequires:	qt4-devel, SDL_mixer-devel
BuildRequires:	p7zip
Requires:	timidity++

%description
The aim of Bubble Chains is to remove all of the targets on
each level, and to do this before the time (indicated with
the blue-colored bar at the right) runs out. Keep doing this
until you have passed the last level and won the game.

%prep
%setup -q -n %{_rname}-%{version}-src
%patch0

%build
qmake-qt4
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{_rname}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{_rname}.png

%files
%{_bindir}/%{_rname}
%{_datadir}/applications/%{_rname}.desktop
%{_datadir}/pixmaps/%{_rname}.png
%doc README
%{_datadir}/%{_rname}/data/*

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
* Mon Apr 15 2013 Simone Sclavi <darkhado@gmail.com> 0.1.1-1
- Initial build
