%global debug_package %{nil}

Name:			aliens
Version:		2001.05.18
Summary:		A Space Invaders/Galaxian type game
License:		GPLv2
URL:			http://www.newbreedsoftware.com/aliens/
Group:			Amusements/Games/Action/Arcade
Release:		5.1
Source:			%{name}-%{version}.tar.bz2
BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig
BuildRequires:		libX11-devel
BuildRequires:		libXpm-devel

%description
"Aliens" is an arcade-style shooting game.

The objective is simple:  Destroy as many aliens as possible!
You have 3 lives in which to do this.  You can gain bonus lives
by reaching certain score thresholds.

%prep
%setup -q

%build
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{name}.host $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2001.05.18
- Rebuild for Fedora
