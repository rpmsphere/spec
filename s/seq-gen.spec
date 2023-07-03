%undefine _debugsource_packages

Summary: Simulation of molecular sequence evolution
Name: seq-gen
Version: 1.3.3
Release: 3.1
License: 1996-2004, Andrew Rambaut & Nick Grassly
Group: Applications/Bioinformatics
Source: Seq-Gen.v%{version}.tgz
URL: https://tree.bio.ed.ac.uk/software/seqgen/

%description
Seq-Gen is a program that will simulate the evolution of nucleotide
sequences along a phylogeny, using common models of the substitution
process. A range of models of molecular evolution are implemented
including the general reversible model. Nucleotide frequencies and
other parameters of the model may be given and site-specific rate
heterogeneity may also be incorporated in a number of ways. Any
number of trees may be read in and the program will produce any
number of data sets for each tree. Thus large sets of replicate
simulations can be easily created. It has been designed to be a
general purpose simulator that incorporates most of the commonly
used (and computationally tractable) models of molecular sequence
evolution.

Rambaut A & Grassly NC (1997)
Seq-Gen: an application for the Monte Carlo simulation of DNA
sequence evolution along phylogenetic trees.
Comput Appl Biosci 13, 235-238.

%prep
%setup -n Seq-Gen.v%{version}

%build
cd source
make

%install
install -Dm755 source/seq-gen $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc examples documentation
%{_bindir}/%{name}

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.3
- Rebuilt for Fedora
* Tue Feb 22 2005 Cymon J. Cox <cymon@duke.edu>
- Rebuild for version 1.3.2
* Mon Feb 9 2004 Cymon J. Cox <cymon@duke.edu>
- First build 
