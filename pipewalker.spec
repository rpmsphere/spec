Name:           pipewalker
Version:        0.9.4
Release:        12.1
Summary:        A clone of the NetWalk game
License:        GPL-3.0
Group:          Amusements/Games/Board/Puzzle
URL:            http://%{name}.sourceforge.net/
Source:         http://downloads.sourceforge.net/pipewalker/%{name}-%{version}.tar.gz
BuildRequires:  SDL-devel
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++

%description
This is a puzzle game where pieces of a computer network are to be turned in
the right/left direction to make all computers connected to the same network.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CXXFLAGS+='-Wno-format-security -DPW_GAMEDATADIR=\"%{_datadir}/%{name}\"'

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_datadir}/menu/%{name}

%files
%doc README COPYING AUTHORS ChangeLog NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
* Mon Mar 18 2013 joop.boonen@opensuse.org
- Corrected the license
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Sat Aug  8 2009 PVince81@yahoo.fr
- Updated package version to 0.7.2
- Fixed game dir issue.
* Sun Jul 12 2009 prusnak@suse.cz
- /usr/share/games -> /usr/share
* Sun Jul 12 2009 PVince81@yahoo.fr
- Initial package
