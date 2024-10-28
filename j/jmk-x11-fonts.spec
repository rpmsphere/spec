%define fontname    jmk

Summary: Character-cell fonts for X11
Name: %{fontname}-x11-fonts
BuildRequires:  imake libX11-devel xorg-x11-xinit xorg-x11-font-utils xorg-x11-fonts-misc
Group: User Interface/X
BuildRequires:  freetype
%define fontdir     /usr/share/fonts/%{fontname}
Version:        3.0
Release: 50.1
License: GPL
URL: https://www.pobox.com/~jmknoble
Source0: https://www.pobox.com/~jmknoble/fonts/%{name}-%{version}.tar.gz
Patch0:         %name-%version.patch
BuildArch:      noarch

%description
These are character-cell fonts for use with the X Window System,
created by Jim Knoble.  The current list of fonts included in this
package are:

  Neep (formerly known as NouveauGothic)

    A pleasantly legible variation on the standard fixed fonts that
    accompany most distributions of the X Window System.  Comes in both
    normal and bold weights in small, medium, large, extra-large, and
    huge sizes, as well as an extra-small size that only comes in
    normal weight.  Comes in the following encodings:

      ISO-8859-1  (Latin1, Western European + Icelandic)
      ISO-8859-2  (Latin2, Eastern European)
      ISO-8859-9  (Latin5, Western European + Turkish)
      ISO-8859-15 (Latin9, Western European + Euro Symbol)

  Modd

    A fixed-width font with sleek, contemporary styling.  Normal and
    bold weights in a 10-point (6x11) and a 12-point (6x13) size.
    ISO-8859-1 encoding only.

These fonts were created using the xmbdfed BDF font editor
<ftp://crl.nmsu.edu/CLR/multiling/General/>.

For more information about fonts and the X Window System, see the X(1)
man page.

%prep
%setup
%patch 0 -p1

%build
make -C neep
xmkmf
make

%install
install -d -m 0755 $RPM_BUILD_ROOT%{fontdir}
make INSTALL_DIR=%{fontdir} DESTDIR=$RPM_BUILD_ROOT install

%files
%doc ChangeLog NEWS README %{name}-%{version}.lsm
%dir %{fontdir}
%{fontdir}/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
* Thu Mar 17 2011 Agnelo de la Crotche <agnelo@unixversal.com>
- Initial package
