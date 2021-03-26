%global debug_package %{nil}

Name: fuego
Summary: An Open-Source Framework and Engine for Go Game
Version: 1.1
Release: 18.1
Group: Amusements/Games
License: LGPLv3
URL: http://fuego.sourceforge.net/
Source0: http://sourceforge.net/projects/fuego/files/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires: boost-devel

%description
Fuego is a collection of C++ libraries for developing software for the game
of Go. It includes a Go player using Monte-Carlo tree search.

%prep
%setup -q
sed -i 's|boost::TIME_UTC|boost::TIME_UTC_|' gtpengine/GtpEngine.cpp go/GoGtpEngine.cpp
sed -i 's|mutable ||' smartgame/SgPointSetUtil.h
sed -i 's|native_file_string|string|' go/GoGtpEngine.cpp fuegomain/FuegoMainUtil.cpp
sed -i 's|, boost::filesystem::native).branch_path(||' fuegomain/FuegoMain.cpp
sed -i '274s|ostream|istream|' smartgame/SgHash.h

%build
export CXXFLAGS=-std=gnu++98
export LDFLAGS=-lpthread
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING COPYING.LESSER TODO README NEWS
%{_bindir}/%{name}*
%{_datadir}/%{name}

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
