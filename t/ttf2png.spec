%undefine _debugsource_packages

Name:          ttf2png
Version:       0.3
Release:       16.1
Summary:       Create a PNG image containing a set of glyphs from a true type font
Group:         Applications/Graphics
URL:           https://www.tdb.fi/ttf2png.shtml
Source:        https://www.tdb.fi/files/ttf2png-%{version}.tar.gz
License:       GPL
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: libpng12-devel
BuildRequires: zlib-devel

%description
ttf2png creates a PNG image containing a set of glyphs from a true type font.
It's mainly aimed for creating bitmap fonts for games.
It supports a multitude of commandline parameters to create suitable images
for many purposes.

%prep
%setup -q
#sed -i 's|libpng12|libpng10|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 ttf2png $RPM_BUILD_ROOT%{_bindir}/ttf2png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%doc Readme gpl.txt

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Fri Sep 03 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.3-1mamba
- package created by autospec
