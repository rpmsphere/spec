%undefine _debugsource_packages
Name:      rlplot
Version:   1.5
Release:   1
Summary:   A plotting program to create high quality graphs from data
License:   GPL
URL:       https://rlplot.sourceforge.net
Group:     Applications/Engineering
Source:    %{name}_%{version}.tar.gz

%description
RLPlot is is a plotting program to create high quality graphs from data.
Based on values stored in a spreadsheet several menus help you to create
graphs of your choice. The Graphs are displayed as you get them (WYSIWIG).
Double click any element of the graph (or a single click with the right
mouse button) to modify its properties. RLPlot is a cross platform
development for Linux and Windows. Exported file formats include
Scalable Vector Graphics (SVG), Encapsulated Postscript (EPS). 

%prep
%setup -q -n %{name}
sed -i -e 's|/lib|/%{_lib}|' -e 's|-lm|-lm -lpthread|' Makefile
sed -i -e 's|QString wtxt(0);|QString wtxt;|' -e 's|QString txt(0);|QString txt;|' QT_Spec.cpp
sed -i 's|return false;|return NULL;|' Fileio.cpp

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_prefix}/bin
install -m 755 exprlp $RPM_BUILD_ROOT%{_prefix}/bin

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc README RLPlot.bmp RLPLOT.ICO RLPlot.xpm gpl.txt
%{_bindir}/rlplot
%{_bindir}/exprlp

%changelog
* Wed Dec 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
* Fri May 2 2008 Reinhard Lackner
- release 1.5
* Fri Sep 14 2007 Reinhard Lackner
- release 1.4
* Sun Feb 25 2007 Reinhard Lackner
- release 1.3
* Thu Oct 19 2006 Reinhard Lackner
- release 1.2
* Fri Feb 24 2006 Reinhard Lackner
- release 1.1
* Wed Sep 07 2005 Reinhard Lackner
- release 1.0
* Tue Dec 21 2004 Reinhard Lackner
- release canditate 2, version 0.99.12b
* Sat May 31 2003 Reinhard Lackner
- modified for RLPlot 0.97b
* Sun Dec 29 2002 Reinhard Lackner
- modified for RLPlot 0.96b
* Mon Nov 25 2002 Guido Gonzato
- initial
