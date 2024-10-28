%undefine _debugsource_packages

Name:          swfmill
Version:       0.3.2
Release:       20.1
Summary:       An xml2swf and swf2xml processor with import functionalities
Group:         Applications/Multimedia
URL:           https://swfmill.org
Source:        https://swfmill.org/releases/swfmill-%{version}.tar.gz
License:       GPL
BuildRequires: gcc-c++, libxml2-devel, libxslt-devel, freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  libpng12-devel

%description
swfmill is an xml2swf and swf2xml processor with import functionalities.

It's most common use is the generation of asset libraries containing images
(PNG and JPEG), fonts (TTF) or other SWF movies for use with MTASC- or haXe-
compiled ActionScript, although swfmill can be used to produce both simple
and complex SWF structures.

%prep
%setup -q

%build
%configure
sed -i 's|-Wall|-Wall -Wno-narrowing|' src/Makefile
make -k ||:
sed -i 's|cd < 0|cd == NULL|' src/gSWFParseXML.cpp src/gSWFWriteXML.cpp
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%files
%{_bindir}/swfmill
%doc AUTHORS COPYING NEWS README

%changelog
* Fri Jun 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
* Fri Jan 15 2010 Automatic Build System <autodist@mambasoft.it> 0.3.0-1mamba
- automatic update by autodist
* Thu Jun 14 2007 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.2.12-1mamba
- package created by autospec
