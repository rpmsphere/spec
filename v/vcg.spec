%global debug_package %{nil}

Summary: Visualization tool for compiler graphs
Name: vcg
Version: 1.30
Release: 5.1
License: GPL
Group: Graphics
URL: http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html
Source: ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/vcg.tar.bz2
Patch0: vcg.1.30-fix-build.patch
Patch1: vcg.1.30-fix-link.patch
BuildRequires: libX11-devel

%description
The VCG tool reads a textual and readable specification of a 
graph and visualizes the graph.  If not all positions of 
nodes are fixed, the tool layouts the graph using several 
heuristics as reducing the number of crossings, minimizing 
the size of edges, centering of nodes.  The specification 
language of the VCG tool is nearly compatible to GRL, the 
language of the edge tool, but contains many extensions.  The 
VCG tool allows folding of dynamically or statically specified 
regions of the graph.  It uses colors and runs on X11.

%prep 
%setup -q -n %{name}.%{version}
%patch0 -p1 -z .pix
%patch1 -p0 -b .link

%build
make xvcg_gcc_noxmkmf xvcg CFLAGS="-c %{optflags -wall}"

%install
install -d %buildroot/{%{_bindir},%{_mandir}/manl}
make SED=sed BINDIR=%buildroot/%{_bindir} MANDIR=%buildroot/%{_mandir}/man1 MANEXT=1 install
cp -f demo/demo.csh expl
chmod 644 expl/cfg.vcg

%files
%doc COPYING README expl
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.30
- Rebuild for Fedora
* Sat Mar 29 2014 SymbianFlo <symbianflo@mandrivausers.ro> 1.30-10
+ Revision: e88f21f
- Spec clean, fix BR, bump rel.try to fix empty debug ( and failed :D )
