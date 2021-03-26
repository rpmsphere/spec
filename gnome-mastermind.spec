Summary: Mastermind game for GNOME
Name: gnome-mastermind
Version: 0.3.1
Release: 1
License: GPL
Group: Applications/Games
Source: %{name}-%{version}.tar.bz2
URL: http://www.autistici.org/gnome-mastermind/
BuildRequires: pkgconfig >= 02.
BuildRequires: glib2-devel >= 2.10
BuildRequires: gtk+-devel >= 1.2.8
BuildRequires: intltool >= 0.23
BuildRequires: perl
BuildRequires:	scrollkeeper
Requires: glib2
Requires: gtk+

%description
The goal of this game is to break a hidden color code following the hints that the game gives us. 

%prep
%setup -q

%build
%configure --with-prefix=/usr
make %{?_smp_mflags}

%install
rm -fR $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -fR $RPM_BUILD_ROOT

%files
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%doc AUTHORS COPYING BUGS NEWS README TODO 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuild for Fedora
* Tue Jun 16 2009 Radu-Cristian Fotescu <info [AT] beranger [DOT] org>
- Initial release.
