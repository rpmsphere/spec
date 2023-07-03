%undefine _debugsource_packages

Summary:			Phylogeny Inference Package
Name:				phylip
Version:			3.697
Release:			1
License:			Freeware
Group:				Sciences/Biology
URL:				https://evolution.genetics.washington.edu/phylip.html
Source0:			https://evolution.gs.washington.edu/phylip/download/%{name}-%{version}.tar.gz
BuildRequires:			libXaw-devel libXt-devel libX11-devel
Patch0:				phylip_documentation_path_fix.patch
Patch1:				%{name}.build.patch

%description
PHYLIP (the PHYLogeny Inference Package) is a package of 35 programs for inferring phylogenies (evolutionary trees).
Output is written onto special files with names like "outfile" and "outtree". Trees written onto "outtree" are 
in the Newick format, an informal standard agreed to in 1986 by authors of a number of major phylogeny packages.
PHYLIP is probably the most widely-distributed phylogeny package. It is the sixth most frequently cited phylogeny package, 
after MrBayes, PAUP*, RAxML, Phyml, and MEGA. PHYLIP is also the oldest widely-distributed package. 
It has been in distribution since October, 1980, and has over 30,000 registered users. It is still being updated.

The author of this package is Joseph Felsenstein, Professor in the Department of Genome Sciences and the Department of 
Biology at the University of Washington, Seattle.

%prep
%setup -q
%patch0
#patch1

%build
sed -i -e 's|-lm|-lm -Wl,--allow-multiple-definition|' -e 's|-fPIC|-fPIC -Wl,--allow-multiple-definition|' src/Makefile.unx
make -C src all -f Makefile.unx

%install
make -C src BINDIR=%{buildroot}%{_libexecdir}/%{name} DATADIR=%{buildroot}%{_datadir} put -f Makefile.unx
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a exe/* %{buildroot}/%{_libexecdir}/%{name}

%files
%doc phylip.html doc/*
%{_libexecdir}/%{name}

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.697
- Rebuilt for Fedora
* Thu Nov 15 2012 Scott Santos <santos@auburn.edu> - 20120412
- initial release
