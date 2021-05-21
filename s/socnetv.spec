%global debug_package %{nil}

Name:		socnetv
Version:	2.1
Release:	11.1
Summary:	A Social Networks Analyser and Visualiser
License:	GPLv3
Group:		Science/Mathematics
URL:		http://socnetv.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/project/socnetv/%{version}/SocNetV-%{version}.tar.bz2
BuildRequires: pkgconfig(Qt5PrintSupport), pkgconfig(Qt5Widgets), pkgconfig(Qt5Gui), pkgconfig(Qt5Xml), pkgconfig(Qt5Network), pkgconfig(Qt5Core)
BuildRequires: mesa-libGL-devel

%description
SocNetV (Social Networks Visualiser) is a flexible and
user-friendly tool for Social Networks Analysis and Visualisation.
It lets you create new networks (graphs) with a few clicks on a
virtual canvas or load networks of various formats (GraphViz,
GraphML, Adjacency, Pajek, etc) and modify them to suit your needs.

The application can compute network properties, such as density,
diameter and distances, as well as node and network centralities.
Various layout algorithms (i.e. Spring-embedder, circular and in
levels according to centralities) are supported for meaningful
visualisations of your networks. Furthermore, simple random
networks (lattice, same degree, etc) can be created.

Author: Dimitris V. Kalamaras <dimitris.kalamaras@gmail.com>

%prep
%setup -q

%build
qmake-qt5
make

%install
mkdir -p %{buildroot}
make install
cp -a usr %{buildroot}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/man/man1/socnetv.1.*
%{_datadir}/%{name}

%changelog
* Tue Nov 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
* Sat Jan 08 2011 TI_Eugene <ti.eugene@gmail.com> - 0.90
- Next version
* Fri Feb 20 2009 TI_Eugene <ti.eugene@gmail.com> - 0.51
- Initital build in OBS
