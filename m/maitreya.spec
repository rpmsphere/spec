Summary:	Vedic and western astrology
Name:		maitreya
Version:	8.0.1
Release:	1
License:	GPLv2+
Group:		Sciences/Astronomy
URL:		https://www.saravali.de/
Source0:	https://github.com/martin-pe/maitreya8/releases/download/v%{version}/maitreya8-%{version}.tar.bz2
BuildRequires:	wxGTK3-devel

%description
Mature Open Source platform for Vedic and western astrology.

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%{name}8
%{_datadir}/applications/*desktop
%{_datadir}/pixmaps/*
%{_datadir}/fonts/truetype/%{name}

%prep
%setup -q -n maitreya8-%{version}

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}8 %{name}.lang

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 8.0.1
- Rebuilt for Fedora
* Thu Mar 02 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 7.1.1-3
- (f5d6531) MassBuild#1273: Increase release tag
