Summary:  Interactive plotting and graphing X11 in command line
Name: xgraph
Version: 12.1
Release: 10.1
License: GPL
Group: Sciences/Mathematics
Source: http://www.isi.edu/nsnam/dist/xgraph-%version.tar.bz2
Patch0: xgraph-12.1-glibc-2.10.patch
Patch1: xgraph-makefile-gentoo.patch
Patch2: xgraph-12.1-fix-str-fmt.patch
URL: http://www.isi.edu/nsnam/xgraph
BuildRequires: libX11-devel

%description
The xgraph program draws a graph on an X display given data read from
either data files or from standard input if no files are specified.  It can
display up to 64 independent data sets using different colors and/or line
styles for each set.  It annotates the graph with a title,  axis labels,
grid lines or tick marks, grid labels, and a legend.  There are options to
control the appearance of most components of the graph.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%configure
make

%install
%make_install
mv %buildroot%{_mandir}/manm %buildroot%{_mandir}/man1
mv %buildroot%{_mandir}/man1/xgraph.man %buildroot%{_mandir}/man1/xgraph.1

%files
%doc README* INSTALL examples
%{_bindir}/xgraph
%{_mandir}/man1/xgraph.*

%clean
rm -fr %buildroot

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 12.1
- Rebuild for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 12.1-9.mga4
+ Revision: 520671
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 12.1-8.mga3
+ Revision: 386990
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun May 08 2011 grenoya <grenoya> 12.1-7.mga1
+ Revision: 96302
- imported package xgraph
* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 12.1-7mdv2010.1
+ Revision: 508727
- add patch to make it build
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 12.1-6mdv2009.0
+ Revision: 262436
- rebuild
* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 12.1-3mdv2008.1
+ Revision: 140957
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 22:49:08 (55550)
- rebuild
* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 22:45:30 (55549)
Import xgraph
* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 12.1-2mdk
- Fix BuildRequires
* Wed Mar 09 2005 Olivier Thauvin <nanardon@mandrake.org> 12.1-1mdk
- initial mdk package
