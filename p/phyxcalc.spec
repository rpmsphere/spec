%global debug_package %{nil}

Name:		phyxcalc
BuildRequires:  qt4-devel gcc-c++ boost-devel qwt-devel
Release:	7.1
URL:		https://github.com/strahlex/PhyxCalc
License:	GPL-3.0
Version:	3rev204
Source0:	PhyxCalc-master.zip
Group:		Productivity/Scientific/Math
Summary:	Physical Expression Calculator

%description
PhyxCalc is a general purpose calculator program that evaluates written lines
of mathematical expressions. It can also unterstand expressions with physical
units as it is written by hand.

%prep
%setup -q -n PhyxCalc-master
sed -i '31,33d' plotwindow.cpp

%build
qmake-qt4
%{__make} %{?jobs:-j %jobs}

%install
%{__install} -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dm 644 misc/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -Dm 644 images/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf %{buildroot}

%files
%doc gpl.txt README doc/doc_en.html
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Aug 26 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 3rev204
- Rebuild for Fedora
* Wed Aug 15 2012 Strahlex <mail.aroessler@gmail.com>
- improved saving and modified status detection
- added autosave
* Sun Apr 15 2012 Strahlex <mail.aroessler@gmail.com>
- added more functionality to plot window
- readded multiplication without multiplication sign
- fixed some critical bugs
* Mon Apr 09 2012 Strahlex <mail.aroessler@gmail.com>
- added functions for logarithmic dataset creation
- added plot dialog
- fixed some bugs
* Wed Apr 04 2012 Strahlex <mail.aroessler@gmail.com>
- improved plot
- updated documentation
- added qwt6 support
* Wed Apr 04 2012 Strahlex <mail.aroessler@gmail.com>
- added plot support
- fixed bugs
* Wed Mar 14 2012 Strahlex <mail.aroessler@gmail.com>
- added fraction ouput
- added latex export (not finished)
- added new functions
* Sun Mar 11 2012 Strahlex <mail.aroessler@gmail.com>
- fixed and reworked calculation
- added new docks
- made unit conversion work
- added new functions
* Tue Mar 06 2012 Strahlex <mail.aroessler@gmail.com>
- added help
- fixed many small bugs
* Sun Mar 04 2012 Strahlex <mail.aroessler@gmail.com>
- added icon themes
* Sat Mar 03 2012 Strahlex <mail.aroessler@gmail.com>
- fixed some bugs
* Sat Mar 03 2012 Strahlex <mail.aroessler@gmail.com>
- added revision 146 to Build Service
