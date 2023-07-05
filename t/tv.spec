Name: tv
Summary: TreeView X
Version: 0.5
Release: 4.1
License: GPL
Group: Sciences/Biology
Source: https://treeviewx.googlecode.com/files/%{name}-%{version}.tar.gz
URL: https://code.google.com/p/treeviewx/
Vendor: Roderic D. M. Page <r.page@bio.gla.ac.uk>
BuildRequires: libpng-devel
BuildRequires: gcc-c++
BuildRequires: wxGTK2-devel

%description
TreeView X is an open source program to display phylogenetic trees on Linux,
Unix, Mac OS X, and Windows platforms.
It can read and display NEXUS and Newick format tree files (such as those
output by PAUP, ClustalX, TREE-PUZZLE, and other programs).

%prep
%setup -q

%build
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc INSTALL COPYING
%{_bindir}/tv

%changelog
* Fri Mar 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Wed May 21 2003 R. D. M. Page <r.page@bio.gla.ac.uk>
- First draft of the spec file
