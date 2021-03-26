%global debug_package %{nil}

Name:           svg2pdf
BuildRequires:  libpng-devel
BuildRequires:  cairo-devel
BuildRequires:  librsvg2-devel
License:        MIT License
Group:          Productivity/Graphics/Convertors
Summary:        Commandline SVG to PDF converter
Version:        20110111
Release:        6.1
URL:            http://wiki.inkscape.org/wiki/index.php/Tools#svg2pdf
Source:         svg2pdf-20110111.tar.bz2

%description
Convert SVG vector graphics to PDF on the commandline without using inkscape.

Authors:
--------
  Kristian Høgsberg <krh@redhat.com>
  Carl Worth <cworth@redhat.com>
  Behdad Esfahbod <besfahbo@redhat.com>

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20110111
- Rebuild for Fedora
* Wed Jan 12 2011 cwh@novell.com
- initially created package
