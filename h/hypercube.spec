%undefine _debugsource_packages

Name:           hypercube
Version:        1.7.0
Release:        6.1
Summary:        Graph visualization tool
License:        GPL-3.0
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://tumic.wz.cz/hypercube
Source0:        https://ufpr.dl.sourceforge.net/project/hypercubegraphv/Source/hypercube-%{version}.tar.gz
BuildRequires:  qt4-devel

%description
Hypercube is a graph visualization tool for drawing DOT (graphviz), GML,
GraphML, GXL and simple text-based graph representations as SVG and EPS images.
It comes with a Qt-based GUI application and a Qt-independent commandline tool.
Hypercube uses a simulated annealing algorithm to lay out the graph, which can
be easily parameterized to achieve the desired look.

%prep
%setup -q

%build
lrelease-qt4 hypercube.pro
qmake-qt4 hypercube.pro
make %{?_smp_mflags}
make clean
qmake-qt4 hypercube-cli.pro
make %{?_smp_mflags}
make clean

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp hypercube %{buildroot}%{_bindir}
cp hypercube-cli %{buildroot}%{_bindir}
cp hypercube.1 %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_mandir}/man1
ln -s hypercube.1 hypercube-cli.1

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jun 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.0
- Rebuilt for Fedora
* Sat Mar 22 2014 tumic@cbox.cz
- Update to version 1.6.3
  * Fixed double layout computation on graph file reload.
  * Fixed layout overflow issue.
  * Fixed displaying broken legend output when no legend should be displayed.
* Tue Mar 18 2014 tumic@cbox.cz
- Update to version 1.6.2
  * Improved layout when graph legend is displayed.
  * Minor fixes.
* Fri Feb 21 2014 tumic@cbox.cz
- Update to version 1.6.1
  * Fixed various GUI issues.
* Sat Feb 15 2014 tumic@cbox.cz
- Update to version 1.6.0:
  * Added selectable node/edge label attributes.
* Mon Sep  2 2013 tumic@cbox.cz
- Update to version 1.5.2:
  * Added internationalization/localization support (plus Czech localization).
  * Various minor bugfixes, particularly in the GXL input provider.
