Summary: A financial, statistics, scientific and programmers calculator for GTK+
Name: gdcalc
Version: 2.20
Release: 1
License: GPL
Group: Applications/Productivity
Source: http://bhepple.freeshell.org/unix/%{name}-%{version}.tar.gz
BuildRequires: libgnomeui-devel
BuildRequires: w3m udisks2
Requires: units
URL: http://bhepple.freeshell.org/dcalc/unix/

%description
gdcalc is a financial, statistics, scientific and programmers
calculator for gtk+-based under Unix and Linux.

It has both Algebraic notation (ie. conventional, TI or Casio-like)
and Reverse Polish Notation (HP-style).

I have also included some nice conversions based on units(1) including
length (miles, km, mm etc), area, (hectares, acres, sq ft etc), volume
(litres, US & UK gallons etc) mass, pressure, fuel consumption (mpg,
litres/100km), temperature, currency ... and anything else that
units(1) can cope with. Metric, US and British units are supported -
e.g. a US gallon is a measly 3.78 litres as opposed to the much more
generous British gallon at 4.54 litres.

It is fully programmable (you've got the source, ninny) and I've left
loads of blank keys on the GUI for you to add in your favourites. If
you add functions that you think would be interesting for the world at
large, please let me have the diffs and I'll put them in.

To get better fonts for the numbers and buttons, copy the file
/usr/share/doc/gdcalc/gdcalc.rc to .gdcalc.rc in your home directory
and customise.

gdcalc is based on my venerable dcalc RPN calculator which I wrote
about a million years ago to learn C and curses - about 1983, I
suppose.

The original dcalc for curses (Unix console) is at
http://bhepple.freeshell.org/unix/dcalcCurses.html

There is another version of this for the Psion (RPN only) at:
http://bhepple.freeshell.org/psion

This is about as much of a manual that I feel like writing - if you
want to know more about RPN calculators (and why they are more
intuitive than algebraic calculators with their = sign) take a
look at http://www.hpcalc.org

Have fun with it! Bob Hepple: mailto:bhepple@freeshell.org

%prep
%setup -q

%build
%configure
make

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m644 doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_datadir}/applnk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING doc/manual_en.html gdcalc.rc
%{_bindir}/*
%{_datadir}/applications/gdcalc.desktop
%{_mandir}/man1/*
%{_datadir}/pixmaps/*

%changelog
* Fri Oct 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.20
- Rebuilt for Fedora
* Sun Apr 01 2012 Bob Hepple <bhepple@freeshell.org>
- Initial package
