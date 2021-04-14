%undefine _debugsource_packages

Name:			defendguin
Version:		0.0.12
Summary:		A Defender clone, with a Linux theme
License:		GPLv2
URL:			http://www.newbreedsoftware.com/defendguin/
Group:			Amusements/Games/Action/Arcade
Release:		6.4
Source:			%{name}-%{version}.tar.gz
BuildRequires:		SDL-devel
BuildRequires:		SDL_image-devel
BuildRequires:		SDL_mixer-devel
BuildRequires:		libX11-devel

%description
Defendguin is a clone of the arcade game "Defender," but with a Linux theme.
Your mission is to defend little penguinoids from being captured and mutated.

%prep
%setup -q
sed -e "s:PREFIX=/usr/local:PREFIX=%{_prefix}:g" -i Makefile

%build
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -m 644 src/%{name}.6 $RPM_BUILD_ROOT/%{_mandir}/man6/
cp -a data/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc docs/*
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.12
- Rebuilt for Fedora
