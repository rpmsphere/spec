%global _version 22-282

Name:           mcl-edge
Version:        22.282
Release:        1
Summary:        Analysis of networks with millions of nodes
License:        GPL
URL:            https://micans.org/mcl/index.html?sec_mcledge
Source0:        https://micans.org/mcl/src/mcl-%{_version}.tar.gz

%description
MCL-edge is a collection of ready-made network analysis tools that includes
the clustering program MCL. MCL-edge is dedicated to analysis of very large 
networks, scaling up to millions of nodes and hundreds of millions of edges.
It is comprised of a small set of tools supporting algorithms that are both 
commonly used and scale well. The tools are ready-to-run, command-line 
based, often allowing multi-processing and job dispatching. It is 
complementary to software packages such as R igraph and NetworkX that 
support a wider assortment of algorithms. 

%prep
%setup -q -n mcl-%{_version}

%build
%configure
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' `find . -name Makefile`
%make_build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT docdir=%{_docdir}/mcl-edge exampledir=%{_docdir}/mcl-edge/examples

%files
%{_bindir}/*
%{_mandir}/man*/*
%doc %{_docdir}/*

%changelog
* Sun Dec 08 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 22.282
- Rebuilt for Fedora
* Tue Jul 07 2015 Josko Plazonic <plazonic@princeton.edu>
- upgrade to version 14-137
* Fri Dec 28 2012 Josko Plazonic <plazonic@math.princeton.edu>
- minor tweaks to the spec file
* Thu Dec 27 2012 Ben Rose <benrose@cs.princeton.edu>
- first build
