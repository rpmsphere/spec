Name:           gri
Version:        2.12.23
Release:        66.1
License:        GPLv3+
Summary:        A language for scientific illustration
URL:            http://gri.sourceforge.net
Group:          Productivity/Scientific/Other
Source:         http://sourceforge.net/projects/gri/files/gri/2.12.23/%{name}-%{version}.tar.bz2
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  perl-devel
BuildRequires:  perl-Time-modules
Source100:	    refcard.ps
Source101:	    cmdrefcard.ps
Patch0:			gri-brace.patch

%description
Gri is a language for scientific graphics programming.  It is a
command-driven application, as opposed to a click/point application.
It is analogous to latex, and shares the property that extensive power
is the reward for tolerating a modest learning curve.  Gri output is
in industry-standard PostScript, suitable for incorporation in
documents prepared by various text processors.

Gri can make x-y graphs, contour-graphs, and image graphs.  In
addition to high-level capabilities, it has enough low-level
capabilities to allow users to achieve a high degree of customization.
Precise control is extended to all aspects of drawing, including
line-widths, colors, and fonts.  Text includes a subset of the tex
language, so that it is easy to incorporate Greek letters and
mathematical symbols in labels.

%prep
%setup -q
cp %{SOURCE100} %{SOURCE101} doc
sed -i -e 's|require "ctime.pl"|use Time::CTime|' -e 's|require "getopts.pl"|use Getopt::Std|' -e 's|Getopts|getopts|' doc/texinfo2HTML
sed -i '18489s|subsubsection|subsection|' doc/gri.texi
%patch0 -p1

%build
%configure
make -i -k DESTDIR=$RPM_BUILD_ROOT libdir=$RPM_BUILD_ROOT%{_datadir}/%{name} CXXFLAGS+=" -fpermissive "

%install
make -i -k DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README COPYING NEWS
%{_bindir}/gri
%{_bindir}/gri_merge
%{_bindir}/gri_unpage
%{_datadir}/%{name}/
%{_datadir}/emacs/site-lisp/gri-mode.el
%{_infodir}/gri.info*
%exclude %{_infodir}/dir
%{_mandir}/man1/gri*

%changelog
* Fri Jan 20 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.12.23
- Rebuilt for Fedora
* Fri Aug 19 2011 badshah400@gmail.com
- Initial package (version 2.12.23)
