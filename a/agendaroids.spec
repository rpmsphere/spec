%undefine _debugsource_packages

Name:			agendaroids
Version:		2002.03.07
Summary:		A clone of the classic "Asteroids" arcade game
License:		GPL
URL:			https://www.newbreedsoftware.com/agendaroids/
Group:			Amusements/Games/Action/Arcade
Release:		4.1
Source:			%{name}-%{version}.tar.bz2
BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig
BuildRequires:		libX11-devel

%description
"Agendaroids" is a clone of the classic arcade game "Asteroids" by Atari.

Your objective is to maneuver a space ship within a field of asteroids,
and shoot them into smaller and smaller pieces, eventually destroying
them completely.

%prep
%setup -q

%build
%{__make} %{?jobs:-j%jobs} host

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{name}.host $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc CHANGES.txt COPYING.txt README.txt TODO.txt

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2002.03.07
- Rebuilt for Fedora
