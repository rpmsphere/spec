Summary:   A library for working with graphs in Python
Name:      python-graph
Version:   1.8.2
Release:   6.1
Source0:   http://python-graph.googlecode.com/files/%{name}-%{version}.zip
License:   MIT
Group:     Development/Libraries/Python
BuildRoot: %{_tmppath}/%{name}-%{_version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel python-setuptools
URL:       http://code.google.com/p/python-graph/

%description
python-graph is a library for working with graphs in Python. 
This software provides a suitable data structure for
representing graphs and a whole set of important algorithms.

Provided features and algorithms: 
* Support for directed, undirected, weighted and non-weighted graphs 
* Support for hypergraphs 
* Canonical operations 
* XML import and export 
* DOT-Language output (for usage with Graphviz) 
* Random graph generation 
* Accessibility (transitive closure) 
* Breadth-first search 
* Cut-vertex and cut-edge identification 
* Depth-first search 
* Heuristic search (A* algorithm) 
* Identification of connected components 
* Minimum spanning tree (Prim's algorithm) 
* Mutual-accessibility (strongly connected components) 
* Shortest path search (Dijkstra's algorithm) 
* Topological sorting 

%prep
%setup -n python-graph

%build
cd core
%{__python} setup.py build
cd ../dot
%{__python} setup.py build

%install
cd core
%{__python} setup.py install \
  --root=$RPM_BUILD_ROOT \
  --prefix=%{_prefix}
cd ../dot
%{__python} setup.py install \
  --root=$RPM_BUILD_ROOT \
  --prefix=%{_prefix}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.2
- Rebuild for Fedora
* Fri May 29 2009 toms@suse.de
  Updated to version 1.5.0 (May 03, 2009):
  Enhancements:
  * Assymptotically faster Mutual Accessibility (now using Tarjan's algorithm);
  * DOT-Language importing;
  * Transitive edge detection;
  * Critical path algorithm.
  Fixes:
  * Cycle detection algorithm was reporting wrong results on some digraphs;
  * Removed Minimal Spanning Tree from Digraphs as Prim's algorithm does not
work on them ( Issue 28 ).
  * Deletion of A--A edge raised an exception;
  * Deletion of an node with an A--A edge raised an exception.
  Important API Changes:
  * Removed minimal_spanning_tree() method from the digraph class.
  (Skipped version 1.4.1 and 1.4.2)
* Mon Feb  9 2009 toms@suse.de
- First initial release 1.4.0
